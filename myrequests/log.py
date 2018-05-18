import logging


class SingletonMeta(type):
    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


class MyLog(metaclass=SingletonMeta):
    def __init__(self):
        self._logger = logging.getLogger('MyRequests')
        self._set_logger()

    def _set_logger(self):
        self._logger.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
        cmd_handler = logging.StreamHandler()
        cmd_handler.setFormatter(formatter)
        file_handler = logging.FileHandler('MyRequestsError.log', mode='a', delay=True)
        file_handler.setLevel(logging.ERROR)
        file_handler.setFormatter(formatter)
        self._logger.addHandler(file_handler)
        self._logger.addHandler(cmd_handler)

    def info(self, message):
        self._logger.info(message)

    def warning(self, message):
        self._logger.warning(message)

    def error(self, message):
        self._logger.error(message)

    def switch_print_info(self, open_info=True):
        if open_info:
            self._logger.setLevel(logging.INFO)
        else:
            self._logger.setLevel(logging.WARNING)


logger = MyLog()

if __name__ == '__main__':
    logger2 = MyLog()
    print(logger is logger2)
    # logger.switch_print_info(False)
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    # logger.error('this is a logger error message')
