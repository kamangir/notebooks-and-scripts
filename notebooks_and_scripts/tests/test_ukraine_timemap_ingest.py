from abcli.modules import objects
from notebooks_and_scripts.ukraine_timemap.functions import ingest


def test_ukraine_timemap_ingest():
    object_name = objects.unique_object()

    assert ingest(object_name)