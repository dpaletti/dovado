from dovado_rtl.explorers.explorer import EndExploration
from nacolla import ImmutableModel


class FlowEnd(ImmutableModel):
    ...


def custom_step(end_exploration: EndExploration) -> FlowEnd:
    """
    This step runs after the end of the exploration section to add extra computation after exploration.
    The EndExploration class contains the last evaluated value, all the values inside the config file and inside the exploration file.
    FlowEnd if not connected to another step makes the flow end.
    This step is made visible to dovado by adding a steps.json file inside the work directory.
    Finally, it is sufficient to specify a flow, as a TOML file in the work directory, where the step is used.
    """

    print("Dovado output directory is: " + str(end_exploration.work_directory))
    # here anything can be executed, for example plot generation from dovado output inside the work directory
    return FlowEnd()
