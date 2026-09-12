import logging
from pathlib import Path

import pandas as pd

logger = logging.getLogger(__name__)

#OUTPUT_PATH = Path(
#    "output/customers.parquet"
#)
OUTPUT_PATH = Path(
    "day18ProductionLogging/output/customers.csv"
)

def load_customers(
    df: pd.DataFrame
) -> None:

    logger.info(
        "Starting customer load"
    )
    
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

 #   df.to_parquet(
 #       OUTPUT_PATH,
 #       index=False,
 #   )

    df.to_csv(
        OUTPUT_PATH,
        index=False,
    )

    logger.info(
        "Data loaded to %s",
        len(df),
    )