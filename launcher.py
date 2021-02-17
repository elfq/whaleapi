from pathlib import Path
from json import load

def loader(filename):
  with Path("data/facts.json").open() as f:
   return load(f)