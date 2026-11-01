"""Six initial writing subgoals reviewed; preserve remark/goal distinction."""
def append(T):
 T('tastbuchstaben','Buchstabenformen ertasten und wiederfinden','186315','39893 39907 39914','Tastbare Buchstaben zu Namen aus einer gemeinsamen Erkundung im Schulumfeld','eine bekannte Buchstabenform ertasten und der sichtbaren Form zuordnen','In einer neuen Erkundungssituation bekannte Buchstabenformen durch Ertasten erfassen, passende Laute zuordnen und die Buchstaben in entdeckten Namen wiederfinden.','FSP-Wahlbereich 1 Sprache entdecken muss tatsächlich gewählt sein. Tastsäckchen und Fühlbuchstaben sind methodische Bemerkungen zum Ziel Buchstaben erfassen, kein allgemeines taktiles FSP-Ziel. Anwenden verlangt Sprachwissen in der neuen Erkundungssituation; bloßes Ertasten genügt nicht.',['186322'])

def refine(cards):
 for c in cards:
  if c['id']=='DE-115':
   c['fine_goals'][0]['criterion']='Bekannte Schriftformen werden anhand eines sichtbaren Formmerkmals unterschieden oder passend zugeordnet; bei der Lautaufgabe wird ein zutreffender Lautunterschied gezeigt. Hilfen und Materialumfang vorab festlegen.'
   c['fine_goals'][1]['criterion']='Ausgangs- und Folgebeobachtung halten fest, welche Laut- und Schriftformunterschiede erkannt werden und welche Hilfen nötig sind. Individuelle Fortschritte beschreiben; kein einheitlicher Abschlussstandard.'
   note=' Visueller Ausschnitt: Formen und ähnliche Buchstaben unterscheiden. Keine vollständige Abdeckung aller Figur-Grund- oder Raum-Lage-Übungen.'
   c['review_note']+=note;c['app_review_message']+=note
  if c['id']=='DE-018':
   c['fine_goals'][0].update(goal='Die Lernenden können eine individuell förderliche Sitz-, Hand- und Stifthaltung erproben und ausgewählte bekannte Buchstaben und lauttreue Wörter formklar schreiben.',criterion='Eine für das Kind praktikable Haltung wird erprobt; die vereinbarten Buchstaben sind erkennbar. Linkshändigkeit und individuelle motorische Voraussetzungen werden berücksichtigt; kein einheitliches Haltungsideal.')
   c['task_suggestions']['GS']='Erprobe mit Unterstützung eine angenehme, förderliche Schreibhaltung und schreibe die vereinbarten bekannten Buchstaben und Wörter lesbar.'
   note=' Schreibhaltung ist im FSP eine methodische Bemerkung zu Kleinbuchstaben. Sie unterstützt den Transfer beim Schreiben und ersetzt ihn nicht; keine isolierte Haltungsnote.'
   c['review_note']+=note;c['app_review_message']+=note
  if c['id']=='DE-131':
   c['fine_goals'][0]['criterion']='Eine bekannte ertastete Buchstabenform wird der passenden sichtbaren Form zugeordnet oder anhand eines Formmerkmals beschrieben.'
   c['fine_goals'][1]['criterion']='In der noch nicht bearbeiteten Erkundungssituation werden ein bekannter Buchstabe und sein Laut passend verbunden und in einem entdeckten Namen wiedergefunden. Reines Fühlen ohne Sprachbezug erfüllt den FSP-Operator nicht. Hilfen und Auswahl vorab festlegen.'
