"""Refine GS3 language forms and communication; DE-UZ-034."""
from pathlib import Path
import json

def append(T):
 T('blumennamen3','Blumennamen sprachlich entdecken','186769','40463 40475 40476 40478','Ein erarbeiteter Blumenname mit auffälliger Wortgestalt oder Bedeutung und die zugehörige Blume','','Eine bekannte Blume benennen, unterscheiden und eine sprachliche Besonderheit ihres Namens wiedererkennen.','Nur Blumennamen im Pflanzenkontext; keine vollständige Namenkunde oder Wortforschung.',['186771','186774','186776'])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_034_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
