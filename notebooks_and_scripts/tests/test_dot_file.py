import pytest
from abcli import file
from abcli.modules import objects
from notebooks_and_scripts.workflow import dot_file
from notebooks_and_scripts.workflow.patterns import list_of_patterns


@pytest.mark.parametrize(
    ["pattern"],
    [[pattern] for pattern in list_of_patterns()],
)
def test_dot_file(pattern: str):
    object_name = objects.unique_object()

    filename = file.absolute(
        f"../workflow/patterns/{pattern}.dot",
        file.path(__file__),
    )

    success, G = dot_file.load_from_file(
        filename,
        export_as_image=objects.path_of(f"{pattern}-loaded.png", object_name),
    )
    assert success

    assert dot_file.save_to_file(
        objects.path_of(f"{pattern}.dot", object_name),
        G,
    )

    assert dot_file.export_graph_as_image(
        G,
        objects.path_of(f"{pattern}-exported.png", object_name),
    )
