import logging
import datetime
from logging.handlers import TimedRotatingFileHandler

class GetLoggerObj:

    def get_logger(self, fname,ctime):
        # Create a custom logger
        logger = logging.getLogger(fname)
        print(fname)
        # Create handlers
        #now = datetime.datetime.now()
        logfilenm = fname + ctime.strftime("%Y%m%d%H%M%S") + '.log'
        print(logfilenm)
        f_handler = logging.FileHandler(logfilenm, mode='a')

        # Create formatters and add it to handlers
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)

        #---Add handlers to the logger, must clear old handlers, otherwise see duplicate entries in logs****
        if (logger.hasHandlers()):
            logger.handlers.clear()

        logger.addHandler(f_handler)

        #Set log level
        logger.setLevel(logging.INFO)

        logger.info("This is the logger object")

        return logger

    """
    Use for bill_generator, and rotate log files every day
    """
    def get_timerotatelogger(self, fname):
        # Create a custom logger

        # Create handlers
        #now = datetime.datetime.now()
        logfilenm = fname + '.log'
        print(logfilenm)
        f_handler = logging.FileHandler(logfilenm, mode='a')

        # Create formatters and add it to handlers
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        f_handler = TimedRotatingFileHandler(logfilenm,
                                           when='midnight',
                                            #when='M',interval=2,
                                           backupCount=10)

        f_handler.setFormatter(f_format)
        logger = logging.getLogger(fname)

        #---Add handlers to the logger, must clear old handlers, otherwise see duplicate entries in logs****
        if (logger.hasHandlers()):
            logger.handlers.clear()

        logger.addHandler(f_handler)

        #Set log level
        logger.setLevel(logging.INFO)

        logger.info("This is the logger object")

        return logger