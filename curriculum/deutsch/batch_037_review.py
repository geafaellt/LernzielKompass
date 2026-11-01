"""Review GS4 speaking, presenting and listening; DE-UZ-037."""
from pathlib import Path
import json

def append(T):
 T('fachbegriffe-informieren4','Fachbegriffe zu körperlichen Merkmalen verständlich erklären','186840','40241 40244 40250','Erarbeitete Sachbegriffe zu körperlichen Merkmalen von Jungen und Mädchen','','Bekannte Sachbegriffe im erarbeiteten Sachkontext verwenden.','Nur ausgewählter Fachwortschatz im benannten Kontext.',['186843'])
 T('fachbegriffe-gespraech4','Fachbegriffe zu körperlichen Merkmalen im Sachgespräch verwenden','186849','40241 40244 40250','Erarbeitete Sachbegriffe zu körperlichen Merkmalen von Jungen und Mädchen','','Bekannte Sachbegriffe im erarbeiteten Sachkontext verwenden.','Nur ausgewählter Fachwortschatz im benannten Kontext.',['186851'])
 T('rollenbeitrag-struktur4','Wesentliche Inhalte für einen eigenen Rollenbeitrag sicher gliedern','186859','40545 40546 40547 40548','Wesentliche Aussagen einer einzelnen Rolle in einer bekannten literarischen Szene','','Wesentliche Handlung des erarbeiteten Theatertextes wiedergeben und festhalten.','Nur bei Wahl von FSP-Wahlbereich 4; keine vollständige Präsentationsstrategie.',['186864','186865'])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_037_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
