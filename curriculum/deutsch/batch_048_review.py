"""Refine existing cards after individual source review DE-UZ-048."""
from pathlib import Path
import json

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_048_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
