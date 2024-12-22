import os
from dotenv import load_dotenv
import logging

# Load env vars
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Azure SQL
AZURE_SQL_SERVER = os.getenv("AZURE_SQL_SERVER")
AZURE_SQL_DATABASE = os.getenv("AZURE_SQL_DATABASE")
AZURE_SQL_USER = os.getenv("AZURE_SQL_USER")
AZURE_SQL_PASSWORD = os.getenv("AZURE_SQL_PASSWORD")
AZURE_SQL_DRIVER = os.getenv("AZURE_SQL_DRIVER", "ODBC Driver 18 for SQL Server")

# Azure OpenAI
AZURE_OPENAI_API_BASE = os.getenv("AZURE_OPENAI_API_BASE")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
