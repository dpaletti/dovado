import pexpect

vivado = None


def start():
    global vivado
    vivado = pexpect.spawnu("vivado -mode tcl")


def execute_command(command):
    vivado.sendline(command)
    # discard actual command
    vivado.readline()
    # go to next prompt
    vivado.expect("Vivado%")
    return vivado.before


def get_parts():
    return execute_command("get_parts")
