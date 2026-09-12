import logging

from logging_config import setup_logging

from pipeline.extract import extract_customers
from pipeline.transform import transform_customers
from pipeline.validation import validate_customers
from pipeline.load import load_customers


logger = logging.getLogger(__name__)


def main():

    setup_logging()

    logger.info(
        "Starting pipeline"
    )

    watermark = "2026-09-01 00:00:00"

    try:

        df = extract_customers(
            watermark
        )

        if df.empty:

            logger.info(
                "No new data"
            )

            return

        df = transform_customers(
            df
        )

        validate_customers(
            df
        )

        load_customers(
            df
        )

        logger.info(
            "Pipeline completed successfully"
        )

    except Exception:

        logger.exception(
            "Pipeline failed"
        )

        raise


if __name__ == "__main__":
    main()