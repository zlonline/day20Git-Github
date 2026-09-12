import logging

import pandas as pd

logger = logging.getLogger(__name__)

def validate_customers(
    df: pd.DataFrame
) -> None:

    logger.info(
        "Starting customer validation"
    )

    required_columns = [
        "customer_id",
        "name",
        "email",
        "city",
        "updated_at",
    ]

    for column in required_columns:

        if column not in df.columns:

            raise ValueError(
                f"Missing column: {column}"
            )

    if df["customer_id"].isnull().any():

        raise ValueError(
            "customer_id contains NULL"
        )
# validate customer_id if it's duplicated
    if df["customer_id"].duplicated().any():

        raise ValueError(
            "Duplicate customer_id found"
        )
# validate updated_at is not null
    if df["updated_at"].isnull().any():

        raise ValueError(
            "updated_at contains NULL"
        )
# validate email format
    invalid_email = ~df["email"].str.contains(
        "@",
        na=False
        )

    if invalid_email.any():

        raise ValueError(
        "Invalid email found"
       )

    logger.info(
        "Validation passed"
    )
