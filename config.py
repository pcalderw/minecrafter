import json

def init(app):
    with open('config.json') as f:
        config = json.load(f)
        for key in config:
           app.config[key] = config[key] 

