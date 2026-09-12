import logging

import pyodbc

from config import (
    DB_SERVER,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)

logger = logging.getLogger(__name__)

def get_connection():

    logger.info(
        "Connecting to SQL Server"
    )


    connection_string = (

        "DRIVER={ODBC Driver 18 for SQL Server};"

        f"SERVER={DB_SERVER};"

        f"DATABASE={DB_NAME};"

        f"UID={DB_USER};"

        f"PWD={DB_PASSWORD};"

        "TrustServerCertificate=yes;"

    )


    conn = pyodbc.connect(
        connection_string
    )


    logger.info(
        "Database connection successful"
    )


    return conn