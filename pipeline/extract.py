import logging

import pandas as pd

from database import get_connection

logger = logging.getLogger(__name__)

def extract_customers(watermark):
    logger.info(
        "Starting customer extraction"
    )
    query = """
        SELECT
            customer_id,
            name,
            email,
            city,
            updated_at
        FROM dbo.Customers
        WHERE updated_at > ?
        ORDER BY updated_at
    """

    conn = get_connection()

    try:

        df = pd.read_sql(
            query,
            conn,
            params=[watermark],
        )

        logger.info(
            "Extracted %s rows",
            len(df),
        )
        
        return df
    
    except Exception:

        logger.exception(
            "Customers extraction failed"
        )
        raise
    
    finally:

        conn.close()

        logger.info(
            "Database connection closed"
        )   