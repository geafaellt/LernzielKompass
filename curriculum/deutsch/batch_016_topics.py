"""Invitation features as a bounded usage-text intersection."""
def append(T):
 T('gebrauchstext-einladung12','Merkmale einer schriftlichen Einladung entdecken','186442','40320 40323','Eine schriftliche Einladung zu einer Klassenveranstaltung','an einer schriftlichen Einladung erste Merkmale ihrer Funktion und Form entdecken','Eine schriftliche Einladung für einen neuen Anlass situationsgerecht verfassen und dafür passende sprachliche Mittel und Formmerkmale nutzen.','GS1/2 Einblick zu FSP3/4 Anwenden. Nur Gebrauchstext Einladung; keine vollständige Abdeckung von Sachtexten, Anleitungen oder Regeln. FSP-Situationsbezug, sprachliche Mittel und Form sind konkretisierende Bemerkungen. GS erkundet Merkmale; FSP muss die Form bei einem neuen Anlass tatsächlich nutzen.',['186444'])
def refine(cards):
 for c in cards:
  if c['id']=='DE-140':
   c['fine_goals'][0]['criterion']='Ein erstes Merkmal der Einladung, etwa Adressierung, Anlassangabe oder Einladungsformulierung, wird erkannt und mit ihrer Funktion verbunden. Keine vollständige Textsortendefinition oder sichere eigene Textproduktion vorausgesetzt.'
   c['fine_goals'][1]['criterion']='Die Einladung zum neuen Anlass enthält die vereinbarten notwendigen Angaben und verwendet eine zum Empfänger passende Einladungsform. Bloßes Benennen von Merkmalen erfüllt Anwenden nicht; Umfang und konkrete Ausgestaltung bestimmt die Lehrkraft.'
