"""Reviewed word and sentence level spelling goals, GS grade 3."""
from pathlib import Path
import json

def append(T):
 T('redezeichen3','Doppelpunkt und Anführungszeichen der wörtlichen Rede erkennen','186589','40202 40204','Eine bekannte Textstelle mit vorangestelltem Begleitsatz und wörtlicher Rede','bekannte Zeichenfunktionen erläutern','Wörtliche Rede an Doppelpunkt und Anführungszeichen erkennen.','GS3 Kennen; FSP3/4 Einblick gewinnen. Kein Komma- oder allgemeiner Verschriftungsanschluss.',['186597','186599','186601'])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_029_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
