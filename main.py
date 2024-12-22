import sys
from sqlalchemy.exc import SQLAlchemyError
from config import logger
from db import get_engine, initialize_database
from agent import get_chat_model, get_sql_agent

def main():
    llm = get_chat_model()
    engine = get_engine()
    db = initialize_database(engine)
    agent = get_sql_agent(llm, db)

    print("Welcome to the Azure SQL LangChain Agent!")
    print("Ask your questions below (type 'exit' to quit).")

    while True:
        user_input = input("\nYour Question: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            response = agent.run(user_input)
            print(f"\nAgent Response: {response}")
        except SQLAlchemyError as db_err:
            logger.error(f"Database error occurred: {db_err}")
            print(f"Database error occurred: {db_err}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)
