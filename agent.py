from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_openai import AzureChatOpenAI
from openai import AzureOpenAI
from config import (logger,
                    AZURE_OPENAI_API_BASE, AZURE_OPENAI_API_KEY,
                    AZURE_OPENAI_API_VERSION, AZURE_OPENAI_DEPLOYMENT_NAME)

def get_chat_model():
    """
    Initialize the Azure OpenAI chat model.
    """
    try:
        model = AzureChatOpenAI(
            deployment_name=AZURE_OPENAI_DEPLOYMENT_NAME,
            temperature=0,
            openai_api_key=AZURE_OPENAI_API_KEY,
            azure_endpoint=AZURE_OPENAI_API_BASE,
            api_version=AZURE_OPENAI_API_VERSION,
        )
        logger.info("Azure ChatOpenAI model initialized successfully.")
        return model
    except Exception as e:
        logger.error(f"Failed to initialize Azure ChatOpenAI model: {e}")
        raise

def get_sql_agent(llm, db):
    try:
        agent = create_sql_agent(
            llm=llm,
            db=db,
            verbose=True,
            agent_type="openai-tools",
        )
        logger.info("SQL Agent created successfully.")
        return agent
    except Exception as e:
        logger.error(f"Failed to create SQL Agent: {e}")
        raise
