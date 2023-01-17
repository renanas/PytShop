# IMPORTS
from flask import Flask

# IMPORT HELLO
from clientController import client_ct
from AnimalController import animal_ct

# APP SETUP
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

print('route /client GET')
app.register_blueprint(client_ct, url_prefix='/client')

print('route /animal GET')
app.register_blueprint(animal_ct, url_prefix='/animal')

app.run()
