from flask import Flask
from launcher import loader
app = Flask('app')
facts = loader("facts")
facts_load = facts["whale_facts"]



def one_fact(facts_load):
  data = {
   "status": "200",
   "fact": facts_load
  }
  return data
