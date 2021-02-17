from flask import Flask
from launcher import loader
import random
from api.ext import one_fact
app = Flask('app')
facts = loader("facts")
facts_load = facts["whale_facts"]



@app.route('/')
def main_entry():
 return '{"endpoints":"/facts/random"}'

@app.route("/facts/random")
def random_fact():
 return one_fact(random.choice(facts_load))

app.run(host='0.0.0.0', port=8080)