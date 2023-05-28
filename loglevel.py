from enum import Enum

#Log Levels
class LogLevel(Enum):
    INFO = 0
    ERROR = 10
    DEBUG = 20
    
    @staticmethod
    def get(value):
        for level in LogLevel:
            if(value == level.value):
                return level
        return LogLevel.INFO