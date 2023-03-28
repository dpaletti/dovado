from dovado_rtl.boxers.boxer import Boxer
from dovado_rtl.explorers.utilities.design_points import DesignPoint
from dovado_rtl.parsers.utilities.port import Port
from nacolla import StatefulStep


class VhdlBoxer(Boxer, StatefulStep):
    def box(self, design_point: DesignPoint) -> DesignPoint:
        return self._box_hdl_antlr(
            design_point,
            "dovado_rtl.boxers.vhdl",
            "box_frame.vhd",
            "box.vhd",
            add_library=True,
        )

        self._fill(
            replacements=[
                str(design_point.target_file.parent) + "." + parsed_module.name,
                design_point.clock_port,
                "".join(port_replacements),
            ],
            package=package,
            resource=frame_file_name,
            out_path=Path(design_point.work_directory, box_file_name),
        )

    @staticmethod
    def _get_port_replacements(ports: list[Port], clock_port_name: str) -> list[str]:
        port_replacements = [
            port.name
            + (
                " => '1',\n"
                if port.dimension == "scalar"
                else " => std_logic_vector'((others => '1')),\n"
            )
            for port in ports
            if (
                port.direction == "input"
                and port.name != clock_port_name
                and not port.has_default
            )
        ]
        port_replacements.insert(0, clock_port_name + " => clk,\n")
        port_replacements[-1] = port_replacements[-1][:-2]
        return port_replacements
