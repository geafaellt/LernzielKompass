"""Card-specific pedagogical corrections; official anchors remain separate."""
def correct(cards):
 byid={c['id']:c for c in cards}
 def gs(cid,goal,criterion):
  c=byid[cid];c['fine_goals'][0].update(goal='Die Lernenden können '+goal+'.',criterion=criterion)
  c['task_suggestions']['GS']=goal[0].upper()+goal[1:]+'.'
 def obj(cid,value):
  c=byid[cid];old=c['shared_object_suggestion']
  def replace(x):
   if isinstance(x,str):return x.replace(old,value)
   if isinstance(x,list):return [replace(v) for v in x]
   if isinstance(x,dict):return {k:replace(v) for k,v in x.items()}
   return x
  c.update(replace(c))
 obj('DE-068','Ein gemeinsam ausgewähltes Märchen mit einem Wunsch- oder Fantasieelement')
 obj('DE-071','Eine gemeinsam ausgewählte Fabel mit einem Fantasieelement')
 obj('DE-075','Eine gemeinsam ausgewählte Ortssage mit einem Fantasieelement')
 for cid in ['DE-067','DE-070','DE-073','DE-077']:
  obj(cid,'Ein vorab mit Titel und Autor benanntes Kinderbuch mit einem Wunsch- oder Fantasieelement')
  gs(cid,'das gemeinsam gelesene Kinderbuch mit Titel und Autor vorstellen und eine zentrale Handlung sowie Figuren wiedergeben','Titel und Autor werden zutreffend genannt; die Inhaltswiedergabe passt zum ausgewählten Kinderbuch.')
 gs('DE-010','den Klassenrat mit einem adressatengerechten, begründeten Vorschlag für eine Gesprächsregel überzeugen','Der Appell richtet sich erkennbar an den Klassenrat; ein sachlich passender Grund stützt den Vorschlag. Die Formulierung gelingt sicher und selbstständig.')
 gs('DE-052','geübte Lesefertigkeiten auf einen vergleichbaren neuen kurzen Text übertragen und ihn zunehmend flüssig und sinnverstehend lesen','Wörter werden weitgehend zusammenhängend erlesen; Wortgruppen sind erkennbar. Eine Inhaltsfrage wird richtig beantwortet.')
 gs('DE-053','einen geeigneten kurzen Text automatisiert, zügig und sinngestaltend lesen','Häufige Wörter werden unmittelbar erkannt; Lesefluss, Pausen und Betonung passen zum Sinn. Eine Inhaltsfrage wird richtig beantwortet.')
 gs('DE-054','einen geeigneten Text selbst auswählen und Lesefertigkeiten dem Text entsprechend flüssig und sinngestaltend anwenden','Textwahl und Leseweise passen zum Lesezweck; Worterkennung, Pausen und Betonung ermöglichen ein verständliches Lesen. Der Inhalt wird zutreffend wiedergegeben.')
 gs('DE-076','eine Deutung zu einer Figur oder Handlung entwickeln und sicher mit einer passenden Textstelle begründen','Deutung und Textbeleg passen nachvollziehbar zusammen; die Fundstelle wird selbstständig gezeigt und erläutert.')
 for cid in ['DE-044','DE-045','DE-046']:
  gs(cid,'für das eigene Buch Textideen, passende Wörter und Informationen sammeln und zu einem Schreibplan gliedern','Die geplante Textfolge ist nachvollziehbar; Wörter und Informationen passen zur Mitteilungsabsicht. Das Sammeln von Bastelmaterial allein erfüllt das Ziel nicht.')
 gs('DE-062','wichtige Textstellen und Schlüsselwörter markieren und eine unverstandene Passage zum Klären erneut lesen','Markierungen erfassen zentrale Informationen; erneutes Lesen führt zu einer nachvollziehbaren Klärung.')
 gs('DE-064','Sinnabschnitte kennzeichnen und die zentrale Aussage eines Textes mit selbst gewähltem Vorgehen in eigenen Worten zusammenfassen','Abschnitte sind inhaltlich sinnvoll; die Zusammenfassung erfasst die zentrale Aussage ohne bloßes Abschreiben.')
 for cid in ['DE-102','DE-103']:
  c=byid[cid]
  c['fine_goals'][1].update(goal='Die Lernenden können Lebensmittelbegriffe ordnen und die eigene Frühstücksauswahl anhand eines erarbeiteten Ernährungskriteriums beurteilen und begründen.',criterion='Die Begriffe sind sinnvoll geordnet; die Beurteilung der eigenen Auswahl bezieht sich auf ein erarbeitetes Ernährungskriterium und nennt einen passenden Grund.')
  c['task_suggestions']['FSP']=c['fine_goals'][1]['goal']
 for c in cards:
  if any(x in c['fsp_target_ids'] for x in ['page146_39869','page146_40480']):
   note=' Materialauswahl im FSP-Kontext Wünsche, Träume und Fantasie: einen Text mit entsprechendem Element wählen und dieses bei der Inhaltswiedergabe benennen.'
   c['review_note']+=note;c['app_review_message']+=note;c['task_suggestions']['FSP']+=note
