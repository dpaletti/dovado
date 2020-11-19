import pexpect
import threading
import re

vivado = None
t_vivado_init = None


def start():
    global vivado
    global t_vivado_init
    vivado = pexpect.spawnu(
        "vivado -mode tcl -nolog -nojournal",
        encoding="utf-8",
        codec_errors="ignore",
    )

    t_vivado_init = threading.Thread(target=vivado.expect, args=("Vivado%",))
    t_vivado_init.start()
    return vivado


def execute_command(command):
    if not vivado.isalive():
        raise Exception(
            "Could not start Vivado, is it installed?"
            + " Is it in your PATH?\n"
            + " Try running 'vivado -mode tcl' yourself and"
            + " debug why it does not start"
        )
    global t_vivado_init
    if t_vivado_init is not None:
        print("Waiting for Vivado to start ...")
        t_vivado_init.join()
        vivado.sendline("set_param tcl.collectionResultDisplayLimit Inf")
        vivado.expect("Vivado%", timeout=None)
        t_vivado_init = None

    vivado.sendline(command)
    vivado.expect("Vivado%", timeout=None)
    return vivado.before


def source(tcl_script):
    vivado_out = execute_command("source " + tcl_script)
    return vivado_out, not re.findall("ERROR:", vivado_out)


def get_parts():
    parts = [
        x.strip()
        for x in re.sub(
            "get_parts\r\n", "", execute_command("get_parts")
        ).split(" ")[1:]
    ]
    family = [
        x.strip()
        for x in re.sub(
            "[get_parts]\r\n",
            "",
            execute_command("get_property FAMILY [get_parts]"),
        ).split(" ")[3:]
    ]
    family[0] = family[0][len("[get_parts]\r\n") :]
    return dict(zip(parts, family))


def get_help(command):
    return execute_command("help " + command)
