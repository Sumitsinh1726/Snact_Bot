
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = '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'

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
