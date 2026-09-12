import logging
from pathlib import Path


def setup_logging():

    Path("day18ProductionLogging/logs").mkdir(
        exist_ok=True
    )

    logging.basicConfig(
        level=logging.INFO,

        format=(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(name)s - "
            "%(message)s"
        ),

        handlers=[
            logging.FileHandler(
                "day18ProductionLogging/logs/pipeline.log"
            ),

            logging.StreamHandler(),
        ],
    )