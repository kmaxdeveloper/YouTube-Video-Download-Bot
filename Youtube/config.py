import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8080910166:AAFxAxoUoaHyTouqlAAbva00908zw2ARGKs")
    API_ID = int(os.environ.get("API_ID",28545775))
    API_HASH = os.environ.get("API_HASH", "f6fc44cfb5b41d81531a9abe22194aad")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
