"""Post-reading heading as bounded shared content."""
def refine(cards):
 for c in cards:
  if c['id']=='DE-060':
   c['fine_goals'][0]['goal']+=' Zur Nachbereitung kann eine passende Teilüberschrift den wesentlichen Inhalt des erarbeiteten Abschnitts bündeln.'
   c['fine_goals'][0]['criterion']+=' Beim Ausschnitt Teilüberschrift fasst diese die zentrale Aussage des bekannten Abschnitts zutreffend zusammen; ihre Passung wird am Text erläutert.'
   c['fine_goals'][1]['goal']+=' Eine passende Teilüberschrift zu einem Abschnitt des unbekannten kleinen Textes finden.'
   c['fine_goals'][1]['criterion']+=' Die Teilüberschrift gibt den wesentlichen Abschnittsinhalt wieder und wird aus dem selbst erlesenen neuen Text gewonnen.'
   note=' Nachbereiten des Lesens ist nur über das Finden passender Teilüberschriften angeschlossen. Überschriften finden ist GS-Bemerkung, Teilüberschriften finden FSP-Bemerkung zu Wesentliches erfassen; kein zusätzlicher amtlicher Operator. Reflexionsgespräch, Verstehensschwierigkeiten und inferierendes Lesen sind nicht pauschal abgedeckt.'
   c['review_note']+=note;c['app_review_message']+=note
