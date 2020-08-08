import pexpect
import threading
import re

vivado = None
t_vivado_init = None


def start():
    global vivado
    global t_vivado_init
    vivado = pexpect.spawnu("vivado -mode tcl -nolog -nojournal")
    t_vivado_init = threading.Thread(target=vivado.expect, args=("Vivado%",))
    t_vivado_init.start()
    return vivado


def execute_command(command):
    if not vivado.isalive():
        raise Exception(
            "Could not start Vivado, is it installed?"
            + "Is it in your PATH?\n"
            + "Try running 'vivado -mode tcl' yourself and"
            + "debug why it does not start"
        )
    global t_vivado_init
    if t_vivado_init is not None:
        print("Waiting for Vivado to start ...")
        t_vivado_init.join()
        t_vivado_init = None

    vivado.sendline(command)
    vivado.expect("Vivado%")
    return vivado.before


def get_parts():
    return re.sub("get_parts\r\n", "", execute_command("get_parts")).split(
        " "
    )[1:-1]


def get_help(command):
    return execute_command("help " + command)
