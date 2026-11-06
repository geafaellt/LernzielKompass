# Mathematik-Abgleich · MA-002

Erster Prüfstand vom 06.11.2026. Grundlage sind der [sächsische Fachlehrplan Mathematik für die Grundschule, Fassung 2026](https://www.schulportal.sachsen.de/lplandb/lehrplan/912), und der [sächsische Fachlehrplan Mathematik für den Förderschwerpunkt Lernen, Fassung 2019](https://www.schulportal.sachsen.de/lplandb/lehrplan/139). Verglichen werden GS 1/2, 3 und 4 mit den gebündelten FSP-Stufenbändern 1/2 und 3/4.

Elf Karten dokumentieren begrenzte Anschlüsse. Neun liegen im passenden Stufenband. MA-002 und MA-011 sind stufenübergreifend. Für Spiegelachsen wurde in FSP 1/2 das verwandte Ziel zu Mustern und Ornamenten geprüft. Der konkrete Spiegelachsenbezug ist in FSP 3/4 belegt.

| Karten | Geprüfte Ausschnitte |
| --- | --- |
| MA-001 und MA-002 | Relative Lage von Objekten und Erkennen einer Spiegelachse |
| MA-003 und MA-004 | Geldbeträge innerhalb einer Einheit und Vergleich von Längen in Metern |
| MA-005 und MA-007 | Schriftliche Addition zweier Summanden in GS 3 und als Verfahrensanschluss in GS 4 |
| MA-006 | Minutengenaues Ablesen von Uhrzeiten in GS 3 und FSP 3/4 |

Die Operatoren stammen aus den übergeordneten Zielzeilen der jeweiligen Lehrpläne. Unterziele grenzen den Anschluss ein. Hinweise aus der Bemerkungsspalte bleiben Kontext. Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlungen, Aufgaben und Hilfsmittel legt die Lehrkraft fest.

[Prüfstand und Zeilenanker](review_progress.json) enthält die ausgewählten amtlichen Anker mit Bereich, Hierarchie und Operator. [Die Karten](mathematik_module.json) enthalten die jeweilige fachliche Grenze, Quellenlinks und die getrennten Ziele. Alle zwölf GS-Lernbereiche sind in der App auswählbar. Bereiche ohne Karte und die restlichen Ausschnitte innerhalb der Bereiche bleiben offen. Eine vollständige Einzelzeilenprüfung und eine Rückwärtsprüfung FSP → GS stehen aus.

Fortsetzung bei Lesen/Sprechen (page912_187038) und Schreiben (page912_187039) von Zahlen und Zahlwörtern. Die Einzelprüfung des Zielblocks Zahldarstellungen bis 100 bleibt offen. [Zeilenprüfung des begonnenen Blocks](row_audit.csv) und [Prüfpaket MA-002](review_batch_002.json) unterscheiden geprüfte Ausschnitte, Kontextziele und offene Zeilen.

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
