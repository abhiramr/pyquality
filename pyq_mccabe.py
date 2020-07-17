'''
Take an input file and based on type convert into dataframe, get the description for that dataset and return it.
This is to illustrate McCabe complexity.
'''
import pandas as pd
import logging
import sys

logger = logging.getLogger('pyq2')
logging.basicConfig(level = logging.DEBUG)

class PandasClass:
    def __init__(self):
        pass

    def file_desc(self, fileName):
        extension = fileName.split(".")[-1]
        logger.info('Extension = {}'.format(extension))
        if  extension == "csv":
            df = pd.read_csv(fileName)
            logger.info("Processing CSV.")
            logger.debug("Top 5 states based on num of CBSE schools\n{}".format(df["state"].value_counts().head()))
        elif extension == "json":
            logger.info("Processing JSON.")
            df = pd.read_json(fileName)
            logger.debug("Top 5 states based on num of CBSE schools\n{}".format(df["state"].value_counts().head()))
        else:
            logger.info("Unsupported extension.")

filename = sys.argv[1]
pdObj = PandasClass()
logger.info("File name - {}".format(filename))
pdObj.file_desc(filename)