"""Individual listening-row audit: bounded source links, not full equivalence."""
def append(T):
 T('hoeren-tonfall','Tonfall und Lautstärke beim Zuhören unterscheiden','186299','39179 39194','Zwei unterschiedlich gesprochene kurze Äußerungen zu einer vertrauten Klassensituation','einen Unterschied in Tonfall oder Lautstärke wahrnehmen und am bekannten Beispiel zeigen','Die Wahrnehmung von Tonfall und Lautstärke an kurzen Äußerungen weiterentwickeln und einen Unterschied durch Zeigen, Zuordnen oder Beschreiben deutlich machen.','FSP Entwickeln bezeichnet einen individuellen Lernprozess. Fortschritt gegenüber der Ausgangsbeobachtung dokumentieren; keine feste Kompetenzstufe oder sichere Deutung fremder Gefühle ableiten. Beispiele in einen vertrauten thematischen Kontext einbetten.',['186308'])

def refine(cards):
 for c in cards:
  if c['id']=='DE-015':
   c['fine_goals'][0].update(goal='Die Lernenden können bei einem bekannten Hörauftrag aufmerksam auf eine vereinbarte Information achten und nach dem Hören eine wesentliche Information aus dem Märchen wiedergeben.',criterion='Die gesuchte Information wird nach dem Hören richtig wiedergegeben oder einem passenden Bild zugeordnet. Eine erneute Hörphase ist zulässig. Aufmerksamkeit wird aufgabenbezogen beobachtet; Blickkontakt oder regungsloses Sitzen sind kein Pflichtnachweis.')
   c['task_suggestions']['GS']='Höre auf die vorher vereinbarte Frage zum Märchen. Gib danach eine passende Information wieder oder zeige das passende Bild. Höre bei Bedarf erneut.'
   note=' Nachbereitung ist nur als angeleitete Inhaltswiedergabe belegt; keine vollständige Reflexion von Verstehen/Nicht-Verstehen, keine eigenständige Auswahl von Zuhörstrategien.'
   c['review_note']+=note;c['app_review_message']+=note
  if c['id']=='DE-130':
   c['fine_goals'][0]['criterion']='An einem bekannten Beispiel wird ein zutreffender Unterschied in Tonfall oder Lautstärke gezeigt, zugeordnet oder beschrieben; eine Vermutung über Gefühle ist kein erforderlicher Nachweis.'
   c['fine_goals'][1]['criterion']='Ausgangsbeobachtung und Folgebeobachtung zu vergleichbaren Hörbeispielen dokumentieren, welche Unterschiede wahrgenommen werden und welche Hilfen nötig sind. Individuelle Veränderung beschreiben; kein einheitlicher Abschlussstandard.'
