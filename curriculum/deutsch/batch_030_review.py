"""Reviewed dictionary procedures, text planning and writing forms, GS grade 3."""
from pathlib import Path
import json

def append(T):
 T('einladung-planen3','Schreibabsicht und Formulierungen einer Einladung klären','186620','40320 40323','Die schriftliche Einladung zu einem neuen gemeinsamen Anlass','eine bekannte Einladungsplanung auf einen neuen Anlass übertragen','Eine schriftliche Einladung situationsgerecht verwenden.','GS3 Übertragen beim Planen; FSP3/4 Anwenden der Gebrauchsform. Keine allgemeine FSP-Planungskompetenz.',['186622','186625'])
 T('mitteilung3','Einen eigenen Gedanken schriftlich mitteilen','186631','40126 40150','Eine kurze eigene Mitteilung mit einem Gedanken oder einer Beobachtung','bekannte Formulierungsweisen auf eine neue Mitteilung übertragen','Bekanntes Schreibwissen für eine neue eigene Mitteilung nutzen.','Nur kurze freie Mitteilung; kein umfassender schriftlicher Gefühlsausdruck.',['186634'])
 T('gebaeude-beschreiben3','Ein regionales historisches Gebäude schriftlich beschreiben','186631','40531 40532 40541','Ein historisches Gebäude einer gemeinsam erkundeten regionalen Anlage','eine bekannte Beschreibungsweise auf ein weiteres Gebäude übertragen','Merkmale der erkundeten Anlage in einfachen Sätzen beschreiben.','Nur bei gewähltem FSP-Wahlbereich 3, mit regionaler Erkundung.',['186636'])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_030_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
