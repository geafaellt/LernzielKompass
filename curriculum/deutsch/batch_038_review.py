"""GS4 writing and reading: ten previously open rows, DE-UZ-038."""
from pathlib import Path
import json

def append(T):
 T("digital-schreiben4","Eine Mitteilung sicher mit einem digitalen Schreibwerkzeug verfassen","186874","40153 40159 40163","Eine kurze lesbare Mitteilung in einem Textprogramm","","Die Lernenden können erarbeitete Bedienhandlungen zum Öffnen eines Textprogramms und Schreiben einer kurzen Mitteilung wiedergeben und am bekannten Beispiel zeigen. Anforderungsniveau: Kennen.","Begrenzter Anschluss digitaler Schreibwerkzeuge über das ausdrücklich genannte Schreiben im Textprogramm. Kein pauschaler Nachweis von Diktierfunktion, automatischer Korrektur, umfassender Formatierung oder Textüberarbeitung. Das Textprogramm ist curricularer Gegenstand; eine konkrete Software oder Hilfsmittelauswahl wird nicht vorgegeben.",["186877"])
 T("einladung-planung4","Textfunktion und Empfänger einer Einladung sicher berücksichtigen","186899","40320 40323","Die schriftliche Einladung zu einem neuen gemeinsamen Anlass","","Die Lernenden können bekannte schriftliche Gebrauchsformen und sprachliche Mittel für eine Einladung zu einem neuen Anlass situationsgerecht verwenden. Anforderungsniveau: Anwenden.","Nur der gemeinsame Ausschnitt Einladung. FSP nennt schriftliche Gebrauchsformen, Situationsbezug und sprachliche Mittel; das übergreifende Stufenbandziel berücksichtigt den Schreibanlass. Eine systematische Textsortenwahl, sämtliche Textfunktionen oder Auswahl von Präsentationsformen werden damit nicht vollständig abgedeckt.",["186900"])
 T("fantasie-fortsetzung4","Eine Fantasiegeschichte sicher und schlüssig schriftlich fortsetzen","186902","40488","Eine gemeinsame Fantasiegeschichte mit offenem Ende","","Die Lernenden können eine eigene Wunsch- oder Fantasieidee als erste Möglichkeit des Ausdrucks in einer Geschichtenfortsetzung erkennbar machen. Anforderungsniveau: Einblick gewinnen.","Begrenzt auf die eigene Fantasieidee in einer Geschichtenfortsetzung. Sie berührt kreatives und produktives Schreiben der GS; die strukturierende Zeile zu verschiedenen Schreibformen ist nur in diesem Ausschnitt angeschlossen. FSP nennt Fortsetzen und Beenden als Bemerkungsbeispiele zum Ausdrucksziel. Schriftlichkeit ist auf FSP-Seite nicht vorgeschrieben. Kein Gesamtanschluss für Umschreiben, kooperatives Schreiben oder sämtliche Schreibformen.",["186904","186906","186908"])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_038_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
