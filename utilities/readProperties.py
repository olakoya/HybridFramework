import os
import configparser

config = configparser.RawConfigParser()
config.read(os.path.dirname(os.getcwd())+"//HybridFramework//configurations//config.ini")

class ReadConfig():
    @staticmethod
    def getEnvironment():
        return config.get('commonInfo', 'environment')

    @staticmethod
    def getApplicationURL():
        return config.get('commonInfo','baseURL')

    @staticmethod
    def getUseremail():
        return config.get('commonInfo','email')

    @staticmethod
    def getPassword():
        return config.get('commonInfo', 'password')

    @staticmethod
    def getEnvironment():
        return config.get('commonInfo', 'environment')


# config = configparser.RawConfigParser()
# config.read(os.path.dirname(os.getcwd())+"//HybridFramework//configurations//config.ini")
# class ReadConfig():
#     @staticmethod
#     def getApplicationURL():
#         url=(config.get('commonInfo','baseURL'))
#         return url
#     @staticmethod
#     def getUseremail():
#         username=(config.get('commonInfo','email'))
#         return username
#     @staticmethod
#     def getPassword():
#         password = (config.get('commonInfo', 'password'))
#         return password


