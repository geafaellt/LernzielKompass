# Mathematik-Abgleich · MA-001

Erster Prüfstand vom 06.11.2026. Grundlage sind der [sächsische Fachlehrplan Mathematik für die Grundschule, Fassung 2026](https://www.schulportal.sachsen.de/lplandb/lehrplan/912), und der [sächsische Fachlehrplan Mathematik für den Förderschwerpunkt Lernen, Fassung 2019](https://www.schulportal.sachsen.de/lplandb/lehrplan/139). Verglichen werden GS 1/2, 3 und 4 mit den gebündelten FSP-Stufenbändern 1/2 und 3/4.

Sieben Karten dokumentieren begrenzte Anschlüsse. Sechs liegen im passenden Stufenband. MA-002 ist stufenübergreifend. Für Spiegelachsen wurde in FSP 1/2 das verwandte Ziel zu Mustern und Ornamenten geprüft. Der konkrete Spiegelachsenbezug ist in FSP 3/4 belegt.

| Karten | Geprüfte Ausschnitte |
| --- | --- |
| MA-001 und MA-002 | Relative Lage von Objekten und Erkennen einer Spiegelachse |
| MA-003 und MA-004 | Geldbeträge innerhalb einer Einheit und Vergleich von Längen in Metern |
| MA-005 und MA-007 | Schriftliche Addition zweier Summanden in GS 3 und als Verfahrensanschluss in GS 4 |
| MA-006 | Minutengenaues Ablesen von Uhrzeiten in GS 3 und FSP 3/4 |

Die Operatoren stammen aus den übergeordneten Zielzeilen der jeweiligen Lehrpläne. Unterziele grenzen den Anschluss ein. Hinweise aus der Bemerkungsspalte bleiben Kontext. Feinziele und Kriterien sind didaktische Konkretisierungen. Lernhandlungen, Aufgaben und Hilfsmittel legt die Lehrkraft fest.

[Prüfstand und Zeilenanker](review_progress.json) enthält die ausgewählten amtlichen Anker mit Bereich, Hierarchie und Operator. [Die Karten](mathematik_module.json) enthalten die jeweilige fachliche Grenze, Quellenlinks und die getrennten Ziele. Alle zwölf GS-Lernbereiche sind in der App auswählbar. Bereiche ohne Karte und die restlichen Ausschnitte innerhalb der Bereiche bleiben offen. Eine vollständige Einzelzeilenprüfung und eine Rückwärtsprüfung FSP → GS stehen aus.

Fortsetzung bei [GS 1/2, Zahldarstellungen bis 100](https://www.schulportal.sachsen.de/lplandb/lehrplan/912#page912_1833). Die Zahlenräume und die Anforderungen an Darstellungswechsel sind getrennt für beide FSP-Stufenbänder zu prüfen.

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
