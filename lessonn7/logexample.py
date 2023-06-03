from logging import debug, info, warning, error, critical, basicConfig, DEBUG, CRITICAL


class ILog:
    def __init__(self, message=""):
        self.Message = message

    def __str__(self):
        if self.Message == "" or self.Message == None:
            raise Exception("Log message is empty!")
        return self.Message

    def ConfigLog(self, level, filename):
        format = "%(asctime)s : %(levelname)s - %(message)s"
        basicConfig(level=level, filemode='a', filename=filename, format=format)

    def LogData(self, filename, level=DEBUG):
        self.ConfigLog(level, filename)
        debug(self.__str__())
        info(self.__str__())
        warning(self.__str__())
        error(self.__str__())
        critical(self.__str__())
