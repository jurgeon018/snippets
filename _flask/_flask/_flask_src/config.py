class Configuration:
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:1@localhost/test2'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123'
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
