from dovado_rtl.boxers.boxer import Boxer
from dovado_rtl.explorers.utilities.design_points import DesignPoint
from dovado_rtl.parsers.utilities.port import Port


class VerilogBoxer(Boxer):
    def __init__(self) -> None:
        super().__init__()

    def box(self, design_point: DesignPoint) -> DesignPoint:
        return self._box_hdl_antlr(
            design_point,
            "dovado_rtl.boxers.verilog",
            "box_frame.sv",
            "box.sv",
        )

    @staticmethod
    def _get_port_replacements(ports: list[Port], clock_port_name: str) -> list[str]:
        port_replacements = [
            "." + port.name + " ('1),\n"
            for port in ports
            if (
                port.direction == "input"
                and port.name != clock_port_name
                and not port.has_default
            )
        ]
        port_replacements.insert(0, "." + clock_port_name + " (clk),\n")
        port_replacements[-1] = port_replacements[-1][:-2]
        return port_replacements
