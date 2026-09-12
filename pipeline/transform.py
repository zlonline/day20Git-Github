import logging

import pandas as pd

logger = logging.getLogger(__name__)

def transform_customers(
    df: pd.DataFrame
) -> pd.DataFrame:

    logger.info(
        "Starting customer transformation"
    )

    result = df.copy()

    result["name"] = (
        result["name"]
        .str.strip()
        .str.title()
    )

    result["email"] = (
        result["email"]
        .str.strip()
        .str.lower()
    )

    result["updated_at"] = pd.to_datetime(
        result["updated_at"]
    )

    result = result.drop_duplicates(
        subset=["customer_id"]
    )

    result["city"] = (
        result["city"]
        .str.strip()
        .str.title()
    )

    logger.info(
        "Customer transformation completed"
    )

    return result