# Mathematik-Abgleich · MA-047

Erster Prüfstand vom 06.11.2026. Grundlage sind der [sächsische Fachlehrplan Mathematik für die Grundschule, Fassung 2026](https://www.schulportal.sachsen.de/lplandb/lehrplan/912), und der [sächsische Fachlehrplan Mathematik für den Förderschwerpunkt Lernen, Fassung 2019](https://www.schulportal.sachsen.de/lplandb/lehrplan/139). Verglichen werden GS 1/2, 3 und 4 mit den gebündelten FSP-Stufenbändern 1/2 und 3/4.

Fünfundfünfzig Karten dokumentieren begrenzte Anschlüsse. Neununddreißig liegen im passenden Stufenband. MA-002, MA-011, MA-012, MA-022, MA-023, MA-025, MA-026, MA-044, MA-045, MA-046, MA-047, MA-048, MA-049, MA-050, MA-051 und MA-054 sind stufenübergreifend. Für Spiegelachsen wurde in FSP 1/2 das verwandte Ziel zu Mustern und Ornamenten geprüft. Der konkrete Spiegelachsenbezug ist in FSP 3/4 belegt.

| Karten | Geprüfte Ausschnitte |
| --- | --- |
| MA-001 und MA-002 | Relative Lage von Objekten und Erkennen einer Spiegelachse |
| MA-003 und MA-004 | Geldbeträge innerhalb einer Einheit und Vergleich von Längen in Metern |
| MA-005 und MA-007 | Schriftliche Addition zweier Summanden in GS 3 und als Verfahrensanschluss in GS 4 |
| MA-006 | Minutengenaues Ablesen von Uhrzeiten in GS 3 und FSP 3/4 |

Die Operatoren stammen aus den übergeordneten Zielzeilen der jeweiligen Lehrpläne. Unterziele grenzen den Anschluss ein. Hinweise aus der Bemerkungsspalte bleiben Kontext. Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlungen, Aufgaben und Hilfsmittel legt die Lehrkraft fest.

[Prüfstand und Zeilenanker](review_progress.json) enthält die ausgewählten amtlichen Anker mit Bereich, Hierarchie und Operator. [Die Karten](mathematik_module.json) enthalten die jeweilige fachliche Grenze, Quellenlinks und die getrennten Ziele. Alle zwölf GS-Lernbereiche sind in der App auswählbar. Bereiche ohne Karte und die restlichen Ausschnitte innerhalb der Bereiche bleiben offen. Eine vollständige Einzelzeilenprüfung und eine Rückwärtsprüfung FSP → GS stehen aus.

App1.354 wurde inzwischen veröffentlicht und bytegenau geprüft; die öffentliche MA-051-Prüfung ist bestanden. Der ursprüngliche Pages-Zeitlimitfehler bleibt in MA-042 dokumentiert.

Fortsetzung bei Geldbeträgen mit zwei Einheiten1916. [MA-047](review_batch_047.json) präzisiert die bestehende MA-003 für Vergleich und Ordnung ganzer Beträge in derselben Einheit.55 Karten und elf Anschlussfragen; weitere Restumfänge bleiben offen. [Zeilenaudit](row_audit.csv).

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

MA-027 verbindet GS 187054 mit dem Vereinigen disjunkter Mengen, MA-028 verbindet GS 187055 mit Wegnehmen einer enthaltenen Teilmenge und Restmenge. Grundlage sind die ausdrücklichen FSP 1/2-Zeilen 37859 (Vereinigungs-/Differenzmengen) und 37863 (Addition/Subtraktion), unter Einblick gewinnen (37851). GS verlangt Kennen (1857). Beide FSP-Bänder wurden geprüft; der passende 1/2-Anschluss wird gegenüber der Alternative Addieren/Subtrahieren bis 100 unter Übertragen (35470) in FSP 3/4 bevorzugt. Diese Operatorzuordnung wurde in MA-020 berichtigt.

Der Feinzielrahmen bis 20 stammt aus dem übergreifenden FSP 1/2-Ziel zu Mengen und Operationsvorstellungen; die Unterzielzeilen nennen keine eigene Obergrenze. Alle Teil-, Gesamt- und Restanzahlen, relevanten Zwischen- und Endergebnisse bleiben darin. Auch die Summe darf 20 nicht überschreiten; weggenommene Mengen sind Teilmengen, negative Ergebnisse ausgeschlossen. Der GS-Zahlenraum bis 100 wird nicht vollständig gedeckt. Aufgaben und Hilfsmittel werden nicht ergänzt.

MA-015 bleibt unverändert bei der Teil-Ganzes-Beziehung unter GS-Beherrschen. Sie wird nicht ein zweites Mal als Operationsverständnis gezählt. Die 26 bisherigen Karten und ihre Grenzen bleiben erhalten. Die neuere Platzierung der FSP-Informationsübersicht unterhalb der Navigation aus App 1.323 wird bewahrt.

Zwei weitere Unterzielzeilen begrenzt geprüft; 1857 und 1858 nur Kontext. Bestand 28 Karten, davon 7 stufenübergreifend; 103 Quellenlinks (101 Zielanker, zwei Kontextquellen), weiterhin 67 inventarisierte Zeilen. Hinzufügen, Ergänzen und vergleichendes Bestimmen der Differenz bleiben als Restumfänge dokumentiert. Fortsetzung bei 187056 (Darstellungsvernetzung), danach 1861. Sechs bisherige Anschlussfragen bleiben offen; der Gesamtvergleich ist nicht abgeschlossen. Prüf- und Veröffentlichungsnachweise: review_batch_019.json.

Datenprüfungen, Zahlenraumregressionen und lokaler Browserdurchlauf aller 28 Mathematikkarten bestanden. Die zehn Fälle der Informationsübersicht wurden ebenfalls im Browser geprüft; eigene Entwürfe bleiben erhalten. App 1.324 wurde mit Commit bb4c08289fcafedb008edbe2bda307e0a0f0b33d auf main veröffentlicht; [Pages-Lauf 42408988638](https://github.com/geafaellt/LernzielKompass/actions/runs/42408988638) ist erfolgreich. Die öffentliche App stimmt bytegenau mit der geprüften Fassung überein. Beide Browserprüfungen wurden auf der öffentlichen Seite erfolgreich wiederholt.


## MA-020 · Bildsituation und Gleichungsansatz · App 1.325

MA-029 verbindet GS 187056 (Darstellungsvernetzung) und 1861 (Lösungsansätze) mit einem einzigen begrenzten Gegenstand: Bildsituation → Additions-/Subtraktionsgleichung. Beide GS-Zeilen gehören zu Kennen (1857). FSP 1/2 nennt wesentliche Angaben/Rechenoperation (37898) und verschiedene Lösungswege (37908) unter Einblick gewinnen (37896); Situationsbilder und Gleichung stehen in den Bemerkungen. Die gerichtete Verbindung wird ausdrücklich didaktisch konkretisiert. Der passende Bandanschluss wird gegenüber geprüften FSP-3/4-Alternativen bevorzugt.

Der FSP-Feinzielrahmen bis 20 stammt aus dem übergreifenden Operationsziel, nicht aus einer eigenen Grenze der Sachaufgabenzielzeilen. Dargestellte Anzahlen, Gleichungswerte sowie Zwischen- und Endergebnisse bleiben darin; Summe höchstens 20, keine negative Restanzahl. Keine Aufgaben, Lernhandlungen oder Hilfsmittel werden vorgeschlagen. Der gesamte GS-Bereich bis 100, sämtliche Darstellungswechsel, die Umkehrrichtung, weitere Tabellen-/Term-/Ungleichungsansätze, verschiedene Platzhalterpositionen und das Probieren mehrerer Lösungswege sind nicht vollständig abgedeckt.

Korrektur zu MA-019: Der alternative FSP-3/4-Unterpunkt 35479 steht unter Übertragen (35470), nicht unter Beherrschen (35461). Der Quell-Elternanker war bereits richtig gespeichert; berichtigt werden die Entscheidungstexte und der Bericht. Die bisherigen 28 Karten und ihre Operatoren, Grenzen und Ziele bleiben unverändert. Die Korrektur ist in beiden Prüfpaketen nachvollziehbar dokumentiert.

Zwei weitere GS-Zeilen begrenzt geprüft, eine neue Karte; keine Doppelzählung der gemeinsamen Karte oder der Elternziele. Bestand 29 Karten, davon sieben stufenübergreifend; 108 Quellenlinks (106 Zielanker, zwei Kontextquellen), weiterhin 67 inventarisierte Zeilen. Fortsetzung bei 1862/1863 (Rechenstrategien, bekannte Aufgaben). Sechs offene Anschlussfragen und bisherige Restumfänge bleiben erhalten. Prüf- und Veröffentlichungsnachweise: review_batch_020.json.

Datenprüfungen, Zahlenraumregressionen und lokaler Browserdurchlauf aller 29 Mathematikkarten bestanden. Die zehn Fälle der Informationsübersicht wurden ebenfalls im Browser erfolgreich geprüft. App 1.325 wurde mit Commit f9acf8f2315ff19b43f54f1a48347f6382a8c80a auf main veröffentlicht; [Pages-Lauf 42462093033](https://github.com/geafaellt/LernzielKompass/actions/runs/42462093033) ist erfolgreich. Die öffentliche App stimmt bytegenau mit der geprüften Fassung überein. Nach anfänglichen Ladezeitüberschreitungen bestanden beide öffentlichen Browserprüfungen bei der Wiederholung. Die vollständigen Nachweise einschließlich Wiederholungen stehen im Prüfpaket.


## MA-021 · Bekannte Additionen nutzen · App 1.326

MA-030 begrenzt GS 1863 auf das Ableiten einer Addition mit zusätzlichem Zehner aus einer bekannten Eineraddition. MA-031 begrenzt GS 187061 auf eine additive Nachbaraufgabe mit um eins größerem zweiten Summanden. Der Nachbarpunkt wird als fachlich zusammenhängender Teil dieses Pakets vorgezogen; bei der späteren Fortsetzung wird er nicht erneut als neue Zielzeile gezählt. GS 1862 bleibt Kontext für die einzelnen Strategien.

Beide Karten verwenden den passenden FSP-Bandanschluss 1/2: Einblick gewinnen (37851), Rechenvorteile bis 20 (37885). Die konkreten Wege stammen aus der Bemerkung. Der Zahlenraum bis 20 steht hier ausdrücklich in der Unterzielzeile; er wird nicht aus dem Bandziel abgeleitet. Ausgangszahlen, Summanden, Zwischen- und Endergebnisse einschließlich der veränderten Summe bleiben darin. Der GS-Rahmen bis 100 wird nicht vollständig gedeckt. Aufgaben und Hilfsmittel werden nicht ergänzt.

Die FSP-3/4-Alternative 35485 unter Übertragen (35470) wurde geprüft, aber nicht allein wegen größerem Zahlenraum oder allgemeinerer Formulierung bevorzugt. Das Wort Übertragen im FSP-1/2-Bemerkungsbeispiel bezeichnet den Rechenweg, keine neue Operatorstufe. Die bisherige Anschlussfrage 1849 zu Stellenwertanalogien unter GS-Beherrschen bleibt separat, mit Hinweis auf den neuen begrenzten Rechenbeleg. Alle 29 bisherigen Karten bleiben unverändert.

Die Zahlenraumprüfung unterstützt nun auch ausdrücklich belegte Grenzen aus Unterzielzeilen. Sie verlangt dafür einen zur Karte gehörenden Zielanker und denselben Beleg im FSP-Geltungsbereich; Verwechslungen mit übergreifenden Bandzielen oder unbelegten Elternzeilen werden geprüft.

Zwei GS-Zeilen begrenzt geprüft, zwei neue Karten. Bestand 31 Karten, davon sieben stufenübergreifend;112 Quellenlinks (110 Zielanker, zwei Kontextquellen), weiterhin 67 inventarisierte Zeilen. Andere Rückführungen, Subtraktions- und Nachbarvarianten bleiben Restumfänge. Fortsetzung bei 187057 (Verdoppeln), anschließend 187058–187060; sechs Anschlussfragen bleiben offen. Prüf- und Veröffentlichungsnachweise: review_batch_021.json.

Datenprüfungen, erweiterte Zahlenraumregressionen und lokaler Browserdurchlauf aller 31 Mathematikkarten bestanden. Auch die bestehende Informationsübersicht und der Erhalt eigener Entwürfe wurden erfolgreich geprüft. App 1.326 wurde mit Commit 5dbd0dd0384d6dbac6a34e328561fa616813949e auf main veröffentlicht; [Pages-Lauf 42463003417](https://github.com/geafaellt/LernzielKompass/actions/runs/42463003417) ist erfolgreich. Die öffentliche App stimmt bytegenau mit der geprüften Fassung überein. Beide Browserprüfungen wurden auf der öffentlichen Seite erfolgreich wiederholt.


## Gemeinsame Lerngegenstände · App 1.329

Alle 31 Vorschläge waren identisch mit den Kartentiteln. Sie benennen jetzt die gemeinsame mathematische Sache oder Beziehung, etwa „Zehner und Einer – der Aufbau einer zweistelligen Zahl und die Werte ihrer beiden Stellen“. Verfahrenskarten behalten ihren konkreten Verfahrensbezug. Gleiche Gegenstände können bei verschiedenen GS-Stufen gleich formuliert sein; Zahlenräume, Operatoren und Feinziele bleiben getrennt. Die Vorschläge sind didaktische Konkretisierungen und keine neuen amtlichen Ziele oder Aufgaben. Eigene Texte werden weiterhin nur nach ausdrücklicher Übernahme ersetzt.

[Formulierungsprüfung aller 31 Karten](review_learning_objects_001.json) mit Vorher/Nachher, Grenzen und bestehenden Quellenankern. Keine neue Anschlusskarte oder geprüfte Zielzeile; Zeilenaudit, Fortschrittszähler und Fortsetzung MA-021 / page912_187057 bleiben unverändert.


## MA-022 · Schrittweise Addition und offene Verdoppelstrategie · App 1.331

MA-032 verbindet GS187058 mit FSP1/2: Addition mit Zehnerüberschreitung (37863) und Rechenwege bis20 (37885), unter Einblick gewinnen (37851). Ergänzen zur Zehn, Zerlegen und individuelle Lösungsschritte stehen in den Bemerkungen; der konkrete Zweischrittweg ist ausdrücklich eine didaktische Konkretisierung. GS verlangt Kennen unter1857. FSP3/4 nennt Nacheinanderausführen von Teilschritten ausdrücklich in der Bemerkung35485 unter Übertragen35470; der tragfähige stufenbandpassende Teilanschluss wird bevorzugt.

Der FSP-Zahlenraum bis20 ist in37885 ausdrücklich belegt. Zwei positive einstellige Summanden mit Zehnerüberschreitung, Ergänzungsteil, Rest, Zwischensumme und Endsumme bleiben darin. GS bis100 ist nicht vollständig gedeckt. Subtraktion, andere Wege, Strategiewahl und Protokollieren bleiben außerhalb. Der gemeinsame Lerngegenstand benennt Ergänzungsteil und Rest; keine Aufgaben oder Hilfsmittel werden ergänzt.

Verdoppeln187057 bleibt eine eigene Anschlussfrage. MA-011 belegt bereits Verdoppeln von Mengen/Zahlbeziehungen unter GS-Beherrschen; die Übernahme in den GS-Kennen-Strategiekontext wird nicht automatisch behauptet. Beide FSP-Bänder wurden geprüft, positive Inhaltsbezüge sind erhalten. Das ist keine pauschale Nichtanschlussentscheidung und kein Ausschluss wegen Zahlenraum.

Eine Zielzeile begrenzt zugeordnet, eine zusätzliche Anschlussfrage offen; keine neue vollständig erledigte Zeile.32 Karten, sieben stufenübergreifend,113 Quellenlinks (111 Zielanker, zwei Kontextquellen), weiterhin67 Inventurzeilen und nun sieben Anschlussfragen. Bestehende31 Karten einschließlich Zahlenraumgrenzen und Lerngegenständen unverändert. Fortsetzung187059/187060;187061 nicht erneut zählen. Prüf- und Veröffentlichungsnachweise: review_batch_022.json.

Datenprüfungen, Zahlenraumregressionen, lokaler und öffentlicher Browserdurchlauf aller32 Mathematikkarten bestanden; die Kartenauswahl wurde zusätzlich in allen drei Fächern geprüft. App1.331 wurde mit Commit165fa992bb4160b33f9a2d82a389ff2e48fdc034 auf main veröffentlicht; [Pages-Lauf42467586448](https://github.com/geafaellt/LernzielKompass/actions/runs/42467586448) ist erfolgreich. Die ausgelieferte App stimmt bytegenau mit dem geprüften Stand überein.


## MA-023 · Tausch- und Umkehraufgaben · App 1.336

MA-033 verbindet das Vertauschen der Summanden mit unveränderter Summe; MA-034 die Ableitung einer zugehörigen Subtraktion aus einer bekannten Addition. Beide sind stufenbandpassend GS1/2 → FSP1/2. GS-Kennen stammt aus1857, FSP-Einblick gewinnen aus37851. Die konkreten Strategien stehen in der Bemerkung37885; der Zahlenraum bis20 steht ausdrücklich in dieser Zielzeile. FSP3/4 bietet additive Gegenbelege in35485 unter Übertragen35470. Die multiplikativen Tausch-/Umkehrbeispiele35442 unter Kennen35439 werden nicht als additive Belege umgedeutet.

Feinziele und Erfolgskriterien sind didaktisch konkretisiert. Alle beteiligten Zahlen und relevanten Zwischen-/Endergebnisse bleiben im FSP bis20. Vertauschen wird nicht auf Subtraktion übertragen; bei Umkehraufgaben wird von der bekannten Summe ein ursprünglicher Summand abgezogen. Keine Aufgaben, Lernhandlungen oder Hilfsmittel ergänzt. Gemeinsame Lerngegenstände benennen die mathematischen Beziehungen.

Zwei Zeilen teilweise geprüft, keine vollständig abgeschlossen.34 Karten, davon27 stufenbandpassend, sieben stufenübergreifend;115 Quellenlinks (113 Zielanker, zwei Kontextquellen), weiterhin67 Auditzeilen. Alle32 bisherigen Karten unverändert. Sieben Anschlussfragen bleiben bestehen; neue Restumfänge sind dokumentiert. Aufgabenfamilien, Umkehrrichtung, Kontrollzweck und selbstständige Strategiewahl bleiben gesondert zu prüfen. Fortsetzung187062;187061 nicht erneut zählen. Nachweise in review_batch_023.json.

Datenprüfungen und Zahlenraumregressionen bestanden. Lokal alle34 Mathematikkarten sowie die Hinweise/Quellen aller347 Karten geprüft; öffentlicher Browserdurchlauf aller34 Mathematikkarten bestanden. App1.336 mit Commitf49e28b207b0a9394ab53b717fc9b10ea1f0a57b veröffentlicht; [Pages-Lauf42476820597](https://github.com/geafaellt/LernzielKompass/actions/runs/42476820597) erfolgreich. Die öffentliche HTML-Datei ist bytegleich zum geprüften Stand. Feedbackfunktion und rechte Bildposition bleiben erhalten.


## MA-024 · Aufgabenfamilien und Ergänzungen · App 1.337

MA-035 verbindet zwei vertauschte Additionen und ihre beiden Umkehraufgaben. Diese vier Beziehungen sind in der FSP-Bemerkung 37885 belegt; ihre Zusammenfassung als Aufgabenfamilie ist didaktisch konkretisiert, kein wörtliches FSP-Unterziel. Das Feinziel ist auf verschiedene positive Summanden begrenzt. MA-036 verbindet eine gesuchte Differenz mit dem fehlenden Summanden einer Ergänzung; die Bemerkungen GS 187063 und FSP 37885 belegen dieselbe Beziehung. Ergänzen bis 10 aus 37863 wird nicht zur Obergrenze der Zielzeile 37885 umgedeutet.

Beide Anschlüsse sind GS 1/2 → FSP 1/2, mit Kennen (1857) und Einblick gewinnen (37851). Die Grenze bis 20 ist in der FSP-Zielzeile ausdrücklich belegt und gilt auch für alle beteiligten Zahlen und relevanten Zwischen-/Endergebnisse der didaktischen Feinziele und Kriterien. GS reicht bis 100; vollständige GS-Zieldeckung wird nicht behauptet. FSP 3/4 wurde mitgeprüft: additive Tausch-/Umkehrbeziehungen in 35485 unter Übertragen, multiplikative Vierergruppen in 35442 unter Kennen. Letztere sind kein additiver Beleg.

Die Einzelbeziehungen MA-033/034 und der Teilschritt in MA-032 bleiben erhalten; keine Doppelzählung. Alle 34 bisherigen Karten unverändert. Zwei weitere Zeilen teilweise geprüft, keine vollständig abgeschlossen. 36 Karten, davon 29 stufenbandpassend und sieben stufenübergreifend; 117 Quellenlinks (115 Zielanker, zwei Kontextquellen), weiterhin 67 Auditzeilen und sieben Anschlussfragen. Sonderfälle, größere Zahlenräume, selbstständige Strategiewahl und Kontrollzweck bleiben abgegrenzt. Keine Aufgaben, Lernhandlungen oder Hilfsmittel ergänzt. Fortsetzung 187064. Test- und Veröffentlichungsnachweise in review_batch_024.json.

Veröffentlicht auf main mit App-Commit `ad4698fa3c27e6507cdf0ef0fc1fcafc883677d7`; [Pages-Lauf 42486092319](https://github.com/geafaellt/LernzielKompass/actions/runs/42486092319) erfolgreich. Ausgelieferte App 1.337 ist bytegleich (SHA-256 `75a62081d79a88bcc99723f505e05b65d22d16435181d4134fe0b3c1d2cd87c1`). Daten-, Zahlenraum- und Lerngegenstandsprüfungen bestanden. Alle 36 Mathematikkarten lokal und öffentlich im Browser geprüft; Hinweise/Quellen für alle 349 Karten lokal geprüft. Zwei anfängliche Wartezeitfehler bei Standard-Browserläufen sind im Prüfpaket dokumentiert; der vollständige unveränderte Test bestand mit abgeschalteter Hintergrunddrosselung ohne erzwungene Klicks oder ausgelassene Prüfungen.


## MA-025 · Gegensinniges und gleichsinniges Verändern · Audit ohne App-Änderung

Die GS-Zeile 187064 unter Kennen (1857) wurde gegen beide FSP-Stufenbänder geprüft, einschließlich Mengeninvarianz, Rechenvorteilen, Variation von Mengen/Sachverhalten sowie einschlägigen Wahlbereichen. Gegenstand sind abgestimmte Änderungen beider Operanden bei gleichbleibender Summe bzw. Differenz. Der GS-Bemerkungsbeleg konkretisiert die Differenzkonstanz.

Kein hinreichend belegter direkter Anschluss: Mengeninvarianz bei Umordnung, Tausch- und Umkehrbeziehungen, Teilschritte und allgemein zugelassene Variation sind mathematisch verwandte, aber nicht identische Belege. Auch FSP 3/4 mit ausdrücklich gleicher Grenze bis 100 liefert in den geprüften Zeilen keinen hinreichend konkreten Ausgleichsbeleg. Ein kleinerer FSP-Zahlenraum ist daher ausdrücklich nicht der Ablehnungsgrund. Eine didaktische Behandlung bleibt möglich; der Befund betrifft die belegte Kartenabdeckung. Quellenanker, Operatoren, Pflicht-/Wahlbereiche und übergreifende Ziele sind im [Prüfpaket MA-025](review_batch_025.json) getrennt dokumentiert.

MA-031 bis MA-036 wurden auf vermeintliche Überschneidungen nachgeprüft und bleiben unverändert, einschließlich FSP-Grenze bis 20 und Grenzen der Feinziele/Kriterien. Keine neue Karte, kein neues Feinziel und keine Aufgaben, Lernhandlungen oder Hilfsmittel. Eine zusätzliche Zeile mit Einzelentscheidung, keine neue Zieldeckung; weiterhin 36 Karten, 117 Quellenlinks/115 Karten-Zielanker, 67 Auditzeilen und sieben Anschlussfragen. Nun vier dokumentierte Zeilenentscheidungen ohne hinreichend belegten direkten Anschluss. Der gesamte spezifische Inhalt 187064 bleibt ohne Kartenabdeckung; keine zusätzliche Zählung der Kontextzeilen 1857/1862. Fortsetzung 1864. App bleibt 1.337.

Audit auf main veröffentlicht mit Commit `ca59c5d0f74c4579c26ac43d6f01f8a9f60264c8`; [Pages-Lauf 42487438962](https://github.com/geafaellt/LernzielKompass/actions/runs/42487438962) erfolgreich. Ausgelieferte App 1.337 unverändert und bytegleich (SHA-256 `75a62081d79a88bcc99723f505e05b65d22d16435181d4134fe0b3c1d2cd87c1`). Deutsch-, Mathematik-, Zahlenraum- und Erhaltungsprüfungen bestanden; keine neue Browserprüfung für die unveränderte App behauptet. Die vollständigen Browsernachweise aus MA-024 bleiben maßgeblich.


## MA-026 · Lösungswege und Kontrolle · App 1.340

MA-037 verbindet das Erproben verschiedener additiver Rechenwege. Die Zahl von zwei Wegen ist didaktisch konkretisiert. GS-Begründen und insbesondere kritisches Bewerten werden nicht als gleichwertige FSP-Anforderung ausgegeben; weiterführende Bezüge aus FSP 3/4 und dessen Wahlbereichen bleiben gesondert dokumentiert. MA-038 konkretisiert die Kontrolle eines angegebenen Additionsergebnisses durch Subtraktion mit anschließender Entscheidung anhand des Ergebnisvergleichs. Das ist gegenüber MA-034 ein zusätzlicher Kontrollzweck; einzelne Strategien und die Aufgabenfamilie MA-035 werden nicht doppelt gezählt.

Beide Anschlüsse sind GS 1/2 → FSP 1/2 mit Kennen (1857) und Einblick gewinnen (37851). MA-037: Grenze bis 20 ausdrücklich aus Zielzeile 37885. MA-038: Kontrollzeile 37889 ohne eigene Obergrenze; bis 20 ausdrücklich als didaktische Ableitung aus übergreifendem Stufenziel 37739. Die benachbarte Zeile 37885 wird nicht als Grenze von 37889 ausgegeben. Feinziele/Kriterien halten alle Ausgangswerte und relevanten Zwischen-/Endergebnisse ein; bei Kontrolle auch richtige/angegebene Summe und Kontrollresultat, ohne negative Werte.

Alle 36 bisherigen Karten und übrigen Fachbestände bleiben erhalten. Zwei weitere GS-Zeilen teilweise geprüft, keine vollständig abgeschlossen. 38 Karten (31 stufenbandpassend, sieben stufenübergreifend), 120 Quellenlinks (118 Karten-Zielanker, zwei Kontextquellen), weiterhin 67 Auditzeilen, sieben Anschlussfragen und vier Entscheidungen ohne hinreichend belegten direkten Anschluss. Bewertungs-/Begründungsreste und Erfahrungsvergleich bleiben offen. Keine Aufgaben, Lernhandlungen oder Hilfsmittel automatisch ergänzt. Fortsetzung 187069; Nachweise im Prüfpaket.

Veröffentlicht auf main mit App-Commit `8bebb9152b2140e5c3a916e4701866f30bb92b33`; [Pages-Lauf 42491626536](https://github.com/geafaellt/LernzielKompass/actions/runs/42491626536) erfolgreich. Ausgelieferte App 1.340 bytegleich (SHA-256 `47dd42f25a9bd3bb46dbb47f29ef6e35890abbaca272a7d52b715e855e63e5fd`). Daten-, Zahlenraum- und Erhaltungsprüfungen bestanden; alle 38 Mathematikkarten lokal und öffentlich im Browser geprüft, einklappbare Hinweise/Quellen für alle 351 Karten lokal geprüft. Der erste öffentliche Prüfaufruf wurde vor Ausführung durch eine Zeitüberschreitung der automatischen Freigabeprüfung abgebrochen; die erlaubte Wiederholung lief erfolgreich. Die neuen Startseitenbeschriftungen Grund-/Oberschule bleiben erhalten.


## MA-027 · Gleichschrittige Zahlenfolgen · App 1.341

MA-039 verbindet den GS-Musterauftrag unter Kennen (1857, 187069/187070) mit dem FSP-Schrittzählen unter Beherrschen (37931, 37950/37952). GS erkennt/beschreibt/ergänzt die ausgewählte gleichschrittige Folge; FSP setzt mit vorgegebener Richtung und Schrittweite im Naturkontext fort. Ein vollständiges selbstständiges Entdecken/Beschreiben einer Bildungsregel wird für FSP nicht behauptet. 2er-/5er-Schritte sind Bemerkungsbeispiele, keine neue Pflicht. Alle Folgenglieder und relevanten Zwischen-/Endergebnisse bleiben im FSP nichtnegativ und bis 20; der Rahmen ist ausdrücklich didaktisch aus Stufenziel 37739 abgeleitet. Die Zählzeilen haben keine eigene Obergrenze. GS bleibt bis 100, ohne vollständige Zieldeckung.

MA-020 bleibt für Zählhandlungen unter dem anderen GS-Hauptoperator Beherrschen erhalten; keine erneute Zählung von 1844. FSP3/4 sowie geometrische Muster, Rechenwege und Wahlbereiche wurden als Gegenbezüge geprüft. Strukturierte Aufgabenformate und operative Serien bleiben eigene Prüfpunkte. Alle 38 bisherigen Karten bleiben unverändert. Eine neue teilweise geprüfte Inhaltszeile (187070), eine Kontextprüfung (187069), kein vollständiger Zeilenabschluss. 39 Karten (32 stufenbandpassend, sieben stufenübergreifend), 122 Quellenlinks/120 Karten-Zielanker plus zwei Kontextquellen, weiterhin 67 Auditzeilen und sieben Anschlussfragen. Keine Aufgaben, Lernhandlungen oder Hilfsmittel ergänzt.

Veröffentlicht auf main mit App-Commit `e58f6996ca474e92405a58ce5b386e9230722721`; [Pages-Lauf 42505192428](https://github.com/geafaellt/LernzielKompass/actions/runs/42505192428) erfolgreich. Ausgelieferte App 1.341 bytegleich (SHA-256 `d7f9c888eac79e810a0cea209f8d05122d7e62caf59bd18eba9ce2f0d3adff7c`). Daten-, Zahlenraum- und Erhaltungsprüfungen bestanden; alle 39 Mathematikkarten lokal und öffentlich geprüft, einklappbare Hinweise/Quellen aller 352 Karten lokal geprüft. Der erste öffentliche Browsertest brach beim Warten auf Schaltflächenstabilität ab; die vollständige Wiederholung mit Kartenprotokoll bestand ohne erzwungene Klicks oder ausgelassene Prüfungen. Der Abbruch ist im Prüfpaket dokumentiert.


## MA-028 · Strukturierte Formate und operative Nachbarmuster · App 1.342 · 09.11.2026

MA-040 verbindet die in beiden Bemerkungsspalten benannten Zahlen-/Rechenmauern, didaktisch begrenzt auf eine vereinbarte additive Beziehung. FSP-Anwenden stammt aus 38017; der Wahlbereich 4 Zahlenzauberei muss gewählt sein. Diese Voraussetzung steht im FSP-Anker, im Zahlenraumfeld und dessen Planungsgrenze sowie im Hinweis. Bis 20 ist aus dem Stufenbandziel 37739 abgeleitet, nicht in der Wahlbereichszeile ausdrücklich festgelegt. Auch Summen höherer Reihen müssen im Rahmen bleiben. Keine konkrete Mauer, Aufgabe, Lernhandlung oder Hilfsmittel vorgeschlagen.

MA-031 wird für 187072 wiederverwendet: nur der lokale Nachbarübergang mit unverändertem ersten Summanden und um eins wachsendem zweiten Summanden/Ergebnis. GS-Kennen bleibt für beide Bezüge identisch. Das GS-Feinziel benennt nun zusätzlich Erkennen/Beschreiben dieses Zusammenhangs; FSP-Feinziel und ausdrückliche Grenze bis 20 bleiben unverändert. Keine neue Karte für denselben Zusammenhang, keine erneute Zählung von 187061, keine Behauptung vollständiger Serienabdeckung.

Zwei weitere GS-Zeilen teilweise geprüft, keine vollständig abgeschlossen. 40 Karten (33 stufenbandpassend, sieben stufenübergreifend), 126 Quellenlinks/124 Karten-Zielanker plus zwei Kontextquellen, weiterhin 67 Auditzeilen, sieben Anschlussfragen und vier Entscheidungen ohne hinreichend belegten direkten Anschluss. Alle übrigen 38 Karten und Fachbestände unverändert. Fortsetzung 187073; Quellen, Voraussetzungen und Restumfänge im Prüfpaket.

Veröffentlicht auf main mit App-Commit `6c61b32bb60c277f2a9c5014e703d9a03ae58d88`; [Pages-Lauf 42578818983](https://github.com/geafaellt/LernzielKompass/actions/runs/42578818983) erfolgreich. Ausgelieferte App 1.342 bytegleich (SHA-256 `00eddba560813d137427df0b10dfc8590db990880a4f8a7c766f676849b3ed5c`). Daten-, Zahlenraum-, Wahlbereichs- und Erhaltungsprüfungen bestanden; alle 40 Mathematikkarten lokal und öffentlich im Browser geprüft, einklappbare Hinweise/Quellen aller 353 Karten lokal geprüft. Eine frühere Browserausführung lieferte keinen aufbewahrten Abschlussnachweis; nur die vollständig protokollierte Wiederholung wird als Nachweis gezählt. Fortsetzung 187073; sieben Anschlussfragen und alle Restumfänge bleiben offen.


## MA-029 · Fachbegriff Summe im Geldkontext · App 1.343 · 09.11.2026

MA-041 verbindet das GS-Verwenden des Fachworts Summe (187073, Kennen aus 1857) mit dem ausdrücklichen FSP-Differenzierungshinweis im Geldkontext (37927, Einblick gewinnen aus 37913). Der unterstützte Begriffszugang ist eine didaktische Konkretisierung, keine allgemeine gleichwertige Fachwortanforderung. FSP bis 20 ist aus dem Stufenbandziel 37739 abgeleitet, nicht in der Geldzeile festgelegt. Alle Einzelbeträge und relevanten Zwischen-/Endergebnisse bleiben innerhalb derselben Einheit Euro oder Cent im Rahmen; keine gemischten Einheiten, Kommaschreibweisen oder Umrechnungen.

Beide FSP-Bänder, übergreifende Sprachziele und bestehende Inhaltskarten geprüft. Die übrigen 14 Fachwörter bleiben ausdrücklich offen; Operations-/Symbolbelege werden nicht mit eigenständiger Wortverwendung gleichgesetzt. Alle 40 bisherigen Karten unverändert. Eine weitere GS-Zeile teilweise geprüft, keine vollständig abgeschlossen. 41 Karten (34 stufenbandpassend, sieben stufenübergreifend), 128 Quellenlinks/126 Karten-Zielanker plus zwei Kontextquellen, 70 Auditzeilen (drei neu inventarisierte, noch ungeprüfte Zeilen des folgenden Grundaufgabenblocks), acht Anschlussfragen und vier Entscheidungen ohne hinreichend belegten direkten Anschluss. Keine Aufgaben, Lernhandlungen oder Hilfsmittel ergänzt. Fortsetzung 1867/55442/55444; Nachweise im Prüfpaket.

Veröffentlicht auf main mit App-Commit `eabe4bb2d13928cbb33b3aace531ae0db0934a5f`; [Pages-Lauf 42581499672](https://github.com/geafaellt/LernzielKompass/actions/runs/42581499672) erfolgreich. Ausgelieferte App 1.343 bytegleich (SHA-256 `2baf6b109e99f40afc7fceecf25b950b4cd9d7ee4c54780d6b86bdc3fdcb9e69`). Daten-, Zahlenraum- und Erhaltungsprüfungen bestanden; alle 41 Mathematikkarten lokal und öffentlich im Browser geprüft, einklappbare Hinweise/Quellen aller 354 Karten lokal geprüft. Die ersten beiden öffentlichen Läufe brachen beim Warten auf Schaltflächenstabilität an MA-036 bzw. MA-013 ab. Der vollständige Lauf mit deaktivierter Grafikbeschleunigung/Native-Win-Occlusion und initialem Bring-to-front bestand mit unverändertem Prüffile, normalen Klicks und sämtlichen Assertions. Eine definitive Ursache der sporadischen Abbrüche ist damit nicht bewiesen. Fortsetzung 1867/55442/55444; acht Anschlussfragen und alle Restumfänge bleiben offen.


## MA-030 · Grundaufgaben bis 10 aus dem Gedächtnis · App 1.344 · 09.11.2026

MA-042 verbindet den ausgewählten GS-Grundaufgabenausschnitt (1867/55442, Beherrschen) mit dem ausdrücklichen FSP-Unterziel zum gedächtnismäßigen Verfügen bis 10 (37869 unter Einblick gewinnen 37851; Operationskontext 37863). Der FSP-Hauptoperator bleibt korrekt zugeordnet; die konkrete Gedächtnisanforderung wird erhalten. Die GS-Zeilen nennen keine eigene Obergrenze: bis 10 ist dort nur die didaktische Auswahl, nicht eine erfundene amtliche Grenze. Sämtliche Ausgangszahlen sowie relevanten Zwischen-/Endergebnisse bleiben nichtnegative ganze Zahlen bis 10. Keine Zeitlimits, konkreten Aufgaben oder Hilfsmittel vorgeschlagen.

Beide FSP-Bänder geprüft: FSP3/4-Einspluseins bis 20 und weiterführende Rechen-/Strategiebezüge bleiben dokumentierte Alternativen. Alle41 bisherigen Karten unverändert; Operations-/Strategieanschlüsse unter GS-Kennen nicht umgewidmet. Eine neue teilweise geprüfte Inhaltszeile, ein geprüfter Hauptzielkontext, kein vollständiger Abschluss. 42 Karten (35 stufenbandpassend, sieben stufenübergreifend), 131 Quellenlinks/129 Karten-Zielanker plus zwei Kontextquellen; weiterhin 70 Auditzeilen, acht Anschlussfragen und vier Entscheidungen ohne hinreichend belegten direkten Anschluss. Fortsetzung 55444, siehe Prüfpaket.

Veröffentlicht auf main mit App-Commit `34cd1938711ec31ce96690a695763613c58b762a`; [Pages-Lauf 42589270552](https://github.com/geafaellt/LernzielKompass/actions/runs/42589270552) erfolgreich. Ausgelieferte App 1.344 bytegleich (SHA-256 `7f8a1baeb8ff1f600e27745174286ce753d7f2af0ba8b4b8fd6eaa683fc3230e`). Daten-, Zahlenraum- und Erhaltungsprüfungen bestanden; alle 42 Mathematikkarten lokal und öffentlich funktional geprüft, einklappbare Hinweise/Quellen aller 355 Karten lokal geprüft. Der erste öffentliche Lauf brach bei MA-025 während des Scrollens zur Zurück-Schaltfläche ab. Die vollständige Wiederholung mit deaktivierter Scrollanimation im Testbrowser bestand mit unverändertem Prüffile, normalen Klicks und sämtlichen Assertions. Die Animation selbst wird durch diesen Wiederholungslauf nicht validiert; App-Code blieb unverändert. Fortsetzung 55444; acht Anschlussfragen und alle Restumfänge bleiben offen.


## MA-031 · Umkehrvernetzung unter Beherrschen · App 1.345 · 09.11.2026

MA-043 konkretisiert die GS-Strategievernetzung (55444 unter Beherrschen1867) über die Ableitung einer Subtraktion aus einer vertrauten Addition zweier positiver einstelliger Summanden. FSP belegt die Beziehung in der Bemerkung zu Rechenvorteilen bis20 (37885 unter Einblick gewinnen37851). GS nutzt die ausgewählte Verknüpfung sicher und selbstständig; für FSP ist keine freie Strategiewahl vorausgesetzt. Die konkrete Strategieauswahl ist didaktisch. GS-Zielzeile ohne eigene Obergrenze, Auswahl bis20 didaktisch; FSP bis20 ausdrücklich. Alle Ausgangszahlen und relevanten Zwischen-/Endergebnisse bleiben im Rahmen. Das gesonderte Gedächtnisziel bis10 bleibt unverändert.

Beide FSP-Bänder und vorhandene Strategiekarten geprüft. MA-034 bleibt unter GS-Kennen erhalten: MA-043 ist eine zusätzliche Zuordnung zu einem anderen GS-Anforderungsniveau, kein neuer mathematischer Gegenstand. Alle42 bisherigen Karten unverändert. Eine weitere Zeile teilweise geprüft, keine vollständig abgeschlossen. 43 Karten (36 stufenbandpassend, sieben stufenübergreifend), 132 Quellenlinks/130 Karten-Zielanker plus zwei Kontextquellen; 86 Auditzeilen, davon16 neu inventarisierte ungeprüfte Zeilen des folgenden Multiplikations-/Divisionsblocks. Acht Anschlussfragen und vier Entscheidungen ohne hinreichend belegten direkten Anschluss bleiben erhalten. Keine Aufgaben oder Hilfsmittel ergänzt. Fortsetzung1881/1882/187075, siehe Prüfpaket.

Veröffentlicht auf main mit App-Commit `72c4e0d579a57b5f23dda265b0489d79ae943e10`; [Pages-Lauf 42625253259](https://github.com/geafaellt/LernzielKompass/actions/runs/42625253259) erfolgreich. Ausgelieferte App 1.345 bytegleich (SHA-256 `0b3c86c4adee4c42dd5870cf1a853304538458962af82fe0545923f20face90f`). Daten-, Zahlenraum- und Erhaltungsprüfungen bestanden; alle 43 Mathematikkarten lokal und öffentlich funktional geprüft, einklappbare Hinweise/Quellen aller 356 Karten lokal geprüft. Scrollanimation war im Testbrowser deaktiviert; normale Klicks und alle Assertions blieben unverändert. Die Animation selbst ist nicht Teil dieses Funktionsnachweises. Fortsetzung 1881/1882/187075; acht Anschlussfragen und alle Restumfänge bleiben offen.


## MA-032 · Multiplikative Grundvorstellungen · App 1.346 · 09.11.2026

MA-044 verbindet Verdoppeln/Halbieren unter GS-Kennen1881 mit dem ausdrücklichen FSP3/4-Unterziel35437 unter Einblick gewinnen35435. MA-011 bleibt mit GS-Beherrschen erhalten; keine erneute Zählung ihrer früheren Zeilen. MA-045 konkretisiert Vervielfachen und gerechtes Verteilen (35438) über gleich große Gruppen, Gesamtmenge und vorgegebene Gruppenanzahl. Aufteilen bei vorgegebener Gruppengröße und Restbehandlung werden nicht gleichgesetzt. Beide Karten sind stufenübergreifend GS1/2 → FSP3/4; die verwandten FSP1/2-Belege wurden geprüft. Der spezifische Inhalt, nicht der kleinere Zahlenraum, begründet die Auswahl.

FSP bis100 ist aus Bandziel35415 didaktisch abgeleitet, keine Obergrenze der Zielzeilen. Auch GS1881/1882/187075 nennt keine eigene Obergrenze; bis100 ist die Auswahl. Verdoppeln nur mit Ausgangsanzahl höchstens50, Halbieren positiver gerader Anzahlen, Gruppenprodukte bis100 und restfreies Verteilen. Alle relevanten Zwischen-/Endergebnisse bleiben im Rahmen. Aufgaben und Hilfsmittel bleiben Lehrkraftentscheidung.

Alle 43 bisherigen Karten unverändert. Eine neue teilweise geprüfte Inhaltszeile, zwei Kontextzeilen, kein vollständiger Abschluss. 45 Karten (36 stufenbandpassend, neun stufenübergreifend), 136 Quellenlinks/134 Karten-Zielanker plus zwei Kontextquellen; weiterhin 86 Auditzeilen. Neun Anschlussfragen und vier Entscheidungen ohne hinreichend belegten direkten Anschluss. Fortsetzung187076/187077; Nachweise im Prüfpaket.

Veröffentlicht auf main mit App-Commit `b54579e9ad253f2f981140ea7941133f8f4294ec`; [Pages-Lauf 42663200063](https://github.com/geafaellt/LernzielKompass/actions/runs/42663200063) erfolgreich. Ausgelieferte App 1.346 bytegleich (SHA-256 `0b2652a495e89808c841241c9d6c30bdc34be499ed8cbda127e6ea0531a4f752`). Daten-, Zahlenraum- und Erhaltungsprüfungen bestanden; alle 45 Mathematikkarten lokal und öffentlich funktional geprüft, einklappbare Hinweise/Quellen aller 358 Karten lokal geprüft. Scrollanimation war im Testbrowser deaktiviert; normale Klicks und alle Assertions blieben unverändert. Die Animation selbst ist nicht Teil dieses Funktionsnachweises. Fortsetzung 187076/187077; neun Anschlussfragen und alle Restumfänge bleiben offen.


## MA-033 · Punktefelder und sprachliche Gruppenbeschreibung · App 1.347 · 09.11.2026

MA-046 konkretisiert GS187076/187077 unter Kennen1881: von einem rechteckigen Punktefeld zur sprachlichen Beschreibung gleich großer Gruppen und ihrer Gesamtmenge. FSP3/4 nennt Vervielfachen/Teilen35438 unter Einblick gewinnen in gerechtes Verteilen35435; Punktfelder und Darstellungsebenen stehen in den Bemerkungen. Die konkrete Übersetzungsrichtung ist didaktische Konkretisierung, kein amtlicher FSP-Vernetzungsoperator. Kandidaten im FSP-Band1/2 wurden geprüft; sie sichern Mengenstruktur/Zahlzuordnung, nicht hinreichend konkret die hier ausgewählte multiplikative Bild-Sprache-Beziehung.

FSP bis100 ist aus Bandziel35415 didaktisch abgeleitet, GS-Zielzeilen ohne eigene Obergrenze. Gruppenanzahl, Punkte je Gruppe, Gesamtmenge und relevante Ergebnisse bleiben bis100; die Gruppierung bleibt gleich. Andere Darstellungen/Richtungen, selbstständige Auswahl, Gleichungsnotation, Division und Restdeutung bleiben offen. Aufgaben und Hilfsmittel bleiben Lehrkraftentscheidung.

Alle45 bisherigen Karten unverändert. Zwei teilweise geprüfte Inhaltszeilen mit einer neuen Karte; wiederverwendete Kontextzeilen werden nicht erneut gezählt. 46 Karten (36 stufenbandpassend, zehn stufenübergreifend),138 Quellenlinks/136 Karten-Zielanker plus zwei Kontextquellen; weiterhin86 Auditzeilen. Neun Anschlussfragen und vier Entscheidungen ohne hinreichend belegten direkten Anschluss. Fortsetzung1884; Nachweise im Prüfpaket.

Daten-, Zahlenraum-, Bestandsschutz- und Browserprüfungen bestanden: alle46 Mathematikkarten und die aufklappbaren Hinweise/Quellen aller359 Karten. Eigene Entwürfe bleiben erhalten, Aufgaben/Hilfsmittel leer. Erster Browserstart brach vor Prüfungen wegen falschem Arbeitsordner ab; korrigierter vollständiger Lauf bestanden. Testbrowser ohne Scrollanimation; Animation selbst nicht bewertet. App1.347 auf main veröffentlicht; Pages-Lauf 42665035746 erfolgreich. Öffentliche HTML-Datei bytegleich zum geprüften Stand (SHA-256 a71dd3860c97b073baaab58c85e0170e7fefa88e776687d533ffe2d3adebd053). Live-Browserprüfung aller46 Mathematikkarten bestanden. Details im [Prüfpaket MA-033](review_batch_033.json).


## MA-034 · Kernaufgaben als Bausteine · App 1.348 · 09.11.2026

MA-047 verbindet GS1885 unter Strategieziel1884/Kennen1881 mit FSP3/4: Kennen von Rechenhandlungen35439, Entdecken/Nutzen verschiedener Lösungswege35442 und Kernaufgaben der 2, 5 und 10 in der Bemerkung. Didaktisch ausgewählt ist die Ableitung eines Produkts durch Summe oder positive Differenz zweier bekannter Kernprodukte mit demselben zweiten Faktor. FSP1/2 wurde geprüft: Schrittzählen, additive Rechenvorteile und allgemeine Strategien sichern diesen spezifischen multiplikativen Weg nicht hinreichend.

GS bis 100 ist ausdrücklich in1884 belegt. FSP bis 100 bleibt aus Bandziel35415 didaktisch abgeleitet. Alle Faktoren im gewählten Ausschnitt liegen zwischen 1 und 10; Kernprodukte, abgeleitetes Produkt und relevante Zwischen-/Endergebnisse bis 100. Division, Nullfälle, andere Ableitungen und die vollständige flexible Strategienutzung bleiben offen. Aufgaben und Hilfsmittel werden nicht vorgeschlagen.

Alle46 bisherigen Karten unverändert. Eine teilweise geprüfte Inhaltszeile, ein neu geprüfter Strategiekontext und ein wiederverwendetes Hauptziel; kein vollständiger Abschluss. 47 Karten (36 stufenbandpassend, elf stufenübergreifend),141 Quellenlinks/139 Karten-Zielanker plus zwei Kontextquellen; weiterhin86 Auditzeilen. Neun Anschlussfragen und vier Entscheidungen ohne hinreichend belegten direkten Anschluss. Fortsetzung1887; Nachweise im Prüfpaket.

Daten-, Zahlenraum-, Bestandsschutz- und Browserprüfungen bestanden: alle47 Mathematikkarten und die aufklappbaren Hinweise/Quellen aller360 Karten. Alle70 zulässigen Zwei-Kernprodukte-Kombinationen erfüllen die Rechenidentität und bleiben einschließlich Zwischenprodukten bis100. Eigene Entwürfe erhalten, Aufgaben/Hilfsmittel leer. Testbrowser ohne Scrollanimation; Animation selbst nicht bewertet. App1.348 auf main veröffentlicht (Commit `bcfad76bdaf3cf23484eb6509d7911b05eceeca9`). Öffentliche HTML-Datei bytegleich zum geprüften Stand (SHA-256 `bf5268708abda9bff57fdf998ead669e95ad73cf1fc67222db1f76d704c360b8`); Live-Browserprüfung aller47 Mathematikkarten bestanden. [Pages-Lauf 42673685859](https://github.com/geafaellt/LernzielKompass/actions/runs/42673685859) meldet insgesamt `failure`, obwohl beide gelisteten Jobs `build` und `deploy` erfolgreich sind und das Veröffentlichungsprotokoll den Erfolg bestätigt. Ursache des Gesamtstatus ungeklärt; Wiederholung wurde von GitHub mit403 abgelehnt. Kein vollständig grüner Workflow behauptet. Details im [Prüfpaket MA-034](review_batch_034.json).


## MA-035 · Vom Quadratprodukt zum Nachbarprodukt · App 1.349 · 09.11.2026

MA-048 verbindet den in der GS-Bemerkung1887 gezeigten positiven Nachbarweg mit den multiplikativen Nachbaraufgaben in der FSP-Bemerkung35442 unter Kennen35439. Die GS-Nachbarzeile187080 wird als fachlich verbundenes Unterziel mitgeprüft. Auf FSP-Seite sind gleiche Ausgangsfaktoren eine didaktische Auswahl innerhalb der belegten Nachbarbeziehung: kein eigenständiger Quadratzahlenauftrag, keine Fachwortpflicht und kein behauptetes Auswendiglernen aller Quadratprodukte. FSP1/2-Belege zu additiven Nachbarn, Schrittzählen und Rechenquadraten sind hierfür nicht gleichzusetzen.

GS bis100 ausdrücklich in1884; FSP bis100 aus Bandziel35415 didaktisch abgeleitet. Gleiche positive Ausgangsfaktoren1 bis9, erster Faktor plus eins, zweiter Faktor unverändert. Ausgangsprodukt, Zuwachs und relevante Ergebnisse bleiben bis100; Ausgangsfaktor10 ausgeschlossen, weil das Nachbarprodukt110 entstünde. Andere Ausgangsprodukte, Richtungen und vollständige Strategiewahl bleiben offen. Aufgaben/Hilfsmittel werden nicht vorgeschlagen.

Alle47 bisherigen Karten unverändert. Zwei teilweise geprüfte Inhaltszeilen mit einer neuen Karte; wiederverwendete Kontextzeilen nicht erneut gezählt. 48 Karten (36 stufenbandpassend, zwölf stufenübergreifend),143 Quellenlinks/141 Karten-Zielanker plus zwei Kontextquellen; weiterhin86 Auditzeilen. Neun Anschlussfragen und vier Entscheidungen ohne hinreichend belegten direkten Anschluss. Fortsetzung187078/187079;187080 bereits teilweise geprüft. Nachweise im Prüfpaket.

Daten-, Zahlenraum-, Bestandsschutz- und Browserprüfungen bestanden: alle48 Mathematikkarten und Hinweise/Quellen aller361 Karten. Alle neun zulässigen Übergänge bleiben mit Zwischen- und Endergebnissen bis100; Ausgangsfaktor10 ausgeschlossen. Aufgaben/Hilfsmittel leer und eigene Entwürfe erhalten. Testbrowser ohne Scrollanimation; Animation selbst nicht bewertet. Nachprüfung der früheren Statusabweichung: GitHub-Lauf42674263970 nennt einen internen Serverfehler (Korrelationskennung im Prüfpaket); keine Behauptung, das Plattformproblem sei bereits behoben. App1.349 auf main veröffentlicht (Commit `0ad31b7367c5c9b32b40d8d98310663297860a80`). [Pages-Lauf 42687092388](https://github.com/geafaellt/LernzielKompass/actions/runs/42687092388) vollständig erfolgreich. Öffentliche HTML-Datei bytegleich zum geprüften Stand (SHA-256 `e44de74b2e3a617ccc7e0ea7da0b53521dc31b1a948a113225f6d675a43d0907`); Live-Browserprüfung aller48 Mathematikkarten bestanden. Die frühere Plattformabweichung ist für diesen neuen Lauf nicht aufgetreten. Details im [Prüfpaket MA-035](review_batch_035.json).


## MA-036 · Multiplikative Aufgabenfamilien · App 1.350 · 10.11.2026

MA-049 bündelt die drei GS-Zeilen187078/187079/187081: Tauschaufgaben, Umkehraufgaben und Aufgabenfamilien unter Kennen1881/Strategieziel1884. FSP3/4 belegt die Multiplikations-/Divisionsbeziehung in35441 und ausdrücklich Vierergruppen, Umkehraufgaben und Vertauschen in der Bemerkung35442 unter Kennen35439. FSP1/2-Kandidaten beziehen sich auf additive Beziehungen oder allgemeine Voraussetzungen und werden nicht gleichgesetzt.

GS bis100 ausdrücklich in1884; FSP bis100 didaktisch aus Bandziel35415. Der ausgewählte Ausschnitt beginnt bei einer bekannten Multiplikation mit zwei verschiedenen Faktoren zwischen2 und10. Produkt und sämtliche Divisionswerte sowie relevante Zwischen-/Endergebnisse bis100; Divisionen restfrei. Null-/Einsfälle, gleiche Faktoren, andere Ausgangspunkte und vollständige Strategiewahl bleiben offen. Die sachliche Frage zu Aufteilen/Resten wird durch formale Gleichungsbeziehungen nicht abgeschlossen. Aufgaben/Hilfsmittel bleiben Lehrkraftentscheidung.

Alle48 bisherigen Karten unverändert. Drei teilweise geprüfte Inhaltszeilen, eine gemeinsame neue Karte; Kontextzeilen nicht erneut gezählt. 49 Karten (36 stufenbandpassend, dreizehn stufenübergreifend),147 Quellenlinks/145 Karten-Zielanker plus zwei Kontextquellen; weiterhin86 Auditzeilen. Neun Anschlussfragen und vier Entscheidungen ohne hinreichend belegten direkten Anschluss. Fortsetzung187082/187083; Nachweise im Prüfpaket.

Daten-, Zahlenraum- und Bestandsschutzprüfungen bestanden. 72 geordnete Faktorkombinationen bilden36 verschiedene Familien; beide Divisionen restfrei, sämtliche Werte bis100. Hinweise/Quellen aller362 Karten im Browser geprüft. Erster Mathematiklauf brach beim Scrollen zu einem Übernahmebutton der unveränderten MA-028 ab; unveränderter vollständiger Wiederholungslauf aller49 Karten bestanden. Keine Assertions ausgelassen. Eigene Entwürfe erhalten, Aufgaben/Hilfsmittel leer. Testbrowser ohne Scrollanimation; Animation selbst nicht bewertet. App1.350 auf main veröffentlicht (Commit `c135ae433c9ef76713d9c8b5c340e04d7ea18a75`). [Pages-Lauf 42735574633](https://github.com/geafaellt/LernzielKompass/actions/runs/42735574633) erfolgreich. Öffentliche HTML-Datei bytegleich (SHA-256 `3dfca89645b3badac3b3439e5d4bb9276e78f05bd64394f55eb64b34aadb2768`). Gezielte öffentliche Prüfung von MA-049 in beiden GS-Jahrgängen bestanden, einschließlich Ziele/Zahlenraum/Output, Quellen, leerer Aufgaben-/Hilfsmittelfelder, erhaltener Entwürfe und ergänzender Fachwechsel-/Mobilprüfungen. **Keine vollständige öffentliche Browserfreigabe:** Drei Gesamtläufe brachen bei Scroll-/Klickaktionen mit Zeitlimit ab; auch ein zusätzlicher Test ohne programmgesteuerte Scrollanimation beseitigte das Problem nicht. Ursache nicht abschließend geklärt. Lokal ist der vollständige49-Karten-Wiederholungslauf bestanden. Details und begrenzter Live-Prüfumfang im [Prüfpaket MA-036](review_batch_036.json).


## MA-037 · Verdoppeln über gleiche Kernprodukte · App 1.351 · 10.11.2026

GS187082 wird teilweise auf bestehender MA-047 ergänzt: zweimal dasselbe Kernprodukt der2 oder5, zweiter Faktor1 bis10. Der FSP-Kernaufgabenbezug35442 unter Kennen35439 trägt diese didaktische Spezialisierung. Keine neue Karte und keine erneute Zählung von1885. MA-011 und MA-044 behalten ihren eigenen Operatoren-/Grundvorstellungskontext.

GS bis100 ausdrücklich in1884; FSP bis100 didaktisch aus35415. Ausgangsprodukt beim Verdoppeln höchstens50, Ergebnis bis100; alle Zwischenwerte im Rahmen. Der übrige bestehende Kernproduktweg bleibt erhalten. Halbieren als multiplikative Strategie ist als neue Anschlussfrage offen; der positive FSP-Halbierungsbeleg35437 wird weder verworfen noch ungeprüft als vollständiger Strategieanschluss eingesetzt. Keine Aufgaben/Hilfsmittel vorgeschlagen.

Eine weitere teilweise geprüfte Inhaltszeile,49 Karten (36 stufenbandpassend,13 stufenübergreifend),148 Quellenlinks/146 Zielanker plus zwei Kontextquellen,86 Auditzeilen. Alle übrigen48 Karten und neun bisherigen Anschlussfragen unverändert; nun zehn Fragen. Fortsetzung187083.

Daten-, Zahlenraum- und Bestandsschutzprüfungen bestanden. Alle20 ausgewählten Verdoppelkonfigurationen halten Ausgangsprodukt50 und Ergebnis100 ein. Vollständiger lokaler Mathematik-Browsertest aller49 Karten und Hinweise/Quellen aller362 Karten bestanden; eigene Entwürfe erhalten, Aufgaben/Hilfsmittel leer. Scrollanimation im Testbrowser deaktiviert, nicht bewertet. App1.351 auf main veröffentlicht (Commit `1b31ae0aada7e02dd34286f367f015ea82292e00`). [Pages-Lauf 42754103237](https://github.com/geafaellt/LernzielKompass/actions/runs/42754103237) erfolgreich. Öffentliche HTML-Datei bytegleich zum geprüften Stand (SHA-256 `38cdd5fb783345759b401a875a602264b033007361bc3f92468c2745052a90ac`). Gezielte öffentliche Prüfung der geänderten MA-047 in beiden GS-Jahrgängen bestanden: Quellen, Zahlenraum auf Karte/Zielen/Output, aktualisierte Ziel-/Kriterienübernahme, leere Aufgaben-/Hilfsmittelfelder und erhaltene Entwürfe; ergänzende Fachwechsel-/Mobilprüfungen bestanden. Vollständiger49-Karten-Lauf lokal bestanden, öffentlich in diesem Lauf nicht wiederholt. Frühere Live-Zeitlimits aus MA-036 bleiben dokumentiert und werden nicht rückwirkend als bestanden gewertet. Details im [Prüfpaket MA-037](review_batch_037.json).


## MA-038 · Audit ohne App-Änderung · 10.11.2026

[Prüfpaket038](review_batch_038.json) prüft gegensinniges und gleichsinniges Verändern187083 unter1884/Kennen1881 gegen beide FSP-Bänder. Der GS-Beleg zeigt das Halbieren eines Faktors und Verdoppeln des anderen bei gleichem Produkt. FSP-Mengenverdopplung, Kernaufgaben, Tausch-/Umkehr- und Nachbarbeziehungen sind fachlich verwandt; die abgestimmte Änderung beider Operanden ist damit nicht hinreichend belegt. Keine Ablehnung allein wegen kleinerer Zahlenräume und kein generelles Urteil gegen didaktische Anschlussfähigkeit.

MA-011, MA-044 und MA-047 bis MA-049 wurden abgegrenzt; alle49 Karten samt FSP-Geltungsbereichen, Feinzielen und Kriterien bleiben unverändert. Ein weiterer Unterpunkt einzeln entschieden, keine vollständige GS-Zieldeckung.86 inventarisierte Auditzeilen sind nicht86 abgeschlossene Prüfungen.148 Quellenverknüpfungen,146 kartengebundene Zielanker, zehn offene Anschlussfragen und nun fünf dokumentierte Zeilen ohne hinreichend belegten direkten Anschluss. Nächster Prüfpunkt187084; Halbierungsfrage187082 bleibt offen. App1.351 unverändert.

Bestanden: Deutsch-/Mathematikprüfung, Pages-Aufbereitung, FSP-Geltungsbereichsregression und Lerngegenstandsprüfung. Mathematikmodul und beide HTML-Dateien sind bytegleich mit App1.351; nur eine Auditzeile geändert. Keine neue Browserprüfung bei unveränderter App. MA-037 dokumentiert vollständige lokale und gezielte öffentliche Browserprüfung; ältere öffentliche Volltest-Zeitüberschreitungen werden nicht nachträglich als bestanden gewertet. Auf main veröffentlicht: `38e940c0b213a0e27301ff0259f85b1edef1ea86`. [Pages-Lauf42791680371](https://github.com/geafaellt/LernzielKompass/actions/runs/42791680371) erfolgreich. Tatsächlich ausgelieferte App bytegleich mit beiden lokalen HTML-Dateien, SHA-256 `38cdd5fb783345759b401a875a602264b033007361bc3f92468c2745052a90ac`. App1.351 unverändert.


## MA-039 · App1.352 · 10.11.2026

[Prüfpaket039](review_batch_039.json) ergänzt MA-050: zwei unterschiedliche Wege zu derselben Multiplikation erproben und ihre rechnerische Stimmigkeit beurteilen. Beleg: GS187084 unter Kennen1881; FSP35442 unter Kennen35439 mit Finden/Ausprobieren/Werten in der Bemerkung. Stufenübergreifend GS1/2 → FSP3/4; additive und allgemeine Strategiebezüge in FSP1/2 geprüft.

Beide Feinziele bis100 didaktisch eingegrenzt, einschließlich sämtlicher Zwischen- und Endwerte. GS187084 enthält keine eigene Obergrenze;1884 ist eine benachbarte Zielzeile. FSP-Rahmen aus Bandziel35415 abgeleitet. Positive Ausgangsfaktoren2 bis10 und zwei Wege sind didaktisch ausgewählt; konkrete Wege, Aufgaben und Hilfsmittel werden nicht vorgegeben. Keine vollständige GS-Zieldeckung; Division, freie Strategiewahl und umfassende Begründung/Bewertung bleiben offen.

50 Karten (36 stufenbandpassend,14 stufenübergreifend),149 Quellen/147 Zielanker plus zwei Kontextquellen;86 inventarisierte Auditzeilen, zehn Anschlussfragen und fünf dokumentierte Zeilen ohne hinreichenden direkten Anschluss. Alle49 vorhandenen Karten unverändert. Fortsetzung187086. Bestanden: alle Daten-/Geltungsbereichsprüfungen, vollständiger lokaler Browsertest aller50 Mathematikkarten und aufklappbare Hinweise/Quellen aller363 Karten. Anfangs fehlende Leerzeichen bei der Zahlenraumangabe korrigiert; endgültigen Stand erneut geprüft.49 bisherige Karten und alle übrigen App-Daten unverändert. App1.352 auf main veröffentlicht (4dae8deefe168bcd5c0ae0fcd59ebe646aaac718), [Pages-Lauf42792783323](https://github.com/geafaellt/LernzielKompass/actions/runs/42792783323) erfolgreich. Ausgelieferte App bytegleich, SHA-256 dbef8faa5cb159cc47f80857883b6576006deaa2e04476e3093e87a4976179da. Öffentliche MA-050-Prüfung in beiden GS-Jahrgängen bestanden: Quellen, Grenzen auf Karte/Zielen/Output, Ziel-/Kriterienübernahme, leere Aufgaben-/Hilfsmittelfelder und erhaltene Entwürfe; ergänzende Fachwechsel-, Neulade- und Mobilprüfungen bestanden. Vollständiger50-Karten-Test lokal; öffentlich gezielter Test der neuen Karte. Ältere öffentliche Volltest-Zeitüberschreitungen aus MA-036 werden nicht nachträglich als bestanden gewertet.


## MA-040 · Audit ohne App-Änderung · 10.11.2026

[Prüfpaket040](review_batch_040.json) dokumentiert für alle23 Begriffe aus187086 die FSP-Gegenbezüge. Wichtig ist der ausdrücklich positive Sprachbezug Versprachlichen der Rechenoperationen35441, ergänzt durch übergreifendes Fachwortverständnis35415. Recheninhalt, Zeichen, Verstehen und selbstständiges Verwenden werden getrennt. Die konkrete sprachliche Zuordnung bleibt offen; dies ist weder vollständige Zeilenprüfung mit Abschluss noch ein pauschaler Nichtanschluss. Singular-/Pluralformen wurden nicht als inhaltlicher Unterschied gewertet.

Keine neue Karte, keine Änderung an Feinzielen, Kriterien oder Zahlenraumgrenzen. Sprachziele ohne eigene Zahlengrenze erhalten keine erfundene Obergrenze; die übergreifenden Operationsrahmen20/100 begrenzen keinen Wortschatz. Alle50 Karten,149 Quellenverknüpfungen und147 kartengebundenen Zielanker unverändert. Nun elf Anschlussfragen, fünf dokumentierte Zeilen ohne hinreichenden direkten Anschluss; diese Liste wurde nicht erweitert.

Drei Zeilen187087–187089 nur für die Fortsetzung inventarisiert:89 Auditzeilen sind nicht89 abgeschlossene Prüfungen. Nächster fachlicher Prüfpunkt187088 unter Beherrschen187087, danach187089. App1.352 unverändert. Daten-/Geltungsbereichsprüfungen und Bestandsschutz bestanden. Eine veraltete Inventar-Kurznotiz aus MA-037 wurde berichtigt. Mathematikmodul und beide HTML-Dateien bleiben bytegleich mit App1.352; kein neuer Browsertest bei unveränderter App. Auf main veröffentlicht (2b5a84d27cebeca6c558157b71ce349664aa5695). [Pages-Lauf42800321751](https://github.com/geafaellt/LernzielKompass/actions/runs/42800321751) erfolgreich. Ausgelieferte App1.352 bytegleich mit dem geprüften Stand, SHA-256 dbef8faa5cb159cc47f80857883b6576006deaa2e04476e3093e87a4976179da.


## MA-041 · App1.353 · 10.11.2026

[Prüfpaket041](review_batch_041.json) ergänzt MA-051 für Malaufgaben mit einem Faktor2,5,10 und einem weiteren Faktor1 bis10 sowie die zugehörige Division durch2,5,10. GS187088 unter Beherrschen187087; FSP35443 unter Kennen35439, Kernaufgabenbezug als Bemerkung35442. FSP1/2-Grundaufgaben sind additiv; Schrittzählen allein ersetzt keinen Mal-/Teilgrundaufgabenauftrag. Stufenübergreifender Anschluss GS1/2 → FSP3/4.

Bis100 auf GS-Seite didaktisch gewählt, auf FSP-Seite aus Bandziel35415 abgeleitet. Beide Zielzeilen ohne eigene numerische Obergrenze. Sämtliche Zwischen- und Endwerte bleiben im Rahmen; keine Restdivision oder Null-/Negativfälle. Kein zusätzlicher automatisierter Gedächtnisabruf auf FSP-Seite. Bestehende50 Karten unverändert; neuer GS-Beherrschensauftrag wird nicht mit bisherigen Kennen-Karten gleichgesetzt. Kein vollständiger Abschluss der GS-Zeile oder des Hauptziels.

51 Karten (36 stufenbandpassend,15 stufenübergreifend),152 Quellenverknüpfungen/150 kartengebundene Zielanker plus zwei Kontextquellen;89 Inventarzeilen, elf Anschlussfragen und fünf dokumentierte Zeilen ohne hinreichenden direkten Anschluss. Fortsetzung187089; keine bisherige offene Frage geschlossen. Alle Daten-/Zahlenraumprüfungen bestanden;30 ausgewählte Kernfaktorkombinationen ergeben Produkte bis100 und restfreie Rückdivisionen. Vollständiger lokaler51-Karten-Browsertest und aufklappbare Hinweise/Quellen aller364 Karten bestanden. Alle50 bisherigen Karten, eigene Entwürfe und andere Fächer erhalten; Aufgaben-/Hilfsmittelfelder leer. App1.353 auf main veröffentlicht (eae5ca12475abf77b6779bd81df61f0f3acdf20b). [Pages-Lauf42839463389](https://github.com/geafaellt/LernzielKompass/actions/runs/42839463389) erfolgreich; die Bereitstellung benötigte rund fünfeinhalb Minuten. Ausgelieferte App bytegleich, SHA-256 3bf8f48be31038c6bbe17f77df67fc22e34266a6dbb424c5197dd9a3134658f0. Öffentliche Prüfung der neuen MA-051 in beiden GS-Jahrgängen bestanden: Quellen, Grenzen auf Karte/Zielen/Output, Ziel-/Kriterienübernahme, leere Aufgaben-/Hilfsmittelfelder und erhaltene Entwürfe; ergänzende Fachwechsel-, Neulade- und Mobilprüfungen bestanden. Vollständiger51-Karten-Test lokal, öffentlich gezielter Test der neuen Karte. Ältere öffentliche Volltest-Zeitüberschreitungen aus MA-036 werden nicht nachträglich als bestanden gewertet.


## MA-042 · App1.354 · 10.11.2026

[Prüfpaket042](review_batch_042.json) ergänzt187089 auf vorhandener MA-051: Eine bekannte Kernmultiplikation trägt die zugehörige Division durch2,5 oder10. GS-Beherrschen187087 und FSP-Kennen35439 bleiben getrennt. Beziehungsziel35441 und Umkehrzuordnung in der Bemerkung35443 stützen den ausgewählten Vernetzungsweg. FSP1/2-Kandidaten bleiben im additiven bzw. allgemeinen Strategiekontext. Kein neuer mathematischer Gegenstand und keine zusätzliche Karte.

Feinziele/Kriterien und Geltungsbereich benennen die Richtung ausdrücklich. Bestehende Faktorwahl und Grenze bis100 einschließlich Zwischen-/Endwerte bleiben bestehen; GS-Grenze didaktisch gewählt, FSP-Grenze aus Bandziel35415 abgeleitet. Weitere Strategien, Umkehrrichtung, vollständige Familien und freie Strategiewahl bleiben offen.187088 nicht erneut gezählt. Alle übrigen50 Karten unverändert.

51 Karten (36 stufenbandpassend,15 stufenübergreifend),153 Quellen/151 Zielanker plus zwei Kontextquellen;92 inventarisierte Zeilen, elf Anschlussfragen.1911/187090/187091 nur inventarisiert, nicht fachlich abgeschlossen. Fortsetzung187090. Daten-/Geltungsbereichsprüfungen und Bestandsschutz bestanden. Alle30 ausgewählten Umkehrverknüpfungen halten die bestehende Grenze100 ein. Vollständiger lokaler51-Karten-Browsertest und Hinweise/Quellen aller364 Karten bestanden; eigene Entwürfe erhalten, Aufgaben-/Hilfsmittelfelder leer. Änderungen auf main gesichert (36f5b012480946d013a0ea3d1c3cb222596fb858). [Pages-Lauf42841736581](https://github.com/geafaellt/LernzielKompass/actions/runs/42841736581) scheiterte beim Synchronisieren nach zehn Minuten; Aufbau erfolgreich. Wiederholung angenommen, am10.11.2026 um15:58UTC weiterhin queued. Öffentlich zuletzt App1.353, SHA-256 3bf8f48be31038c6bbe17f77df67fc22e34266a6dbb424c5197dd9a3134658f0. App1.354 und die öffentliche MA-051-Prüfung sind noch nicht bestätigt. Erster Fortsetzungsschritt: Veröffentlichung reparieren/prüfen und öffentliche Browserprüfung nachholen; erst danach187090. Details im Prüfpaket.


## MA-043 · App 1.355 · 10.11.2026

Die Veröffentlichung von App1.354 wurde über den erfolgreichen [Pages-Lauf42887376050](https://github.com/geafaellt/LernzielKompass/actions/runs/42887376050) nachgeprüft: Live-Datei bytegleich, gezielte öffentliche MA-051-Prüfung in beiden GS-Jahrgängen bestanden. Der vollständige51-Karten-Durchlauf wurde öffentlich nicht wiederholt. Frühere Fehlversuche bleiben im MA-042-Nachweis erhalten.

MA-052 verbindet das GS-Fragenstellen187090 mit dem FSP1/2-Erkennen einer Frage und wesentlicher Angaben37898. Gemeinsamer Gegenstand sind bekannte Teilanzahlen und die gesuchte Gesamtanzahl; beide Hauptoperatoren sind Einblick gewinnen. Erkennen ist ein Bemerkungsbeleg und wird nicht als selbstständiges Fragenstellen ausgegeben. FSP3/4-Fragenbezüge35505/35508 sind ausdrücklich positiv dokumentiert; der passende1/2-Vorläufer wird für diesen differenzierten Ausschnitt bevorzugt. MA-029 bleibt als anderer Gegenstand unter GS-Kennen unverändert.

FSP bis20 ist didaktisch aus dem Bandziel37739 abgeleitet; GS bis20 ebenfalls didaktisch gewählt, keine amtliche Zielzeilenobergrenze. Beide Teilanzahlen, gesuchte Summe und relevante Zwischen-/Endwerte sind begrenzt. Keine konkreten Aufgaben oder Hilfsmittel werden vorgegeben. Rest: andere Fragearten/Operationen, Spiele und unvollständige oder unrealistische Situationen sowie vollständige GS-Zieldeckung.52 Karten (37 passend,15 stufenübergreifend),155 Quellen,153 Zielanker;92 Inventurzeilen bleiben92, eine davon jetzt teilweise geprüft. Elf Anschlussfragen unverändert. Fortsetzung187091.

Daten-, Zahlenraum- und Bestandserhaltungsprüfungen bestanden. Alle52 Mathematikkarten lokal im Browser geprüft; ergänzende Quellen-/Hinweisprüfung über alle365 Karten bestanden. Zielübernahme, leere Aufgaben-/Hilfsmittelfelder, erhaltene Entwürfe und mobile Ansichten bestätigt. Veröffentlicht mit Commit8f30d947639d913de5d8b93ff6d2498d844cd85a und erfolgreichem [Pages-Lauf42913481303](https://github.com/geafaellt/LernzielKompass/actions/runs/42913481303). App1.355 ist live bytegleich zum geprüften Stand (SHA2568045760c036698512bb5c8e6fc6c08bb099c1a7b032d931c43277758ec8cfcf4). Gezielte öffentliche MA-052-Prüfung in beiden GS-Jahrgängen einschließlich Entwurfserhalt, Fachwechsel, Neuladen und mobiler Ansicht bestanden. Der erste Versuch brach beim Neuladen mit net::ERR_NETWORK_CHANGED ab; unveränderte vollständige Wiederholung erfolgreich. Kein vollständiger52-Karten-Livedurchlauf behauptet.


## MA-044 · App 1.356 · 11.11.2026

MA-053 ergänzt den stufenbandpassenden Skizzenausschnitt aus GS187091. FSP37908 nennt die Skizze in der Bemerkung zum Probieren verschiedener Lösungswege;37898 begründet den Bezug auf wesentliche Angaben und Rechenoperation. Beide Hauptoperatoren sind Einblick gewinnen. FSP3/4-Skizzieren35509 ist ein positiver weiterführender Kandidat, der passende1/2-Beleg wird bevorzugt. Die Darstellung muss Teile und Ganzes mathematisch verbinden, nicht nur die Situation illustrieren.

MA-029 bleibt unverändert: anderer Gegenstand Bildsituation → Gleichung unter GS-Kennen1857. MA-052 betrifft das Fragenstellen/-erkennen. Ihre Zeilen werden nicht erneut gezählt. Die neue Karte nimmt keine vollständige Deckung des Modellierens oder sämtlicher FSP-Lösungswege vorweg. Tabellen, Terme, Gleichungen, andere Operationen und funktionale Beziehungen bleiben offen.

GS bis20 ist didaktisch gewählt; FSP bis20 aus übergreifendem Bandziel37739 abgeleitet. Die Zielzeilen haben keine eigene Höchstzahl. Beide Teilanzahlen, Gesamtanzahl, dargestellte Werte sowie relevante Zwischen-/Endwerte bleiben bis20. Aufgaben, Zeichenstil und Hilfsmittel bleiben Lehrkraftentscheidung.53 Karten (38 passend,15 stufenübergreifend),156 Quellen und154 Zielanker.94 Inventurzeilen:187092/187093 neu, aber ungeprüft. Elf Anschlussfragen erhalten. Fortsetzung187092.

Daten-, Zahlenraum- und Bestandserhaltungsprüfungen bestanden. Alle53 Mathematikkarten mit unveränderten Prüfaussagen in sieben getrennten Browsergruppen erfolgreich geprüft; außerdem gezielte MA-053-Prüfung und Hinweis-/Quellenprüfung aller366 Karten bestanden. Drei lange Gesamtdurchläufe brachen an unterschiedlichen vorhandenen Karten mit Zeitlimits ab; deren Ursache ist nicht abschließend geklärt. Kein erfolgreicher ununterbrochener Gesamtdurchlauf behauptet. Die frischen Browsersitzungen prüfen dieselben Karten, Zielübernahme, Grenzen, Quellen, Entwurfserhalt, Fachwechsel, Neuladen und mobile Ansicht. Veröffentlicht mit Commit c4df5f25b2d22bc5c967fa015fe2fb827337ca42 und erfolgreichem [Pages-Lauf42979881815](https://github.com/geafaellt/LernzielKompass/actions/runs/42979881815). App1.356 ist live bytegleich zum geprüften Stand (SHA2569f4a18967b1fad8f6006d95efdc6aac77375ca7c883db0de9d931f02b9b427e4). Die gezielte öffentliche Prüfung von MA-053 in GS1 und2 einschließlich Ziel-/Gegenstandsübernahme, Grenzen, Entwurfserhalt, Fachwechsel, Neuladen und mobiler Ansicht ist bestanden. Kein vollständiger53-Karten-Livedurchlauf behauptet.


## MA-045 · App 1.357 · 11.11.2026

MA-054 verbindet GS187092 mit dem selbstständigen Sachaufgabenbilden aus der FSP3/4-Bemerkung35505 unter Einblick gewinnen35504. Beide Hauptoperatoren sind Einblick gewinnen. Die Karte begrenzt den Anschluss auf eine vorgegebene Addition zweier positiver ganzer Teilanzahlen und eine Gesamtanzahlfrage im Naturkontext des FSP-Lernbereichs3. Diese konkrete Richtung und Auswahl sind didaktisch. FSP1/2-Rechengeschichten, Umformulieren und das Erschließen vorhandener Sachaufgaben sind positive Vorläufer, belegen aber nicht hinreichend die umgekehrte Erzeugungsrichtung. Der zusätzliche Selbstbildungsbeleg35586 liegt im Wahlbereich Tierwelt und wird nicht zum allgemeinen Pflichtziel umgedeutet.

MA-029,MA-052 undMA-053 bleiben unverändert: andere Übersetzungsrichtungen bzw. Gegenstände. Kein erneutes Zählen ihrer Zeilen. GS bis100 ist didaktisch gewählt; FSP bis100 aus Bandziel35415 abgeleitet. Keine eigene Obergrenze der ausgewählten Zielzeilen. Alle Anzahlen, Summe und relevante Zwischen-/Endwerte sind begrenzt. Es werden keine fertigen Sachaufgaben oder Hilfsmittel in die Planung eingefügt. Andere Operationen, mehrschrittige Aufgaben, Nullfälle, weitere Kontexte und vollständige Zieldeckung bleiben offen.

54 Karten (38 passend,16 stufenübergreifend),159 Quellen und157 Zielanker;94 Inventurzeilen bleiben94. Elf Anschlussfragen erhalten. Fortsetzung187093. Daten-, Zahlenraum- und Bestandserhaltungsprüfungen bestanden. Alle54 Mathematikkarten in sieben frischen Browsergruppen mit unveränderten Prüfaussagen erfolgreich geprüft, alle367 Karten in der Quellen-/Hinweisprüfung bestätigt. Alle Gruppen bestanden im ersten Versuch. Wegen der in MA-044 dokumentierten Zeitlimits langer Sitzungen wurde kein ununterbrochener Gesamtdurchlauf behauptet. Zielübernahme, sichtbare FSP-Grenzen, leere Aufgaben-/Hilfsmittelfelder, erhaltene Entwürfe, Fachwechsel, Neuladen und mobile Ansicht bestätigt. Auf main gesichert mit Commit f02815eefb0c7b5e038a8dbde7eb296926aeae25. Zunächst war kein neuer Pages-Lauf beobachtbar und live noch1.356; diese Zwischenbeobachtung bleibt im Prüfpaket erhalten. Inzwischen veröffentlichte der nachfolgende Nachweiscommit e5ddd6f488e5af6567c3eb694f2739f4a4b3b47c dieselben App-Dateien erfolgreich über [Pages-Lauf42981483143](https://github.com/geafaellt/LernzielKompass/actions/runs/42981483143). App1.357 ist live bytegleich zum geprüften Stand (SHA256880a43905f14fcce845b791a1bf1b90026198a74558c89e35d26b263ee282930). Gezielte öffentliche MA-054-Prüfung in beiden GS-Jahrgängen einschließlich Ziel-/Gegenstandsübernahme, Grenzen, Entwurfserhalt, Fachwechsel, Neuladen und mobiler Ansicht bestanden. Kein vollständiger54-Karten-Livedurchlauf behauptet.


## MA-046 · App 1.358 · 11.11.2026

MA-055 begrenzt GS187093 auf das sprachliche Darstellen eines geometrischen Probierwegs in einem Knobelspiel. FSP1/2:38022 nennt Probieren und Probehandeln unter Einblick gewinnen38021; der geometrische Bezug stammt aus der Bemerkung. Sprachbegleitung und unterstütztes Erklären sind eine didaktische Konkretisierung des übergreifenden Sprachziels37739. Kein Beschreibungsoperator wird der Unterzielzeile zugeschrieben. Der Anschluss gilt nur bei gewähltem FSP-Wahlbereich4 Zahlenzauberei; dies steht auf Karte, bei den Zielen und im Planungsoutput. Der positive FSP3/4-Beschreibungsbeleg35580 bleibt als weiterführender Kandidat dokumentiert.

Der Ausschnitt ist nichtnumerisch. Weder eine Höchstzahl von Teilen noch ein Zahlenraum20 wird erfunden; Rechnen und Messen gehören nicht zu den hinterlegten Feinzielen. Allgemeine Muster, arithmetische bzw. zufallsabhängige Strategien und Gewinnstrategien bleiben offen. Bestehende54 Karten unverändert.55 Karten (39 passend,16 stufenübergreifend),162 Quellen,160 Zielanker.

Elf Geldblockzeilen wurden ausschließlich für die Fortsetzung inventarisiert:105 Inventurzeilen insgesamt, keine zusätzliche fachliche Prüfung dieser elf Zeilen. Vorhandene MA-003-Bezüge an1913/1915 bleiben erhalten; ihre erneute Einzelprüfung samt Restumfang und Zahlenraumgrenze folgt als Nächstes. Elf Anschlussfragen unverändert. Daten-, Geltungsbereichs- und Bestandserhaltungsprüfungen bestanden. Alle55 Mathematikkarten in sieben frischen Browsergruppen mit unveränderten Prüfaussagen erfolgreich geprüft, alle368 Karten in der Quellen-/Hinweisprüfung bestätigt. Alle Gruppen bestanden im ersten Versuch. Kein ununterbrochener Gesamtdurchlauf behauptet; die in MA-044 dokumentierten Langzeitlimits werden durch getrennte Sitzungen berücksichtigt. Zielübernahme, Wahlbereichshinweis, leere Aufgaben-/Hilfsmittelfelder, Entwurfserhalt, Fachwechsel, Neuladen und mobile Ansicht bestätigt. Veröffentlicht mit Commit671b58fd0c33ff20713cfb65a81759faa239785e und erfolgreichem [Pages-Lauf42996907715](https://github.com/geafaellt/LernzielKompass/actions/runs/42996907715). App1.358 ist live bytegleich zum geprüften Stand (SHA25674f01a7997b4317f8b2a2a414a9d9dde4e12b2b47a9f6fbe0f6bc30638307603). Gezielte öffentliche MA-055-Prüfung in beiden GS-Jahrgängen mit Wahlbereichshinweis, Geltungsbereich, Ziel-/Gegenstandsübernahme, erhaltenen Entwürfen, Fachwechsel, Neuladen und mobiler Ansicht bestanden. Kein vollständiger55-Karten-Livedurchlauf behauptet.


## MA-047 · App 1.359 · 11.11.2026

Die vorhandene MA-003 wurde für1913/1915 gegen beide FSP-Bänder erneut geprüft. FSP1/2 nennt Vergleich und Ordnung ausdrücklich in37926, Euro/Cent in37921 unter Einblick gewinnen37913. Der stufenpassende Anschluss bleibt erhalten. FSP3/4 liefert weiterführende Geldbezüge35491–35495 sowie Preisvergleiche im Wahlbereich1; sie sind keine Voraussetzung für den bereits belegten engen Anschluss. Keine neue Karte und keine doppelte Erstzuordnung.

Feinziele und Kriterien benennen nun auch Ordnen, Gleichheit und Einheitenerhalt. Bis20 Euro oder20 Cent bleibt didaktisch aus Zahlaufbau37739 und der Bemerkung „Zahlenraum beachten“37926 abgeleitet. Die Zielzeilen selbst nennen keine Obergrenze. Alle Beträge und relevanten Zwischen-/Endwerte halten den gewählten Rahmen ein; keine gemischten Einheiten, Umrechnungen oder Dezimalbeträge. Auch das GS-Feinziel wählt einen engen Rahmen bis20, ohne dies als amtliche GS-Höchstgrenze auszugeben. Erfassen/Darstellen in weiteren Formen und weitere Geldinhalte bleiben offen. Fortsetzung1916, danach1917/1918.

55 Karten (39 passend,16 stufenübergreifend),162 Quellen,160 Zielanker,105 Inventurzeilen und elf Anschlussfragen unverändert. Daten-, Geltungsbereichs- und Bestandserhaltungsprüfungen bestanden. Alle55 Mathematikkarten in sieben frischen Browsergruppen mit unveränderten Prüfaussagen erfolgreich geprüft; alle368 Karten in der Quellen-/Hinweisprüfung bestätigt. Alle Gruppen bestanden im ersten Versuch. Kein ununterbrochener55-Karten-Durchlauf behauptet; die in MA-044 dokumentierten Langzeitlimits werden durch getrennte Sitzungen berücksichtigt. Übernahme der Ziele, sichtbare FSP-Grenzen, leere Aufgaben-/Hilfsmittelfelder, Entwurfserhalt, Fachwechsel, Neuladen und mobile Ansicht bestätigt. Veröffentlichung und öffentliche Prüfung noch ausstehend.
