"""Bounded word-level spelling intersections; GS1/2 to FSP3/4."""
def append(T):
 T('doppelkonsonanten12','Doppelkonsonanten in zweisilbigen Wörtern','186330','40226','Bekannte zweisilbige Modellwörter mit Doppelkonsonanten, etwa Sonne und Tasse','an bekannten zweisilbigen Modellwörtern die erarbeitete Doppelkonsonantenschreibung zeigen und erläutern','An ausgewählten zweisilbigen Wörtern die doppelte Konsonantenschreibung entdecken und mit dem gesprochenen Wort vergleichen.','Stufenübergreifend GS1/2 zu FSP3/4. Doppelte Konsonanten konkretisieren das FSP-Einblicksziel in den Bemerkungen. Keine vollständige Regelkenntnis, Ableitungsstrategie oder Beherrschung im FSP unterstellen; ck/tz bleiben außerhalb.',['186334','186336'])
 T('ie-zweisilber12','ie in zweisilbigen Modellwörtern entdecken','186330','40226','Bekannte zweisilbige Wörter mit ie, etwa Biene und Wiese','die erarbeitete ie-Schreibung an bekannten zweisilbigen Modellwörtern zeigen und erläutern','In ausgewählten Wörtern ein lang gesprochenes i und seine Schreibung mit ie entdecken und miteinander vergleichen.','Stufenübergreifend GS1/2 zu FSP3/4. Enger Ausschnitt der GS-Bemerkung zur ie-Schreibung; keine vollständige Abdeckung offener/geschlossener oder betonter/unbetonter Silben. Langes i ist FSP-Bemerkung, ie eine didaktische Auswahl; keine Regel behaupten, nach der jedes lange i mit ie geschrieben wird.',['186334','186335'])
def refine(cards):
 for c in cards:
  if c['id']=='DE-132':
   c['fine_goals'][0]['criterion']='Die Doppelkonsonanten werden in den bekannten Modellwörtern richtig gezeigt; die erarbeitete Beziehung zur Silben- bzw. Vokalstruktur wird am Modell zutreffend erläutert.'
   c['fine_goals'][1]['criterion']='Die doppelt geschriebenen Konsonanten werden entdeckt oder markiert; das gehörte Wort wird mit der Schriftvorlage verglichen. Keine allgemeine Regelbegründung oder ungeübte Rechtschreibanwendung verlangt.'
  if c['id']=='DE-133':
   c['fine_goals'][0]['criterion']='Die Schreibung ie wird im bekannten zweisilbigen Modellwort richtig gezeigt und mit dem langen i-Laut verbunden; keine Verallgemeinerung auf alle langen i-Laute.'
   c['fine_goals'][1]['criterion']='Die Buchstabenfolge ie wird im ausgewählten Wort entdeckt und dem gehörten langen i zugeordnet. Der erste Zugang kann durch Zeigen oder Markieren sichtbar werden; keine routinierte Schreibung verlangt.'
