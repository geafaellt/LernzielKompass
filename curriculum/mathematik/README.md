# Mathematik-Abgleich · MA-006

Erster Prüfstand vom 06.11.2026. Grundlage sind der [sächsische Fachlehrplan Mathematik für die Grundschule, Fassung 2026](https://www.schulportal.sachsen.de/lplandb/lehrplan/912), und der [sächsische Fachlehrplan Mathematik für den Förderschwerpunkt Lernen, Fassung 2019](https://www.schulportal.sachsen.de/lplandb/lehrplan/139). Verglichen werden GS 1/2, 3 und 4 mit den gebündelten FSP-Stufenbändern 1/2 und 3/4.

Fünfzehn Karten dokumentieren begrenzte Anschlüsse. Zwölf liegen im passenden Stufenband. MA-002, MA-011 und MA-012 sind stufenübergreifend. Für Spiegelachsen wurde in FSP 1/2 das verwandte Ziel zu Mustern und Ornamenten geprüft. Der konkrete Spiegelachsenbezug ist in FSP 3/4 belegt.

| Karten | Geprüfte Ausschnitte |
| --- | --- |
| MA-001 und MA-002 | Relative Lage von Objekten und Erkennen einer Spiegelachse |
| MA-003 und MA-004 | Geldbeträge innerhalb einer Einheit und Vergleich von Längen in Metern |
| MA-005 und MA-007 | Schriftliche Addition zweier Summanden in GS 3 und als Verfahrensanschluss in GS 4 |
| MA-006 | Minutengenaues Ablesen von Uhrzeiten in GS 3 und FSP 3/4 |

Die Operatoren stammen aus den übergeordneten Zielzeilen der jeweiligen Lehrpläne. Unterziele grenzen den Anschluss ein. Hinweise aus der Bemerkungsspalte bleiben Kontext. Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlungen, Aufgaben und Hilfsmittel legt die Lehrkraft fest.

[Prüfstand und Zeilenanker](review_progress.json) enthält die ausgewählten amtlichen Anker mit Bereich, Hierarchie und Operator. [Die Karten](mathematik_module.json) enthalten die jeweilige fachliche Grenze, Quellenlinks und die getrennten Ziele. Alle zwölf GS-Lernbereiche sind in der App auswählbar. Bereiche ohne Karte und die restlichen Ausschnitte innerhalb der Bereiche bleiben offen. Eine vollständige Einzelzeilenprüfung und eine Rückwärtsprüfung FSP → GS stehen aus.

Fortsetzung beim Zielblock Zahlbeziehungen und Orientierung bis 100 (page912_1842), zunächst Zählen und Zahlenvergleich. Drei Anschlussfragen sowie dokumentierte Teilumfänge des ersten Blocks bleiben offen. [Prüfpaket MA-006](review_batch_006.json) und [Zeilenaudit](row_audit.csv) dokumentieren die Grenzen.

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
