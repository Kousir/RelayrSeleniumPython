import configparser

"""
To fetch the data from .ini file which will be implemented in the test suite
"""

config = configparser.RawConfigParser()
config.read('.//Configuration//conf.ini')

class Readconfig:
    @staticmethod
    def getURL():
        url = config.get('basic module data', 'URL')
        return url