from pathlib import Path
from dovado_rtl.explorers.utilities.spaces import DiscreteSpace


def test_discrete_space():
    path_prefix: str = "resources"

    toml_file = Path(path_prefix + "/exploration_files/neorv_exploration_file.csv")

    space = DiscreteSpace(
        toml_file, project_root=Path(path_prefix, "neorv32/rtl/neorv32")
    )

    assert space.get_points(
        Path("neorv32_top.vhd"), "neorv32_top", "CPU_EXTENSION_RISCV_B"
    ) == ["0", "0", "1", "1"]

    assert space.get_points(
        Path("neorv32_top.vhd"), "neorv32_top", "PMP_NUM_REGIONS"
    ) == ["0", "1", "0", "4"]

    assert space.get_points(
        Path("neorv32_top.vhd"), "neorv32_top", "MEM_INT_IMEM_SIZE"
    ) == ["1024", "1024", "2048", "4096"]
