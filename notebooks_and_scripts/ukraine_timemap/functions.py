from abcli import file
from typing import Tuple
from abcli.modules import objects
import geopandas as gpd
from geojson import Point
from notebooks_and_scripts.ukraine_timemap import NAME
from notebooks_and_scripts.logger import logger

api_url = "https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json"


def ingest(
    object_name: str,
    sorted: bool = True,
    do_save: bool = True,
    verbose: bool = False,
) -> Tuple[bool, gpd.GeoDataFrame]:
    logger.info(f"{NAME}.ingest -> {object_name}")
    filename = objects.path_of(
        "ukraine_timemap.json",
        object_name,
        create=True,
    )

    gdf = gpd.GeoDataFrame()

    success = file.download(api_url, filename)
    if not success:
        return success, gdf

    success, list_of_events = file.load_json(filename)
    if not success:
        return success, gdf
    logger.info("{:,} event(s) ingested from the api.".format(len(list_of_events)))

    records = []
    failure_count = 0
    for event in list_of_events:
        try:
            point = Point(
                (
                    float(event["longitude"]),
                    float(event["latitude"]),
                )
            )
            record = {
                "geometry": point,
                "sources": ", ".join(event["sources"]),
                "id": event["id"],
                "description": event["description"],
                "date": event["date"],
                "location": event["location"],
                "graphic": event["graphic"],
                "associations": ", ".join(event["associations"]),
                "time": event["time"],
            }
        except Exception as e:
            logger.error(f"ingest failed:\nevent: {event}\nerror: {e}")
            failure_count += 1
            continue

        records.append(record)
    gdf = gpd.GeoDataFrame(records)

    gdf["date"] = gdf["date"].apply(
        lambda date: "/".join(
            [
                date.split("/")[2],
                date.split("/")[0],
                date.split("/")[1],
            ]
        )
    )

    if sorted:
        gdf = gdf.sort_values(by="date", ascending=False)

    logger.info("{:,} event(s) ingested into the gdf.".format(len(gdf)))
    if failure_count:
        logger.error(f"{failure_count:,} event(s) failed to ingest.")

    if do_save and not gdf.empty:
        if not file.save_geojson(
            objects.path_of("ukraine_timemap.geojson", object_name),
            gdf,
            log=verbose,
        ):
            return False, gdf

    return True, gdf
