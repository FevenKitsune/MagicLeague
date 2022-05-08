import logging
import os
import sqlite3

config_db = sqlite3.connect(os.environ['MAGICLEAGUE_DATABASE'])
config_db.text_factory = str
logger = logging.getLogger(__name__)


def init() -> None:
    logger.info("Database initialization called. Checking for table...")
    init_cursor = config_db.cursor()
    init_cursor.execute("SELECT count(*) "
                        "FROM sqlite_master "
                        "WHERE type='table' and name='config'")
    if init_cursor.fetchone()[0] == 1:
        logger.info("Configuration table found.")
    else:
        logger.warning("Configuration table was not found. Creating table...")
        init_cursor.execute("CREATE TABLE config {"
                            "id     TEXT,"
                            "name   TEXT,"
                            "value  TEXT"
                            "}")
        config_db.commit()
        logger.warning("Configuration table has been created.")

    init_cursor.close()
    return


def get_configuration(guild_id: str, parameter: str) -> str:
    return


def set_configuration(guild_id: str, parameter: str, value: str) -> str:
    return


def add_configuration(guild_id: str, parameter: str, value: str) -> str:
    return


def remove_configuration(guild_id: str, parameter: str, value: str) -> str:
    return


def clear_configuration(guild_id: str, parameter: str):
    return
