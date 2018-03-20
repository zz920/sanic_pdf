from sanic.log import logger, error_logger


class InfoLog():

    @classmethod
    def dump(cls, message):
        logger.info(message)


class ErrorLog():

    @classmethod
    def dump(cls, message):
        logger.error(message)
