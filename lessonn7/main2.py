from logexample import ILog
from logging import DEBUG, CRITICAL
try:
    log = ILog("Lesson 8 - logging")
    log.LogData(level=DEBUG, filename="logs.log")
except Exception as ex:
    print(ex)