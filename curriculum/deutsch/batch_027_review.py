"""Bounded presentation and listening review, preserving card IDs."""
from pathlib import Path
import json

def append(T):
 T('rollenbeitrag-vorbereiten3','Wesentliche Inhalte für einen Rollenbeitrag festhalten','186548','40545 40546 40547 40548','Wesentliche Aussagen einer einzelnen Rolle in einer bekannten literarischen Szene','ein bekanntes Auswahl- und Strukturierungsverfahren auf einen vergleichbaren neuen Rollenbeitrag übertragen','Wesentliches eines bekannten geeigneten Theatertextes wiedergeben und schriftlich festhalten.','Nur bei tatsächlicher Wahl des FSP-Wahlbereichs 4; kein allgemeiner Strategie- oder Auswendiglernanschluss.',['186551','186552','186553'])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_027_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
