"""Reviewed listening follow-up and writing skills for GS grade 3."""
from pathlib import Path
import json

def append(T):
 T('digitales-schreiben3','Ein digitales Schreibwerkzeug für eine Mitteilung nutzen','186584','40153 40159 40163','Eine kurze lesbare Mitteilung in einem Textprogramm','bekannte digitale Schreibfertigkeiten auf eine vergleichbare neue Mitteilung übertragen','Erarbeitete Textprogrammhandlungen am bekannten Beispiel zeigen.','GS3 Übertragen mit erprobendem Unterziel; FSP3/4 Kennen. Kein allgemeiner Werkzeug- oder Überarbeitungsanschluss.',['186588'])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_028_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
