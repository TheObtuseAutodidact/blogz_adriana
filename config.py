import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xf82\x1b\xbb\xd1\xf6\x8bp\xbf\xd5\xbb\xa0\xd93]\xc1\x9c\x14\xc3\x9a\xf5\x1aI\xc9\xbb'
    # SECRET_KEY = os.urandom(25)
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
