import logging
import sys
LOG_LEVEL = "DEBUG"
PATH = './logs/log.log'

DEBUG_LOG_FORMAT = '%(asctime)s :: %(levelname)s :: %(pathname)s:%(lineno)d :: %(funcName)s :: %(message)s'
INFO_LOG_FORMAT = '%(asctime)s :: %(levelname)s :: %(filename)s:%(lineno)d :: %(funcName)s :: %(message)s'

DEFAULT_DATE_FORMAT = '%m/%d/%Y %H:%M:%S'
# -------------------------------
def get_log_level(log_level):
    """Returns log level.

    Args:
        log_level (str): Application environment.

    Returns:
        int: Log level.
    """
    if log_level in logging._nameToLevel:
        return logging._nameToLevel[log_level]
    else:
        return logging.INFO


def get_logger():
    """Rotated log creator.

    Args:

    Returns:
        logging.Logger: Logger.
    """
    logging.basicConfig(
        format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
        level=get_log_level(LOG_LEVEL))
    custom_logger = logging.getLogger(__name__)

    formatter = logging.Formatter(
        DEBUG_LOG_FORMAT,
        datefmt=DEFAULT_DATE_FORMAT
    )
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.ERROR)
    handler.setLevel(get_log_level(LOG_LEVEL))
    handler.setFormatter(formatter)

    custom_logger.addHandler(handler)
    custom_logger.propagate = False

    return custom_logger


logger = get_logger()
