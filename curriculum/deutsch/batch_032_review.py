"""Reviewed GS3 reading comprehension and media access, DE-UZ-032."""
from pathlib import Path
import json

def append(T):
 T('gebrauchstext-einladung3','Merkmale einer schriftlichen Einladung erklären','186707','40320 40323','Eine schriftliche Einladung zu einer Klassenveranstaltung','','Eine schriftliche Einladung für einen neuen Anlass situationsgerecht verwenden.','Nur Gebrauchstext Einladung; GS Kennen und FSP Anwenden unterscheiden.',['186712'])
 T('informationsangebote-einrichtung3','Informationsangebote zu einer öffentlichen Einrichtung kennen','186717','40395 40396 40397','Informationsangebote über die Bedeutung einer örtlichen öffentlichen oder sozialen Einrichtung','','Erste Informationen zur Bedeutung der Einrichtung gewinnen.','Nur Einrichtungen und deren Bedeutung; keine allgemeine Suchmaschinenkompetenz.',['186722'])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_032_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
