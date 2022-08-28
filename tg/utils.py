import logging

logger = logging.getLogger(__name__)


def log(func):
    def wrapper(*args):
        event = args[0]
        log_msg = f'User: {event.from_user} Msg: "{event.text}"'
        logger.info(log_msg)
        return func(*args)
    return wrapper