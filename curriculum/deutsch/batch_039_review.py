"""GS4 reading and media: ten individually reviewed rows, DE-UZ-039."""
from pathlib import Path
import json

def append(T):
 T("buchpraesentation4","Ein eigenes Buch sicher als Textpräsentation verwenden","186994","39950","Ein eigenes kleines Buch mit Text und Bild","","Die Lernenden können: Sprachwissen beim verständlichen Vorstellen und Lesen des eigenen Buches in einer neuen Präsentationssituation anwenden.","Nur das sprachliche Vorstellen und Lesen eines eigenen Buches. Digitale Textgestaltung, Plakat und Fotogalerie sind GS-Bemerkungsbeispiele und hier nicht abgedeckt. FSP-Buchherstellung ist ein gesondertes Ziel und ersetzt die sprachliche Präsentation nicht. Die GS-Vielfalt verschiedener Formen bleibt als Restumfang bestehen.",["187000"])
 T("medienerfahrung-freizeit4","Eigene Erfahrungen mit digitalen Freizeitangeboten beschreiben und einordnen","186953","40324 40326 40332","Ein bekanntes digitales Freizeitangebot und seine Bedeutung für die eigene Freizeit","","Die Lernenden können die Nutzung eines bekannten digitalen Freizeitangebots gegenüber einer nichtmedialen Freizeitmöglichkeit begründet einschätzen und eine eigene Position vertreten. Anforderungsniveau: Sich positionieren.","Nur eigene Erfahrungen mit digitalen Medien in der Freizeit. FSP nennt mediale und nichtmediale Angebote sowie den Austausch darüber; die allgemeinen Grundlagen ergänzen Wirkungen eigenen medialen Handelns und bewusste Alternativen. Kein Gesamtanschluss für sämtliche digitalen Leseerfahrungen, ein Medientagebuch oder eine Glaubwürdigkeitsprüfung. Beschreiben und begründetes Sich-Positionieren bleiben getrennte Anforderungen. Keine Offenlegung privater Nutzungsdaten.",["186965","186969"])
 T("glueckwunsch-merkmale4","Merkmale eines schriftlichen Glückwunsches erklären","186944","40320 40322","Ein schriftlicher Glückwunsch zu einem persönlichen oder gemeinsamen Anlass","","Die Lernenden können einen schriftlichen Glückwunsch für einen neuen Anlass situations- und empfängerbezogen verwenden. Anforderungsniveau: Anwenden.","Begrenzt auf den ausdrücklich im FSP genannten Glückwunsch in schriftlicher Form. Für GS4 muss dieser Text das bereits erarbeitete Textrepertoire erweitern; andernfalls ist diese Karte für das Ziel weiterer Texte nicht passend. Der konkrete Lernstand ist durch die Lehrkraft zu prüfen. Keine Vollabdeckung aller Sach- und Gebrauchstexte und keine Gleichsetzung von Merkmalskenntnis mit Textproduktion.",["186947"])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_039_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
