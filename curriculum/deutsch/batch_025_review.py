"""Article relation and intonation as bounded grammatical intersections."""
def refine(cards):
 for c in cards:
  if c['id']=='DE-121':
   c['fine_goals'][0]['goal']='Die Lernenden können an bekannten Beispielen bestimmte und unbestimmte Artikel unterscheiden und ihre Beziehung zum begleiteten Nomen erläutern. Anforderungsniveau: Kennen.'
   c['fine_goals'][0]['criterion']='Artikel und zugehöriges Nomen werden zutreffend verbunden; am erarbeiteten Beispiel wird erkennbar, welches Nomen der Artikel begleitet. Keine vollständige Analyse erweiterter Nominalgruppen verlangt.'
   c['fine_goals'][1]['criterion']='Bekannten Substantiven werden passende bestimmte und unbestimmte Artikel zugeordnet; die Zuordnung wird am erarbeiteten Beispiel richtig wiedergegeben. Keine Anwendung an neuem Stoff vorausgesetzt.'
   c['review_note']+=' Begleiterfunktion nur als Artikel-Nomen-Beziehung angeschlossen. Der Rechtschreibrahmen geht mit der erweiterbaren Nominalgruppe darüber hinaus; diese Gesamtstruktur wird nicht als abgedeckt behauptet.'
  if c['id']=='DE-124':
   c['fine_goals'][0]['criterion']='An einer bekannten Frage und Aussage wird die Sprechweise variiert und deren Wirkung zutreffend verglichen. Das Vorgehen als Klangprobe wird im erarbeiteten Kontext nachvollziehbar erläutert; bloßes Benennen eines Satzzeichens genügt nicht.'
   c['fine_goals'][1]['criterion']='Eine erste zutreffende Beobachtung zur unterschiedlichen Intonation von Frage und Aussage wird erkennbar. Kein routiniertes Untersuchungsverfahren oder vollständiger Satzartenvergleich verlangt.'
   c['review_note']+=' Verfahren zum Untersuchen von Sätzen ist nur über den Ausschnitt Klangprobe/Intonation angeschlossen. Ausrufe, Erweiterungs-, Umstell-, Ersatz- und Weglassprobe bleiben außerhalb; FSP-Intonation ist eine Bemerkung zum Satzartenziel.'
  if c['id'] in ['DE-121','DE-124']:
   c['app_review_message']=c['review_note']+' Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlung/Aufgabe und Hilfsmittel bestimmt ausschließlich die Lehrkraft.'
