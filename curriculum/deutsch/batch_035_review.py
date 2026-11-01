"""Refine personal pronouns and add time markers in harvest context; DE-UZ-035."""
from pathlib import Path
import json

def append(T):
 T('zeitmarkierung-ernte3','Vergangenheit und Gegenwart beim Sprechen über Ernte unterscheiden','186789','40463 40470 40472','Erarbeitete Aussagen zur Getreideernte früher und heute mit eindeutigen Zeitbezügen','','Bekanntes über die Getreideernte früher und heute mit verständlichem Zeitbezug wiedergeben.','Nur Zeitmarkierungen im erarbeiteten Getreide-/Erntekontext; keine Tempusgrammatik oder Sprichwortdeutung.',['186805'])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_035_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
