import logging

def test_loggingDemo() :
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)  #filehandler object

    logger.setLevel(logging.DEBUG)
    logger.debug("A debud statement is executed")
    logger.info("information ststement")
    logger.warning("Something is warning mode")
    logger.error("A major has happend")
    logger.critical("critical issue")
