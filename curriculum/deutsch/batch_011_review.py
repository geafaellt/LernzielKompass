"""Bounded syllable and sentence reading; retain teacher-owned planning fields."""
def refine(cards):
 for c in cards:
  if c['id']=='DE-051':
   c['fine_goals'][0]['goal']='Die Lernenden können Silben in Wörtern sicher erfassen und Wörter sowie kurze Sätze sinnverstehend lesen. Anforderungsniveau: Beherrschen.'
   c['fine_goals'][0]['criterion']='Die vereinbarten Silben werden in Wörtern zuverlässig zusammengelesen; Wörter und kurze Sätze werden sicher gelesen und ihr Sinn zutreffend wiedergegeben. Silbenmarkierungen sind eine mögliche methodische Unterstützung, kein zusätzliches Lernziel.'
   c['fine_goals'][1]['criterion']='Bekannte Laut-Buchstaben-Beziehungen werden auf noch nicht bearbeitete Silbenkombinationen in Wörtern und einen kleinen Text übertragen; die Wörter werden selbst erlesen und eine Inhaltsfrage zutreffend beantwortet. Kein automatisiertes Lesen sämtlicher Funktionswörter vorausgesetzt.'
   note=' Ergänzter Ausschnitt: Silben beim Lesen von Wörtern. GS-Silbenmarkierungen sind eine Bemerkung; daraus wird kein verbindliches Hilfsmittel abgeleitet.'
   c['review_note']+=note;c['app_review_message']+=note
  if c['id']=='DE-055':
   c['fine_goals'][0]['goal']='Die Lernenden können kurze Sätze über Zeilenwechsel hinweg sicher lesen und Satzgrenzen sowie eine zum Satzsinn passende Satzmelodie beachten. Anforderungsniveau: Beherrschen.'
   c['fine_goals'][0]['criterion']='Zeilenwechsel führen nicht zu sachlich falschen Satzabbrüchen; Satzenden und die zum Inhalt passende Betonung werden beim Lesen zuverlässig hörbar. Keine vollständige Beherrschung aller Ausdrucksmittel verlangt.'
   c['fine_goals'][1]['criterion']='Erarbeitete Lesefertigkeiten werden auf einen unbekannten kleinen Text übertragen: Sinneinheiten bleiben über Zeilenwechsel erkennbar und der Satzsinn wird zutreffend wiedergegeben. Passende Satzmelodie wird angebahnt; kein routinierter ausdrucksvoller Vortrag als FSP-Abschlussstandard.'
   note=' Ergänzter Ausschnitt: Satzgrenzen über Zeilenwechsel und sinntragende Satzmelodie. Der FSP-Bezug zur Satzmelodie ist die Bemerkung ausdrucksvolles Lesen anbahnen, kein eigenständiges Beherrschensziel. Keine vollständige Abdeckung aller Satzarten oder der Wortgrenzenstrategie mit Großschreibung.'
   c['review_note']+=note;c['app_review_message']+=note;c['operator_relation']+=note
