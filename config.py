import os

class Config:
    


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}
