"""Digital learning format and two distinct text-presentation subgoals."""
def append(T):
 T('lernformat12','Ein digitales Sprachlernformat erproben','186460','39318 39324','Ein digitales Lernprogramm mit sprachbezogenen Inhalten','ein digitales Sprachlernformat erproben und erste Erfahrungen mit seiner Nutzung äußern','Sprachwissen bei einer neuen sprachlichen Anforderung innerhalb eines Lernprogramms anwenden.','Nur ein Sprachlernformat als Schnittmenge. Kein pauschaler Anschluss für Wikis, Podcasts, Videoclips, Suchmaschinen oder Chancen und Risiken. GS1/2 Einblick gewinnen, FSP1/2 Anwenden; reine Programmbedienung erfüllt den FSP-Anspruch nicht.',['186465'])
 T('naturgedicht-praesentation12','Ein Naturgedicht als Textpräsentation erproben','186466','39818 39841 39843','Ein Gedicht zu jahreszeitlichen Naturveränderungen','den Vortrag eines Naturgedichts als Form der Textpräsentation erproben','Ein bekanntes Naturgedicht verständlich vortragen und seinen jahreszeitlichen Naturbezug wiedergeben.','GS1/2 Einblick gewinnen zu FSP1/2 Kennen jahreszeitlicher Veränderungen. FSP-Unterziel Gedichte vortragen bleibt an Natur und Jahreszeiten gebunden. Techniken des Auswendiglernens sind GS-Bemerkung, kein mitbelegtes FSP-Ziel.',['186468'])
 T('sinngestaltend12','Einen literarischen Text sinngestaltend vorlesen','186466','40480 40484','Ein kurzer literarischer Text über Wünsche, Träume oder Fantasie','nach Vorbereitung erste Möglichkeiten sinngestaltenden Vorlesens erproben','Einen vorbereiteten literarischen Text ausdrucksvoll und seinem Sinn entsprechend lesen.','GS1/2 Einblick gewinnen zu FSP3/4 Kennen literarischer Texte. Ausdrucksvolles Lesen ist FSP-Unterziel; Vorbereitung steht in beiden Lehrplänen als Bemerkung. Kein spontanes Lesen unbekannter Texte und keine Gleichsetzung mit bloßem Zuhören.',['186469'])
def refine(cards):
 for c in cards:
  if c['id']=='DE-143':
   c['fine_goals'][0]['criterion']='Eine grundlegende Nutzungsmöglichkeit des digitalen Sprachlernformats wird erprobt; eine erste dazu passende Erfahrung wird erkennbar. Selbstständige Beherrschung des Programms ist nicht vorausgesetzt.'
   c['fine_goals'][1]['criterion']='Bei einer neuen sprachlichen Anforderung im Programm wird erarbeitetes Sprachwissen fachlich passend eingesetzt. Bloßes Öffnen, Klicken oder eine Punktzahl ohne erkennbaren Sprachbezug genügt nicht.'
  if c['id']=='DE-144':
   c['fine_goals'][0]['criterion']='Ein erster Gedichtvortrag wird erprobt, bei dem der ausgewählte Textabschnitt für Zuhörende erkennbar ist. Vollständig auswendiger oder bereits routiniert gestalteter Vortrag wird nicht verlangt.'
   c['fine_goals'][1]['criterion']='Das bekannte Gedicht wird verständlich vorgetragen; eine darin dargestellte Naturveränderung wird zutreffend einer Jahreszeit zugeordnet. Das Kriterium wahrt den übergeordneten Naturkontext.'
  if c['id']=='DE-145':
   c['fine_goals'][0]['criterion']='Nach Vorbereitung wird an einer Textstelle eine zum Sinn passende Betonung oder Pause erprobt. Ein erster Gestaltungsversuch genügt dem Einblick; durchgängig sicherer Ausdruck ist nicht vorausgesetzt.'
   c['fine_goals'][1]['criterion']='Der vorbereitete Text wird mit sinnentsprechender Betonung und Gliederung verständlich gelesen. Die Gestaltung passt zum Inhalt; bloße Lautstärke ohne Sinnbezug genügt nicht.'
  if c['id'] in ['DE-143','DE-144','DE-145']:
   c['app_review_message']=c['review_note']+' Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlung/Aufgabe und Hilfsmittel bestimmt ausschließlich die Lehrkraft.'
