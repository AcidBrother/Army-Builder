from __future__ import print_function
from pprint import pprint
from flask import Flask
from flask import render_template
from unit import *
from loader import *
import json
#export FLASK_APP=server

app = Flask(__name__)

print("")
print("⣿⣿⣿⣿⣿⣿⠏⠌⣾⣿⣿")
print("⣿⣿⣿⣿⣿⠀⠀⠸⠿⣿⣿⣿")
print("⣿⣿⣿⣿⠃⠀⣠⣾⣿⣿⣿")
print("⣿⣿⡿⠃⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿")
print("⣿⣿⠃⠀⠀⣾⣿⣿⣿⣿⣿⣦⠀⠈⠻⣿⣿⣿")
print("⣿⣿⠀⠀⠀⣿⣿⣿⠟⠉⠉⠉⢃⣤⠀⠈⢿⣿⣿⣿")
print("⣿⣿⠀⠀⠀⢸⣿⡟⠀⠀⠀⠀⢹⣿⣧⠀⠀⠙⣿⣿")
print("⣿⣿⡆⠀⠀⠈⠻⡅⠀⠀⠀⠀⣸⣿⠿⠇⠀⠀⢸⣿")
print("⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠔⠛⠁⠀⠀⠀⣠⣿⣿")
print("⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿")
print("⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿")
print("⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿")
print("⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢰⣿")
print("⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿")
print("⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿")
print("⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿")
print("⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿")
print("⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿")
print("")

jnecro1 = jsonFromFile("necro1")
print(toJSON(fromJSON(jnecro1)))

@app.route("/")
def list_units():
    return render_template('list_units.html')

@app.route('/necrons/')

@app.route('/unit/')
@app.route('/unit/<name>')
def unit(name=None):
    if (name=="necw"):
        return render_template('unit.html',n=n1)
    if (name=="cads"):
        return render_template('unit.html',n=n2)
