from logging import Formatter, handlers, StreamHandler, getLogger, DEBUG

class Logger:

    _unique_instance = None

    def __init__(self, name=__name__):
        self.logger = getLogger(name)
        self.logger.setLevel(DEBUG)
        formatter = Formatter("[%(asctime)s] [%(process)d] [%(name)s] [%(levelname)s] %(message)s")

        # stdout
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # file
        handler = handlers.RotatingFileHandler(filename = 'backup.log',
                                               maxBytes = 1048576,
                                               backupCount = 3)
        handler.setLevel(DEBUG)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)



    @classmethod
    def get_instance(cls):
        if not cls._unique_instance:
            cls._unique_instance = cls()

        return cls._unique_instance

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)