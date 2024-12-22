import urllib.parse
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from langchain_community.utilities import SQLDatabase
from config import (logger, AZURE_SQL_SERVER, AZURE_SQL_DATABASE,
                    AZURE_SQL_USER, AZURE_SQL_PASSWORD,
                    AZURE_SQL_DRIVER)

# Prepare connection string
encoded_password = urllib.parse.quote_plus(AZURE_SQL_PASSWORD)
encoded_driver = urllib.parse.quote_plus(AZURE_SQL_DRIVER)
connection_string = (
    f"mssql+pyodbc://{AZURE_SQL_USER}:{encoded_password}@{AZURE_SQL_SERVER}/"
    f"{AZURE_SQL_DATABASE}?driver={encoded_driver}&TrustServerCertificate=yes"
    "&Encrypt=yes&Connection Timeout=30"
)

def get_engine():
    try:
        engine = create_engine(
            connection_string,
            connect_args={
                "driver": AZURE_SQL_DRIVER,
                "TrustServerCertificate": "yes",
                "Encrypt": "yes"
            },
            pool_pre_ping=True
        )
        # Test the connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        logger.info("Database connection successful.")
        return engine
    except SQLAlchemyError as e:
        logger.error(f"Failed to connect to the database: {e}")
        raise

def initialize_database(engine):
    """
    Initialize SQLDatabase with proper configuration,
    including custom table info.
    """
    custom_table_info = {
        # ... your existing table descriptions ...
        # could be table description, along with each column description
        # Example:
        #BT_TRANSACTIONS": "Contains budget transactions with amount, date, and category:\n"+ "COLUMNS:\n"+ "BRT_DOC=Unique Document Number or Transaction ID identifying a specific budget or financial transaction. \n"
    }
    
    try:
        db = SQLDatabase(
            engine,
            include_tables=['YOUR_TABLES'],
            sample_rows_in_table_info=5,
            custom_table_info=custom_table_info,
            schema='dbo'
        )
        logger.info("SQLDatabase initialized successfully.")
        return db
    except Exception as e:
        logger.error(f"Failed to initialize SQLDatabase: {e}")
        raise
