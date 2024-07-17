import logging

def test_logging():
    logger = logging.getLogger(__name__)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s: %(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.setLevel(logging.DEBUG)     ####### from info level it will print the logs till critical (Info to critical)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in waning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")