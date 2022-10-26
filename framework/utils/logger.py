import logging


class Logger:
    __logger = logging.getLogger()
    file_handler = logging.FileHandler('logger.log', mode='w')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    __logger.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    __logger.addHandler(file_handler)
    _instance = __logger

    @staticmethod
    def info(message):
        Logger._instance.info(msg=message)

    @staticmethod
    def debug(message):
        Logger._instance.debug(msg=message)

    @staticmethod
    def warning(message):
        Logger._instance.warning(msg=message)

    @staticmethod
    def error(message):
        Logger._instance.error(msg=message)

    @staticmethod
    def fatal(message):
        Logger._instance.fatal(msg=message)

    @staticmethod
    def step(message):
        Logger._instance.info(msg=message)
