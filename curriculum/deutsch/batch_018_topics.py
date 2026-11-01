"""Bounded text access and informative reading; no motivation-performance equation."""
def append(T):
 T('vorlesezugang12','Eine vorgelesene Textvorlage erschließen','186450','39954','Eine kurze literarische Textvorlage für den FSP-Wahlbereich Wir spielen Theater','an einer vorgelesenen literarischen Textvorlage erste Vorstellungen zum Inhalt äußern','Den Inhalt der erarbeiteten Textvorlage in wesentlichen Zügen wiedergeben.','Nur Vorlesen als Zugang zu Texten; keine eigene Vortragsleistung und kein Nachweis von Lesefreude. FSP1/2 Wahlbereich 3 ist Voraussetzung. Vorlesen steht dort als Bemerkung zum Kennen des Inhaltes; es ist kein zusätzlicher FSP-Leistungsoperator.',['186453'])
 T('sachtext-informierend12','Informationen in einem kurzen Sachtext erschließen','186450','40107 40123','Ein kurzer Sachtext zu einer gemeinsam gewählten Sachfrage','in einem kurzen Sachtext erste sachbezogene Informationen entdecken und mit der Sachfrage verbinden','Erarbeitete Lesefertigkeiten auf einen unbekannten kleinen Sachtext übertragen und eine für die Sachfrage wesentliche Information erfassen.','GS1/2 Einblick gewinnen zu FSP3/4 Übertragen. Nur informierendes Lesen und ein Ausschnitt des Sachtextverstehens; kein vollständiger Anschluss aller vier Lesezwecke, keiner sämtlicher Gebrauchstexte oder grafischer Darstellungen. Sachtexte sind FSP-Bemerkung zum Leseziel; Wesentliches erfassen ist Unterziel.',['186454','186457'])
def refine(cards):
 for c in cards:
  if c['id']=='DE-141':
   c['fine_goals'][0]['criterion']='Eine erste inhaltlich passende Vorstellung zur vorgelesenen Textvorlage wird erkennbar. Eigene flüssige oder ausdrucksvolle Vorleseleistung und bekundete Lesefreude sind keine Kriterien dieses Ausschnitts.'
   c['fine_goals'][1]['criterion']='Wesentliche Inhalte der erarbeiteten Textvorlage werden zutreffend wiedergegeben. Szenische Umsetzung ist ein anderes Ziel und wird hier nicht vorausgesetzt.'
  if c['id']=='DE-142':
   c['fine_goals'][0]['criterion']='Eine erste sachbezogene Information aus dem kurzen Text wird erkannt und nachvollziehbar auf die Sachfrage bezogen. Keine vollständige Analyse oder selbstständige Strategieauswahl vorausgesetzt.'
   c['fine_goals'][1]['criterion']='Aus einem selbst erlesenen unbekannten kleinen Sachtext wird eine für die Sachfrage wesentliche Information zutreffend gewonnen. Bloßes Erinnern an zuvor vorgelesene Inhalte erfüllt Übertragen auf das Erlesen nicht.'
  if c['id'] in ['DE-141','DE-142']:
   c['app_review_message']=c['review_note']+' Feinziele und Kriterien sind didaktische Konkretisierungen, keine amtlichen Formulierungen. Lernhandlung/Aufgabe und Hilfsmittel bestimmt ausschließlich die Lehrkraft.'
