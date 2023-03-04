from typing import Dict, Tuple
import pexpect
import re
import threading


class Vivado:
    def __init__(self) -> None:
        self.__vivado = pexpect.spawnu(
            "vivado -mode tcl -nolog -nojournal",
            encoding="utf-8",
            codec_errors="ignore",
        )
        self.__t_vivado_init = threading.Thread(
            target=self.__vivado.expect, args=("Vivado%",)
        )
        self.__t_vivado_init.start()

    def execute_command(self, command: str) -> str:
        if not self.__vivado.isalive():
            raise Exception(
                "Could not start Vivado, is it installed?"
                + " Is it in your PATH?\n"
                + " Try running 'vivado -mode tcl' yourself and"
                + " debug why it does not start"
            )
        if self.__t_vivado_init:
            print("Waiting for Vivado to start ...")
            self.__t_vivado_init.join()
            self.__vivado.sendline("set_param tcl.collectionResultDisplayLimit Inf")
            self.__vivado.expect("Vivado%", timeout=None)  # type: ignore
            self.__t_vivado_init = None

        self.__vivado.sendline(command)
        self.__vivado.expect("Vivado%", timeout=None)  # type: ignore
        return str(self.__vivado.before)

    def execute_script(self, tcl_script: str) -> Tuple[str, bool]:

        vivado_out = self.execute_command("source " + tcl_script)
        return vivado_out, not re.findall("ERROR:", vivado_out)

    def get_boards(self) -> Dict[str, str]:
        parts = [
            x.strip()
            for x in re.sub(
                "get_parts\r\n", "", self.execute_command("get_parts")
            ).split(" ")[1:]
        ]
        family = [
            x.strip()
            for x in re.sub(
                "[get_parts]\r\n",
                "",
                self.execute_command("get_property FAMILY [get_parts]"),
            ).split(" ")[3:]
        ]
        family[0] = family[0][len("[get_parts]\r\n") :]
        return dict(zip(parts, family))

    def is_board_valid(self, board: str) -> bool:
        boards = self.get_boards()
        if board in set(boards.keys()):
            return True
        return False
