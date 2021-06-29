import configparser

#Method to read from the config.ini file

config = configparser.RawConfigParser()
config.read('.//Configuration//conf.ini')

class Readconfig:
    @staticmethod
    def getURL():
        url = config.get('basic module data', 'URL')
        return url