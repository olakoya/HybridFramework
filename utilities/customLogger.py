import os # specifying log file ie location of the log file dynamically
import logging

# from pkg_resources import file_ns_handler


class LogGen:
    @staticmethod
    def loggen(): # creating a method
        path = (os.path.abspath(os.getcwd()) + "//logs//automation.log") # getting current directory from the utilities package
        logger = logging.getLogger(__name__) # get a logger with the name of the current module i.e specify module name
        logger.setLevel(logging.DEBUG) # Capturing the log level e.d Debug log which is superior in the Warn>Debug>info>error>fatal log levels
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p') # date and time format in the log page
        file_handler = logging.FileHandler(path) # Create a file handler to write log messages
        file_handler.setFormatter(formatter) # Set the formatter for the file handler
        logger.addHandler(file_handler) # Add the file handler to the longer
        return logger # Return the configured logger