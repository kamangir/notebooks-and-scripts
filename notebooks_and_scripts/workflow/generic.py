from typing import Any
import networkx as nx
from abcli.modules import objects
from abcli.plugins.metadata import post, MetadataSourceType, get
from notebooks_and_scripts import env
from notebooks_and_scripts.workflow import dot_file
from notebooks_and_scripts.workflow import patterns


class Workflow:
    def __init__(
        self,
        job_name: str = "",
        load: bool = False,
    ):
        self.job_name = job_name if job_name else objects.unique_object()

        self.runner_type: str = "generic"

        self.G: nx.DiGraph = nx.DiGraph()

        if load:
            success, self.G = dot_file.load_from_file(
                objects.path_of(
                    filename="workflow.dot",
                    object_name=self.job_name,
                )
            )
            assert success

            self.runner_type = self.get_metadata(
                "runner",
                {},
            ).get(
                "type",
                "generic",
            )

    def get_metadata(
        self,
        key: str,
        default: str = "",
    ) -> str:
        return get(
            key,
            default,
            source=self.job_name,
            source_type=MetadataSourceType.OBJECT,
        )

    def load_pattern(
        self,
        pattern: str = env.NBS_DEFAULT_WORKFLOW_PATTERN,
    ) -> bool:
        success, self.G = patterns.load_pattern(
            pattern=pattern,
            export_as_image=objects.path_of(f"{pattern}.png", self.job_name),
        )
        if not success:
            return success

        self.G.add_node("X")
        for node in self.G.nodes:
            if self.G.in_degree(node) == 0 and node != "X":
                self.G.add_edge("X", node)

        for node in self.G.nodes:
            self.G.nodes[node]["command_line"] = (
                "workflow monitor node={},publish={} {}".format(
                    node,
                    int(node == "X"),
                    self.job_name,
                )
            )

        return self.post_metadata(
            "load_pattern",
            {"pattern": pattern},
        )

    def post_metadata(
        self,
        key: str,
        value: Any,
    ) -> bool:
        return post(
            key,
            value,
            source=self.job_name,
            source_type=MetadataSourceType.OBJECT,
        )

    def save(self) -> bool:
        return dot_file.save_to_file(
            objects.path_of(
                filename="workflow.dot",
                object_name=self.job_name,
            ),
            self.G,
        ) and self.post_metadata(
            "runner",
            {"type": self.runner_type},
        )
