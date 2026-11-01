"""Resolve bounded GS connections from uncertainty review DE-UZ-041."""
from pathlib import Path
import json

def append(T):
 T("freundschaft-andere-sicht3","Die Sicht eines anderen in einem Freundschaftsgespräch verstehen","186538","40305 40307 40309 40317","Unterschiedliche Sichtweisen zu einer überschaubaren Freundschaftssituation","","Die Lernenden können zum Umgang miteinander in einer Freundschaft begründet Stellung nehmen und dabei die geäußerten Probleme und Befindlichkeiten einer anderen Person berücksichtigen.","Begrenzt auf den FSP-Kontext Freundschaft und Umgang miteinander. Der ausdrückliche Zuhör- und Verständnisbezug trägt den Anschluss. Keine vollständige Abdeckung beliebiger Debatten, politischer Positionen oder schriftlicher Perspektivanalyse. Gefühle werden nicht als Meinungen gleichgesetzt; maßgeblich ist die geäußerte Sicht mit ihrem Anliegen oder Grund.",["186544"])
 T("sprichwort-ernte3","Ein Sprichwort zur Ernte in seinem Sinn verstehen","186769","40463 40470 40472","Ein Sprichwort mit Saat- oder Erntebezug und der zugehörige Sachzusammenhang der Getreideernte","","Die Lernenden können einen bekannten Sachverhalt zur Getreideernte früher oder heute im Zusammenhang mit einem passenden Sprichwort in Grundzügen wiedergeben. Anforderungsniveau: Kennen.","Anschluss nur bei einem tatsächlich zum Getreide-/Erntekontext passenden Sprichwort. Sprichwörter sind ein FSP-Bemerkungsbeispiel, kein verbindlicher Auftrag zur umfassenden Gattungs-, Herkunfts- oder Metaphernanalyse. Eine Bauernregel ist nicht automatisch ein Sprichwort. Der gemeinsame Bildbereich verbindet unterschiedliche GS- und FSP-Nachweise; ein bloßes Stichwort Ernte genügt nicht.",["186771","186772"])
 T("nomen-erscheinungen3","Nomen für nichtgegenständliche Erscheinungen erkennen","186789","40166 40175 40177","Ein erarbeitetes Nomen für eine nichtgegenständliche Erscheinung, beispielsweise Kälte","","Die Lernenden können ein bekanntes Substantiv als Bezeichnung einer erarbeiteten Erscheinung erkennen und die gemeinte Erscheinung verständlich benennen. Anforderungsniveau: Kennen.","Begrenzt auf nichtgegenständliche Erscheinungen. Kälte ist eine didaktische Konkretisierung, keine amtliche Wortliste. Die FSP-Kategorie Erscheinungen umfasst nicht ausschließlich Abstrakta und deckt die GS-Kategorie Gefühle nicht pauschal ab. Das kommunikative Äußern von Gefühlen wird nicht als Wortartklassifikation benutzt. Der GS-Rechtschreibrahmen ergänzt Schriftstrukturwissen, erweitert aber keine FSP-Ziele.",["186793","186795"])

def refine(cards):
 patches=json.loads((Path(__file__).parent/'batch_041_cards.json').read_text())
 assert set(patches).issubset({c['id'] for c in cards})
 for c in cards:
  if c['id'] in patches:
   cid=c['id']
   c.clear()
   c.update(patches[cid])
