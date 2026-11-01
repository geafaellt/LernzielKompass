"""Reproducible, individually reviewed intersections for batch DE-UZ-026."""
from pathlib import Path
import json

def append(T):
 T('informieren-haushalt3','Über eine häusliche Tätigkeit berichten','186526','39579 39597 39600','Ein sachlicher Bericht über eine vertraute, überschaubare Tätigkeit im häuslichen Umfeld','über eine vertraute Tätigkeit sachlich berichten','Eine vertraute häusliche Tätigkeit benennen und darüber berichten.','Nur häuslicher Kontext, GS3 Kennen zu FSP1/2 Kennen.',['186528'])
 T('wortschatz-lage3','Räumlichen Wortschatz verständlich verwenden','186526','39794','Eine mündliche Suchanweisung zu einem Gegenstand im Klassenraum','bekannte Lagewörter passend verwenden und erläutern','Lagewörter an einer neuen räumlichen Anordnung selbst auswählen.','Nur räumlicher Wortschatz; GS3 Kennen zu FSP1/2 Anwenden.',['186530'])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_026_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
