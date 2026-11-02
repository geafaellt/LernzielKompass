# Deutsch-Abgleich · App 1.256

Arbeitsstand vom 30.10.2026. Amtliche Grundlage: GS Deutsch 2004/2009/2019/2025/2026 (Lehrplan 908), FSP Lernen Deutsch-Heimatkunde/Sachunterricht 2005/2010/2019 (Lehrplan 146), Sächsischer Rechtschreibrahmen 2025. Der FSP-Deutschplan für die Sekundarstufe wird nicht verwendet.

122 begrenzte Anschlussvorschläge; 117 GS-Zielblöcke mit Erstentscheidung, darunter 23 ohne hinreichend belegten direkten Anschluss. GS umfasst 488 inventarisierte Zeilen, FSP 451. Nach der zweiten Quellenprüfung bleiben 241 GS-Unterzielzeilen außerhalb der ausdrücklich ausgewählten Karten. Das ist weder eine Behauptung vollständiger Lehrplanabdeckung noch eine fachliche Freigabe sämtlicher Unterziele. Feinziele, Aufgaben und Kriterien sind didaktische Vorschläge, nicht amtlicher Wortlaut.

Die zweite Quellenprüfung präzisiert Textsorten, Kinderbuchbezug, Leseflüssigkeit, Textbelege, Schreibplanung und den thematischen FSP-Rahmen. DE-106 und DE-107 sind wegen unzureichenden direkten GS3/4-Satzartenbezugs zurückgezogen; ihre IDs werden nicht neu vergeben. 15 weitere enge Anschlüsse sind DE-110–124. Stufenübergreifende Zuordnungen sowie notwendige FSP-Wahlbereiche werden angezeigt. Bemerkungen sind Beispiele und keine eigenständigen gleichwertigen Zieloperatoren.

## Reproduktion

1. `python curriculum/deutsch/extract_inventory.py` (benötigt BeautifulSoup4; arbeitet aus den gespeicherten amtlichen HTML-Quellen).
2. `python curriculum/deutsch/build_deutsch.py`
3. `python scripts/update-deutsch.py`
4. `python scripts/check-deutsch.py`

`id_registry.json` bewahrt Karten-IDs. `additional_topics.py` und `review_corrections.py` enthalten die zweite Prüfung. `row_audit.csv` zeigt pro GS-Zeile die ausdrückliche Kartenreferenz beziehungsweise den offenen Restumfang; fehlende Referenz bedeutet nicht automatisch fehlende curriculare Anschlussfähigkeit.

## Validierung

Syntax aller eingebetteten JavaScript-Blöcke, Karten-IDs, Ziel-/Quellenreferenzen, Klassenstufen, Operatoren und Hauptzielanker geprüft. Sachunterricht-Nutzdaten bleiben bytegleich zum Ausgangscommit c3f403d51fa2311684580e0981dcb0f56adf89b2.

Browser: erste 109 Karten in allen Jahrgängen/Bereichen geladen, Zielfelder und Bewertung kontrolliert. Nach Korrekturen neue Karte DE-110 und aktualisierte Bereichsauswahl geprüft. Fachwechsel erhält getrennte Entwürfe. Planvorschau mit Bewertungszeilen wurde geprüft. PDF-Download konnte im Testbrowser nicht bestätigt werden; es wurde kein erfolgreicher PDF-Export behauptet.

## Einzelprüfung DE-UZ-001 · 30.10.2026

Vier bisher offene Unterzielzeilen geprüft: page908_186277, 186279, 186286, 186298 (jeweils mit Präfix page908_). Jeweils kein hinreichend belegter direkter Anschluss; Begründungen, Kandidaten beider FSP-Bänder und Unsicherheiten in `review_batch_001.json`. Keine Kartenänderung. 241 Unterzielzeilen bleiben ohne Kartenabdeckung, davon 237 noch ohne Einzelprüfung. Bereits zugeordnete Unterziele sind anschließend zu prüfen. Fortsetzung: page908_186275 (Informieren), danach Erklären und Wortschatz. App 1.256 bleibt unverändert. Der Onlineabruf der amtlichen Quellen war in diesem Lauf nicht erfolgreich; Entscheidungen beruhen auf den gespeicherten Fassungen.

## Einzelprüfung DE-UZ-002 · App 1.257 · 30.10.2026

Fünf Unterzielzeilen geprüft: Informieren (186275), Erklären (186276), Verwenden des Wortschatzes (186278), Entwickeln einer Gesprächskultur (186292), Entwickeln gemeinsamer Gesprächsregeln (186294), jeweils page908_. Fünf begrenzte Karten DE-125–129 ergänzt. DE-129 ist stufenübergreifend GS1/2 → FSP3/4. Ziele, Unterziele und Bemerkungen bleiben getrennt; konkrete Feinziele/Kriterien sind didaktische Vorschläge. Alle bisherigen Karten und Sachunterricht unverändert.

127 Karten; 236 Unterzielzeilen ohne Kartenabdeckung, davon 232 noch ohne Einzelprüfung. Vier begründete Nichtanschlüsse aus DE-UZ-001 bleiben dokumentiert. Fortsetzung bei page908_186301 (Vorbereiten des Zuhörens). `review_progress.json` enthält den aktuellen Fortsetzungspunkt, `review_batch_002.json` die Einzelbelege. Die amtlichen Seiten GS 2026 und FSP 2019 waren diesmal online abrufbar. Reproduktion: Batch 002 wird durch build_deutsch.py automatisch eingebunden; row_audit.csv enthält den separaten manuellen Einzelprüfstand und darf nicht durch eine reine Kartenliste ersetzt werden.

## Einzelprüfung DE-UZ-003 · App 1.258 · 30.10.2026

Acht offene GS1/2-Zeilen zum Zuhören geprüft (186301, 186302, 186305, 186306, 186308, 186309, 186310, 186311; Präfix page908_). Zwei begrenzte Zuordnungen ergänzen DE-015; DE-130 ergänzt Tonfall/Lautstärke mit FSP-Entwicklungsziel. Fünf begründete Nichtanschlüsse: Vorbereitung, Hörbedingungen, Strategieerprobung, nonverbale Beobachtung, Verstehen/Nicht-Verstehen ausdrücken. Einzelfälle mit Kandidaten beider FSP-Bänder, Grenzen und Kriterien in review_batch_003.json.

128 Karten; 233 Unterzielzeilen ohne Karte, davon 224 noch ohne Einzelprüfung und 9 dokumentierte Nichtanschlüsse. Insgesamt 17 bisher offene Zeilen geprüft. Nächster Schritt: page908_186319 (visuell). Bereits zugeordnete Unterziele stehen später noch zur systematischen Prüfung an. Reproduktion integriert batch_003_topics.py automatisch. Vorhandene Karten außer DE-015 unverändert, Sachunterricht bytegleich. Quellenfassungen online bestätigt; keine erneute PDF-Prüfung.

## Einzelprüfung DE-UZ-004 · App 1.259 · 30.10.2026

Sechs offene GS1/2-Schreibzeilen geprüft: 186319, 186321, 186322, 186323, 186324, 186329 (Präfix page908_). DE-115 um visuelle Wahrnehmung, DE-018 um die unterstützende Schreibhaltung präzisiert. DE-131: Buchstaben ertasten, ausdrücklich nur bei Wahl des FSP-Wahlbereichs 1. Drei begründete Nichtanschlüsse zu kinästhetischer Schreibwahrnehmung, Schreibgeräte-Erprobung und Schreibreflexion. Die genauen Abgrenzungen und Kriterien stehen in review_batch_004.json.

129 Karten; 230 Unterzielzeilen ohne Karte, davon 218 ohne Einzelprüfung und 12 begründete Nichtanschlüsse. Insgesamt 23 zuvor offene Zeilen geprüft. Fortsetzung: page908_186332 (Selbstlaute). Reproduktion bindet batch_004_topics.py automatisch ein. Alle anderen Karten und Sachunterricht unverändert. Daten-/Syntaxprüfungen bestanden; kein neuer Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-005 · App 1.260 · 31.10.2026

Zwei offene GS1/2-Unterzielzeilen geprüft: page908_186332 (Selbstlaute) und page908_186333 (Mitlaute). Beide eng an DE-117 zugeordnet. Konkrete FSP1/2-Buchstabenanker ergänzt; Umlaute und weitere Lautgruppen nicht pauschal abgedeckt. Differenzierungsbemerkungen bleiben von verbindlichen Zielinhalten getrennt. Die verwandte Lesekarte DE-118 erhält dieselben Quellenpräzisierungen und Grenzen; sie zählt nicht als zusätzliche Einzelprüfung.

129 Karten unverändert in ihrer Anzahl; 228 Zeilen ohne Karte, davon 216 ohne Einzelprüfung und 12 dokumentierte Nichtanschlüsse. Insgesamt 25 zuvor offene Zeilen geprüft. Fortsetzung: page908_186334 (Wortebene). Einzelbelege in review_batch_005.json, Reproduktion über batch_005_review.py. Alle anderen Karten und Sachunterricht unverändert; Daten- und Syntaxprüfungen bestanden.

## Einzelprüfung DE-UZ-006 · App 1.261 · 31.10.2026

Fünf offene Zeilen geprüft: page908_186334–186338. Wortebene ist eine strukturierende Unterzielzeile und erhält keinen eigenen Operator. DE-132/133 verbinden eng Doppelkonsonanten bzw. ie-Schreibung mit FSP3/4-Einblick; GS1/2 → FSP3/4 ausdrücklich markiert. Keine vollständige Silbenstrukturabdeckung. Wortstammkonstanz und produktive Wortbildung bleiben begründete Nichtanschlüsse.

131 Karten; 225 Zeilen ohne Karte, davon 211 ohne Einzelprüfung und 14 begründete Nichtanschlüsse. Insgesamt 30 zuvor offene Zeilen geprüft. Nächste Zeile: page908_186340 (Satzebene). Einzelbelege: review_batch_006.json. Reproduktion bindet batch_006_topics.py ein. Alte 129 Karten und Sachunterricht unverändert; Daten-/Syntaxprüfung bestanden.

## Einzelprüfung DE-UZ-007 · App 1.262 · 31.10.2026

Vier offene Zeilen geprüft: page908_186340, 186355, 186357, 186359. Satzebene nur für bestehende konkrete Ausschnitte DE-022/023 zugeordnet. Aufbau/Suchhilfen über alphabetische Grundordnung und erarbeitete Suchfolge in DE-039 eingegrenzt; Fehleraufmerksamkeit bleibt begründeter Nichtanschluss. Keine neuen Karten.

131 Karten; 222 Zeilen ohne Karte, davon 207 ohne Einzelprüfung und 15 dokumentierte Nichtanschlüsse. Insgesamt 34 zuvor offene Zeilen geprüft. Fortsetzung: page908_186361 (Entwickeln von Schreibfreude und -motivation). Einzelbelege in review_batch_007.json; Reproduktion über batch_007_review.py. Alle weiteren Karten und Sachunterricht unverändert; Daten-/Syntaxprüfungen bestanden.

## Einzelprüfung DE-UZ-008 · App 1.263 · 31.10.2026

Vier offene Zeilen geprüft: page908_186361, 186364, 186367, 186368. DE-134 ergänzt eigene kurze Schreibideen/persönliche Notizen, DE-135 einfache Sachnotizen. Schreibfreude hat einen übergeordneten FSP-Bezug, aber keinen hinreichend genauen direkten Tabellenanschluss; Motivation wird nicht aus dem Produkt abgeleitet oder benotet.

133 Karten; 219 Zeilen ohne Karte, davon 203 ohne Einzelprüfung und 16 begründete Nichtanschlüsse. Insgesamt 38 zuvor offene Zeilen geprüft. Fortsetzung: page908_186371 (Erkennen von Schreibanlässen). Einzelbelege review_batch_008.json; Reproduktion batch_008_topics.py. Alte 131 Karten und Sachunterricht unverändert; Daten-/Syntaxprüfungen bestanden.

## Einzelprüfung DE-UZ-009 · App 1.264 · 31.10.2026

Sechs zuvor offene Zeilen geprüft: page908_186371, 186383, 186384, 186385, 186390, 186392. DE-136 ergänzt den Schreibanlass Einladung; DE-137 die kurze eigene Erlebnis-Mitteilung; DE-138 die schriftliche Gebäudebeschreibung einer erkundeten regionalen historischen Anlage, nur im FSP-Wahlbereich 3. Drei Nichtanschlüsse mit Unsicherheit dokumentiert: formale Textgestaltung, kriteriengeleitete Überarbeitung und Rückmeldungsnutzung. Schriftgröße/Schriftart als Differenzierung belegt keine eigenständige Gestaltungshandlung.

136 Karten; 216 Unterzielzeilen ohne Karte, davon 197 ohne Einzelprüfung und 19 dokumentierte Nichtanschlüsse. Insgesamt 44 zuvor offene Zeilen geprüft. Fortsetzung: page908_186402 (Entwickeln einer differenzierten Wahrnehmungsfähigkeit). Bereits zugeordnete Unterziele bleiben anschließend systematisch zu prüfen. Einzelbelege in review_batch_009.json; Reproduktion über batch_009_topics.py.

Daten-/Syntaxprüfung bestanden: alle bisherigen 133 Karten unverändert, IDs erhalten, Sachunterricht bytegleich. Kein neuer Browser- oder PDF-Test.

## Verbindliche Planungsregel · App 1.265

Auf Wunsch der Lehrkraft vom 31.10.2026 werden Lernhandlung/Aufgabe und Hilfsmittel niemals aus Anschlusskarten vorgeschlagen oder übernommen. Diese Entscheidungen trifft ausschließlich die Lehrkraft, analog zum Sachunterricht. Der Feinziel-Übernahmebutton ändert nur Feinziel und Erfolgskriterium. Eigene Eingaben und gespeicherte Planungen bleiben erhalten. Die veröffentlichten Deutsch-Karten enthalten keine task_suggestions oder aid_suggestions; der Generator entfernt diese Felder nach allen fachlichen Korrekturen. Diese Regel gilt auch für alle künftigen Prüfpakete. Der fachliche Einzelprüfstand und Fortsetzungspunkt aus DE-UZ-009 bleiben unverändert.

## Einzelprüfung DE-UZ-010 · App 1.266 · 31.10.2026

Sechs Wahrnehmungszeilen 186402–186407 (page908_) geprüft: zwei zuvor offene, vier bereits zugeordnete Zeilen als notwendige Gegenprüfung derselben Karte. DE-116 erhält den Zwischenanker Entwickeln und getrennte Fortschrittskriterien; rhythmisch/melodisch ausdrücklich nur begrenzt abgedeckt. DE-139 ergänzt taktiles Buchstabenerfassen, ausschließlich im FSP-Wahlbereich 1 und mit Sprachbezug bei der Umwelterkundung.

137 Karten; 214 Unterzielzeilen ohne Karte, davon 195 ohne Einzelprüfung und 19 dokumentierte Nichtanschlüsse. 46 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft; diese Zähler bleiben getrennt. Fortsetzung: page908_186411 (Silben). Audit review_batch_010.json; Reproduktion batch_010_topics.py. Aufgaben/Hilfsmittel werden weiterhin nicht als Vorschläge veröffentlicht.

Validierung: Daten-/Syntaxprüfung bestanden, bisherige Karten außer DE-116 unverändert, IDs erhalten, Sachunterricht bytegleich. Kein neuer Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-011 · App 1.267 · 31.10.2026

Fünf offene Zeilen geprüft: page908_186411, 186413, 186415, 186416, 186417. DE-051 um Silbenlesen ergänzt; DE-055 um Satzgrenzen und angebahnte Satzmelodie eingegrenzt. Automatisiertes Funktionswortlesen und gezielte Wortgrenzenstrategie bleiben begründete Nichtanschlüsse. Keine neuen Karten.

137 Karten; 211 Unterzielzeilen ohne Karte, davon 190 ohne Einzelprüfung und 21 dokumentierte Nichtanschlüsse. 51 zuvor offene und weiterhin 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186421 (still, leise und laut). Einzelbelege review_batch_011.json; Reproduktion batch_011_review.py. Aufgaben und Hilfsmittel bleiben ausschließlich Entscheidung der Lehrkraft.

Validierung: Daten-/Syntaxprüfungen bestanden; nur DE-051/055 geändert; IDs erhalten, Sachunterricht bytegleich. Kein neuer Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-012 · App 1.268 · 31.10.2026

Vier offene Zeilen page908_186421–186424 geprüft. DE-056 deckt nur hörbares Lesen aus still/leise/laut ab; DE-052 präzisiert Genauigkeit als schriftgetreues Erlesen. Lesetempo und spezielle Lautleseverfahren bleiben begründete Nichtanschlüsse. Keine neuen Karten.

137 Karten; 209 Unterzielzeilen ohne Karte, davon 186 ohne Einzelprüfung und 23 dokumentierte Nichtanschlüsse. 55 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186427 (Vorbereiten des Lesens). Belege review_batch_012.json; Reproduktion batch_012_review.py. Aufgaben und Hilfsmittel bleiben Entscheidung der Lehrkraft.

Daten-/Syntaxprüfung bestanden: nur DE-052/056 geändert, IDs erhalten, Sachunterricht bytegleich. Kein neuer Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-013 · App 1.268 unverändert · 31.10.2026

Drei offene Zeilen page908_186427–186429 geprüft: Vorbereiten des Lesens, Leseerwartungen, Lesebedingungen. Jeweils begründeter vorläufiger Nichtanschluss; genaue Abgrenzungen zu Gedichteinstimmung, Vortragsvorbereitung, Bild-Text-Zuordnung und Lernumgebung in review_batch_013.json. Keine Karten- oder App-Änderung.

137 Karten unverändert; 209 Unterzielzeilen ohne Karte, davon 183 ohne Einzelprüfung und 26 dokumentierte Nichtanschlüsse. 58 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186430 (sinnverstehendes Lesen). Aufgaben/Hilfsmittel bleiben Entscheidung der Lehrkraft.

## Einzelprüfung DE-UZ-014 · App 1.269 · 31.10.2026

Zwei offene Zeilen page908_186430 und 186432 geprüft und begrenzt an DE-059/060 zugeordnet. Sinnverstehen und fragestellungsbezogene Relevanzauswahl konkretisiert; überfliegendes Lesen nicht abgedeckt. Keine neuen Karten. Das vorherige Paket DE-UZ-013 mit drei Nichtanschlüssen war bereits im Quellstand gespeichert und wird mit dieser Veröffentlichung mitgeführt.

137 Karten; 207 Unterzielzeilen ohne Karte, davon 181 ohne Einzelprüfung und 26 dokumentierte Nichtanschlüsse. 60 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186434 (Nachbereiten des Lesens). Einzelbelege review_batch_014.json; Reproduktion batch_014_review.py. Aufgaben und Hilfsmittel bleiben Entscheidung der Lehrkraft.

Daten-/Syntaxprüfung bestanden: nur DE-059/060 geändert, IDs erhalten, Sachunterricht bytegleich. Kein neuer Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-015 · App 1.270 · 31.10.2026

Drei offene Zeilen page908_186434, 186435, 186437 geprüft. Nachbereitung eng über Teilüberschriften an DE-060 angeschlossen. Verstehensschwierigkeiten und einfache Schlussfolgerungen bleiben begründete Nichtanschlüsse. Keine neuen Karten.

137 Karten; 206 Unterzielzeilen ohne Karte, davon 178 ohne Einzelprüfung und 28 dokumentierte Nichtanschlüsse. 63 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186444 (Sach- und Gebrauchstexte). Einzelbelege review_batch_015.json; Reproduktion batch_015_review.py. Aufgaben und Hilfsmittel bleiben Entscheidung der Lehrkraft.

Daten-/Syntaxprüfung bestanden: nur DE-060 geändert, IDs erhalten, Sachunterricht bytegleich. Kein neuer Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-016 · App 1.271 · 31.10.2026

Zwei offene Zeilen page908_186444/186445 geprüft. DE-140 ergänzt nur Merkmale einer schriftlichen Einladung als Gebrauchstext, GS1/2 zu FSP3/4. Auditive/audiovisuelle/digitale Textmerkmale bleiben begründeter Nichtanschluss; Mediennutzung allein genügt nicht.

138 Karten; 205 Unterzielzeilen ohne Karte, davon 176 ohne Einzelprüfung und 29 dokumentierte Nichtanschlüsse. 65 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186452 (Entwickeln von Lesemotivation und Leseinteresse durch). Einzelbelege review_batch_016.json; Reproduktion batch_016_topics.py. Aufgaben/Hilfsmittel bleiben Entscheidung der Lehrkraft.

Daten-/Syntaxprüfung bestanden: bisherige 137 Karten unverändert, IDs erhalten, Sachunterricht bytegleich. Kein neuer Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-017 · App 1.271 unverändert · 31.10.2026

Eine neue Zeile (186452 Lesemotivation) geprüft, eine frühere Entscheidung (186437 Schlussfolgerungen) nachgeprüft und korrigiert. Übergreifende FSP-Stufenbandziele belegen Zielnähe; sie fehlen in der Tabelleninventur. Der frühere Nichtanschluss zu Schlussfolgerungen wird zurückgenommen. Beide Kartenanschlüsse bleiben ausdrücklich offen, bis Quellenrepräsentation und Kriterien geklärt sind. Keine neue Karte und keine App-Änderung. Details und Quellenabgrenzung in review_batch_017.json; frühere Bewertung in Paket 015 als überholt markiert.

138 Karten; 205 Unterzielzeilen ohne Karte: 175 ohne Einzelprüfung, 28 dokumentierte Nichtanschlüsse, 2 geprüfte offene Anschlüsse. Insgesamt 66 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186453 (Vorlesen). Zusätzlich offene Anschlüsse 186437/186452 verfolgen; übergreifende Ziele bei weiteren Prüfungen einbeziehen. Aufgaben und Hilfsmittel bleiben ausschließlich Entscheidung der Lehrkraft.

## Einzelprüfung DE-UZ-018 · App 1.272 · 31.10.2026

Drei offene Zeilen 186453, 186454, 186457 geprüft. DE-141: Vorlesen als Textzugang, ausschließlich FSP1/2 Wahlbereich 3 Theater; kein Vortragstraining und kein Nachweis von Motivation. DE-142: informierendes Lesen und Sachtextverstehen, GS1/2 zu FSP3/4. Andere Lesezwecke, sämtliche Gebrauchstexte und grafische Darstellungen sind nicht mit abgedeckt. Vorlesen als Bemerkung auf FSP-Seite bleibt vom Kennen des Inhaltes unterschieden.

140 Karten; 202 Unterzielzeilen ohne Karte: 172 ohne Einzelprüfung, 28 dokumentierte Nichtanschlüsse, 2 geprüfte offene Anschlüsse. Insgesamt 69 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186465 (Erproben von digitalen Formaten). Offene Anschlüsse 186437/186452 weiterhin verfolgen. Belege review_batch_018.json, Reproduktion batch_018_topics.py. Aufgaben/Hilfsmittel bleiben Entscheidung der Lehrkraft.

Bisherige 138 Karten unverändert. Daten-/Syntaxprüfung und Sachunterricht-Vergleich ausgeführt; kein Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-019 · App 1.273 · 31.10.2026

Drei offene Zeilen 186465, 186468, 186469 geprüft. DE-143: digitales Sprachlernformat, GS1/2 Einblick zu FSP1/2 Anwenden von Sprachwissen. DE-144: Gedichtvortrag im jahreszeitlichen Naturkontext, GS1/2 zu FSP1/2. DE-145: vorbereitetes sinngestaltendes Vorlesen eines literarischen Textes, GS1/2 zu FSP3/4. Keine vollständige Abdeckung aller digitalen Formate, Medienrisiken oder Auswendiglerntechniken.

143 Karten; 199 Unterzielzeilen ohne Karte: 169 ohne Einzelprüfung, 28 dokumentierte Nichtanschlüsse, 2 geprüfte offene Anschlüsse. Insgesamt 72 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186472 (Erproben verschiedener Präsentationsformen). Offene Anschlüsse 186437/186452 bleiben zu bearbeiten. Belege review_batch_019.json, Reproduktion batch_019_topics.py. Aufgaben/Hilfsmittel bleiben Entscheidung der Lehrkraft.

Bisherige 140 Karten unverändert; Daten-/Syntaxprüfung und Sachunterricht-Vergleich ausgeführt. Kein Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-020 · App 1.274 · 31.10.2026

Eine offene Zeile 186472 geprüft. DE-146 ergänzt das eigene Buch als begrenzte Präsentationsform, GS1/2 Einblick zu FSP1/2 Anwenden im Wahlbereich 2. Buchherstellung allein genügt nicht; verschiedene Präsentationsformen und konkrete GS-Beispiele bleiben außerhalb dieses Ausschnitts.

144 Karten; 198 Unterzielzeilen ohne Karte: 168 ohne Einzelprüfung, 28 dokumentierte Nichtanschlüsse, 2 geprüfte offene Anschlüsse. Insgesamt 73 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186479 (Sprechen über Verstehens- und Verständigungsprobleme). Offene Anschlüsse 186437/186452 bleiben zu bearbeiten. Belege review_batch_020.json, Reproduktion batch_020_topics.py. Aufgaben/Hilfsmittel bleiben Entscheidung der Lehrkraft.

Bisherige 143 Karten unverändert; Daten-/Syntaxprüfung und Sachunterricht-Vergleich ausgeführt. Kein Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-021 · App 1.275 · 31.10.2026

Drei offene Zeilen 186479–186481 geprüft. DE-147 verbindet das Sprechen über eine Wortunklarheit und ihre Klärung ausschließlich am Begriff Unterschrift, GS1/2 zu FSP3/4. FSP-Anwenden persönlicher Angaben bleibt zusätzlich erforderlich; kein allgemeiner Anschluss aller Verständigungsprobleme. Mehrdeutigkeit bleibt begründeter vorläufiger Nichtanschluss; Sprachspiele und Rätsel reichen als Beleg nicht aus. Übergreifende Kommunikationsziele wurden berücksichtigt.

145 Karten; 196 Unterzielzeilen ohne Karte: 165 ohne Einzelprüfung, 29 dokumentierte Nichtanschlüsse, 2 geprüfte offene Anschlüsse. Insgesamt 76 zuvor offene und 4 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186483 (Erkennen grundlegender Unterschiede). Offene Anschlüsse 186437/186452 bleiben zu bearbeiten. Belege review_batch_021.json, Reproduktion batch_021_topics.py. Aufgaben/Hilfsmittel bleiben Entscheidung der Lehrkraft.

Bisherige 144 Karten unverändert; Daten-/Syntaxprüfung und Sachunterricht-Vergleich ausgeführt. Kein Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-022 · App 1.276 · 31.10.2026

Eine offene Zeile 186483 und die bereits zugeordnete Nachbarzeile 186484 geprüft. DE-094 präzisiert: GS erprobt beide Einladungsformen und beobachtet erste Unterschiede; FSP3/4 wendet beide situationsgerecht bei einem neuen Anlass an. Keine Gleichsetzung von Mündlichkeit/Nähe und Schriftlichkeit/Distanz, keine vollständige Kommunikationstheorie. Keine neuen Karten.

145 Karten; 195 Unterzielzeilen ohne Karte: 164 ohne Einzelprüfung, 29 dokumentierte Nichtanschlüsse, 2 geprüfte offene Anschlüsse. Insgesamt 77 zuvor offene und 5 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186486 (Beschreiben eigener Erfahrungen). Offene Anschlüsse 186437/186452 bleiben zu bearbeiten. Belege review_batch_022.json, Reproduktion batch_022_review.py. Aufgaben/Hilfsmittel bleiben Entscheidung der Lehrkraft.

Nur DE-094 geändert; IDs erhalten. Daten-/Syntaxprüfung und Sachunterricht-Vergleich ausgeführt. Kein Browser- oder PDF-Test.

## Einzelprüfung DE-UZ-023 · App 1.276 unverändert · 01.11.2026

Zwei offene Zeilen 186486/186487 zur sprachlichen Vielfalt geprüft. Eigene Spracherfahrungen beschreiben und Sprachvarianten vergleichen bleiben begründete vorläufige Nichtanschlüsse. FSP-Mehrsprachigkeit und kulturelle Vielfalt wurden als didaktischer Kontext bzw. Bemerkung berücksichtigt, nicht als eigenständige Vergleichs- oder Beschreibungsziele umgedeutet. Keine Karten- oder App-Änderung.

145 Karten; 195 Unterzielzeilen ohne Karte: 162 ohne Einzelprüfung, 31 dokumentierte Nichtanschlüsse, 2 geprüfte offene Anschlüsse. Insgesamt 79 zuvor offene und 5 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186492 (Zentrum des Satzes). Offene Anschlüsse 186437/186452 bleiben zu bearbeiten. Einzelbelege review_batch_023.json. Aufgaben/Hilfsmittel bleiben Entscheidung der Lehrkraft.

## Einzelprüfung DE-UZ-024 · App 1.276 unverändert · 01.11.2026

Zwei offene Zeilen 186492/186496 geprüft: Verb als Zentrum des Satzes und Nomen als Kern der Nominalgruppe. Beide bleiben begründete vorläufige Nichtanschlüsse. Wortartenwissen, Personalformen, Artikelfähigkeit und Verwendung von Satzmustern werden nicht mit Kenntnis dieser syntaktischen Funktionen gleichgesetzt. Keine Karten- oder App-Änderung.

145 Karten; 195 Unterzielzeilen ohne Karte: 160 ohne Einzelprüfung, 33 dokumentierte Nichtanschlüsse, 2 geprüfte offene Anschlüsse. Insgesamt 81 zuvor offene und 5 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186499 (Begleiter des Nomens). Offene Anschlüsse 186437/186452 bleiben zu bearbeiten. Einzelbelege review_batch_024.json. Aufgaben/Hilfsmittel bleiben Entscheidung der Lehrkraft.

## Einzelprüfung DE-UZ-025 · App 1.277 · 01.11.2026

Neun offene und zwei bereits zugeordnete Zeilen geprüft (Einzelbelege review_batch_025.json). DE-121 ergänzt die Begleiterfunktion, DE-124 das Satzuntersuchungsverfahren begrenzt über Klangprobe. Beide Kriterien präzisiert. Sieben vorläufige Nichtanschlüsse: Adjektivstellung, Zusammensetzung, Präfixableitung, Wortfamilien, Wortfelder, Wortgruppenstruktur, Erweiterungsprobe. Lesen von Wortbausteinen und Satzverwendung wurden von Wortbildung bzw. Satzuntersuchung getrennt. GS-Rechtschreibrahmen zu Morphologie und Nominalgruppen berücksichtigt.

145 Karten; 193 Unterzielzeilen ohne Karte: 151 ohne Einzelprüfung, 40 dokumentierte Nichtanschlüsse, 2 geprüfte offene Anschlüsse. Insgesamt 90 zuvor offene und 7 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186528 (Informieren). Offene Anschlüsse 186437/186452 weiter verfolgen. Reproduktion batch_025_review.py. Aufgaben/Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

## Einzelprüfung DE-UZ-026 · App 1.278 · 01.11.2026

Acht offene und zwei bereits zugeordnete Zeilen geprüft (186528–186542; zehn Einzelbelege in review_batch_026.json). DE-148 ergänzt Informieren im häuslichen Kontext, DE-149 räumlichen Wortschatz, jeweils GS3 zu FSP1/2 mit getrennten Operatoren. DE-004 grenzt den Theateranschluss auf belegte Körper- und Stimmmittel ein; Pausen/Blickkontakt sind nicht ausdrücklich belegt. DE-007 ergänzt Gesprächskultur und wertschätzende Gesprächsatmosphäre im Klassenrat mit begründeter FSP-Positionierung. Vier vorläufige Nichtanschlüsse: Bildungs-/Fachsprache, kriterienbezogene Redebeitragsrückmeldung, Diktierfunktion, Sprachvarietäten. Übergreifende Sprachförderungsziele und Bemerkungen sind berücksichtigt.

147 Karten; 189 Unterzielzeilen ohne Karte: 143 ohne Einzelprüfung, 44 dokumentierte Nichtanschlüsse, 2 geprüfte offene Anschlüsse. Insgesamt 98 zuvor offene und 9 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186544 (Verstehen anderer Meinungen). Offene Anschlüsse 186437/186452 bleiben erhalten. Reproduktion: batch_026_review.py und batch_026_cards.json, eingebunden in build_deutsch.py. Aufgaben/Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Daten-/Quellen-/Syntaxprüfung und Sachunterricht-Vergleich bestanden; Prüfinvarianten des Python-Skripts mit Node ausgeführt, da Python auf dem Host fehlt. Python-Generator nicht ausgeführt. Nur DE-004/007 geändert; übrige 143 vorhandene Karten unverändert. Kein PDF-Download-Test.

Live-Browserkontrolle nach Veröffentlichung bestanden: Version 1.278 mit Datum 01.11.2026, DE-148/149 in Deutsch Klasse 3 sichtbar; DE-148 mit Quellen und Operatorenvergleich geöffnet.

## Einzelprüfung DE-UZ-027 · App 1.279 · 01.11.2026

Elf offene und drei bereits zugeordnete Zeilen in drei zusammenhängenden Teilpaketen geprüft: Gespräch, Vortragen/Präsentationsvorbereitung und Hörverstehen (14 Einzelbelege in review_batch_027.json). DE-150 ergänzt einen begrenzten Anschluss für Inhaltsauswahl und Sprechvorlage eines Rollenbeitrags im FSP-Wahlbereich 4; der Strategieanschluss ist auf diese Schritte beschränkt. Das Manuskript ist curricularer Zielgegenstand, keine Hilfsmittelvorgabe. DE-012 präzisiert den Unterschied zwischen GS-Transfer und FSP-Kennen beim literarischen Vortrag. DE-016 ergänzt Hörverstehen und aufmerksames Zuhören, grenzt Aussagen von Absichten ab und präzisiert die Nachweise. DE-007 für 186546 bestätigt und unverändert.

Fünf vorläufige Nichtanschlüsse: Bezugnahme auf Vorredner, Einüben des Redebeitrags, Auswendiglerntechniken, Zuhörvorbereitung und Hörerwartung. Bei 186544 (Verstehen anderer Meinungen) ist eine belegte Nähe zu Gespräch/Verständnis anderer dokumentiert; ein Kartenanschluss bleibt offen, damit Empathie und Verstehen fremder Begründungen nicht gleichgesetzt werden.

148 Karten; 184 Unterzielzeilen ohne Karte: 132 ohne Einzelprüfung, 49 dokumentierte Nichtanschlüsse, 3 geprüfte offene Anschlussfragen. Insgesamt 109 zuvor offene und 12 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186564 (Nutzen von Zuhörstrategien). Unsicherheiten 186437, 186452 und 186544 bleiben zu bearbeiten. Reproduktion: batch_027_review.py und batch_027_cards.json, eingebunden in build_deutsch.py. Aufgaben/Lernhandlungen und Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Daten-/Quellenanker-/Operatoren-/Syntaxprüfung und Sachunterricht-Vergleich bestanden. Gleichwertige Prüfungen und Datumssynchronisierung mit Node, da Python nicht verfügbar ist; Python-Generator nicht ausgeführt. Nur DE-012/016 geändert, DE-150 ergänzt; übrige 145 vorhandene Karten unverändert. Kein PDF-Download-Test.

Live-Browserprüfung nach Veröffentlichung bestanden: Version 1.279 mit Datum 01.11.2026; neue Karte DE-150 im Bereich Deutsch Klasse 3 sichtbar und als FSP-Wahlbereich gekennzeichnet.

## Einzelprüfung DE-UZ-028 · App 1.280 · 01.11.2026

Acht offene und zwei bereits zugeordnete Zeilen geprüft: 186564–186569 und 186585–186588 (zehn Einzelbelege in review_batch_028.json). DE-016 ergänzt Nachbereitung und Sicherung ausdrücklich gehörter Informationen; Schlussfolgerungen und versteckte Informationen werden nicht als FSP-Hörziele ausgegeben. DE-020 korrigiert die falsche Beherrschen-Erklärung für GS3 zu Übertragen und präzisiert Handschrift und einfache Textanordnung. Das übergreifende FSP3/4-Ziel zur übersichtlichen Gliederung schriftlicher Arbeiten wird positiv und separat als Quelle berücksichtigt. DE-151 ergänzt digitales Schreiben im Textprogramm, mit Unterscheidung von GS-Elternoperator Übertragen, Unterziel Erproben und FSP-Kennen.

Vier vorläufige Nichtanschlüsse: eigene Zuhörstrategien/Hörbedingungen, Zusatzinformationen, bewusstes Nachfragen bei Nichtverstehen, Schriftreflexion. Eingeräumte Rückfragemöglichkeiten bzw. kommentierendes Schreiben werden nicht mit metakognitiven Zielnachweisen gleichgesetzt.

149 Karten; 180 Unterzielzeilen ohne Karte: 124 ohne Einzelprüfung, 53 dokumentierte Nichtanschlüsse, 3 geprüfte offene Anschlussfragen. Insgesamt 117 zuvor offene und 14 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186591 (Wortebene). Unsicherheiten 186437, 186452 und 186544 bleiben zu bearbeiten. Reproduktion: batch_028_review.py und batch_028_cards.json, eingebunden in build_deutsch.py. Der Generator vermeidet doppelte Rechtschreibrahmen-Verweise bei präzisierten Karten. Aufgaben/Lernhandlungen und Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Daten-/Quellen-/Operatoren-/Syntaxprüfung und Sachunterricht-Vergleich bestanden. Gleichwertige Prüfung und Datumssynchronisierung mit Node, da Python nicht verfügbar ist; Python-Generator nicht ausgeführt. Nur DE-016/020 geändert, DE-151 ergänzt; übrige 146 vorhandene Karten unverändert. Kein PDF-Download-Test.

Live-Browserprüfung nach Veröffentlichung bestanden: Version 1.280 und Datum 01.11.2026 sichtbar; DE-020 mit präzisierter Textanordnung sichtbar; DE-151 mit Quellen und Operatorenvergleich Übertragen/Kennen geöffnet.


### DE-UZ-029 · 01.11.2026 · GS3 Rechtschreibung

11 Zeilen einzeln geprüft: 8 zuvor offene sowie 3 zuvor zugeordnete Zeilen. Wortebene und Satzebene als Gliederungszeilen ausgewiesen. DE-025 (Doppelkonsonanten/Stammkonstanz bei Auslautverhärtung) und DE-114 (Worttrennung) präzisiert; DE-152 für Doppelpunkt und Anführungszeichen bei wörtlicher Rede ergänzt. Vier begründete Nichtanschlüsse: silbentrennendes h, Wortbildungsformen, Anredepronomina, syntaktische Großschreibung erweiterbarer Nominalgruppenkerne. FSP-Dehnungs-h, lesende Wortbausteinerkennung und Substantivgroßschreibung wurden nicht gleichgesetzt.

Stand: 150 Karten; 176 Zeilen ohne Karte, davon 116 noch einzeln zu prüfen, 57 dokumentierte Nichtanschlüsse und 3 unveränderte Unsicherheiten. Kumulativ 125 zuvor offene und 17 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186615 „Aufsuchen von Wörtern nach Zweit- und Drittbuchstabe“. Details, Kriterien, Restumfang und Belege: review_batch_029.json. App 1.281, Modul DE-2026-11-01.5. Sachunterricht und stabile Karten-IDs erhalten; Aufgaben und Hilfsmittel bleiben Lehrkraftentscheidung.

Validierung vor Veröffentlichung bestanden: 150 Karten und 117 Zielblöcke, Quellen/Operatoren/Stufenbänder, eingebettete Daten und drei Skripte geprüft; Sachunterricht bytegleich, 147 übrige Karten unverändert. Node-Prüfungen äquivalent zu check-deutsch.py/prepare-pages.py; Python-Generator mangels Python nicht ausgeführt. Liveprüfung auf GitHub Pages bestanden: Version 1.281, Datum 01.11.2026 und neue Karte DE-152 mit Kennen/Einblick gewinnen, passendem Stufenband und Quellenlinks sichtbar kontrolliert. Kein PDF-Download-Test.


## Einzelprüfung DE-UZ-030 · App 1.282 · 01.11.2026

15 Zeilen in drei Teilpaketen einzeln geprüft: Wörterbuchverfahren (3), Textplanung (4), Formulieren und Schreibformen (8). Davon 11 zuvor offen und 4 bereits zugeordnet. DE-045 präzisiert das Buchprojekt und die unterschiedlichen Planungs-/Herstellungsanforderungen; DE-123 präzisiert Fantasiegeschichte und Kriterien, mit begrenzten Bezügen auf kreatives/produktives Schreiben. DE-048 unverändert bestätigt. Neu: DE-153 (Schreibabsicht und Formulierungen einer Einladung, mit zusätzlichem übergreifendem Schreibanlass-Beleg), DE-154 (eigene kurze Mitteilung), DE-155 (schriftliche Beschreibung einer erkundeten historischen Anlage, nur FSP-Wahlbereich 3).

Fünf begründete Nichtanschlüsse: Zweit-/Drittbuchstabensuche, Grundformbildung für das Nachschlagen, gesondertes Wortteilnachschlagen, digitale Textgestaltung, kooperatives Schreiben. Alphabetische Grundsuche, Wortartenwissen, Lesen von Wortbausteinen, Formatierung als Differenzierung und allgemeine Kooperation wurden nicht als Belege für die spezifischen GS-Handlungen ausgegeben.

Stand: 153 Karten; 170 Zeilen ohne Karte, davon 105 ohne Einzelprüfung, 62 dokumentierte Nichtanschlüsse und 3 unveränderte Unsicherheiten. Kumulativ 136 zuvor offene und 21 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186653 „Überarbeiten nach ausgewählten Kriterien“. Einzelbelege, Restumfang, Operatoren und Kriterien: review_batch_030.json. Reproduktion: batch_030_review.py/batch_030_cards.json, in build_deutsch.py integriert. Modul DE-2026-11-01.6. Aufgaben und Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Validierung: Daten-/Quellen-/Operatoren-/Stufenband-/Syntaxprüfung bestanden; Sachunterricht bytegleich, 148 bisherige Karten unverändert. CSV und Restumfang abgeglichen. Gleichwertige Node-Prüfungen und Datumssynchronisierung, da python3 auf dem Host nicht nutzbar ist; Python-Generator nicht ausgeführt. Liveprüfung auf GitHub Pages bestanden: Version 1.282, Datum 01.11.2026 und neue Karten DE-153/154/155 sichtbar, DE-155 mit FSP-Wahlbereichshinweis. DE-153 mit Operatoren Übertragen/Anwenden und zusätzlicher Schreibanlass-Quelle geöffnet. Kein PDF-Download-Test.


## Einzelprüfung DE-UZ-031 · App 1.283 · 01.11.2026

15 Zeilen in drei Teilpaketen geprüft: Textüberarbeitung (9), Leseflüssigkeit/Verfahren (2), Lesevorbereitung (4). Davon 14 zuvor offen und 1 bereits zugeordnete Zeile mit zwei Karten. DE-053 und DE-057 präzisiert: GS-Beherrschen mit automatisierter, zügiger und sinngestaltender Leseflüssigkeit von FSP-Übertragen beim eigenen Erlesen getrennt; GS-Lesereflexion berücksichtigt. Eine richtige Inhaltsantwort allein weist keine Leseflüssigkeit nach. Keine neuen Karten.

13 begründete Nichtanschlüsse. Selbstkontrolle (page908_186659) als zusätzliche offene Anschlussfrage dokumentiert: FSP-Stufenbandziele 1/2 und 3/4 sowie Lernen lernen belegen Kontrolle ausdrücklich. Textbezogene Eingrenzung und Operatorrepräsentation unter dem GS-Zwischenziel Rückmeldungsnutzung bleiben zu klären. Dieser positive übergreifende Beleg wird nicht als fehlend ausgegeben; noch keine Karte. Die Blockbegründung 186651 weist die offene Frage jetzt aus. Allgemeine Ergebniskontrolle, digitale Bedienung, Sprachwissen und Vortragsvorbereitung werden nicht pauschal mit Textrevision bzw. Lesevorbereitung gleichgesetzt.

Stand: 153 Karten; 170 Zeilen ohne Karte, davon 91 ohne Einzelprüfung, 75 dokumentierte Nichtanschlüsse und 4 offene Anschlussfragen. Kumulativ 150 zuvor offene und 22 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186700 „Heranziehen von Hintergrundwissen zum Textverständnis“; die unmittelbar vorangehende zugeordnete Zeile 186699 ist bei der zusammenhängenden Kartenprüfung mit zu beachten. Belege, Zwischenziele und Restumfang: review_batch_031.json. Reproduktion über batch_031_review.py/batch_031_cards.json. Modul DE-2026-11-01.7. Aufgaben und Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Validierung: Daten-/Quellen-/Operatoren-/Stufenband-/Syntaxprüfung bestanden; 151 übrige Karten unverändert, Sachunterricht bytegleich. CSV und Unsicherheitszähler abgeglichen. Gleichwertige Node-Prüfungen und Datumssynchronisierung, da Python auf dem Host nicht verfügbar ist; Python-Generator nicht ausgeführt. Liveprüfung auf GitHub Pages bestanden: Version 1.283 und Datum 01.11.2026 sichtbar; DE-053/057 in der Auswahl mit präzisierten Zielausschnitten. DE-057 geöffnet: Operatoren Beherrschen/Übertragen, Begrenzung auf eigenes Lesen, Abgrenzung der GS-Leseflüssigkeit und sechs amtliche Quellenanker sichtbar. Screenshot lokal als live-1.283.png gesichert. Kein PDF-Download-Test.


## Einzelprüfung DE-UZ-032 · App 1.284 · 01.11.2026

14 Zeilen in drei zusammenhängenden Paketen geprüft: Leseverstehen/Nachbereitung (7), Merkmale medialer Texte (2), Medienangebote und Bezugsquellen (5). Davon 10 zuvor offen und 4 bereits zugeordnet. DE-062 präzisiert Sinnerfassung und Textgliederung mit passenden Feinzielen; GS-Kennen bleibt vom FSP-Übertragen beim unbekannten kleinen Text getrennt. DE-079 ergänzt die Bibliothek als begrenzte Bezugsquelle und bildet Auswahlbegründung, Adressatenbezug und FSP-Wunsch-/Traum-/Fantasiekontext genauer ab.

Neue Karten: DE-156 verbindet Merkmalskenntnis einer schriftlichen Einladung (GS3 Kennen) mit deren situationsgerechter Verwendung für einen neuen Anlass (FSP3/4 Anwenden). DE-157 verbindet Kenntnis unterschiedlicher Informationsangebote mit einem ersten Zugang zur Bedeutung öffentlicher/sozialer Einrichtungen (FSP3/4 Einblick gewinnen). Drei zuvor offene Zeilen erhalten begrenzte Zuordnungen. Keine allgemeinen Recherche- oder vollständigen Textsortenanschlüsse.

Fünf begründete Nichtanschlüsse: Hintergrundwissen als Lesestrategie, Aufbauen/Prüfen von Sinnerwartungen, Informationsermittlung trotz widersprüchlicher Aussagen, Merkmale auditiver/audiovisueller/digitaler Texte sowie Ordnungskriterien von Medien. Zwei zusätzliche Anschlussfragen bleiben offen (186705/186706): Die FSP3/4-Stufenbandziele belegen ausdrücklich Wertungen und Schlussfolgerungen aus Gelesenem. Die präzise Eingrenzung von Interpretation bzw. begründetem Schlussfolgern und die Operatorrepräsentation benötigen weitere Prüfung. Der positive Beleg wird nicht als fehlender FSP-Anschluss ausgegeben.

Stand: 155 Karten; 167 Zeilen ohne Karte, davon 81 ohne Einzelprüfung, 80 dokumentierte Nichtanschlüsse und 6 offene Anschlussfragen. Kumulativ 160 zuvor offene und 26 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186727 „Vertiefen von Lesemotivation, Leseinteresse und Leseerfahrungen“. Einzelbelege, Kandidaten beider Stufenbänder, übergreifende Ziele und Restumfang: review_batch_032.json. Reproduktion über batch_032_review.py/batch_032_cards.json, in build_deutsch.py eingebunden; Karten-IDs im Register ergänzt. Modul DE-2026-11-01.8. Aufgaben und Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Validierung: Daten-/Quellen-/Operatoren-/Stufenband-/Syntaxprüfung bestanden; 151 übrige Karten und Sachunterricht unverändert. CSV, Unsicherheiten und Restumfang konsistent. Gleichwertige Node-Prüfungen und Datumssynchronisierung entsprechend check-deutsch.py/prepare-pages.py, da Python auf dem Host nicht verfügbar ist; Python-Generator nicht ausgeführt. Append-/Refine-Hooks und Quellensynchronisierung geprüft. Liveprüfung auf GitHub Pages bestanden: Version 1.284 und Datum 01.11.2026 sichtbar; neue Karten DE-156/157 in GS3/Medienangeboten auswählbar. DE-156 geöffnet mit Kennen/Anwenden, vier Quellenankern und begrenztem Einladungskontext. DE-157 geöffnet mit Kennen/Einblick gewinnen, fünf Quellenankern und ausdrücklicher Bindung an die Bedeutung öffentlicher/sozialer Einrichtungen. Screenshot lokal als live-1.284.png gesichert. Kein PDF-Download-Test.


## Einzelprüfung DE-UZ-033 · App 1.285 · 01.11.2026

12 Zeilen in drei Paketen geprüft: literarische Erschließung (5), Recherche und digitale Medien (5), Präsentation (2). Davon 6 zuvor offen und 6 bereits zugeordnet. DE-072 präzisiert Handlungslogik, Figurenabsicht und GS-Textbezug gegenüber dem FSP-Grundverständnis. DE-089 weist den ersten GS-Medienvergleich konkret nach, ohne ihn dem FSP zuzuschreiben. DE-083 grenzt Textprogrammbedienung gegen Routine und umfassende Medienproduktion ab. DE-087 trennt GS-Kennen szenischer Möglichkeiten von der FSP-Übertragung in eine Szene.

Neue Karten: DE-158 eigenes Buch als Präsentationsform (GS3/FSP1/2, nur FSP-Wahlbereich 2); DE-159 digitale Freizeitangebote und eigene Nutzung einschätzen (GS3/FSP3/4, konkrete Freizeitziele plus allgemeine Medienbildung); DE-160 Stellungnahme zum Verhalten einer Märchenfigur (GS3/FSP1/2, Kennen gegenüber Sich positionieren). Vier zuvor offene Zeilen erhalten begrenzte Anschlüsse.

Suchmaschinen-Erprobung bleibt begründeter Nichtanschluss: digitale Recherche und Speichern im Textprogramm belegen den spezifischen GS-Zielkomplex nicht. Lesemotivation (186727) bleibt eine zusätzliche offene Anschlussfrage: Der positive übergreifende FSP-Beleg zu Lesefreude und Leseinteressen ist gesichert, eine angemessene Kartenabbildung ohne Bewertung persönlicher Motivation noch zu klären. Kein pauschales Fehlen des FSP-Inhalts behauptet.

Stand: 158 Karten; 163 Zeilen ohne Karte, davon 75 ohne Einzelprüfung, 81 dokumentierte Nichtanschlüsse und 7 offene Anschlussfragen. Kumulativ 166 zuvor offene und 32 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186770 „Erkennen des Zusammenhangs zwischen Äußerungsabsicht, sprachlichen Mitteln und Wirkung“. Der Fachbegriffsblock 186752 behält seine bisherige Blockabgrenzung; seine gesamte Begriffsliste wurde in diesem Paket nicht zusätzlich einzeln geprüft. Belege und Restumfang: review_batch_033.json. Reproduktion: batch_033_review.py/batch_033_cards.json mit Append-/Refine-Hooks und stabilen Register-IDs. Modul DE-2026-11-01.9. Aufgaben und Hilfsmittel bestimmt ausschließlich die Lehrkraft.

Validierung: Daten-/Quellen-/Operatoren-/Stufenband-/Wahlbereichs-/Syntaxprüfung bestanden; 151 übrige Karten und Sachunterricht unverändert. CSV, Register, Unsicherheiten und Restumfang konsistent. Gleichwertige Node-Prüfungen und Berliner Datumssynchronisierung entsprechend check-deutsch.py/prepare-pages.py, da Python auf dem Host nicht verfügbar ist; Python-Generator nicht ausgeführt. Append-/Refine-Hooks und ergänzende Medienbildungsquelle geprüft. Liveprüfung auf GitHub Pages bestanden: Version 1.285 und Datum 01.11.2026 sichtbar. DE-158, DE-159 und DE-160 geöffnet; Stufenbandkennzeichnungen und Operatoren Kennen/Anwenden bzw. Kennen/Sich positionieren korrekt. DE-158 zeigt ausdrücklich FSP1/2-Wahlbereich 2; DE-160 enthält die Märchenanker; DE-159 zeigt den Freizeitkontext und die ergänzende allgemeine Medienbildungsquelle. Screenshot lokal als live-1.285.png gesichert. Kein PDF-Download-Test.


## Einzelprüfung DE-UZ-034 · App 1.286 · 01.11.2026

13 Zeilen in drei Paketen geprüft: Sprachformen/Absicht/Wirkung (7), Kommunikationsgrundlagen (2), sprachliche Vielfalt (4). Davon 11 zuvor offen und 2 bereits zugeordnet. DE-092 verbindet Absicht, sprachliche Form, Gegenüber und mögliche Wirkung auf GS-Seite mit bekannten FSP1/2-Umgangsformen. DE-095 präzisiert Sprecher-/Schreiber- und Hörer-/Leserrollen gegenüber FSP3/4-Anwendung von Einladungsformen auf einen neuen Anlass.

Neue Karte DE-161: Blumennamen sprachlich entdecken. GS3-Namen/Wortphänomene werden mit dem ausdrücklichen FSP3/4-Sprachunterziel im Pflanzenkontext verbunden. Vier zuvor offene Zeilen erhalten begrenzte Zuordnungen, einschließlich des strukturierenden Unterziels besonderer Sprachformen. Keine vollständige Namenkunde, Wortforschung oder Abdeckung aller Sprachformen.

Sechs begründete Nichtanschlüsse: Redensarten/Herkunft, mehrdeutige Kommunikationssituationen, eigene Erfahrungen mit sprachlicher Vielfalt, Dialekt, Standard-/Umgangssprache und Sprachvergleich. Positive Belege zu Kommunikation, kultureller Vielfalt und Mehrsprachigkeit sind berücksichtigt; sie belegen nicht automatisch Varietätenkenntnis oder Sprachsystemvergleich. Sprichwörter (186772) bleiben eine zusätzliche Anschlussfrage: Der FSP nennt sie ausdrücklich im Erntekontext. Die Eingrenzung eines gemeinsamen Gegenstands mit passenden Feinzielen und die Unterscheidung zu Bauernregeln sind noch zu klären.

Stand: 159 Karten; 159 Zeilen ohne Karte, davon 64 ohne Einzelprüfung, 87 dokumentierte Nichtanschlüsse und 8 offene Anschlussfragen. Kumulativ 177 zuvor offene und 34 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186790 „Verb“. Belege, Kandidaten beider FSP-Bänder, übergreifende Ziele und Restumfang: review_batch_034.json. Reproduktion: batch_034_review.py/batch_034_cards.json, Append-/Refine-Hooks und Register-ID DE-161. Modul DE-2026-11-01.10. Aufgaben und Hilfsmittel bestimmt ausschließlich die Lehrkraft.

Validierung: PASS: 159 eindeutige Karten, 117 Zielblöcke; Quellenanker, Elternziele, Operatoren, Stufenbänder und zwei Feinziele je Karte geprüft. Zwei Karten präzisiert und eine ergänzt; übrige 156 Karten sowie bestehende IDs unverändert. Sachunterricht bytegleich zur Baseline, Inventuren und Ausgangsdateien gegen aktuelle GitHub-Blob-SHAs verifiziert. Deutsch-JSON identisch eingebettet; drei JavaScript-Blöcke syntaktisch geprüft. Root/dist identisch mit Datum 01.11.2026. CSV, eindeutige Prüf-IDs, 64 offene Zeilen, 87 Nichtanschlüsse, 8 Unsicherheiten und Fortsetzungspunkt abgeglichen. Gleichwertige Node-Prüfungen und Datumssynchronisierung entsprechend scripts/check-deutsch.py und scripts/prepare-pages.py; Python auf dem Host nicht verfügbar, Python-Generator nicht ausgeführt. Register und Append-/Refine-/Quellensynchronisierung geprüft. Keine Aufgaben-/Hilfsmittelvorschläge. Liveprüfung auf GitHub Pages bestanden: Version 1.286 und Datum 01.11.2026 sichtbar. DE-092 geöffnet mit stufenübergreifendem GS3/FSP1/2-Bezug, Kennen/Kennen, Absicht/Wirkung und acht Quellenankern. DE-095 geöffnet mit Kennen/Anwenden, ausdrücklichem Rollenbezug und vier Quellenankern. DE-161 geöffnet mit GS3/FSP3/4, Kennen/Kennen, Pflanzen-/Blumennamenkontext, klarer Restbegrenzung und acht Quellenankern. Screenshot lokal als live-1.286.png gesichert. Kein PDF-Download-Test.


## Einzelprüfung DE-UZ-035 · App 1.287 · 01.11.2026

16 Zeilen in den Paketen Wortartmerkmale (14) und Wortbildung (2) einzeln geprüft: 13 zuvor offen und 3 bereits zugeordnete Pronomenzeilen. DE-101 präzisiert die Personalpronomen-Funktion mit dem ergänzten FSP-Unteranker „Ersatz für Substantive“. GS-Kennen umfasst Stellvertretung und Zahlbezug; FSP-Einblick gewinnen bleibt ein erster Zugang ohne vollständige Nominalgruppen-/Subjekttheorie oder Formenreihen.

Neue Karte DE-162: Vergangenheit und Gegenwart beim Sprechen über Ernte unterscheiden. Der FSP3/4-Unterpunkt „über Ernte früher und heute sprechen“ trägt einen engen Anschluss für GS-Zeitwörter/-wendungen. Sprachliche Zeitmarkierung und sachbezogene Kenntnis der Getreideernte erhalten getrennte Feinziele. Keine Abdeckung von Präsens/Präteritum oder Sprichwortdeutung; der historische Gebrauch von „heute“ bleibt kontextbezogen.

Zehn begründete Nichtanschlüsse: Verb als strukturierende Zeile der weiteren Merkmale, Präsens/Präteritum, Prädikatsfunktion, weitere Artikelwörter, Adjektiv als strukturierende Zeile, Steigerungsstufen, als/wie, Nominalgruppen-/Subjektfunktion sowie Zusammensetzungen und Ableitungen. Bloße Wortartnamen, Sachvergleiche und lesendes Wiedererkennen von Wortteilen genügen nicht für die jeweils spezifische GS-Anforderung. Zwei zusätzliche Unsicherheiten (186793/186795) betreffen Nomen/Abstrakte: FSP3/4 nennt „Erscheinungen“, dessen Reichweite für Gefühle und Nichtgegenständliches ist nicht eindeutig genug für eine neue Karte. Der positive Beleg wird ausdrücklich dokumentiert.

Stand: 160 Karten; 158 Zeilen ohne Karte, davon 51 ohne Einzelprüfung, 97 dokumentierte Nichtanschlüsse und 10 offene Anschlussfragen. Kumulativ 190 zuvor offene und 37 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186811 „Erkennen von Wortstämmen“. Belege, Kandidaten beider FSP-Bänder, übergreifende Ziele, ergänzender Rechtschreibrahmen und Restumfang: review_batch_035.json. Reproduktion über batch_035_review.py/batch_035_cards.json mit Append-/Refine-Hooks und stabiler Register-ID DE-162. Modul DE-2026-11-01.11. Aufgaben und Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Validierung: PASS: 160 eindeutige Karten, 117 Zielblöcke; Quellenanker, Elternziele, Operatoren, Stufenbänder und zwei Feinziele je Karte geprüft. Eine Karte präzisiert und eine ergänzt; übrige 158 Karten sowie bestehende IDs unverändert. Sachunterricht bytegleich zur Baseline, Inventuren und Ausgangsdateien gegen GitHub-Blob-SHAs verifiziert. Deutsch-JSON identisch eingebettet; drei JavaScript-Blöcke syntaktisch geprüft. Root/dist identisch mit Datum 01.11.2026. CSV, eindeutige Prüf-IDs, 51 offene Zeilen, 97 Nichtanschlüsse, 10 Unsicherheiten und Fortsetzungspunkt abgeglichen. Gleichwertige Node-Prüfungen und Datumssynchronisierung entsprechend scripts/check-deutsch.py und scripts/prepare-pages.py; Python auf dem Host nicht verfügbar, Python-Generator nicht ausgeführt. Register und Append-/Refine-/Quellensynchronisierung geprüft. Keine Aufgaben-/Hilfsmittelvorschläge. Liveprüfung auf GitHub Pages bestanden: Version 1.287 und Datum 01.11.2026 sichtbar. DE-101 geöffnet mit GS3/FSP3/4, Kennen/Einblick gewinnen, ausdrücklich ergänztem Ersatz-Unteranker und sechs amtlichen Quellen. DE-162 geöffnet mit Kennen/Kennen, Zeitmarkierungs-/Getreideerntekontext, klarer Abgrenzung zur Tempusgrammatik und fünf Quellenankern. Screenshot lokal als live-1.287.png gesichert. Kein PDF-Download-Test.


## Eindeutige Kartentitel · App 1.288 · 01.11.2026

Alle 160 Deutsch- und 135 Sachunterrichtskarten auf identische Überschriften geprüft. 29 doppelte Deutsch-Titelgruppen mit 89 Karten und ein Sachunterricht-Titelpaar konkretisiert. Die Überschriften benennen den ausgewählten Gegenstand, die Zielperspektive bzw. das Anforderungsniveau. Bei sachlich gleichen Karten unterschiedlicher Stufen werden GS-Klasse oder FSP-Band ergänzt. Beispiel GS3-Literatur: „Merkmale einer Fabel erkennen und erläutern“, „Handlungslogik und Figurenperspektiven verstehen“, „Ein weiteres Kinderbuch vorstellen · GS 3“.

Die zentrale Zuordnung in ../card_titles.json wird im Deutsch-Generator nach allen historischen Patches angewendet. Für Sachunterricht werden ausschließlich die angezeigten Titel überschrieben; die Baseline bleibt bytegleich. prepare-pages.py synchronisiert den separaten Titel-Datenblock; check-deutsch.py kontrolliert eindeutige Titel über beide Fächer. IDs, fachliche Anker, Feinziele, Kriterien, Unterrichtsplanung und Fortschritt der Einzelprüfung bleiben erhalten. Die Änderung ist eine redaktionelle Titelprüfung, keine zusätzliche fachliche Freigabe. Modul DE-2026-11-01.12. Nachweis: ../card_title_review.json.

Validierung der Kartentitel: PASS: 295 eindeutige angezeigte Titel nach Unicode-/Leerraum-/Großkleinschreibungsnormalisierung; 89 Deutsch- und 2 Sachunterrichtstitel konkretisiert. Titelzuordnung im isolierten JavaScript-Kontext ausgeführt und gegen alle 295 Karten geprüft. Alle IDs und Nicht-Titelfelder unverändert; Sachunterricht-Baseline bytegleich, Deutsch-Prüffortschritt unverändert. Quellenanker, Elternoperatoren und Stufenbänder der 160 Deutschkarten gültig; 117 Zielblöcke erhalten. Drei JavaScript-Blöcke syntaktisch geprüft; root/dist identisch, Datum 01.11.2026. Generatorüberschreibung erfolgt nach historischen Patches. Gleichwertige Node-Prüfung und Pages-Synchronisierung; Python auf dem Host nicht verfügbar, Python-Generator nicht ausgeführt. Liveprüfung auf GitHub Pages bestanden: Version 1.288 und Aktualisierungsdatum 01.11.2026 sichtbar; konkrete Deutsch-Titel DE-071, DE-072 und DE-073 in Auswahlliste und Kartenansicht sowie Sachunterricht-Titel SU-022 und SU-100 geprüft. Screenshot: live-1.288-titles.png (lokaler Prüfnachweis).


## Einzelprüfung DE-UZ-036 · App 1.290 · 01.11.2026

13 Zeilen in zwei zusammenhängenden Paketen geprüft: Wortschatzerweiterung (4) und Satzstrukturen (9). Davon 11 zuvor offen und 2 bereits zugeordnet. DE-102 ergänzt den Zwischenanker gesunde Ernährung und trennt den GS-Transfer der Oberbegriffsbildung von der FSP-Positionierung zu Ernährungsgewohnheiten. DE-108 konkretisiert GS-Zeichensetzung bei vorangestelltem Begleitsatz und begrenzt FSP auf einen ersten Zugang zum Erkennen und mündlichen Gebrauch wörtlicher Rede. Die bisher als Feinziel vorgegebene Rollenleseform ist entfernt; Methodenentscheidungen bleiben der Lehrkraft vorbehalten. Keine neuen Karten.

Zehn begründete Nichtanschlüsse: Assoziationen, lexikalische Mehrdeutigkeit, Satzteile, Subjekt, valenzbezogenes Prädikat, Wortgruppen als Satzstruktureinheit und die Verfahren Ersatz-/Umstell-/Weglassprobe einschließlich ihrer strukturierenden Oberzeile. Allgemeine Wortschatz-, Schriftstruktur- und Arbeitstechnikziele sind berücksichtigt; sie ersetzen keinen spezifischen Verfahrensnachweis. FSP-Pronomenersatz ist ein positiver Vorläufer, keine gleichwertige Ersatzprobe zur Satzanalyse.

Wortstämme (186811) bleiben als zusätzliche Anschlussfrage offen: Der FSP nennt sie ausdrücklich beim Lesen häufiger Wortbausteine. Der gemeinsame Ausschnitt mit GS-Wortschatzerweiterung und Stammschreibung benötigt noch genauere Eingrenzung und Kriterien; der positive Beleg wird nicht als fehlend ausgegeben.

Stand: 160 Karten; 158 Zeilen ohne Karte, davon 40 ohne Einzelprüfung, 107 dokumentierte Nichtanschlüsse und 11 offene Anschlussfragen. Kumulativ 201 zuvor offene und 39 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186843 „Verwenden von Bildungs- und Fachsprache“, GS Klasse 4. Der bereits zugeordnete GS3-Fachbegriffsblock 186828 ist nicht zusätzlich als einzelgeprüft gezählt. Nach offenen Zeilen folgen Unsicherheiten und die übrigen zugeordneten Unterziele. Belege und Restumfang: review_batch_036.json. Reproduktion: batch_036_review.py/batch_036_cards.json mit Refine-Hook und Quellensynchronisierung. Modul DE-2026-11-01.14. Eindeutige Kartentitel und verständliche Bezeichnung übergeordneter Lehrplanziele bleiben erhalten.

Validierung: PASS: 13 Zeilen geprüft (11 zuvor offen, 2 zuvor zugeordnet); 160 Karten und 117 Zielblöcke. Quellenanker, übergeordnete Ziele, Operatoren, Stufenbänder, Feinziele und Kriterien geprüft. Zwei Karten präzisiert; 158 übrige Karten und sämtliche IDs unverändert. Sachunterricht bytegleich; 295 eindeutige Kartentitel erhalten. Deutsch- und Titel-JSON korrekt eingebettet; drei JavaScript-Blöcke syntaktisch gültig; root/dist identisch, Datum 01.11.2026. CSV und Fortschritt konsistent: 40 offen, 107 Nichtanschlüsse, 11 Unsicherheiten; Fortsetzung page908_186843. Generator-Refine-Hook, Quellensynchronisierung und nachgelagerte Titel-/Begriffsbereinigung geprüft. Gleichwertige Node-Prüfung und Pages-Synchronisierung; Python auf dem Host nicht verfügbar, Python-Generator nicht ausgeführt. GitHub-Pages-Veröffentlichung für Commit 5392117cbcc650e1d47b5585508ddbd566243f3a erfolgreich. Liveprüfung bestanden: Version 1.290 und Datum 01.11.2026 sichtbar; DE-102 mit gesunder Ernährung, getrennten Operatoranforderungen und zusätzlichem Quellenanker 40354 geöffnet. DE-108 mit Übertragen/Einblick gewinnen, vorangestelltem Begleitsatz, fünf Quellenankern und ausdrücklicher Methodenfreiheit geöffnet. Screenshot lokal: live-1.290.png. Kein PDF-Download-Test.


## Einzelprüfung DE-UZ-037 · App 1.291 · 01.11.2026

14 Zeilen in drei Paketen geprüft: Fachsprache/Rückmeldung (4), Präsentieren (5), Zuhören (5). Davon 12 zuvor offen und 2 bereits zugeordnet. DE-013 trennt sicheren GS-Vortrag von vorbereitetem FSP-Lesen; DE-017 ergänzt aufmerksames Zuhören und nachbereitende Inhaltswiedergabe, ohne Absichts-/Strukturanalyse oder Schlussfolgerungen als gleichwertig zu behaupten. Literarischer Wunsch-/Traum-/Fantasiebezug und fachliche Kriterien sind ausdrücklich enthalten.

Drei neue Karten: DE-163 und DE-164 verbinden Fachwortgebrauch in zwei unterschiedlichen GS4-Kommunikationszielen mit dem ausdrücklichen FSP3/4-Unterziel Sachbegriffe verwenden im Kontext körperlicher Merkmale. Der gleiche Sachgegenstand ist kein zusätzlicher Inhalt, sondern ein getrennt ausgewiesener curricularer Zugang. DE-165 begrenzt Präsentationsstrategien auf Auswahl und Gliederung wesentlicher Inhalte eines Rollenbeitrags; tatsächliche Wahl von FSP-Wahlbereich 4 ist erforderlich. Sechs zuvor offene Zeilen erhalten begrenzte Zuordnungen.

Zwei begründete Nichtanschlüsse: Rückmeldungen zu Redebeiträgen sowie Vorbereitung des zielgerichteten Zuhörens. Vier zusätzliche Unsicherheiten: Umfang des Wortschatzes (186844), Visualisierung für Präsentationen (186860), Auswendiglerntechniken (186866) und Sichern/Weiterverwenden gehörter Informationen (186872). Die allgemeinen FSP-Grundlagen nennen Visualisierungs-, Präsentations- und Mnemotechniken ausdrücklich; diese positiven Belege werden gesichert, ohne einen Tabellenoperator oder eine stufenbezogene Vollentsprechung zu erfinden. Frühere GS3-Entscheidungen 186529/186555 sind für spätere Wiederprüfung mit den ergänzten Belegen vorgemerkt, in diesem Paket nicht erneut gezählt.

Stand: 163 Karten; 152 Zeilen ohne Karte, davon 28 ohne Einzelprüfung, 109 dokumentierte Nichtanschlüsse und 15 offene Anschlussfragen. Kumulativ 213 zuvor offene und 41 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186876 „Reflektieren über das Schreiben“, GS4. Weitere zugeordnete Gesprächszeilen wurden nicht zusätzlich als geprüft gezählt. Belege und Restumfang: review_batch_037.json. Reproduktion: batch_037_review.py/batch_037_cards.json; Append-/Refine-Hooks, stabile IDs DE-163–165 und Quellensynchronisierung. Modul DE-2026-11-01.15. Aufgaben/Lernhandlungen und Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Validierung: PASS: 14 Einzelzeilen (12 zuvor offen, 2 zuvor zugeordnet); 163 Deutschkarten, 117 Zielblöcke, gültige Quellenanker, übergeordnete Operatoren und Stufenbänder. Zwei bestehende Karten präzisiert, drei ergänzt; übrige 158 Karten und bestehende IDs unverändert. Sachunterricht bytegleich, 298 eindeutige Titel über beide Fächer. Deutsch- und Titel-JSON korrekt eingebettet; drei JavaScript-Blöcke syntaktisch geprüft; root/dist identisch, Datum 01.11.2026. CSV und Fortschritt konsistent: 28 offen + 109 Nichtanschlüsse + 15 Unsicherheiten = 152 Zeilen ohne Karte. Neue IDs eindeutig registriert; Append-/Refine-Hooks, Quellen- und Zeilensynchronisierung sowie nachgelagerte Titel-/Begriffsbereinigung geprüft. Gleichwertige Node-Prüfung und Pages-Synchronisierung; Python auf dem Host nicht verfügbar, Python-Generator nicht ausgeführt. GitHub-Pages-Veröffentlichung für Commit 75b8807b98f27a8f4714b0771093b782b4780449 erfolgreich. Liveprüfung bestanden: Version 1.291 sichtbar; DE-163/164/165 in GS4 Sprechen und Zuhören auswählbar. Beide Fachwortkarten zeigen ihre unterschiedlichen GS-Zielanker und den FSP-Sachbegriffsanker 40250; DE-165 zeigt den erforderlichen FSP-Wahlbereich 4 und die begrenzte Auswahl-/Gliederungsanforderung. Screenshot lokal: live-1.291.png. Kein PDF-Download-Test.


## Rückwärtsprüfung FSP-REVERSE-001 · Deutsch und Sachunterricht · 01.11.2026

Auf ausdrücklichen Nutzerwunsch wurde der Vergleich von GS Deutsch allein auf GS Deutsch 2026 und GS Sachunterricht 2019, jeweils Klassen 1–4, erweitert. Basis: main 84d84af499e91417eb84ddbc90fa6b96c97f9f87, App 1.291. Ergebnis und Quellenanker: [fsp_reverse_review_001.json](fsp_reverse_review_001.json).

Alle 22 FSP-Bereich-Band-Kombinationen wurden auf vollständig fehlende Gegenbezüge geprüft. In jedem Bereich ist mindestens ein sprachlicher oder sachlicher Gegenbezug feststellbar. Kein ganzer FSP-Lern- oder Wahlbereich ist damit als vollständig anschlusslos nachgewiesen. Das ist keine Feststellung vollständiger Abdeckung aller 451 Einzelzeilen. Die vier zuvor im Deutschmodul unreferenzierten Bereiche sind im kombinierten Vergleich keine pauschalen Lehrplanlücken.

Konkrete Einschränkungen bleiben: Unterschrift ohne eigenständigen spezifischen GS-Zielanker; familiäre Strukturen/Aufgabenverteilung nur teilweise durch historischen Familienvergleich; Nutzholz und Herstellungsweg nur unter passenden Wahlbedingungen; basale FSP3/4-Anforderungen mit GS1/2-Gegenankern; Buchherstellung im FSP verbindlich innerhalb des Wahlbereichs, im GS-Deutsch-Präsentationsbereich konkretes Buchformat nur als Bemerkungsbeispiel. Allgemeine Sprachziele ersetzen kein Sachwissen. Gleicher Gegenstand ersetzt keine Prüfung der Operatoren. Einzelbefunde und Restumfang sind im JSON getrennt ausgewiesen.

Gezielte Node-Validierung bestanden: Bereichszahl, Inventurumfang, IDs, Klassen/Bänder, übergeordnete Ziele, FSP-/Deutsch-Quellenanker und elf Ausgangsdateien gegen aktuelle Git-Blob-SHAs geprüft. GS-Sachunterricht anhand amtlicher Webquelle und vorhandener Inventur gegengeprüft. Reine Auditänderung: keine Karten-/App-Änderung, keine Versionssteigerung, keine Aufgaben-/Hilfsmittelvorschläge. Der Vorwärtsfortschritt bleibt DE-UZ-037 mit 28 offenen Zeilen, 15 Anschlussfragen und Fortsetzung page908_186876. Die Bereichsprüfung zählt keine neuen Einzelprüfungen.


## Einzelprüfung DE-UZ-038 · App 1.292 · 01.11.2026

Die bisherige GS-Deutsch-Unterzielprüfung wird fortgeführt. Auf ausdrücklichen Nutzerwunsch erfolgt keine Einzelprüfung für den zusätzlichen Rückwärtsvergleich FSP-REVERSE-001; dessen Bereichsergebnis bleibt bestehen.

10 zuvor offene Zeilen in zwei Paketen geprüft: Schreiben (6) und Lesen (4). Drei Karten ergänzt: DE-166 digitale Mitteilung mit GS4-Beherrschen gegenüber FSP3/4-Kennen; DE-167 textfunktions- und adressatenbezogene Planung einer Einladung mit FSP-Anwenden; DE-168 eigene Fantasieidee in einer Geschichtenfortsetzung mit GS-Schriftlichkeit und FSP-Einblick ohne vorgeschriebene Darstellungsform. Vier zuvor offene Zeilen erhalten begrenzte Anschlüsse.

Vier dokumentierte Nichtanschlüsse: kooperatives Schreiben, passende Leseförderverfahren, Vorbereitung des Lesens und Formulieren von Texterwartungen. Allgemeine Kooperations-, Lese- und Lernstrategien wurden berücksichtigt; sie belegen diese engeren Verfahren nicht automatisch. Zwei zusätzliche Anschlussfragen bleiben offen: Reflexion von Lesbarkeit/Flüssigkeit unter Berücksichtigung der FSP-Lernergebniskontrolle sowie Textsortenklärung als vorbereitende Lesestrategie unter Berücksichtigung des FSP-Textartenwissens.

Stand: 166 Karten; 148 Unterziele ohne Karte, davon 18 ohne Einzelprüfung, 113 dokumentierte Nichtanschlüsse und 17 Anschlussfragen. Kumulativ 223 zuvor offene und unverändert 41 zuvor zugeordnete Zeilen geprüft. Fortsetzung: page908_186928 „Herstellen von Bezügen zwischen Text, Bild und Ton bei digitalen Texten“, GS4. Belege und Restumfang: review_batch_038.json. Reproduktion: batch_038_review.py/batch_038_cards.json, Append-/Refine-Hooks und stabile IDs DE-166–168. Modul DE-2026-11-01.16. Aufgaben/Lernhandlungen und Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Validierung: PASS: 10 zuvor offene Unterziele einzeln geprüft; 166 Deutschkarten und 117 Zielblöcke. Drei Karten ergänzt; alle 163 bestehenden Karten und IDs unverändert. Quellenanker, übergeordnete Ziele, Operatoren, Bänder, Feinziele und Kriterien gültig. Sachunterricht und Inventuren bytegleich; 301 eindeutige Kartentitel. Deutsch-/Titel-JSON korrekt eingebettet, drei JavaScript-Blöcke syntaktisch gültig; root/dist identisch mit Datum 01.11.2026. CSV und Fortschritt konsistent: 18 offen + 113 Nichtanschlüsse + 17 Anschlussfragen = 148 Unterziele ohne Karte. Die 23 separat abgegrenzten übergeordneten Zielblöcke werden nicht als Unterziele mitgezählt. Fortsetzung page908_186928. Neue IDs, Append-/Refine-Hooks und Quellensynchronisierung geprüft. prepare-pages.py wegen fehlender Python-Laufzeit/Xcode-Werkzeuge nicht ausführbar; gleichwertige Node-Synchronisierung und Prüfungen entsprechend check-deutsch.py/prepare-pages.py durchgeführt. Python-Generator nicht ausgeführt. GitHub-Pages-Veröffentlichung für Commit eed77f7ad8b223171d0cba316d3aaebd766e5951 erfolgreich. Liveprüfung bestanden: Version 1.292 und Datum 01.11.2026 sichtbar. DE-166, DE-167 und DE-168 in GS4 Schreiben auswählbar und geöffnet; Beherrschen/Kennen, Beherrschen/Anwenden und Beherrschen/Einblick gewinnen korrekt angezeigt. Quellenanker und Restbegrenzungen einschließlich fehlender FSP-Schriftvorgabe bei der Fantasiegeschichte sichtbar. Screenshot lokal: live-1.292.png. Kein PDF-Download-Test.


## Einzelprüfung DE-UZ-039 · App 1.293 · 01.11.2026

Fortsetzung der bisherigen GS-Deutsch-Unterzielprüfung; keine Einzelprüfung des zusätzlichen Rückwärtsvergleichs FSP-REVERSE-001. Zehn zuvor offene GS4-Zeilen in zwei Paketen geprüft: Lesen (3) und Texte/Medien (7).

Drei begrenzte Anschlüsse ergänzt: DE-169 eigenes Buch als sichere Textpräsentation (GS4 Beherrschen / FSP1/2 Anwenden, Wahlbereich 2 erforderlich); DE-170 eigene digitale Freizeiterfahrungen beschreiben und einordnen (GS4 Übertragen / FSP3/4 Sich positionieren); DE-171 Merkmale eines schriftlichen Glückwunsches (GS4 Kennen / FSP3/4 Anwenden). Der Glückwunsch muss für GS4 das bereits erarbeitete Textrepertoire erweitern; diese Lernstandsvoraussetzung ist ausdrücklich ausgewiesen. Unterschiedliche Operatoren werden durch getrennte Feinziele und Kriterien erhalten.

Fünf begründete Nichtanschlüsse: digitale Text-Bild-Ton-Bezüge, Navigationsstrukturen beim Lesen, Bewertung sprachlicher Mittel, Merkmale auditiver/audiovisueller/digitaler Textformen und Bezüge zwischen unterschiedlichen Texten. Medienzugang, Gerätebedienung, Figurenbewertung und Inhaltswiedergabe werden nicht mit diesen engeren Anforderungen gleichgesetzt. Zwei zusätzliche offene Anschlussfragen: Glaubwürdigkeit/Aussagekraft von Informationen (186971) sowie kritischer Informationsumgang mit Rechten und Identitätsschutz (186993). Die ausdrücklichen positiven Grundlagen- und Bemerkungsbelege sind gesichert, ohne daraus einen selbstständigen Tabellenoperator zu erfinden.

Stand: 169 Karten; 145 Unterziele ohne Karte, davon 8 ohne Einzelprüfung, 118 dokumentierte Nichtanschlüsse und 19 Anschlussfragen. Kumulativ 233 zuvor offene und unverändert 41 zuvor zugeordnete Zeilen geprüft. Die 23 separat abgegrenzten übergeordneten Zielblöcke sind nicht in der Unterzielzahl enthalten. Fortsetzung: page908_187013 „Untersuchen verschiedener Perspektiven“, GS4. Nach den offenen Zeilen folgen Anschlussfragen und die verbleibenden bereits zugeordneten Unterziele. Belege und Restumfang: review_batch_039.json. Reproduktion: batch_039_review.py/batch_039_cards.json, Append-/Refine-Hooks, stabile IDs DE-169–171; Modul DE-2026-11-01.17. Aufgaben/Lernhandlungen und Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Validierung: PASS: 10 zuvor offene Unterziele einzeln geprüft; 169 Deutschkarten, 117 Zielblöcke. Drei neue Karten; alle 166 bisherigen Karten und IDs unverändert. Quellenanker, übergeordnete Operatoren, Bänder, Feinziele und Kriterien geprüft. Sachunterricht, Inventuren und Quellen bytegleich; 304 eindeutige Kartentitel. Deutsch- und Titel-JSON korrekt eingebettet; drei JavaScript-Blöcke syntaktisch geprüft. root/dist identisch, App 1.293, Datum 01.11.2026. CSV und Fortschritt konsistent: 8 offen + 118 Nichtanschlüsse + 19 Anschlussfragen = 145 Unterziele ohne Karte. Fortsetzung page908_187013. Reproduktionshooks und stabile IDs geprüft. Gleichwertige Node-Prüfungen und Pages-Synchronisierung entsprechend check-deutsch.py/prepare-pages.py; Python auf diesem Host nicht verfügbar, Python-Generator nicht ausgeführt. GitHub-Pages-Veröffentlichung für Commit 307669f0714a3ec2d875a86427ab476616ab711d erfolgreich (Workflow 41326870952). Liveprüfung bestanden: App 1.293 und Aktualisierungsdatum 01.11.2026 sichtbar; alle drei neuen Karten in GS4 Texte/Medien auswählbar und geöffnet. DE-169 zeigt Beherrschen/Anwenden und FSP1/2-Wahlbereich 2; DE-170 Übertragen/Sich positionieren und den begrenzten Freizeitkontext; DE-171 Kennen/Anwenden und die Voraussetzung eines erweiterten GS-Textrepertoires. Quellen und Restbegrenzungen sichtbar. Screenshot lokal: live-1.293.png. Kein PDF-Download-Test.


## Einzelprüfung DE-UZ-040 · Audit ohne App-Änderung · 01.11.2026

Die letzten acht bislang offenen Unterzielzeilen in GS4 Sprache und Sprachgebrauch wurden in zwei Paketen einzeln geprüft: Kommunikation/Wortarten (6), Satzstrukturen (2). Das ist ein Abschluss der Phase offener Zeilen, kein Abschluss des gesamten Abgleichs. Keine Einzelprüfung des Rückwärtsvergleichs FSP-REVERSE-001.

Fünf dokumentierte Nichtanschlüsse: die gliedernde Verbzeile mit ihren weiteren Merkmalen, Perfekt/Futur I, zweiteilige Verbformen mit Hilfsverben, zusätzliche satzbezogene Formveränderung von Nomen sowie Untersuchung von Ergänzungen gegenüber Subjekt/Prädikat. Basale Verbbeugung, Artikelzuordnung, Pluralbildung oder einfache Satzmuster werden nicht als Nachweis der spezielleren GS4-Anforderungen gewertet. Der Rechtschreibrahmen 2025 wurde zur Abgrenzung von Nominalgruppenerweiterung, Satzgliedern und Formverwendung einbezogen; seine fachlichen Erläuterungen erzeugen keine zusätzlichen FSP-Ziele.

Drei zusätzliche offene Anschlussfragen: Perspektiven in mündlicher/schriftlicher Kommunikation (187013), Wörter und Wendungen für Zeitstufen (187030), satzbezogenes experimentelles/kreatives Sprachhandeln (187036). Positive Belege wie Verständnis für Probleme anderer, temporale Adverbien und Sprachspiele bleiben mit ihrem jeweiligen Sachkontext dokumentiert; ein hinreichend bestimmter Kartenanschluss wird daraus noch nicht behauptet. Belege und Einzelbegründungen: review_batch_040.json. Keine neuen Karten, Feinziele, Aufgaben oder Hilfsmittel.

Stand: 169 Karten; keine bislang ungeprüften offenen Unterzielzeilen mehr. Von 145 Unterzielen ohne Karte sind 123 als Nichtanschlüsse dokumentiert und 22 Anschlussfragen offen. Kumulativ 241 zuvor offene und unverändert 41 zuvor zugeordnete Zeilen einzeln geprüft. Außerdem sind 89 bereits zugeordnete Unterzielzeilen noch nicht einzeln geprüft. Die 23 separat abgegrenzten übergeordneten Zielblöcke werden nicht als Unterziele mitgezählt. Nächste Phase: Anschlussfragen in Inventurreihenfolge, beginnend page908_186437 „Ziehen einfacher Schlussfolgerungen“, GS1/2. Danach verbleibende bereits zugeordnete Unterziele. App unverändert 1.293, Modul DE-2026-11-01.17.

Validierung: PASS: Acht zuvor offene Zeilen einzeln geprüft; CSV enthält keine Zeile mit Einzelprüfung offen mehr. 241 zuvor offene und 41 zuvor zugeordnete Zeilen dokumentiert. 145 Unterziele ohne Karte = 123 Nichtanschlüsse + 22 offene Anschlussfragen; weitere 89 zugeordnete Unterziele noch einzeln zu prüfen. Fortsetzung page908_186437, Phase uncertain_connections, Gesamtprüfung nicht abgeschlossen. Quellenanker, übergeordnete Operatoren und FSP-Bänder geprüft. Nur acht CSV-Entscheidungstexte geändert; Karten-/Zuordnungsfelder unverändert. Alle 169 Karten, IDs, Modul, Generator, Inventuren, amtliche Quellen, Sachunterricht und root/dist bytegleich. Gleichwertige Node-Daten-, Quellenanker-, Syntax- und Regressionstests nach check-deutsch.py bestanden; drei JavaScript-Blöcke gültig. Python auf diesem Host nicht verfügbar. Keine App-Änderung und deshalb keine neue App-Version oder Pages-Aufbereitung erforderlich.


## Einzelprüfung DE-UZ-041 · App 1.294 · 01.11.2026

Zehn vorhandene Anschlussfragen erneut geprüft, nicht als neue Erstprüfungen gezählt. Neun Fragen sind für ausdrücklich begrenzte Zielausschnitte geklärt. Drei Karten ergänzt: DE-172 Verstehen einer anderen Sicht im Freundschaftsgespräch (GS3 Übertragen / FSP3/4 Sich positionieren); DE-173 Sinn eines Sprichwortes im Getreide-/Erntekontext (beide Kennen, unterschiedliche sprachliche bzw. sachliche Nachweise); DE-174 Nomen für nichtgegenständliche Erscheinungen (beide Kennen, GS-Abstraktum gegenüber FSP-Erscheinungsbezeichnung). DE-174 ordnet die gliedernde Nomenzeile und Abstrakte gemeinsam, jedoch nur im Ausschnitt Nichtgegenständliches, zu. Gefühle als Nomenklasse bleiben außerhalb.

Fünf übergreifende Teilanschlüsse sind positiv gesichert: 186437 einfache Schlussfolgerungen GS1/2 ↔ FSP3/4; 186452 Entwicklung von Lesefreude GS1/2 ↔ FSP1/2; 186705 interpretierender Ausschnitt über textbezogene Wertungen/Schlussfolgerungen; 186706 Schlussfolgerungen mit zusätzlicher, getrennt ausgewiesener GS-Begründungsanforderung; 186727 Vertiefung von Lesefreude/Interesse. Die letzten drei betreffen GS3 ↔ FSP3/4. Fachliche Gegenstände, didaktisch konkretisierte Feinziele/Kriterien und Restumfang stehen in review_batch_041.json. Motivationsentwicklung wird nicht aus einer einzelnen Leistung oder bloßer Teilnahme abgeleitet oder benotet.

Diese fünf Zeilen erhalten bewusst keine Operatorenkarte: Ihr FSP-Beleg ist ein übergreifendes Stufenbandziel ohne tabellarischen Operator. Das vorhandene Kartenmodell verlangt hingegen einen konkreten Tabellenzielanker. Kein Kennen oder Übertragen wird aus einem anderen Tabellenziel geliehen. Der gesicherte curriculare Teilanschluss wird deshalb in review_progress.json unter overarching_connection_ids und documented_overarching_connection_without_card sowie in row_audit.csv gesondert ausgewiesen. Fehlende Karte bedeutet hier ausdrücklich keinen fehlenden Anschluss. Die Zielblöcke und ihre uncovered_child_ids bleiben eine Karteninventur und werden nicht in eine behauptete curriculare Vollabdeckung umgedeutet.

186659 Selbstkontrolle bleibt offen: Die Zwischenzeile verlangt Verwendung von Rückmeldungen bei Textprüfung. Allgemeine Kontrolle von Lernergebnissen allein klärt diesen engeren Zusammenhang nicht. Die Frage wird nicht durch bloße Umbenennung in einen übergreifenden Anschluss als erledigt markiert. Fortsetzung zunächst bei den noch nicht erneut geprüften Anschlussfragen ab page908_186811 „Erkennen von Wortstämmen“; anschließend verbleibende Rückfragen einschließlich 186659.

Stand: 172 Karten; 141 Unterziele ohne Karte = 123 dokumentierte Nichtanschlüsse + 13 Anschlussfragen + 5 gesicherte übergreifende Teilanschlüsse ohne Karte. 241 zuvor offene und 41 zuvor zugeordnete Zeilen erstmals geprüft; zusätzlich jetzt 10 dokumentierte Wiederprüfungen von Anschlussfragen. 89 bereits zugeordnete Unterzielzeilen bleiben noch einzeln zu prüfen. Gesamtprüfung nicht abgeschlossen. Keine Rückwärts-Einzelprüfung. Sachunterricht und bisherige Karten erhalten; Aufgaben/Lernhandlungen und Hilfsmittel weiterhin ausschließlich Lehrkraftentscheidung. Reproduktion: batch_041_review.py/batch_041_cards.json mit Append-/Refine-Hooks, IDs DE-172–174; Modul DE-2026-11-01.18.

Validierung: PASS: Zehn vorhandene Anschlussfragen erneut geprüft, neun begrenzt geklärt; keine Doppelzählung als neue Unterzielzeilen. Drei Karten ergänzt für vier Zeilen; fünf übergreifende Teilanschlüsse ohne erfundenen Tabellenoperator gesondert gezählt; 186659 bleibt offen. 172 Deutschkarten, 117 Zielblöcke, gültige Anker/Operatoren/Bänder und getrennte Feinziele/Kriterien. Alle 169 bisherigen Karten und IDs, Inventuren, Quellen und Sachunterricht unverändert. 307 eindeutige Kartentitel; Deutsch-/Titel-JSON korrekt eingebettet, drei JavaScript-Blöcke syntaktisch gültig, root/dist identisch mit App 1.294 und Datum 01.11.2026. 141 Unterziele ohne Karte = 123 Nichtanschlüsse + 13 Anschlussfragen + 5 gesicherte übergreifende Teilanschlüsse. 89 zugeordnete Unterziele weiterhin ungeprüft. Reproduktionshooks, Registry, Quellensynchronisierung und Fortsetzung 186811 geprüft. Python auf diesem Host nicht verfügbar; gleichwertige Node-Prüfungen und Pages-Synchronisierung nach check-deutsch.py/prepare-pages.py durchgeführt. Python-Generator nicht ausgeführt. GitHub Pages für Commit d5f6b74dcda01e7e3c696f394386ca09ad2024d1 erfolgreich veröffentlicht (Workflow 41332878724). Liveprüfung: Version 1.294 sichtbar; DE-172 in GS3 Sprechen/Zuhören und DE-173/174 in GS3 Sprache/Sprachgebrauch auswählbar und geöffnet. Operatoren Übertragen/Sich positionieren sowie Kennen/Kennen, Quellenanker, Erntekontext und Begrenzung auf nichtgegenständliche Erscheinungen korrekt angezeigt. Aufgaben-/Hilfsmittelfelder nicht befüllt. Screenshot lokal live-1.294.png. Kein PDF-Download-Test.


## Einzelprüfung DE-UZ-042 · Audit ohne App-Änderung · 01.11.2026

Zehn vorhandene Anschlussfragen erneut geprüft, keine neuen Erstprüfungen gezählt. Vier begrenzte übergreifende Teilanschlüsse gesichert: Wortschatzbreite (186844), Visualisierung zur Präsentation (186860), Gedächtnistechniken (186866) und prüfender Umgang mit medialen Informationen (186971). Getrennte Feinziele, Kriterien und Restumfang stehen in review_batch_042.json.

Wortschatzbreite ist im fachlichen FSP-Stufenbandziel 3/4 verankert. Die drei methodischen Anschlüsse stützen sich dagegen auf allgemeine Schulartziele im Abschnitt Lernen lernen bzw. Medienbildung. Deren Konkretisierung in 3/4 wird nicht als wörtliches Stufenbandziel oder identisches GS4-Leistungsniveau ausgegeben. Kein Tabellenoperator wird geliehen; deshalb keine neue Operatorenkarte. Aufgaben und Hilfsmittel werden nicht vorgeschlagen.

Ein begründeter Nichtanschluss ist nun entschieden: Textsortenklärung als vorbereitende Lesestrategie (186926). FSP-Textartenkenntnis bleibt ausdrücklich anerkannt; der genaue vorbereitende Strategiegebrauch ist in den geprüften Quellen nicht hinreichend belegt. Fünf Fragen dieses Pakets bleiben offen: Wortstammfunktion, Weiterverwendung gehörter Informationen, Reflexion von Lesbarkeit/Flüssigkeit, digitaler Rechtebezug und Untersuchung von Perspektiven. Neue Gegenprüfungen berücksichtigen insbesondere Befragung und gezieltes Fragen bei öffentlichen Einrichtungen, die Trennung von Schreibprozess und Schriftprodukt sowie weitere Rechtebemerkungen. Die GS-Perspektivzeile wird nicht durch eine unbelegte Pflicht zu formaler linguistischer Analyse verschärft.

Stand: 172 Karten; 141 Unterziele ohne Karte = 124 dokumentierte Nichtanschlüsse + 8 offene Anschlussfragen + 9 gesicherte übergreifende Teilanschlüsse. Weiterhin 241 zuerst offene und 41 zuvor zugeordnete Zeilen erstmals geprüft; 89 bereits zugeordnete Zeilen noch einzeln zu prüfen. Insgesamt sind jetzt 20 unterschiedliche bestehende Anschlussfragen erneut geprüft. Zusätzlich ist eine Quellen-Nachprüfung des verwandten GS3-Auswendiglernfalls 186555 vorgemerkt und separat gezählt. Keine Rückwärts-Einzelprüfung.

Fortsetzung: page908_187030, anschließend 187036, danach verbliebene Anschlussfragen, die vorgemerkte Quellen-Nachprüfung und die noch nicht einzeln geprüften Kartenzeilen. Gesamtprüfung nicht abgeschlossen. App unverändert 1.294, Modul DE-2026-11-01.18; keine Versionssteigerung.

Validierung: PASS: Zehn bestehende Anschlussfragen erneut geprüft, vier begrenzte übergreifende Teilanschlüsse und ein begründeter Nichtanschluss geklärt. Fünf in diesem Paket weiterhin offen. 172 Karten, 117 Zielblöcke; alle Quellenanker, Operatoren, Bänder, Feinziele und Kriterien der bestehenden Karten gültig. 307 eindeutige Kartentitel. Inventuren (488 GS-/451 FSP-Zeilen), Quellenprüfsummen, Sachunterricht, Registry, Generator, Modul und root/dist gegenüber main unverändert. Drei eingebettete JavaScript-Blöcke syntaktisch gültig; Daten vollständig eingebettet. Zehn CSV-Prüftexte geändert, alle Zuordnungs- und Quelldatenfelder erhalten. 241 Erstprüfungen, 41 Prüfungen zuvor zugeordneter Zeilen; keine Doppelzählung der Wiederprüfungen. 141 Unterziele ohne Karte = 124 Nichtanschlüsse + 8 offene Anschlussfragen + 9 gesicherte übergreifende Teilanschlüsse. 89 zugeordnete Zeilen ungeprüft, eine gesonderte Quellen-Nachprüfung 186555 vorgemerkt. Fortsetzung 187030. Gleichwertige Node-Prüfungen gemäß check-deutsch.py; Python-Aufruf scheitert an fehlenden Xcode-Werkzeugen. Keine App-Änderung, keine künstliche Versionssteigerung und keine Pages-Aufbereitung erforderlich.


## Einzelprüfung DE-UZ-043 · App 1.295 · 01.11.2026

Zehn unterschiedliche Zeilen geprüft: die acht verbliebenen Anschlussfragen, die vorgemerkte Quellen-Nachprüfung 186555 und die benachbarte bereits zugeordnete Handschriftzeile 186875. Fünf eng begrenzte Karten DE-175–179 ergänzt: Wortstammwiedererkennung mit getrenntem GS-Wortschatz- und FSP-Lesenachweis; mündliche Auskunft zu einer öffentlichen Einrichtung; Rechte an fremden Bildern/Texten in digitaler Schulfestinformation; Vergleich begründeter Sichtweisen im Freundschaftskonflikt; zusätzliche Zeitwörter zur Ernte früher/heute.

Die Kriterien erhalten die unterschiedlichen Operatoren. Bei DE-176 muss GS4 die gehörte Information tatsächlich weiterverwenden; FSP3/4 bleibt beim Einblick in die Einrichtung. DE-177 wahrt den Schulfestkontext und behandelt die digitale Form auf FSP-Seite als didaktische Konkretisierung. DE-178 deckt einen mündlichen Perspektivvergleich, nicht zugleich schriftliche Perspektivgestaltung. DE-179 deckt Vergangenheit/Gegenwart nur bei nachgewiesen erweitertem GS-Wortrepertoire; Zukunft ist ausdrücklich nicht abgedeckt.

Zwei weitere übergreifende Teilanschlüsse ohne Operatorenkarte: Reflexion eigener Lesbarkeit (186876, Flüssigkeitsreflexion außerhalb) und bewusste Nutzung einer Gedächtnistechnik (186555). Die frühere negative Einordnung zu 186555 wird für diesen übergreifenden Ausschnitt korrigiert. Zwei begründete Nichtanschlüsse sind entschieden: rückmeldungsbezogene Selbstkontrolle bei Textüberarbeitung (186659) und satzbezogenes kreatives Sprachhandeln (187036). Allgemeine Kontrolle bzw. kreative Sprache im FSP bleiben ausdrücklich anerkannt; die genaueren GS-Funktionen sind damit nicht automatisch belegt.

DE-021 präzisiert als einzige bestehende Karte die Unterscheidung zwischen individueller GS-Handschrift und FSP-Schulausgangsschrift. Lesbarkeit wird am Produkt, Flüssigkeit am Prozess betrachtet; eine durchgehend verbundene GS-Schreibspur ist nicht zwingend. Aufgaben/Lernhandlungen und Hilfsmittel bleiben ausschließlich Lehrkraftentscheidung.

Stand: 177 Karten; 136 Unterziele ohne Karte = 125 dokumentierte Nichtanschlüsse + 11 gesicherte übergreifende Teilanschlüsse. Keine offene Anschlussfrage und keine vorgemerkte Quellen-Nachprüfung mehr in dieser Phase. Dies ist kein Abschluss des gesamten Abgleichs: 88 bereits zugeordnete Unterzielzeilen stehen noch zur Einzelprüfung an. 241 zuerst offene und 42 zuvor zugeordnete Zeilen erstmals geprüft; neun Wiederprüfungen dieses Pakets separat. Alle 22 bisher erfassten Anschlussfragen haben nun eine begrenzte Entscheidung. Die 22 übergeordneten Zielblöcke ohne Karte werden nicht als Unterziele mitgezählt. Fortsetzung: page908_186273 Erzählen (GS1/2), Phase previously_assigned_rows. Keine Rückwärts-Einzelprüfung.

Reproduktion: batch_043_review.py/batch_043_cards.json, Append-/Refine-Hooks, Registry DE-175–179; Modul DE-2026-11-01.19.

Validierung: PASS: Zehn unterschiedliche Zeilen geprüft: acht Anschlussfragen, eine Quellen-Nachprüfung und eine zuvor zugeordnete Zeile. 177 Deutschkarten, 117 Zielblöcke, 312 eindeutige Titel. Fünf neue Karten DE-175–179; ausschließlich DE-021 unter den bisherigen 172 Karten fachlich geändert, alle IDs erhalten. Ziele, Operatoren, Bänder, Quellenanker, getrennte Feinziele/Kriterien und Reproduktionshooks geprüft. Keine Aufgaben- oder Hilfsmittelvorschlagsfelder. Inventuren, amtliche Quellen, Sachunterricht und Titeldatei unverändert; Deutschdaten korrekt eingebettet. Drei JavaScript-Blöcke syntaktisch gültig. 136 Unterziele ohne Karte = 125 Nichtanschlüsse + 11 übergreifende Teilanschlüsse, keine offene Anschlussfrage; 22 gesonderte übergeordnete Blöcke ohne Karte. 241 zuerst offene Zeilen und 42 zuvor zugeordnete Zeilen erstmals geprüft; Wiederprüfungen nicht doppelt gezählt. 88 zugeordnete Unterziele verbleiben; Fortsetzung 186273. CSV-Quelldaten erhalten, alle Kartenzuordnungen exakt; zehn neue Einzelprüftexte und sechs reine Ankervermerke. Gleichwertige Node-Daten-, Quellenanker-, Syntax- und Regressionstests nach check-deutsch.py sowie Pages-Aufbereitung nach prepare-pages.py bestanden. Python auf diesem Host nicht verfügbar (fehlende Xcode-Werkzeuge); Python-Generator nicht ausgeführt. Root und dist werden bytegleich mit App 1.295, Modul DE-2026-11-01.19 und Datum 01.11.2026 gespeichert.

Veröffentlichung und Liveprüfung: GitHub Pages veröffentlichte Commit 4e7a121a47b7329c7dba37b5d8ad83a33c690365 erfolgreich (Workflow 41344565023). Liveprüfung: App 1.295 und Aktualisierungsdatum 01.11.2026 sichtbar. DE-175 in GS3 Sprache/Sprachgebrauch, DE-176 in GS4 Sprechen/Zuhören, DE-177 in GS4 Texte/Medien sowie DE-178/179 in GS4 Sprache/Sprachgebrauch ausgewählt und geöffnet. Operatoren Übertragen/Übertragen, Beherrschen/Einblick gewinnen, Übertragen/Sich positionieren und Kennen/Kennen sowie Quellenanker und Restbegrenzungen korrekt angezeigt. DE-021 in GS4 Schreiben geöffnet: unterschiedliche Handschriftanforderungen und Prozessbezug sichtbar. Keine Planungsfelder befüllt. Kein PDF-Download-Test. 125 verfügbare Repository-Dateien nach dem Speichern bytegenau gegen GitHub-Blobs geprüft, einschließlich binärer amtlicher PDF-Quelle.

## Einzelprüfung DE-UZ-044 · App 1.296 · 02.11.2026

Zwölf zuvor zugeordnete GS1/2-Zeilen erstmals einzeln geprüft: Erzählen (186273), Körperhaltung (186282), Stimmeinsatz (186283), wertschätzende Gesprächsatmosphäre (186293), Textvortrag (186297), Aufbau von Hörverstehen (186303), Höraufträge (186307), angeleitete Informationssicherung (186312), differenzierte Wahrnehmung (186317), optisch-graphomotorische (186318) und auditive Wahrnehmung (186320) sowie Druckschrift als Erstschrift (186326). Sieben vorhandene Karten präzisiert; keine neue Karte oder ID.

DE-001 hält den GS-Einblick in das Erzählen vom FSP3/4-Positionieren zum Klassenleben getrennt; alternative FSP1/2-Belege sind dokumentiert. DE-003 heißt nun „Theaterspiel: Körperhaltung und Lautstärke“. Der FSP-Wahlbereich belegt Körpersprache und Lautstärke; Tempo und Betonung werden nicht aus Rhythmus/Melodie gleichgesetzt. DE-006 bindet Höflichkeitsformen an die respektvolle Gesprächsatmosphäre. DE-011 verlangt beim Jahreszeitengedicht auch den FSP-Zeitbezug.

DE-015 deckt Hörauftragsbezug und angeleitete inhaltliche Nachbereitung weiterhin begrenzt ab. 186303 wurde jedoch aus der Karte entfernt: Die amtliche Hierarchie ordnet „Aufbauen von Hörverstehen“ dem Zwischenziel „Vorbereiten des Zuhörens“ zu. Aktives Zuhören und Inhaltswiedergabe belegen noch nicht eindeutig diese vorbereitende Funktion. Die positive FSP-Hörkompetenz bleibt anerkannt; dokumentiert ist eine offene Anschlussfrage, kein pauschaler Nichtanschluss. Diese Frage ist als Nächstes zu klären.

DE-018 trennt GS-Kennen der unverbundenen Erstschrift vom FSP-Übertragen bekannter Laut-Buchstaben-Beziehungen; bloßes Abschreiben genügt dem Transfer nicht. DE-115 berücksichtigt das ausdrücklich entwicklungsbezogene Zwischenziel: auditive Differenzierung, visuelle Formwahrnehmung und Auge-Hand-Koordination sind eigene Nachweise, bezogen auf die individuelle Entwicklung. Aufgaben/Lernhandlungen und Hilfsmittel bestimmt ausschließlich die Lehrkraft.

Stand: 177 Karten; 137 Unterziele ohne Karte = 125 dokumentierte Nichtanschlüsse + 11 übergreifende Teilanschlüsse + 1 Anschlussfrage. 241 ursprünglich offene und 54 zuvor zugeordnete Zeilen erstmals geprüft. Noch 76 zugeordnete Zeilen einzeln zu prüfen. Fortsetzung zunächst page908_186303, danach page908_186328 (zunehmend flüssiges Schreiben). Die 22 übergeordneten Zielblöcke ohne Karte werden gesondert geführt. Keine Rückwärts-Einzelprüfung.

Reproduktion: batch_044_review.py/batch_044_cards.json mit sieben Refine-Patches; Kartenzielabdeckung nach allen historischen Patches neu berechnet, damit zurückgenommene Zuordnungen nicht fortbestehen. Zentrale Titeldatei nur für DE-003 geändert; ID-Registry unverändert.

Validierung: PASS: Zwölf zuvor zugeordnete Zeilen erstmals einzeln geprüft, elf begrenzte Anschlüsse präzisiert und eine Anschlussfrage offengelegt. 177 Deutschkarten und 117 Zielblöcke; nur DE-001/003/006/011/015/018/115 verändert, alle IDs erhalten. Keine Aufgaben- oder Hilfsmittelvorschlagsfelder. Ziele, Operatoren, Bänder, Quellenanker, Zwischenkontext 186301/186303, getrennte Feinziele/Kriterien und Reproduktionshooks geprüft. 312 eindeutige Anzeigetitel; zentral ausschließlich DE-003 präzisiert. Amtliche Quellen, Inventuren, ID-Registry und Sachunterricht unverändert. Deutsch- und Titeldaten korrekt eingebettet; drei JavaScript-Blöcke syntaktisch gültig. CSV-Quelldaten erhalten, zwölf Prüftexte aktualisiert, allein die Kartenreferenz zu 186303 entfernt. 137 Unterziele ohne Karte = 125 Nichtanschlüsse + 11 übergreifende Teilanschlüsse + 1 Anschlussfrage. 241 zuerst offene und 54 zuvor zugeordnete Zeilen erstmals geprüft; 76 zugeordnete Unterziele verbleiben. 22 gesonderte übergeordnete Blöcke ohne Karte. Fortsetzung zuerst 186303, danach 186328. Gleichwertige Node-Daten-, Quellenanker-, Syntax- und Regressionstests nach check-deutsch.py und Pages-Aufbereitung nach prepare-pages.py bestanden. Python auf diesem Host nicht verfügbar (fehlende Xcode-Werkzeuge); Python-Generator nicht ausgeführt. Root und dist werden bytegleich mit App 1.296, Modul DE-2026-11-02.1 und Datum 02.11.2026 gespeichert.

Veröffentlichung und Liveprüfung: GitHub Pages veröffentlichte App-Commit e25a01f0b076581a1b5c60608b0313b410818aed erfolgreich (Workflow 41406578192). Liveprüfung: App 1.296 und Datum 02.11.2026 sichtbar. Alle sieben präzisierten Karten DE-001/003/006/011/015/018/115 in GS1/2 ausgewählt und geöffnet. Neuer Titel „Theaterspiel: Körperhaltung und Lautstärke“, Wahlbereichs- und Stufenbandgrenze, unterschiedliche Operatoren, zusätzliche Quellenanker, vorbereitende Abgrenzung der Hörkarte und getrennte Entwicklungsnachweise der Wahrnehmungskarte korrekt angezeigt. Keine Planungsfelder befüllt, keine Lernhandlungen oder Hilfsmittel übernommen. Kein PDF-Download-Test. 128 verfügbare Repository-Dateien bytegenau gegen GitHub-Blobs geprüft, einschließlich binärer amtlicher PDF-Quelle; .gitignore war lokal nicht verfügbar und wurde durch den unveränderten Basisbaum erhalten.
