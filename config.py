import os

class Config:

   	NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
   	ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'
   	NEWS_API_KEY = '7a7977d6a91a424eb4b03048da201678'
   	@staticmethod
   	def init_app(app):
   		pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig

}