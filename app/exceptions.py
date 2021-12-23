# Exceptions of App

class _KaggleException(BaseException):
    """Exceptions involving Kaggle functionality"""
    pass


class KaggleKeysFile(_KaggleException):
    """Kaggle file API keys not founded on app"""
    pass


class KaggleKeysEnviron(_KaggleException):
    """Kaggle API keys not founded on environ app"""
    pass

class KaggleTokenInvalid(_KaggleException):
    """Kaggle Token Invalid"""
    pass


class _ETLExceptions(BaseException):
    """Base Exceptions of ETL execution"""
    pass


class LevelETLException(_ETLExceptions):
    """Level not defined to run"""
    pass
