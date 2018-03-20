from sanic.log import logger


class InfoLog():
    """
    Info Log shaper class
    """
    @classmethod
    def dump(cls, message):
        logger.info(message)


class ErrorLog():
    """
    Error Log shaper class
    """
    @classmethod
    def dump(cls, message):
        logger.error(message)
