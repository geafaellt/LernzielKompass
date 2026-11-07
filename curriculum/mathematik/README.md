# Mathematik-Abgleich · MA-009

Erster Prüfstand vom 06.11.2026. Grundlage sind der [sächsische Fachlehrplan Mathematik für die Grundschule, Fassung 2026](https://www.schulportal.sachsen.de/lplandb/lehrplan/912), und der [sächsische Fachlehrplan Mathematik für den Förderschwerpunkt Lernen, Fassung 2019](https://www.schulportal.sachsen.de/lplandb/lehrplan/139). Verglichen werden GS 1/2, 3 und 4 mit den gebündelten FSP-Stufenbändern 1/2 und 3/4.

Einundzwanzig Karten dokumentieren begrenzte Anschlüsse. Achtzehn liegen im passenden Stufenband. MA-002, MA-011 und MA-012 sind stufenübergreifend. Für Spiegelachsen wurde in FSP 1/2 das verwandte Ziel zu Mustern und Ornamenten geprüft. Der konkrete Spiegelachsenbezug ist in FSP 3/4 belegt.

| Karten | Geprüfte Ausschnitte |
| --- | --- |
| MA-001 und MA-002 | Relative Lage von Objekten und Erkennen einer Spiegelachse |
| MA-003 und MA-004 | Geldbeträge innerhalb einer Einheit und Vergleich von Längen in Metern |
| MA-005 und MA-007 | Schriftliche Addition zweier Summanden in GS 3 und als Verfahrensanschluss in GS 4 |
| MA-006 | Minutengenaues Ablesen von Uhrzeiten in GS 3 und FSP 3/4 |

Die Operatoren stammen aus den übergeordneten Zielzeilen der jeweiligen Lehrpläne. Unterziele grenzen den Anschluss ein. Hinweise aus der Bemerkungsspalte bleiben Kontext. Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlungen, Aufgaben und Hilfsmittel legt die Lehrkraft fest.

[Prüfstand und Zeilenanker](review_progress.json) enthält die ausgewählten amtlichen Anker mit Bereich, Hierarchie und Operator. [Die Karten](mathematik_module.json) enthalten die jeweilige fachliche Grenze, Quellenlinks und die getrennten Ziele. Alle zwölf GS-Lernbereiche sind in der App auswählbar. Bereiche ohne Karte und die restlichen Ausschnitte innerhalb der Bereiche bleiben offen. Eine vollständige Einzelzeilenprüfung und eine Rückwärtsprüfung FSP → GS stehen aus.

Fortsetzung bei Vorgänger, Nachfolger und Nachbarzehner (page912_1846), danach doppelte/halbe und gerade/ungerade Zahlen. Drei Anschlussfragen sowie dokumentierte Teilumfänge des ersten Blocks bleiben offen. [Prüfpaket MA-008](review_batch_008.json) und [Zeilenaudit](row_audit.csv) dokumentieren die Grenzen.

## App-Daten aktualisieren und prüfen

```sh
python3 scripts/update-mathematik.py
python3 scripts/check-deutsch.py
python3 scripts/prepare-pages.py
python3 scripts/check-mathematik.py
```

## Prüfung für App 1.305

Die Mathematikprüfung bestätigt sieben Karten mit 32 amtlichen Zeilenankern und identische HTML-Dateien für App und GitHub Pages. Die bestehende Deutschprüfung bestätigt 178 Deutschkarten, 117 Zielblockentscheidungen, die unveränderten Sachunterrichtsdaten und gültige JavaScript-Syntax.

Im lokalen Chromium-Test wurden alle sieben Mathematikkarten, die Klassenfilter 1–4, Bereiche ohne Karte, Operatoren, Quellenlinks und getrennte Fachentwürfe einschließlich Neuladen geprüft. Die Feinzielübernahme wurde für beide Bildungsgänge geprüft. Aufgaben- und Hilfsmittelfelder blieben dabei leer.


## MA-002 · App 1.306 · 06.11.2026

Vier neue Karten ergänzen strukturierte Mengen bis sechs (MA-008), Mengenvergleich (MA-009), Anzahl und Zahl im Naturkontext (MA-010) sowie doppelte und halbe Anzahlen (MA-011). Die letzten beiden Zahlaspekte werden jeweils im belegten Lehrplankontext eingegrenzt. Die GS-Zahlenraumgrenze bis 100 wird den FSP1/2-Ankern nicht zugeschrieben.

MA-011 verbindet GS1/2 mit FSP3/4. Mengenstrukturierung und allgemeine Rechenhandlungen aus FSP1/2 wurden als Kandidaten geprüft. Der ausdrückliche Anker für Verdoppeln und Halbieren steht in FSP3/4. Der dortige Operator Einblick gewinnen bleibt gegenüber dem GS-Beherrschen sichtbar.

Der neue Zeilenaudit umfasst zunächst die 14 Zeilen des begonnenen GS-Zielblocks. Vier Unterzielausschnitte sind geprüft, drei übergeordnete Zeilen dienen als Kontext und sieben weitere Zeilen bleiben offen. Diese Teilinventur ist kein Gesamtinventar des Faches. Die sieben bisherigen Karten bleiben erhalten.

Prüfung bestanden mit elf Mathematikkarten und 49 Quellenankern. Alle elf Karten wurden im lokalen Browser mit Klassenfiltern, Quellenlinks und Operatoren geprüft. Fachwechsel und Wiederherstellung der Entwürfe nach Neuladen funktionieren. Die vorhandene Deutschprüfung und die Synchronisation der beiden App-Dateien sind bestanden.

Veröffentlicht mit Commit b371ecc590d4de7a62922eafbeabfa08c4fbdd25. Der [Pages-Lauf 42272284490](https://github.com/geafaellt/LernzielKompass/actions/runs/42272284490) war erfolgreich. Die öffentliche HTML-Datei stimmt bytegenau mit der lokal geprüften App 1.306 überein. Der Browsertest aller elf Mathematikkarten wurde auf GitHub Pages erfolgreich wiederholt.


## MA-003 · App 1.307 · 06.11.2026

MA-012 verbindet das Lesen und Schreiben von Zahlen in Ziffernschreibweise bis 100 in GS1/2 mit FSP3/4. Der FSP-Hauptoperator Beherrschen stammt aus dem Ziel zu Zahlen bis 100. Die konkrete Nennung von Lesen und Schreiben steht in der Bemerkung. Diese Einordnung ist in der App sichtbar. Der stufengleiche Kandidat zur Zahlwort-Menge-Zuordnung in FSP1/2 trägt den gesamten Ausschnitt nicht.

Beide GS-Zeilen sind teilweise geprüft. Lesen und Schreiben ausgeschriebener Zahlwörter bleiben als zwei offene Anschlussfragen bestehen. Weitere Zahlenbedeutungen und der gesamte GS-Zielblock sind weiterhin offen.

Inventurkorrektur zu MA-002. Die CSV enthielt trotz der Angabe 14 nur 13 Zeilen. Die fehlende Ordinalzahlzeile 187041 wurde als ungeprüft ergänzt. Diese Korrektur erhöht den Prüfungsfortschritt nicht.

Daten- und lokale Browserprüfung bestanden mit zwölf Karten und 54 Quellenankern. Die Fortsetzungspunktprüfung nutzt jetzt den offenen Zeilenstatus. Ein Quellenanker kann als Kontext eingebunden und fachlich weiterhin offen sein.

Veröffentlichung von App 1.307 mit Commit 18c419b032fe307b36dcf365165bb911ce87a838 und [Pages-Lauf 42284869647](https://github.com/geafaellt/LernzielKompass/actions/runs/42284869647) erfolgreich. Die Live-Datei ist bytegleich zum geprüften Stand. Der Browserdurchlauf aller zwölf Mathematikkarten wurde öffentlich erfolgreich wiederholt.


## MA-004 · App 1.308 · 07.11.2026

Zwei stufenbandpassende Anschlüsse ergänzen das Deuten numerischer Umweltangaben (MA-013) und die Zahlposition über Nachbarzahlen (MA-014). Jeweils wurden Kandidaten in FSP1/2 und 3/4 geprüft. Der konkrete Beleg im Band 1/2 wird bevorzugt. Die Hauptoperatoren sind jeweils Beherrschen.

Bei MA-014 steht der ordinale Zahlaspekt in der FSP-Bemerkung zur Zahlbegriffsbildung. Der verbindliche Unterpunkt zu Nachbarzahlen begrenzt die Konkretisierung. Die App weist diese Belegart ausdrücklich aus. MA-013 verwendet den verbindlichen Unterpunkt zum Deuten von Daten in der Umwelt im eingeschränkten Ausschnitt numerischer Angaben.

Beide GS-Zeilen sind teilweise geprüft. Weitere Zahlenbedeutungen, Ordnungszahlkontexte und Darstellungen sowie die zwei Zahlwortfragen bleiben offen. Kartenbezüge gelten nur für den beschriebenen Ausschnitt. Der alte Kontextbezug der MA-012 auf 1834 erzeugt weiterhin keine Abdeckung durch diese Karte.

Daten- und lokale Browserprüfung bestanden mit vierzehn Karten und 57 Quellenankern. Quellenprüfung vom 06.11.2026, Paketabschluss am 07.11.2026.

Veröffentlichung von App 1.308 mit Commit 82878c3f99292d4b5a79d4c8901422853a8c30dc und [Pages-Lauf 42341739055](https://github.com/geafaellt/LernzielKompass/actions/runs/42341739055) erfolgreich. Die Live-Datei ist bytegleich zum geprüften Stand. Der Browserdurchlauf aller vierzehn Mathematikkarten wurde öffentlich erfolgreich wiederholt. Die unterbrochene Veröffentlichung wurde fortgesetzt, ohne fachliche Zeilen erneut zu zählen.


## MA-005 · App 1.309 · 07.11.2026

MA-015 ergänzt einen stufenbandpassenden Teilanschluss zwischen zwei Teilmengen und ihrer Gesamtmenge. GS-Beherrschen und FSP-Einblick bleiben getrennt. Die Zerlegung ist in der FSP-Bemerkung zum verbindlichen Unterpunkt über Vereinigungs- und Differenzmengen belegt. Alle Zerlegungsmöglichkeiten und die vollständige GS-Zahlenraumforderung sind durch die Karte nicht abgedeckt.

Für quasi-simultanes Erfassen wurde kein hinreichend belegter direkter Anschluss gefunden. Nichtzählendes Erfassen kleiner Mengen, Strukturieren, Bündeln und Rechenstrategien beider FSP-Bänder wurden geprüft. Sie belegen die spezifische Erfassungsstrategie nicht eindeutig. Diese Entscheidung schließt didaktische Verbindungen nicht aus.

Eine Zeile wurde begrenzt zugeordnet, eine begründet abgegrenzt. Die Zahlwortfragen und weitere Teilumfänge bleiben offen.

Daten- und lokale Browserprüfung bestanden mit fünfzehn Karten und 60 Quellenankern.

Veröffentlichung von App 1.309 mit Commit 49d7f07c0e3c3089b79d570624580cf56852f3a1 und [Pages-Lauf 42358750784](https://github.com/geafaellt/LernzielKompass/actions/runs/42358750784) erfolgreich. Die Live-Datei ist bytegleich zum geprüften Stand. Der Browserdurchlauf aller fünfzehn Mathematikkarten wurde öffentlich erfolgreich wiederholt.


## MA-006 · App 1.310 · 07.11.2026

MA-009 präzisiert den sprachlichen Mengenvergleich mit mehr als, weniger als und gleich viel. Der GS-Unterpunkt 1837 wird als Quellenanker ergänzt. Auf FSP-Seite sind die Formulierungen ausdrücklich in der Bemerkung zu 37813 belegt. Operatoren bleiben GS-Beherrschen und FSP-Kennen. Die Feinzielkriterien berücksichtigen nun die fachlich passende Vergleichssprache.

Das sprachliche Verwenden von das Doppelte und die Hälfte bleibt als zusätzliche Anschlussfrage offen. Der mathematische Anschluss MA-011 ersetzt diese Sprachprüfung nicht. Damit bestehen drei offene Anschlussfragen einschließlich der beiden Zahlwortfragen.

Der folgende GS-Zielblock 1842 wird vollständig als ungeprüfte Teilinventur ergänzt. Das erzeugt keinen fachlichen Prüffortschritt. Die Fortsetzung wechselt zu Zählen und Zahlenvergleich, während die Restumfänge des ersten Blocks dokumentiert bleiben.

Datenprüfungen und Browserprüfung bestanden: fünfzehn Karten, 61 Quellenanker. App 1.310 wurde mit Commit 6dce5cd2d6f507196a3adc82dbf35a04a823d797 veröffentlicht; [Pages-Lauf 42359637078](https://github.com/geafaellt/LernzielKompass/actions/runs/42359637078) ist erfolgreich. Die öffentlich ausgelieferte Datei ist bytegleich zum geprüften Stand. Alle fünfzehn Mathematikkarten wurden im Live-Browser erfolgreich geprüft.


## MA-007 · Zahlenraumprüfung · App 1.311 · 07.11.2026

Auf Nutzerwunsch wurde geprüft, ob ein kleinerer FSP-Zahlenraum zusätzliche fachliche Teilanschlüsse zulässt. Ergebnis: vier neue Karten (MA-016–019) in zwei Inhaltsfamilien: Zählen in Schritten sowie Vergleichen und Ordnen, jeweils GS 3 und GS 4 gegenüber dem passenden FSP-Band 3/4. GS verlangt bis 1 000 beziehungsweise 1 000 000, FSP bis 100. Die Zahlenraumdifferenz und die fehlende Vollabdeckung des GS-Ziels stehen ausdrücklich im sichtbaren Kartenhinweis. Die getrennten Feinziele bewahren beide Zahlenräume.

Ein kleinerer Zahlenraum ist allein kein Ausschlussgrund; Inhalt, Verfahren, Operator, Belegart und Stufenband bleiben eigene Prüfkriterien. Bei Zählen stehen Richtungen und Schrittweite in der FSP-Bemerkung, beim Vergleichen/Ordnen im verbindlichen Unterziel. Beide Hauptoperatoren lauten Beherrschen. Kandidaten in FSP1/2 wurden mitgeprüft; das passende Band 3/4 wird bevorzugt. Nicht ausdrücklich belegte Grenzen werden nicht erfunden.

Die bestehende Sammlung ließ Unterschiede bereits zu, beispielsweise beim schriftlichen Additionsverfahren (MA-007). Die vier neuen Karten sind deshalb kein Nachweis, dass bisherige Nichtanschlüsse allein am Zahlenraum scheiterten. Zahlwortfragen und der fehlende direkte Beleg für quasi-simultanes Erfassen werden durch diese Regel nicht gelöst.

[Prüfpaket MA-007](review_batch_007.json) unterscheidet vier Zielzeilen von zwei Inhaltsfamilien. Acht Zeilen wurden ergänzend inventarisiert, davon vier nur als Kontext; 35 Zeilen im Teilinventar sind kein Gesamtumfang des Faches. Der reguläre Fortsetzungspunkt bleibt page912_1842. Die neuen GS3/4-Zeilen müssen bei der späteren systematischen Prüfung als bereits teilweise bearbeitet berücksichtigt werden.

Datenprüfungen, lokale und öffentliche Browserprüfung bestanden: 19 Karten, 70 Quellenanker. Bei allen vier neuen Karten wurden der sichtbare Zahlenraumhinweis und die Übernahme beider getrennten Ziele/Kriterien geprüft; Aufgaben und Hilfsmittel bleiben leer. App 1.311 ist mit Commit 23fb1ba06f669ac7653d447af4c8aa2344d68774 veröffentlicht; [Pages-Lauf 42363644033](https://github.com/geafaellt/LernzielKompass/actions/runs/42363644033) ist erfolgreich. Die Live-Datei ist bytegleich zum geprüften Stand.


## MA-008 · App 1.312 · 07.11.2026

MA-020 und MA-021 verbinden GS1/2-Zählen sowie Zahlenvergleich/-ordnung mit den ausdrücklichen FSP1/2-Unterzielen im Naturkontext. Beide Hauptoperatoren lauten Beherrschen. Kandidaten in FSP3/4 bis 100 wurden geprüft; der vorhandene stufenbandpassende Anschluss wird bevorzugt.

Der Kartenhinweis trennt die GS-Anforderung bis 100 vom FSP-Bandziel zum Zahlaufbau bis 20. Die FSP-Unterzielzeile hat selbst keine eigene Obergrenze. Das Feinziel bis 20 ist deshalb ausdrücklich eine didaktische Eingrenzung aus dem übergreifenden Ziel, keine neue amtliche Zahlenraumforderung. Die zusätzliche Bandzielquelle page139_37739 wird getrennt von Haupt- und Unterzielankern geführt und ist auf der Karte verlinkt.

Vergleichszeichen sind FSP-Zieltext und GS-Bemerkung. Bestimmte Zählschritte und Unterbrechen/Fortsetzen sind Bemerkungen und werden nicht zu zusätzlichen Pflichtzielen umgedeutet. Zwei Unterzielzeilen wurden begrenzt geprüft, zwei Elternzeilen nur als Kontext behandelt. Die Teilinventur bleibt bei 35 Zeilen. Der übrige Zielblock, die drei Anschlussfragen und frühere Restumfänge bleiben offen. Fortsetzung bei page912_1846.

Datenprüfungen und lokale sowie öffentliche Browserprüfung bestanden: 21 Karten, 77 Zielanker und eine getrennte übergreifende Quelle. App 1.312 ist mit Commit 44dc1e95a21110d28550de1f1447cb3a59a37d24 veröffentlicht; [Pages-Lauf 42364097450](https://github.com/geafaellt/LernzielKompass/actions/runs/42364097450) ist erfolgreich. Die Live-Datei ist bytegleich zum geprüften Stand. Der stündliche Auftrag enthält nun die Zahlenraumregel und verweist ohne veraltete Startanker auf den aktuellen Repository-Fortsetzungspunkt.


## MA-009 · FSP-Geltungsbereich auf jeder Karte · App 1.313

Alle 21 bestehenden Mathematikkarten führen das Pflichtfeld „FSP-Zahlenraum / Geltungsbereich“ in der Kartenauswahl, der Detailansicht, direkt bei den FSP-Zielen und im Planungsoutput. Quellenlinks und Belegarten bleiben sichtbar: sechs ausdrückliche Grenzen, sieben didaktisch aus übergreifenden Zielen abgeleitete Grenzen, vier noch festzulegende Zahlenräume, zwei fachspezifische Geltungsbereiche (Uhrzeiten/Umweltangaben), zwei nicht zahlenraumbezogene Ziele (Lage/Spiegelachse).

Die FSP-Feinziele und Erfolgskriterien wurden auf allen Karten geprüft und bei Bedarf präzisiert. Mengen, Nachbarzahlen, Teil-/Gesamtmengen sowie doppelte und halbe Anzahlen bleiben einschließlich relevanter Ergebnisse innerhalb des ausgewiesenen Rahmens. Geld, Meterangaben und schriftliche Addition erhalten keine erfundene pauschale Grenze; ihr Zahlenraum ist vor Verwendung festzulegen. Übergreifende Ziele sind gesonderte Quellen und ersetzen keinen Zieloperator.

Keine neue Karte oder zusätzliche GS-Zeile wird als abgeschlossen gezählt. Die reguläre Fortsetzung bleibt bei page912_1846; alle bisherigen Restumfänge bleiben bestehen. Aufgaben und Hilfsmittel werden nicht befüllt. Bestehende Lehrkraftentwürfe werden nicht überschrieben; Freitext muss fachlich gegen den angezeigten Rahmen geprüft werden. Die Datenprüfung sichert das Pflichtfeld, die Quellenzuordnung sowie die Grenzangaben in den hinterlegten FSP-Feinzielen und Kriterien. Sie behauptet keine vollständige semantische Prüfung beliebiger Aufgaben.

Zusätzliche Regressionen: `python3 scripts/test-mathematik-scope.py`. Browserprüfung vom Repository-Stamm mit installiertem Playwright und Chromium: `node scripts/check-mathematik-browser.cjs`; bei Bedarf `LZK_PLAYWRIGHT` auf das Playwright-Modul setzen. `LZK_APP_URL` erlaubt dieselbe Prüfung gegen die veröffentlichte App. Die Prüfung umfasst alle Karten, Quellen, Bereichswechsel, Zielübernahme, unveränderte eigene Entwürfe, Planungsoutput und mobile Breite.

Veröffentlichung: App 1.313 mit Commit 288814ba2dee17a9afec8bab19e29b5377fac0f4; [Pages-Lauf 42365836749](https://github.com/geafaellt/LernzielKompass/actions/runs/42365836749) erfolgreich. Die öffentliche Datei ist bytegleich zum geprüften Stand. Datenprüfungen, Negativtests zur Grenzprüfung und Browserprüfungen aller 21 Karten lokal und live bestanden; mobile Darstellung visuell geprüft. Der stündliche Auftrag enthält das Pflichtfeld und die Prüfregel für Feinziele/Kriterien einschließlich relevanter Zwischen- und Endergebnisse. Vier nicht eindeutig belegte Obergrenzen bleiben ausdrücklich offen.
