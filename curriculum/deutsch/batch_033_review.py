"""Refine GS3 literary understanding, media use and presentation; DE-UZ-033."""
from pathlib import Path
import json

def append(T):
 T('buchpraesentation3','Ein eigenes Buch als Textpräsentation verwenden','186746','39950','Ein eigenes kleines Buch mit Text und Bild','','Sprachwissen beim Vorstellen und Lesen des Buches anwenden.','Nur bei Wahl des FSP1/2-Wahlbereichs 2; eine Präsentationsform.',['186750'])
 T('freizeit-medienreflexion3','Digitale Freizeitangebote und eigene Nutzung einschätzen','186739','40324 40326 40332','Ein bekanntes digitales Freizeitangebot und seine Bedeutung für die eigene Freizeit','','Eine begründete Position zur medialen Freizeitgestaltung vertreten.','Nur Freizeitkontext; allgemeine Medienbildung ergänzt den konkreten Tabellenanker.',['186743','186744'])
 T('maerchen-position3','Zum Verhalten einer Märchenfigur Stellung nehmen','186726','39882 39888 39891','Eine ausgewählte Handlung einer Märchenfigur','','Das Verhalten der Märchengestalt begründet einschätzen.','Stufenübergreifend GS3/FSP1/2; nur Figurenverhalten im Märchen.',['186728'])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_033_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
