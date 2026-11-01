"""A concrete word-meaning clarification, without general semantic equivalence."""
def append(T):
 T('wortbedeutung-unterschrift12','Die Bedeutung von Unterschrift klären','186477','40227 40240','Der Ausdruck Unterschrift in einem schulischen Text mit persönlichen Angaben','eine Unklarheit beim Wort Unterschrift benennen und erste Einsichten in seine Bedeutung äußern','Persönliche Angaben in einem neuen schulischen Zusammenhang verwenden und die eigene Unterschrift ihrer geklärten Funktion entsprechend einsetzen.','Nur Wortbedeutung Unterschrift als begrenztes Verständigungsproblem. GS1/2 Einblick zu FSP3/4 Anwenden persönlicher Angaben. Begriffsklärung ist FSP-Bemerkung zum Unterziel Unterschrift; kein eigenständiger allgemeiner Bedeutungsoperator. Keine vollständige Abdeckung von Verständigungsproblemen oder allgemeiner Wortklärungsstrategien.',['186479','186480'])
def refine(cards):
 for c in cards:
  if c['id']=='DE-147':
   c['fine_goals'][0]['criterion']='Die Unklarheit beim Ausdruck Unterschrift wird erkennbar benannt; eine erste zutreffende Erklärung wird mit dem schulischen Beispiel verbunden. Bloßes Abschreiben des Wortes weist Bedeutungsklärung nicht nach.'
   c['fine_goals'][1]['criterion']='Im neuen schulischen Beispiel werden passende persönliche Angaben verwendet und die Unterschrift entsprechend ihrer geklärten Funktion eingesetzt. Ihre Funktion wird am Beispiel nachvollziehbar erläutert; eine bloße Wortdefinition erfüllt Anwenden nicht.'
   c['app_review_message']=c['review_note']+' Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlung/Aufgabe und Hilfsmittel bestimmt ausschließlich die Lehrkraft.'
