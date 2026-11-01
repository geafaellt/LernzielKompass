"""Observe differences and try communication forms without overstating GS level."""
def refine(cards):
 for c in cards:
  if c['id']=='DE-094':
   c['fine_goals'][0]['goal']='Die Lernenden können mündliches und schriftliches Einladen erproben und einen ersten Unterschied beider Kommunikationsformen am selben Anlass erkennen. Anforderungsniveau: Einblick gewinnen.'
   c['fine_goals'][0]['criterion']='Beide Formen werden erprobt. Eine zutreffende erste Beobachtung zu ihrer Verständigungssituation wird erkennbar, etwa zur unmittelbaren Rückfragemöglichkeit im persönlichen Gespräch gegenüber einem übergebenen Einladungstext. Keine vollständige Erklärung einer Kommunikationstheorie verlangt.'
   c['fine_goals'][1]['criterion']='Für einen neuen Anlass werden eine mündliche und eine schriftliche Einladung situationsgerecht formuliert. Beide enthalten die nötigen Angaben; die sprachliche Form passt zum jeweiligen Kommunikationsweg. Bloßes Benennen von Unterschieden erfüllt Anwenden nicht.'
   note=' Die GS-Unterziele Unterschiede erkennen und Kommunikationssituationen erproben sind nur am Beispiel Einladung angeschlossen. FSP verlangt die situationsgerechte Verwendung beider Formen, keinen theoretischen Medienvergleich. Nähe/Distanz sowie Mimik/Gestik bleiben konkretisierende GS-Bemerkungen; keine pauschale Abdeckung sämtlicher Aspekte. Mündlich wird nicht generell mit Nähe und schriftlich nicht generell mit Distanz gleichgesetzt.'
   c['review_note']+=note
   c['operator_relation']+=note
   c['app_review_message']=c['review_note']+' Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlung/Aufgabe und Hilfsmittel bestimmt ausschließlich die Lehrkraft.'
