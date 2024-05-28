from notebooks_and_scripts import NAME, VERSION, DESCRIPTION, ICON
from notebooks_and_scripts.logger import logger
from blueness.argparse.generic import main

success, message = main(__file__, NAME, VERSION, DESCRIPTION, ICON)
if not success:
    logger.error(message)
