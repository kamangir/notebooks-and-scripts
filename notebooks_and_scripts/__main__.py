from notebooks_and_scripts import NAME, VERSION, DESCRIPTION, ICON
from notebooks_and_scripts.logger import logger
from notebooks_and_scripts import README
from blueness.argparse.generic import main

main(
    ICON=ICON,
    NAME=NAME,
    DESCRIPTION=DESCRIPTION,
    VERSION=VERSION,
    main_filename=__file__,
    tasks={
        "build_README": lambda _: README.build(),
    },
    logger=logger,
)
