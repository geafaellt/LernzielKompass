"""Reading accuracy and audible reading, without invented rate or method standards."""
def refine(cards):
 for c in cards:
  if c['id']=='DE-052':
   c['fine_goals'][0]['criterion']='In einem vergleichbaren neuen kurzen Text werden die vereinbarten Wörter schriftgetreu gelesen; Auslassungen, Ersetzungen und Selbstkorrekturen werden nachvollziehbar erfasst. Wortgruppen werden zunehmend zusammenhängend erlesen und eine Inhaltsfrage zutreffend beantwortet. Keine pauschale Fehlerquote oder Geschwindigkeit als Lehrplanvorgabe.'
   c['fine_goals'][1]['criterion']='Bekannte Laut-Buchstaben-Beziehungen werden auf unbekannte Wörter übertragen; die erlesenen Wörter entsprechen der Vorlage und ihr Sinn wird zutreffend erfasst. Beobachtete Abweichungen und Selbstkorrekturen werden getrennt dokumentiert; kein identischer Flüssigkeitsstandard beider Bildungsgänge.'
   note=' Genauer Ausschnitt: schriftgetreues Erlesen, keine festgelegte Leserate. Genauigkeit ist eine didaktische Konkretisierung des FSP-Erlesens, kein zusätzlicher amtlicher Operator.'
   c['review_note']+=note;c['app_review_message']+=note
  if c['id']=='DE-056':
   c['fine_goals'][0]['goal']='Die Lernenden können geübte Lesefertigkeiten auf einen vergleichbaren neuen kurzen Text übertragen und ihn hörbar, zunehmend flüssig und in sinnvollen Einheiten lesen.'
   c['fine_goals'][0]['criterion']='Beim hörbaren Lesen des neuen Textes bleiben sinnvolle Wortgruppen erkennbar; der Textinhalt wird zutreffend wiedergegeben. Der Transfer auf den neuen Text wird vom bloßen Wiederholen eines geübten Textes unterschieden.'
   c['fine_goals'][1]['criterion']='Ein unbekannter kleiner Text wird selbst hörbar erlesen; sinnvolle Wortgruppen und eine zutreffende Inhaltswiedergabe zeigen den Transfer. Ausdruck wird angebahnt; kein routinierter Vortrag und kein bestimmtes Lesetempo vorausgesetzt.'
   note=' Von GS still, leise und laut ist hier ausschließlich hörbares Lesen begrenzt angeschlossen. FSP-Bemerkung ausdrucksvolles Lesen anbahnen stützt diesen Ausschnitt; stilles und leises Lesen sind nicht ausdrücklich mitgeprüft oder abgedeckt. Keine Vorgabe für Lautleseverfahren.'
   c['review_note']+=note;c['app_review_message']+=note;c['operator_relation']+=note
