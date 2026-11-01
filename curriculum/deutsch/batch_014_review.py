"""Trace sense-making and relevance selection without full strategy coverage."""
def refine(cards):
 for c in cards:
  if c['id']=='DE-059':
   c['fine_goals'][0]['criterion']='Im bekannten erarbeiteten Text wird eine inhaltliche Frage zutreffend beantwortet und die passende Textstelle gezeigt oder erläutert. Bloßes Entziffern ohne Sinnbezug genügt nicht.'
   c['fine_goals'][1]['criterion']='In einem kleinen unbekannten Text werden erarbeitete Lesefertigkeiten genutzt, eine passende Information gefunden und mit einer Frage oder einem Bild zutreffend verbunden. Der Text wird selbst erlesen; bloßes Erinnern an einen zuvor vorgelesenen Inhalt genügt nicht.'
  if c['id']=='DE-060':
   c['fine_goals'][0]['goal']='Die Lernenden können im erarbeiteten kurzen Text eine für die vereinbarte Fragestellung wesentliche Information von einem nebensächlichen Detail unterscheiden und ihre Auswahl mit Textbezug erläutern. Anforderungsniveau: Kennen.'
   c['fine_goals'][0]['criterion']='Die zentrale Information beantwortet die vereinbarte Frage; ein dafür nebensächliches Detail wird zutreffend abgegrenzt. Die Auswahl wird am bekannten Text nachvollziehbar erläutert; Wichtigkeit wird nicht als absolute Eigenschaft jeder Aussage behandelt.'
   c['fine_goals'][1]['criterion']='Im unbekannten kleinen Text wird eine für die vereinbarte Frage wesentliche Information ausgewählt und mit einer passenden Textstelle verbunden. Das Vorgehen überträgt erarbeitete Lesefertigkeiten; keine vollständige Inhaltsanalyse oder freie Strategieauswahl verlangt.'
  if c['id'] in ['DE-059','DE-060']:
   note=' Sinnverstehendes Lesen ist hier auf die benannten Informationen begrenzt. Die GS-Bemerkung überfliegendes Lesen wird dadurch nicht mit abgedeckt. Aufgaben und Hilfsmittel bestimmt die Lehrkraft.'
   c['review_note']+=note;c['app_review_message']+=note
