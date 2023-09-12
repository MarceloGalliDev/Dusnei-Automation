# flake8: noqa
# pylint: disable=all
import logging
import os
import sys
from sqlalchemy import create_engine, exc
from dotenv import load_dotenv


sys.path.append('Z:/repositório/Dusnei-Automation/log')
import log_config


load_dotenv()


def get_db_engine():
    logger = log_config.setup_logger('mccain_log.log')
    try:
        db_url = os.getenv('DUSNEI_URL')
        engine = create_engine(db_url)
        # Test connection
        with engine.connect() as connection:  # noqa: F841
            logger.info('Conexão estabelecida!')
            pass
        logger.info('Banco de dados conectado!')
        return engine
    except exc.SQLAlchemyError as e:
        logger.info(f"Error: {e}")
        return None


if __name__ == "__main__":
    get_db_engine()
