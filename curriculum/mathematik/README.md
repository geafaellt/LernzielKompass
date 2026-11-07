# Mathematik-Abgleich · MA-019

Erster Prüfstand vom 06.11.2026. Grundlage sind der [sächsische Fachlehrplan Mathematik für die Grundschule, Fassung 2026](https://www.schulportal.sachsen.de/lplandb/lehrplan/912), und der [sächsische Fachlehrplan Mathematik für den Förderschwerpunkt Lernen, Fassung 2019](https://www.schulportal.sachsen.de/lplandb/lehrplan/139). Verglichen werden GS 1/2, 3 und 4 mit den gebündelten FSP-Stufenbändern 1/2 und 3/4.

Achtundzwanzig Karten dokumentieren begrenzte Anschlüsse. Einundzwanzig liegen im passenden Stufenband. MA-002, MA-011, MA-012, MA-022, MA-023, MA-025 und MA-026 sind stufenübergreifend. Für Spiegelachsen wurde in FSP 1/2 das verwandte Ziel zu Mustern und Ornamenten geprüft. Der konkrete Spiegelachsenbezug ist in FSP 3/4 belegt.

| Karten | Geprüfte Ausschnitte |
| --- | --- |
| MA-001 und MA-002 | Relative Lage von Objekten und Erkennen einer Spiegelachse |
| MA-003 und MA-004 | Geldbeträge innerhalb einer Einheit und Vergleich von Längen in Metern |
| MA-005 und MA-007 | Schriftliche Addition zweier Summanden in GS 3 und als Verfahrensanschluss in GS 4 |
| MA-006 | Minutengenaues Ablesen von Uhrzeiten in GS 3 und FSP 3/4 |

Die Operatoren stammen aus den übergeordneten Zielzeilen der jeweiligen Lehrpläne. Unterziele grenzen den Anschluss ein. Hinweise aus der Bemerkungsspalte bleiben Kontext. Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlungen, Aufgaben und Hilfsmittel legt die Lehrkraft fest.

[Prüfstand und Zeilenanker](review_progress.json) enthält die ausgewählten amtlichen Anker mit Bereich, Hierarchie und Operator. [Die Karten](mathematik_module.json) enthalten die jeweilige fachliche Grenze, Quellenlinks und die getrennten Ziele. Alle zwölf GS-Lernbereiche sind in der App auswählbar. Bereiche ohne Karte und die restlichen Ausschnitte innerhalb der Bereiche bleiben offen. Eine vollständige Einzelzeilenprüfung und eine Rückwärtsprüfung FSP → GS stehen aus.

Fortsetzung beim Operationsverständnis Addition/Subtraktion (page912_1857). Sechs Anschlussfragen sowie dokumentierte Teilumfänge des ersten Blocks bleiben offen. [Prüfpaket MA-018](review_batch_018.json) und [Zeilenaudit](row_audit.csv) dokumentieren die Grenzen.

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


## MA-010 · Vertiefte Prüfung offener Zahlenräume · App 1.314

Die vier Karten MA-003, MA-004, MA-005 und MA-007 wurden gegen die amtliche HTML-Fassung und die PDF-Fassung geprüft. Ziel- und Bemerkungsspalten sowie die übergreifenden Ziele sind auf den gedruckten Seiten 9, 12, 13, 17 und 21 visuell gegengeprüft. [Prüfpaket MA-010](review_batch_010.json) enthält Quellen, Seitenzuordnung, Entscheidungen und PDF-Prüfsumme.

MA-003 erhält einen didaktischen Rahmen bis 20 Euro oder bis 20 Cent für ganze Beträge innerhalb derselben Einheit. Begründung: Zahlaufbau bis 20 im Stufenbandziel und ausdrücklicher Zahlenraumhinweis in der Geld-Bemerkung. Weder 20 Euro noch 20 Cent werden als wörtliche Grenze der Zielzeile ausgegeben; Umrechnungen und gemischte Einheiten bleiben ausgeschlossen.

MA-005 und MA-007 erhalten den didaktischen Rahmen bis 100 für zwei nichtnegative ganzzahlige Summanden, relevante Zwischenwerte und das Ergebnis. Die übergreifenden Operationsziele tragen diesen Ausschnitt. Die eigene Zielzeile zum schriftlichen Verfahren nennt keine Obergrenze; insbesondere ist bis 100 keine amtliche Höchstgrenze aller schriftlichen Additionen. Die Bemerkung zu unterschiedlichen Stellenzahlen und Kommazahlen bei Größen bleibt als weitergehender Kontext abgegrenzt. Der Operator Kennen bleibt unverändert.

MA-004 bleibt ohne belegte numerische Obergrenze. Meter ist die belegte Einheit. Ein Meter-Repräsentant ist keine maximale Länge; aus Zahlaufbau bis 20 folgt keine amtliche Höchstlänge von 20 m. Zahlenraum und Darstellungsform bleiben Lehrkraftentscheidung. Feinziele und Kriterien berücksichtigen die jeweiligen Grenzen.

Es bleiben 21 Karten: sechs ausdrücklich begrenzte, zehn didaktisch abgeleitete, eine noch ohne belegte numerische Obergrenze, zwei fachspezifische und zwei nicht zahlenraumbezogene Geltungsbereiche. Keine zusätzliche GS-Zielzeile wurde als abgeschlossen gezählt; der reguläre Fortsetzungspunkt page912_1846 und alle bisherigen Restumfänge bleiben erhalten.

Datenprüfungen, Grenzregressionen und lokale sowie öffentliche Browserprüfungen aller 21 Karten bestanden. App 1.314 ist mit Commit 91678696a0ccdb127dc03ca138e6251159a1f7e4 veröffentlicht; [Pages-Lauf 42366502579](https://github.com/geafaellt/LernzielKompass/actions/runs/42366502579) ist erfolgreich. Die öffentliche Datei stimmt bytegenau mit dem geprüften Stand überein.


## MA-011 · Vorgänger, Nachfolger und Nachbarzehner · App 1.315

GS-Unterziel page912_1846 wurde gegen beide FSP-Bänder geprüft. Vorgänger und Nachfolger nutzen die vorhandene Karte MA-014 mit dem verbindlichen FSP1/2-Nachbarzahlbeleg. Ihr Feinziel bleibt didaktisch auf den aus dem Bandziel abgeleiteten Zahlenraum bis 20 begrenzt; Ausgangszahl und beide Nachbarzahlen müssen darin liegen. Die neue GS-Zielhierarchie wird als `additional_gs_target_groups` separat geführt und geprüft. Der bisherige Ordinalzahlbezug und alle Karten-IDs bleiben erhalten. Gleicher Inhalt wird nicht durch eine zweite Karte gezählt.

MA-022 ergänzt Nachbarzehner als stufenübergreifenden Anschluss GS1/2 zu FSP3/4. Nachbarzehner stehen in der FSP-Bemerkung zu Zählen und Abzählen (35466); Hauptoperator Beherrschen und Zahlenraum bis 100 stammen aus 35461. Unmittelbare Nachbarzahlen, Schrittzählen, Bündeln und Zehnerüberschreitung in FSP1/2 reichen als ausdrücklicher Beleg für Nachbarzehner nicht aus.

Das neue Feinziel beschränkt sich auf nicht durch zehn teilbare Ausgangszahlen. Beide begrenzenden Zehnerzahlen und die Ausgangszahl bleiben bis 100. Diese eindeutige didaktische Konkretisierung erhebt keine zusätzliche Lehrplanforderung; die Behandlung genauer Zehnerzahlen ist nicht festgelegt. Die übergeordnete GS-Struktur- und Darstellungsvielfalt wird nicht als abgedeckt behauptet.

Eine GS-Unterzielzeile mit zwei Ausschnitten wurde begrenzt geprüft: eine neue Karte und eine wiederverwendete Karte. Bestand: 22 Karten, davon vier stufenübergreifend; 80 Quellenlinks (78 Zielanker und zwei übergreifende Kontextquellen). Teilinventur unverändert 35 Zeilen. Frühere Anschlussfragen bleiben bestehen; Fortsetzung bei page912_1847 unter Berücksichtigung von MA-011. Aufgaben und Hilfsmittel bleiben leer.

Datenprüfungen, Grenzregressionen und lokaler Browserdurchlauf aller 22 Karten bestanden. Die Prüfung zusätzlicher GS-Belege verwirft vermischte Zielhierarchien, falsche Operatoren, fehlende Quellen und als Abdeckung gezählten Kontext. Die übrigen 20 Karten sowie Feinziele und FSP-Geltungsbereich von MA-014 sind unverändert. App 1.315 ist mit Commit 713e91ed1367ebdb876853543dcec4692b3d103e veröffentlicht; [Pages-Lauf 42367536843](https://github.com/geafaellt/LernzielKompass/actions/runs/42367536843) ist erfolgreich. Die öffentliche Datei stimmt bytegenau mit dem geprüften Stand überein. Die Browserprüfung aller 22 Mathematikkarten wurde auf der öffentlichen Seite erfolgreich wiederholt.


## MA-012 · Doppelte/halbe und gerade/ungerade Zahlen · App 1.316

Zwei GS 1/2-Unterzielzeilen wurden gegen beide FSP-Bänder geprüft. Der mathematische Ausschnitt von 1847 nutzt MA-011 für doppelte und halbe Anzahlen im Verteilungskontext. Die zusätzliche GS-Zielhierarchie ist separat belegt; Hauptoperatoren bleiben GS-Beherrschen und FSP 3/4-Einblick gewinnen. Die bestehende Frage nach dem sprachlichen Verwenden der Nominalformulierungen (1837) bleibt offen.

MA-023 ergänzt gerade/ungerade Zahlen aus GS 1848 mit dem Teilaspekt Teilbarkeit durch 2 aus FSP 35444. Gerade/ungerade stehen in der FSP-Bemerkung; das Hauptziel 35439 verlangt Kennen. Die Teilbarkeitsregeln für 5 und 10 werden nicht mitgezählt. Strukturieren, paarweises Zuordnen und Schrittzählen in FSP 1/2 reichen als ausdrücklicher Beleg dieses Inhalts nicht aus. Beide Karten bleiben stufenübergreifend; die Bandbezeichnung 3/4 wird nicht auf Einzelklassen aufgeteilt.

Beide FSP-Feinziele sind didaktisch aus den übergreifenden Zielen 35415 auf 100 begrenzt. Die Unterzielzeilen nennen keine eigene Obergrenze. Bei MA-011 müssen Ausgangs- und Ergebnisanzahlen innerhalb des Bereichs bleiben, die Hälfte muss ganzzahlig sein. MA-023 gilt nur für nichtnegative ganze Zahlen und die Teilbarkeit durch 2; relevante Zwischenwerte und ganzzahlige Ergebnisse bleiben ebenfalls im Bereich. Die gleiche gewählte Obergrenze wie in GS erzeugt keine vollständige Zieldeckung. Andere Operatoren sowie die breitere GS-Struktur- und Darstellungsforderung bleiben sichtbar.

Eine neue Karte und eine wiederverwendete Karte, zwei erstmals begrenzt geprüfte Zielzeilen. Bestand 23 Karten, fünf stufenübergreifend, 84 Quellenlinks (82 Zielanker und zwei Kontextquellen); Teilinventur 35 Zeilen unverändert. Alle übrigen 21 Karten und die bisherigen Feinziele/Geltungsbereiche von MA-011 bleiben erhalten. Fortsetzung bei 1849, danach 1850. Frühere Anschlussfragen und Restumfänge bleiben bestehen.

Datenprüfungen, Grenzregressionen und lokaler Browserdurchlauf aller 23 Karten bestanden. App 1.316 ist mit Commit a53837af33ad6372dfab94fa994a205885c5232b veröffentlicht; [Pages-Lauf 42368583693](https://github.com/geafaellt/LernzielKompass/actions/runs/42368583693) ist erfolgreich. Die öffentliche Datei stimmt bytegenau mit dem geprüften Stand überein. Der Browserdurchlauf aller 23 Mathematikkarten wurde öffentlich erfolgreich wiederholt.


## MA-013 · Stellenwertanalogien und Zahlenzerlegung · App 1.317

GS 1849 und 1850 wurden gegen beide FSP-Bänder geprüft. Für Stellenwertanalogien bleibt eine fachliche Anschlussfrage offen: FSP 1/2 nennt zweistellige Zahlstruktur und eine Rechenübertragung bei zusätzlichem Zehner, FSP 3/4 Zahlenaufbau und Zahlbildungs-/Rechenstrategien. Die Gleichsetzung mit dem konkreten GS-Unterpunkt ist noch nicht eindeutig belegt. Das Wort Übertragen in der FSP-Bemerkung 37885 wird nicht als Zieloperator übernommen. Die Frage beruht auf dem Inhalt, nicht auf der Zahlenraumreduktion. Keine Karte ist hier kein abschließender Nichtanschluss.

MA-024 verbindet Zahlenzerlegung begrenzt mit der Zehner-Einer-Struktur zweistelliger Zahlen in FSP 1/2. Das Unterziel 37871 nennt Strukturelemente; die Zusammensetzung aus Zehner- und Einerwert steht in seiner Bemerkung. Hauptoperator bleibt Einblick gewinnen unter 37851, gegenüber GS-Beherrschen unter 1842. Die stufengleiche Verbindung wird gegenüber den höheren FSP-Belegen bis 100 bevorzugt.

FSP-Feinziel und Erfolgskriterium sind didaktisch aus dem Bandziel 37739 auf 20 begrenzt. Ausgangszahl, Zehnerwert, Einerwert sowie Zwischen- und Endergebnisse bleiben im Bereich. Zehnerwert und Zehneranzahl werden unterschieden; der Einerwert liegt zwischen null und neun. Die Unterzielzeile nennt keine eigene Obergrenze. Andere Zerlegungen, systematisches Finden aller Möglichkeiten und die vollständige GS-Zahlenraumforderung bleiben offen.

Die bestehende Karte MA-015 zu Teilmengen und Gesamtmenge wurde erneut geprüft und bleibt einschließlich ihrer Ziele/Grenzen unverändert. Ihr Mengenbezug wird nicht als zusätzlicher Zahlenzerlegungsbeleg gezählt. Alle bisherigen 23 Karten bleiben unverändert; eine neue Karte ergänzt den Bestand auf 24 (19 stufenbandpassend, fünf stufenübergreifend). 87 Quellenlinks: 85 Zielanker und zwei Kontextquellen. Zwei neue Zielzeilen untersucht, davon eine begrenzt angeschlossen und eine offene Anschlussfrage; eine bereits zugeordnete Zeile erneut geprüft. Die Teilinventur bleibt bei 35 Zeilen. Fortsetzung bei 1851 und 187047–187048; insgesamt vier Anschlussfragen bleiben offen.

Zusätzlich wurde die amtliche Progressionsübersicht Zahl und Operation, Seite 2, abgerufen und visuell geprüft. Sie wiederholt Stellenwertanalogien ohne weitere Erläuterung; die Anschlussfrage bleibt daher offen. Datenprüfungen, Grenzregressionen und lokaler Browserdurchlauf aller 24 Karten bestanden. App 1.317 ist mit Commit 36e2dd86b1ff61960e4ab241b7226f2483f82211 veröffentlicht; [Pages-Lauf 42371546199](https://github.com/geafaellt/LernzielKompass/actions/runs/42371546199) ist erfolgreich. Die öffentliche Datei stimmt bytegenau mit dem geprüften Stand überein. Der Browserdurchlauf aller 24 Mathematikkarten wurde öffentlich erfolgreich wiederholt.


## MA-014 · Darstellungsvernetzung · App 1.318

Der gerichtete Ausschnitt Menge → Zahlwort/Zahl aus GS 187047 nutzt die bestehende Karte MA-010. Die zusätzliche GS-Zielhierarchie ist getrennt dokumentiert. Beide Hauptoperatoren bleiben Beherrschen; FSP 1/2 belegt die Zuordnung ausdrücklich in 37941. FSP 3/4 nennt auch die Umkehrrichtung in der Bemerkung 35463; sie wird nicht der FSP1/2-Karte zugeschrieben. Das Feinziel bleibt didaktisch bis 20 begrenzt, GS verlangt bis 100. Flexibler Wechsel aller Darstellungsarten, Umkehrrichtung und sämtliche Sachsituationsbezüge bleiben offen.

Für GS 187048 wurde kein hinreichend belegter direkter Anschluss zum Begründen passender Darstellungen gefunden. Ziel- und Bemerkungszeilen beider FSP-Bänder sowie die übergreifenden Sprachziele wurden geprüft. Zuordnen, Darstellen, Rechenwege begründen und Ergebnisse kontrollieren sind fachlich verwandte, aber unterschiedliche Forderungen. Die allgemeinen Ziele unterstützen mögliche didaktische Begründungen, liefern hier jedoch keinen ausreichend spezifischen direkten Zielbeleg. Daraus folgt keine didaktische Unmöglichkeit; der kleinere Zahlenraum ist nicht der Abgrenzungsgrund.

Die Elternzeile 1851 bleibt Kontext und wird nicht als vollständig abgedeckt gezählt. Zwei neue Unterzielzeilen geprüft: ein begrenzter Anschluss und eine begründete direkte Abgrenzung. Der vorhandene Kardinalzahl-Ausschnitt 187040 wurde erneut bestätigt. Keine neue Karte, unverändert 24 Karten und fünf stufenübergreifende Anschlüsse; 89 Quellenlinks (87 Zielanker und zwei Kontextquellen). Alle Feinziele und Geltungsbereiche sowie die übrigen 23 Karten bleiben unverändert. Fortsetzung bei 187049; vier bestehende Anschlussfragen und alle Restumfänge bleiben erhalten.

Datenprüfungen, Grenzregressionen und lokaler Browserdurchlauf aller 24 Karten bestanden. App 1.318 ist mit Commit 4c4cdffe7a921ae188e502f32c8d78f8996a784e veröffentlicht; [Pages-Lauf 42373087888](https://github.com/geafaellt/LernzielKompass/actions/runs/42373087888) ist erfolgreich. Die öffentliche Datei stimmt bytegenau mit dem geprüften Stand überein. Der Browserdurchlauf aller 24 Mathematikkarten wurde öffentlich erfolgreich wiederholt.


## MA-015 · Fachbegriffe und Zwischen-Beziehung · App 1.319

GS 187049 wurde in getrennten Sprachausschnitten gegen beide FSP-Bänder geprüft. MA-014 ergänzt die Zwischen-Beziehung bei unmittelbaren Nachbarzahlen; FSP 1/2 nennt Formulierungshilfen in der Bemerkung zu 37947. Identischer Satzbau mit liegt/steht wird nicht behauptet. Alle drei Zahlen bleiben innerhalb des didaktisch aus dem Bandziel abgeleiteten FSP-Rahmens bis 20.

MA-023 bezeichnet die vorhandene Klassifikation nun ausdrücklich mit gerade/ungerade. Die Wörter stehen in FSP 3/4 in der Bemerkung zu 35444. Ihre Verwendung ist als didaktische Konkretisierung des Kennens gekennzeichnet, nicht als neue amtliche Sprachzielzeile. Der Rahmen bleibt didaktisch bis 100; nichtnegative ganze Zahlen und relevante Ergebnisse bleiben darin. Die Operatoren und gebündelten Stufenbänder beider Karten sind unverändert.

Zahlwort, Ziffer, Zahl, Vorgänger, Nachfolger, Nachbarzehner und die übrigen Zahlenvergleichsformulierungen bleiben als zusätzliche Anschlussfrage offen. Das Vorkommen eines Fachworts im Lehrplan, das Benennen einer konkreten Zahl und die Verwendung eines Vergleichszeichens sind nicht automatisch eine vollständige Fachsprachforderung. Vorhandene Karten MA-010, MA-012, MA-021 und MA-022 werden dafür nicht ungeprüft mitgezählt.

Eine neue GS-Zeile mit zwei begrenzten Sprachausschnitten geprüft, zwei bestehende mathematische Ausschnitte erneut bestätigt. Keine neue Karte: Bestand 24, fünf stufenübergreifend; 90 Quellenlinks (88 Zielanker und zwei Kontextquellen). Alle Geltungsbereiche und die übrigen 22 Karten unverändert. Neun Zeilen des nächsten GS-Stellenwertblocks wurden ausschließlich inventarisiert; die Teilinventur umfasst jetzt 44 Zeilen. Das ist kein zusätzlicher fachlicher Prüffortschritt. Fortsetzung bei 1852; fünf Anschlussfragen und frühere Restumfänge bleiben erhalten.

Datenprüfungen, Grenzregressionen und lokaler Browserdurchlauf aller 24 Karten bestanden. App 1.319 ist mit Commit de24ce691e5b4abd6ab309e35d2a3591c114ee15 veröffentlicht; [Pages-Lauf 42388682438](https://github.com/geafaellt/LernzielKompass/actions/runs/42388682438) ist erfolgreich. Die öffentliche Datei stimmt bytegenau mit dem geprüften Stand überein. Der Browserdurchlauf aller 24 Mathematikkarten wurde öffentlich erfolgreich wiederholt.


## MA-016 · Bündelung und Stellenwert · App 1.320

MA-024 wird für den Zehner-Einer-Ausschnitt von GS 1854 wiederverwendet. Der FSP1/2-Beleg 37871 nennt zweistellige Zahlstruktur und in der Bemerkung Zehner/Einer. Feinziele und Kriterien unterscheiden nun ausdrücklich Ziffer, Zehneranzahl und Zehnerwert; die bestehende Zerlegung bleibt erhalten. Der FSP-Rahmen bleibt didaktisch bis 20. Hunderter, weitere Stellenwertveränderungen und Stellenwertanalogien werden dadurch nicht vollständig abgedeckt.

MA-025 ergänzt die dekadische Bündelung als stufenübergreifenden Anschluss GS1/2 zu FSP3/4. Bündelung und dekadisches Positionssystem stehen gemeinsam in der Bemerkung zu 35468, Beherrschen und bis 100 im Hauptziel 35461. Die Gleichwertigkeit zehn Einer/ein Zehner und zehn Zehner/ein Hunderter konkretisiert diesen Bezug mathematisch; sie wird nicht als zusätzliche wörtliche Lehrplanforderung ausgegeben. FSP1/2-Bündeln und zweistellige Zahlstruktur wurden geprüft, aber nicht mit der gesamten rekursiven Bündelungsregel gleichgesetzt. Der größere Zahlenraum allein entscheidet nicht über diese Zuordnung.

Alle dargestellten Werte, relevanten Zwischenwerte und Ergebnisse der neuen Karte bleiben bis 100; keine Rechenverfahren oder Hilfsmittel werden ergänzt. Weitere Darstellungs-/Notationsformen bleiben offen. GS 1852 und 1853 sind Kontextzeilen, keine vollständig erledigten Ziele. Zwei Unterzielzeilen begrenzt geprüft und die bestehende Zahlenzerlegung 1850 erneut bestätigt. Bestand 25 Karten, davon sechs stufenübergreifend; 95 Quellenlinks (93 Zielanker, zwei Kontextquellen). Die Teilinventur bleibt 44 Zeilen. Fortsetzung bei 1855; fünf Anschlussfragen bleiben erhalten.

Datenprüfungen, Grenzregressionen und lokaler Browserdurchlauf aller 25 Karten bestanden. App 1.320 ist mit Commit 2a3c123c89d48bd4bf3b21ad41396aaefbb77843 veröffentlicht; [Pages-Lauf 42392427908](https://github.com/geafaellt/LernzielKompass/actions/runs/42392427908) ist erfolgreich. Die öffentliche Datei stimmt bytegenau mit dem geprüften Stand überein. Der Browserdurchlauf aller 25 Mathematikkarten wurde öffentlich erfolgreich wiederholt.


## MA-017 · Bedeutung der Null · Audit ohne App-Änderung

GS 1855 wurde im Kontext des dekadischen Positionssystems gegen beide FSP-Bänder geprüft. Die FSP-Belege zu Mengen, Zahlenbildung, zweistelliger Struktur und dekadischem Zahlenaufbau sind fachlich verwandt. Sie präzisieren die Nullfunktion jedoch nicht als eigenen Zielausschnitt. Der ausdrückliche Nullhinweis in [FSP 35501](https://www.schulportal.sachsen.de/lplandb/lehrplan/139#page139_35501) steht in der Bemerkung zum Ergänzungsverfahren unter Kennen der schriftlichen Verfahren (35498); er wird nicht auf das GS-Beherrschen des Positionssystems übertragen. Gleichungsplatzhalter sind ebenfalls keine Belege für die Null als Stellenziffer.

MA-024 berücksichtigt den Einerwert null bei vollen Zehnern bereits didaktisch innerhalb des Rahmens bis 20. MA-025 bleibt bei dekadischer Bündelung bis 100. Beide Karten, Feinziele und Erfolgskriterien bleiben unverändert und werden nicht zusätzlich auf GS 1855 angerechnet. Mathematisch lässt sich die Nullfunktion aus dem dekadischen System erschließen; damit wird weder eine ausdrückliche zusätzliche Zieldeckung behauptet noch eine didaktische Verbindung ausgeschlossen. Der kleinere Zahlenraum ist kein Ablehnungsgrund.

Eine weitere Zielzeile einzeln geprüft, kein hinreichend belegter direkter Anschluss eingetragen. Weiterhin 25 Karten, sechs stufenübergreifend, 95 Kartenquellen und 44 inventarisierte Zeilen. Drei begründete direkte Abgrenzungen sind nun dokumentiert. Fünf Anschlussfragen sowie frühere Teilumfänge bleiben offen. Fortsetzung bei 1856/187051; der Gesamtvergleich ist nicht abgeschlossen. App 1.320 bleibt unverändert. Deutsch-, Mathematik-, Synchronisations- und Zahlenraumprüfungen bestanden. Modul und beide App-Dateien sind bytegleich zu MA-016; vorhandene Karten, Grenzen und Entwürfe bleiben unberührt. Kein erneuter Browserlauf bei dieser reinen Auditänderung; der öffentliche Browsernachweis für App 1.320 liegt in MA-016. Audit auf main veröffentlicht mit Commit 6c6f359359ab3bec160414df7e13771d5a56a8d1. [Pages-Lauf 42400107460](https://github.com/geafaellt/LernzielKompass/actions/runs/42400107460) erfolgreich; die öffentliche App wurde erneut abgerufen und stimmt bytegenau mit der geprüften App 1.320 überein.


## MA-018 · Hunderterfeld und Darstellungsvernetzung · App 1.321

MA-026 verbindet GS 187051 mit dem FSP3/4-Zahlenaufbau 35461/35468. Hunderterfeld und Bündelung stehen in der FSP-Bemerkung; beide Hauptoperatoren lauten Beherrschen. Die Karte konkretisiert die Erkennung voller Zehnergruppen und übriger Einer bis 100. Der ausdrückliche Darstellungsbezug entscheidet für das höhere Band, nicht allein der Zahlenraum. Weitere Feldmuster bleiben offen. MA-025 behält den anderen Schwerpunkt der Zehn-zu-eins-Bündelung.

MA-024 wird für GS 187052 und den Zehner-/Einer-Ausschnitt von 187053 wiederverwendet. Die FSP-Bemerkung 37871 nennt Sprechen, Darstellen und Verwenden von Zehner/Einer. Zahl und Zehner-Einer-Darstellung werden in beiden Richtungen didaktisch zugeordnet; der Operator Einblick gewinnen bleibt bestehen. Die FSP-Grenze bis 20 bleibt ausdrücklich aus dem Bandziel abgeleitet und umfasst alle relevanten Teilwerte, Zwischenwerte und Ergebnisse. Hunderter, Stellenwert und Stellenwerttafel als eigenständige Fachwörter bleiben Anschlussfrage; vollständiger flexibler Darstellungswechsel und Sachsituationsbezüge sind nicht behauptet.

Drei neue Unterzielzeilen begrenzt geprüft, Elternzeile 1856 nur als Kontext. Bestehende Zahlenzerlegung und Zehner-Einer-Stellenwerte erneut bestätigt. Bestand 26 Karten, sieben stufenübergreifend, 99 Quellenlinks (97 Zielanker und zwei Kontextquellen). Die übrigen 24 Karten bleiben unverändert. 23 Zeilen des nächsten Operationsblocks wurden nur inventarisiert; die Teilinventur umfasst jetzt 67 Zeilen. Inventur zählt nicht als fachlicher Prüffortschritt. Fortsetzung bei 1857, sechs Anschlussfragen und frühere Restumfänge bleiben erhalten. Datenprüfungen, Grenzregressionen und lokaler Browserdurchlauf aller 26 Karten bestanden. App 1.321 ist mit Commit 02c9b536d13bd49326790ddba133d6f55094d770 veröffentlicht; [Pages-Lauf 42403704070](https://github.com/geafaellt/LernzielKompass/actions/runs/42403704070) ist erfolgreich. Die öffentliche Datei stimmt bytegenau mit dem geprüften Stand überein. Der Browserdurchlauf aller 26 Mathematikkarten wurde öffentlich erfolgreich wiederholt.


## MA-019 · Operationsverständnis: Vereinigen und Wegnehmen · App 1.324

MA-027 verbindet GS 187054 mit dem Vereinigen disjunkter Mengen, MA-028 verbindet GS 187055 mit Wegnehmen einer enthaltenen Teilmenge und Restmenge. Grundlage sind die ausdrücklichen FSP 1/2-Zeilen 37859 (Vereinigungs-/Differenzmengen) und 37863 (Addition/Subtraktion), unter Einblick gewinnen (37851). GS verlangt Kennen (1857). Beide FSP-Bänder wurden geprüft; der passende 1/2-Anschluss wird gegenüber der Alternative Addieren/Subtrahieren bis 100 unter Beherrschen in FSP 3/4 bevorzugt.

Der Feinzielrahmen bis 20 stammt aus dem übergreifenden FSP 1/2-Ziel zu Mengen und Operationsvorstellungen; die Unterzielzeilen nennen keine eigene Obergrenze. Alle Teil-, Gesamt- und Restanzahlen, relevanten Zwischen- und Endergebnisse bleiben darin. Auch die Summe darf 20 nicht überschreiten; weggenommene Mengen sind Teilmengen, negative Ergebnisse ausgeschlossen. Der GS-Zahlenraum bis 100 wird nicht vollständig gedeckt. Aufgaben und Hilfsmittel werden nicht ergänzt.

MA-015 bleibt unverändert bei der Teil-Ganzes-Beziehung unter GS-Beherrschen. Sie wird nicht ein zweites Mal als Operationsverständnis gezählt. Die 26 bisherigen Karten und ihre Grenzen bleiben erhalten. Die neuere Platzierung der FSP-Informationsübersicht unterhalb der Navigation aus App 1.323 wird bewahrt.

Zwei weitere Unterzielzeilen begrenzt geprüft; 1857 und 1858 nur Kontext. Bestand 28 Karten, davon 7 stufenübergreifend; 103 Quellenlinks (101 Zielanker, zwei Kontextquellen), weiterhin 67 inventarisierte Zeilen. Hinzufügen, Ergänzen und vergleichendes Bestimmen der Differenz bleiben als Restumfänge dokumentiert. Fortsetzung bei 187056 (Darstellungsvernetzung), danach 1861. Sechs bisherige Anschlussfragen bleiben offen; der Gesamtvergleich ist nicht abgeschlossen. Prüf- und Veröffentlichungsnachweise: review_batch_019.json.

Datenprüfungen, Zahlenraumregressionen und lokaler Browserdurchlauf aller 28 Mathematikkarten bestanden. Die zehn Fälle der Informationsübersicht wurden ebenfalls im Browser geprüft; eigene Entwürfe bleiben erhalten. App 1.324 wurde mit Commit bb4c08289fcafedb008edbe2bda307e0a0f0b33d auf main veröffentlicht; [Pages-Lauf 42408988638](https://github.com/geafaellt/LernzielKompass/actions/runs/42408988638) ist erfolgreich. Die öffentliche App stimmt bytegenau mit der geprüften Fassung überein. Beide Browserprüfungen wurden auf der öffentlichen Seite erfolgreich wiederholt.
