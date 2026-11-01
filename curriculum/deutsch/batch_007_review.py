"""Bounded sentence-level grouping and dictionary orientation."""
def refine(cards):
 for c in cards:
  if c['id'] in ['DE-022','DE-023']:
   note=' Die strukturierende GS-Zeile Satzebene ist nur für die bereits konkret benannten Satzanfangs- bzw. Satzschlussanforderungen zugeordnet. Erweiterbare Nominalgruppen, Überschriften und Interpunktionsgespräche sind damit nicht insgesamt abgedeckt.'
   c['review_note']+=note;c['app_review_message']+=note
  if c['id']=='DE-039':
   c['fine_goals'][0].update(goal='Die Lernenden können am bekannten Wörterverzeichnis die alphabetische Grundordnung zeigen, eine vereinbarte alphabetische Suchhilfe erläutern und ein bekanntes Wort nach dem Anfangsbuchstaben auffinden.',criterion='Der passende Anfangsbuchstabenbereich wird gezeigt, die erarbeitete Suchhilfe zutreffend erklärt und das vereinbarte Wort gefunden. Keine digitale Suche oder Kenntnis sämtlicher Wörterbuchangaben verlangt.')
   c['task_suggestions']['GS']='Zeige im bekannten Wörterverzeichnis den passenden Buchstabenbereich. Erkläre die vereinbarte alphabetische Suchhilfe und finde das bekannte Wort.'
   note=' Aufbau nur als alphabetische Grundordnung; Suchhilfe nur als erarbeitete alphabetische Orientierung. Ein Buchstabenregister ist gegebenenfalls didaktische Materialwahl, kein vorgeschriebenes FSP-Ziel. Keine vollständige Wörterbuchkunde, digitale Suchfunktion oder eigenständige Fehleraufmerksamkeit abgedeckt.'
   c['review_note']+=note;c['app_review_message']+=note
