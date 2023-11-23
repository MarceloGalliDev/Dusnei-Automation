# flake8: noqa
# pylint: disable=all
import logging
import os
from sqlalchemy import create_engine, exc
from dotenv import load_dotenv
import sys
sys.path.append('D:/Python/Dusnei-Automation')

load_dotenv()


def get_db_engine():
    try:
        db_url = os.getenv('DUSNEI_URL')
        engine = create_engine(db_url)
        # Test connection
        with engine.connect() as connection:  # noqa: F841
            print('Conexão estabelecida!')
            pass
        print('Banco de dados conectado!')
        return engine
    except exc.SQLAlchemyError as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    get_db_engine()
