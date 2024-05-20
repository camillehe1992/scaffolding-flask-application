import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = "mysql://user@localhost/foo"


class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", default="Thisisasecret")
    # SMTP
    SMTP_HOST = os.environ.get("SMTP_HOST", default="smtp.qq.com")
    SMTP_PORT = os.environ.get("SMTP_PORT", default=465)
    SMTP_USER = os.environ.get("SMTP_USER", default="")
    SMTP_PASS = os.environ.get("SMTP_PASS", default="")
    # Database
    DATABASE_URI = os.environ.get("DATABASE_URI", default="")
    DB_HOST = os.environ.get("DB_HOST", default="")
    DB_PORT = os.environ.get("DB_PORT", default=3306)
    DB_USER = os.environ.get("DB_USER", default="")
    DB_PASS = os.environ.get("DB_PASS", default="")
    DB_NAME = os.environ.get("SMTP_PASS", default="demo")


class LocalConfig(Config):
    DEBUG = True
    SECRET_KEY = "Thisisasecret"
    # SMTP
    SMTP_HOST = "locahost"
    SMTP_PORT = 2525
    SMTP_USER = "no-reply@example.com"
    # Database
    DATABASE_URI = ""
    DB_HOST = "127.0.0.1"
    DB_PORT = 3306
    DB_USER = "root"
    DB_PASS = "mysql123"
    DB_NAME = "demo"
