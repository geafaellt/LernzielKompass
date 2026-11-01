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
