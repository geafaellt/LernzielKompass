"""Own book as one bounded presentation form, FSP elective required."""
def append(T):
 T('buchpraesentation12','Ein eigenes Buch als Präsentationsform erproben','186466','39950','Ein eigenes kleines Buch mit Text und Bild','das Vorstellen eines eigenen Buches als eine Form der Textpräsentation erproben','Sprachwissen beim verständlichen Vorstellen und Lesen des eigenen Buches in einer neuen Präsentationssituation anwenden.','Nur eine Präsentationsform; die GS-Forderung verschiedener Formen bleibt darüber hinaus offen. FSP1/2 Wahlbereich 2 Mein Buch ist Voraussetzung. Buchherstellung ist ein gesondertes FSP-Ziel und hier kein Ersatz für sprachliches Vorstellen und Lesen. Leporello, Faltbuch und Lapbook sind GS-Bemerkungen und keine ausdrücklich benannten FSP-Formate.',['186472'])
def refine(cards):
 for c in cards:
  if c['id']=='DE-146':
   c['fine_goals'][0]['criterion']='Ein erster Versuch der Präsentation des eigenen Buches macht einen Inhalt für andere erkennbar. Die Verbindung von Text und Bild wird einbezogen; routinierter Vortrag oder Vergleich mehrerer Formate ist nicht vorausgesetzt.'
   c['fine_goals'][1]['criterion']='In der neuen Präsentationssituation werden Inhalte des eigenen Buches sprachlich verständlich vorgestellt und ausgewählte Textanteile gelesen. Erarbeitetes Sprachwissen wird passend eingesetzt; bloßes Zeigen oder Herstellen des Buches genügt nicht.'
   c['app_review_message']=c['review_note']+' Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlung/Aufgabe und Hilfsmittel bestimmt ausschließlich die Lehrkraft.'
