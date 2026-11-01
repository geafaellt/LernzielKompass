"""Limit the explicit vowel/consonant link to the FSP1/2 inventory."""
def refine(cards):
 for c in cards:
  if c['id'] in ['DE-117','DE-118']:
   note=' FSP1/2 ausdrücklich: A, E, I, O, U sowie Ei und Au; M, N, S, R, L, P, T, F, H und Sch. D, B, G, K, W stehen als Differenzierung in den Bemerkungen. Umlaute, weitere Zwielaute und weitere Mitlaute sind durch diese Karte nicht vollständig abgedeckt. Lautzuordnung ist keine vollständige Fachbegriffs- oder Lautklassifikationsprüfung.'
   c['review_note']+=note;c['app_review_message']+=note;c['operator_relation']+=note
   for goal in c['fine_goals']:
    goal['criterion']='Bei vorab ausgewählten, bereits erarbeiteten Laut-Buchstaben-Zuordnungen wird zum Laut das passende Schriftzeichen und zum Schriftzeichen der passende Laut gezeigt; eine einfache Lautanalyse oder Lautsynthese gelingt am bekannten Wort. Buchstabennamen allein ersetzen die Lautzuordnung nicht. Auswahl und Hilfen vorab festlegen.'
