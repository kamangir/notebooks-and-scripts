from abcli import file
from abcli.modules import objects
import geopandas as gpd
import geojson
from geojson import Feature, Point, FeatureCollection
from notebooks_and_scripts.ukraine_timemap import NAME
from notebooks_and_scripts.logger import logger

api_url = "https://bellingcat-embeds.ams3.cdn.digitaloceanspaces.com/production/ukr/timemap/api.json"


def ingest(
    object_name: str,
    verbose: bool = False,
) -> bool:
    logger.info(f"{NAME}.ingest -> {object_name}")
    filename = objects.path_of("api.json", object_name)

    success = file.download(api_url, filename)
    if not success:
        return success

    success, list_of_events = file.load_json(filename)
    if not success:
        return success
    logger.info("{:,} events(s) ingested.".format(len(list_of_events)))

    records = []
    failure_count = 0
    for event in list_of_events:
        try:
            point = Point(float(event["longitude"]), float(event["latitude"]))
            record = {
                "geometry": point,
                "sources": event["sources"],
                "id": event["id"],
                "description": event["description"],
                "date": event["date"],
                "location": event["location"],
                "graphic": event["graphic"],
                "associations": event["associations"],
                "time": event["time"],
            }
        except Exception as e:
            logger.error(f"ingest failed:\nevent: {event}\nerror: {e}")
            failure_count += 1
            continue

        records.append(record)
    gdf = gpd.GeoDataFrame(records)

    logger.info(f"ingested {len(gdf)} event(s).")
    if failure_count:
        logger.error(f"failed to ingest {failure_count} event(s).")

    if not len(gdf):
        return True

    return file.save_geojson(
        objects.path_of("api.geojson", object_name),
        gdf,
        log=verbose,
    )
