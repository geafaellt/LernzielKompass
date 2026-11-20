# LernzielKompass

Der LernzielKompass unterstützt Lehrkräfte bei der Planung lernzieldifferenzierten Unterrichts im Förderschwerpunkt Lernen in Sachsen. Er stellt begrenzte Anschlussvorschläge zwischen Lehrplanzielen gegenüber und macht gemeinsame Lerngegenstände, die Lernzielebenen und konkreten Zielhandlungen sowie didaktisch konkretisierte Feinziele und Erfolgskriterien nachvollziehbar.

Lernzielebenen wie „Kennen“ oder „Anwenden“ beschreiben die Anforderungen eines Lehrplanziels. Aufgabenoperatoren wie „nenne“ oder „erkläre“ geben die konkrete Tätigkeit in einer Aufgabe vor. Die bestehenden technischen Feldnamen `gs_operator`, `fsp_operator` und `operator_relation` bleiben aus Kompatibilitätsgründen erhalten. Die Felder können auch Zielhandlungen und Hinweise aus der konkreten Zielzeile enthalten. Gespeicherte Bewertungsentwürfe behalten ihre bisherigen Schlüssel.

**[Veröffentlichte App öffnen](https://geafaellt.github.io/LernzielKompass/)** · **App 1.404** · **Fachlicher Deutsch-Prüfstand: DE-UZ-052 vom 03.11.2026**

Diese Übersicht wurde am 08.11.2026 mit den Projektnachweisen abgeglichen. Maßgeblich sind die unten verlinkten Prüfdateien; ältere Prüfpakete dokumentieren historische Stände.

**Die dokumentierte Deutsch-Einzelprüfung ist einschließlich der Anschlussfragen abgeschlossen.** Die App bleibt ein Instrument zur fachlichen Erprobung. Der Abschluss des festgelegten Prüfumfangs bedeutet weder vollständige Lehrplanabdeckung noch amtliche Freigabe. Die Rückwärts-Einzelprüfung FSP → GS und der PDF-Download gehören nicht zu diesem Abschluss.

## Startseite und Einstieg

App 1.327 öffnet eine kompakte Startseite mit dem Anschlussstellenmodell. Erst „Jetzt lernzieldifferent planen“ führt zur Lehrplanauswahl. Das Modell trennt die curriculare Anschlussstelle vom gemeinsamen Lerngegenstand und zeigt beide Planungsspuren einschließlich Feinziel, Aufgabe/Lernhandlung, Unterstützung und Kriterien. Lernvoraussetzungen, Ressourcen und Barrieren bleiben die durchgehende Prüfperspektive. Die ausführliche Einführung ist aufklappbar. „Zur Startseite“ und ein erneutes Öffnen erhalten eigene Entwürfe; der Einstieg beginnt immer bei der Auswahl.

Das Modell ist eine für den aktuellen GS-Bereich der App verdichtete HTML-Darstellung der von der Projektverantwortlichen bereitgestellten Präsentation „Anschlussstellenmodell_lernzieldifferente_Unterrichtsplanung_praezisiert_v2.pptx“, Folie 1. Der Lehrplanabgleich und alle Fachbestände bleiben unverändert. Die Datei selbst wird nicht veröffentlicht. Prüfung: `scripts/check-startpage-browser.cjs`, vorhandene Browser- und Datenprüfungen. Veröffentlichungsnachweise: `releases/startpage_1.327.json`.

## Gemeinsame Lerngegenstände in Deutsch und Sachunterricht

App 1.330 präzisiert nach Prüfung aller 313 Karten 25 Deutsch- und 100 Sachunterrichtsvorschläge. Sie benennen den gemeinsamen sprachlichen oder sachlichen Gegenstand, ohne Arbeitsaufträge und Hilfsmittel vorzugeben. Bereits geeignete Formulierungen bleiben erhalten; Bedingungen und fachliche Grenzen gelten weiter. [Prüfung und Dokumentation](curriculum/learning_objects/README.md).

## Gemeinsamer Lerngegenstand in Mathematik

App 1.329 ersetzt auf allen 31 Mathematikkarten die Wiederholung des Kartentitels durch eine Formulierung der gemeinsamen mathematischen Sache oder Beziehung. Die Vorschläge bleiben didaktische Konkretisierungen. Zahlenraumgrenzen, Quellen, Lernzielebenen, Feinziele und eigene Entwürfe bleiben erhalten. [Prüfung mit Vorher/Nachher](curriculum/mathematik/review_learning_objects_001.json).

## Feedback zur App

Ab App 1.333 öffnet „Feedback zur App“ am Seitenende einen kurzen Hinweis und verlinkt das Feedbackformular bei Tally in einem neuen Tab. Es werden weder Planungsinhalte noch Kontaktdaten automatisch übertragen; es gibt keine Hintergrundanfragen an Tally. Die Empfängeradresse bleibt ausschließlich in den privaten Tally-Einstellungen. Tally verwaltet das Formular, reCAPTCHA und Benachrichtigungen. Änderungen der Zieladresse und Zustellprüfung erfolgen dort, nicht im öffentlichen Repository. Test: `scripts/check-feedback-browser.cjs`.

## Hinweise und Quellen bei Bedarf

Ab App 1.332 erscheinen unter dem Vergleich der Lernzielebenen keine dauerhaften gelben Hinweisbänder mehr. „Hinweise zum Lehrplananschluss“ enthält die vorhandenen Einordnungen und Grenzen aufklappbar; vollständig enthaltene Doppeltexte werden nur einmal gezeigt. „Amtliche Quellen“ und Quellenbelege der Mathematik-Geltungsbereiche sind ebenfalls aufklappbar. Zahlenraum, Planungsgrenzen und Erläuterungen der Lernzielebenen per Klick bleiben erhalten. Eigene Texte und sämtliche Fachdaten bleiben unverändert. Prüfung: `scripts/check-review-disclosures-browser.cjs`; Nachweise: `releases/review_disclosures_1.332.json`.

## Anschlussstelle prüfen

Ab App 1.328 zeigt Schritt 2 zunächst nur die ausgewählte Karte. „anderen Anschluss wählen“ blendet die passenden Karten ein; nach einer Auswahl schließt sich die Liste wieder. Ohne Auswahl bleiben die verfügbaren Karten direkt zugänglich. Eigene Planungstexte und Fachbestände bleiben erhalten. Prüfung: `scripts/check-connection-picker-browser.cjs`. Veröffentlichungsnachweis: `releases/connection_picker_1.328.json`.

## Informationen zu offenen FSP-Inhalten

App 1.322 enthält einen aufklappbaren, nach Fach filterbaren Informationsbereich mit zehn vertieft geprüften Fällen: zwei konkrete Spezifizierungen ohne ausdrücklich gleichen GS-Gegenanker, sechs Teil- oder wahlabhängige Bezüge und zwei Abgrenzungsfälle. Jeder Eintrag verlinkt amtliche FSP-Zielzeilen und GS-Gegenbezüge; Hauptziele, Wahlbereiche und Bemerkungen werden unterschieden. Es handelt sich nicht um eine vollständige Negativliste oder abgeschlossene FSP-zu-GS-Einzelprüfung. Entwürfe und Anschlusskarten bleiben davon unabhängig. [Befunde und Grenzen](curriculum/fsp-rueckwaerts/offene_inhalte_2026-11-07.md) · [Daten und Reproduktion](curriculum/fsp-rueckwaerts/README.md)

## Umfang der vorhandenen Lehrplanvergleiche

| Bereich | Vorhandener Umfang | Einordnung des Prüfstands |
| --- | --- | --- |
| Sachunterricht, Grundschule 1–4 | 135 Anschlusskarten; GS Sachunterricht ↔ FSP Deutsch-Heimatkunde/Sachunterricht, ausschließlich Stufenbänder 1/2 und 3/4; Datenbasis v2.46 | Der dokumentierte ZA-Prüfumfang wurde bearbeitet; die Projektverantwortliche hat die 21 ZA-Punkte am 23.10.2026 inhaltlich freigegeben. Das ist keine amtliche Freigabe und keine Aussage vollständiger Zieldeckung. Der Bestand bleibt bei den Deutsch-Erweiterungen unverändert. |
| Deutsch, Grundschule 1–4 | 178 Anschlusskarten; GS 1/2, 3 und 4 ↔ FSP Deutsch-Heimatkunde/Sachunterricht 1/2 und 3/4 | Quellenbasierter Abgleichsentwurf; dokumentierte Einzelprüfung einschließlich Anschlussfragen abgeschlossen. Grenzen und Restumfang siehe unten. |
| Mathematik, Grundschule 1–4 | Vierundneunzig begrenzte Anschlüsse zwischen GS 1/2, 3, 4 und FSP Lernen Mathematik 1/2, 3/4 | Prüfstand MA-090 mit siebenundsechzig stufenbandpassenden und siebenundzwanzig stufenübergreifenden Anschlüssen. Weitere Zielzeilen bleiben offen. [Quellen und Prüfstand](curriculum/mathematik/README.md). App1.397: parallele und rechtwinklige Rechteckbeziehungen; Datenprüfungen und gezielte lokale/öffentliche Browserprüfung bestanden. [Veröffentlichungsnachweis](curriculum/mathematik/review_batch_089.json). [MA-090](curriculum/mathematik/review_batch_090.json): Schnittlagenfrage offen dokumentiert; reine Auditänderung, App1.397 unverändert und live dateigleich bestätigt |
| Oberschule und weitere Fächer | Weitere Entwicklungsbereiche | Die Oberschule bleibt in der Auswahl deaktiviert. |

Die FSP-Stufenbänder werden nicht als Einzelklassen interpretiert. Stufenübergreifende Zuordnungen und notwendige Wahlbereiche sind zu beachten. Sekundarstufenanschlüsse gehören nicht zum aktuellen Deutsch-Abgleich.

Grundlagen sind die sächsischen Lehrpläne GS Deutsch (Fassung 2026), GS Sachunterricht (Überarbeitung 2019) und FSP Lernen Deutsch-Heimatkunde/Sachunterricht (2019). Der Sächsische Rechtschreibrahmen 2025 wird im Deutsch-Abgleich ergänzend zur fachlichen Abgrenzung herangezogen; er erzeugt keine zusätzlichen FSP-Ziele. Quellenanker und gesicherte Fassungen sind im Repository dokumentiert.

## Deutsch: abgeschlossener Prüfumfang und dokumentierter Restumfang

Quelle: [review_progress.json](curriculum/deutsch/review_progress.json), [Einzelprüfungen je Zielzeile](curriculum/deutsch/row_audit.csv) und [Prüfpaket DE-UZ-052](curriculum/deutsch/review_batch_052.json).

| Kennzahl | Stand DE-UZ-052 | Bedeutung |
| --- | ---: | --- |
| Vorhandene Deutsch-Karten | 178 | Begrenzte Anschlussvorschläge; keine Zahl vollständig geprüfter Kompetenzen. |
| GS-Zielblöcke mit Erstabgleich | 117 | Die Inventur enthält 488 GS- und 451 FSP-Zeilen. Erstabgleich und Inventur ersetzen keine Einzelprüfung. |
| Zuvor offene Unterzielzeilen erstmals geprüft | 241 | Diese erste Prüfphase ist abgearbeitet; Wiederprüfungen werden nicht erneut mitgezählt. |
| Unterzielzeilen ohne Karte | 136 | Zusammensetzung: 125 begründete Nichtanschlüsse und 11 belegte übergreifende Teilanschlüsse ohne Karte. |
| Davon: begründete Nichtanschlüsse | 125 | Für den jeweils geprüften Zielausschnitt ist kein hinreichend belegter direkter Anschluss nachgewiesen; kein pauschaler Ausschluss jeder didaktischen Verbindung. |
| Davon: übergreifende Teilanschlüsse ohne Karte | 11 | Positive Belege aus übergreifenden Zielen; bewusst keine Anschlusskarte mit einer erfundenen oder aus einer anderen Zielzeile übernommenen Lernzielebene. |
| Offene Anschlussfragen / vorgemerkte Quellen-Nachprüfungen | 0 / 0 | Alle 23 dokumentierten Anschlussfragen sind entschieden; zuletzt 186303 als begrenzter literarischer Anschluss in DE-015. |
| Bereits zugeordnete Unterzielzeilen einzeln geprüft | 130 | Separat von den 241 zuvor offenen Zeilen gezählt. |
| Bereits zugeordnete Unterzielzeilen noch einzeln zu prüfen | **0** | Alle 371 Unterzielzeilen wurden mindestens einmal geprüft; keine Anschlussfrage bleibt offen. |

Die Rechnung lautet **136 = 125 + 11**. Daneben sind 22 übergeordnete Zielblöcke ohne Karte gesondert erfasst; sie werden nicht als Unterziele mitgezählt. Karten, hierarchische Lehrplanzeilen und Zielblöcke sind unterschiedliche Zähleinheiten und erlauben keine einfache Abdeckungsquote.

**Abschluss:** DE-UZ-052 entscheidet die letzte Anschlussfrage zu page908_186303 als begrenzten Anschluss für das Bedeutungsverstehen eines gehörten Märchens. Alle 371 GS-Unterzielzeilen sind einzeln geprüft; complete: true, kein nächster Prüfpunkt. Der Zwischenkontext Vorbereiten bleibt sichtbar, ohne den gesamten Vorbereitungsbereich als abgedeckt zu führen. Eine Rückwärts-Einzelprüfung FSP → GS ist nicht durchgeführt.

## Was die Nachweise aussagen – und was noch offen ist

| Ebene | Belegt bzw. geprüft | Grenze |
| --- | --- | --- |
| Technische Daten- und Funktionsprüfung | Karten-IDs, Quellenreferenzen, Belege für Lernzielebenen und Zielhandlungen, Stufenbänder, eingebettete Daten und JavaScript-Syntax; identische App-Dateien in `index.html` und `dist/index.html`. Dokumentierte Browserprüfungen umfassen Auswahl und Anzeige der neuen Karten DE-175–179 sowie der präzisierten Karte DE-021. Frühere Prüfungen betreffen unter anderem Fachwechsel, getrennte Entwürfe und Planvorschau. | Das belegt technische Konsistenz und die jeweils getesteten Abläufe, keine fachliche Vollständigkeit. Nicht alle Funktionen wurden mit jedem Prüfpaket erneut im Browser getestet. Ein erfolgreicher PDF-Download ist bislang nicht bestätigt. |
| Fachlich belegte Anschlussvorschläge | Einzelbegründungen, konkrete Quellenanker, unterschiedliche Anforderungen, Voraussetzungen und Restumfang stehen in den Prüfpaketen. Auch die 11 übergreifenden Teilanschlüsse ohne Karte sind positive fachliche Ergebnisse. | Ein Teilanschluss gilt nur für den ausdrücklich belegten Ausschnitt. Er bedeutet weder identische Leistungsanforderungen noch vollständige Abdeckung des GS-Ziels. Fehlende Karte bedeutet nicht automatisch fehlenden Anschluss. |
| Abschluss und Grenzen | 371 GS-Unterzielzeilen einschließlich zuvor zugeordneter Zeilen und aller dokumentierten Anschlussfragen geprüft. | Kein Vollabdeckungsanspruch, keine amtliche Freigabe; Rückwärts-Einzelprüfung und PDF-Download sind nicht Teil dieses Abschlusses. |

Für DE-UZ-052 wurden gleichwertige Daten-, Quellenanker-, Syntax- und Regressionsprüfungen sowie die Pages-Aufbereitung im Speicher erfolgreich durchgeführt. Die schreibgeschützte lokale Umgebung erlaubt keinen regulären Python-Build; eine Ausführung der Python-Skripte wird nicht behauptet. Veröffentlichung und Live-Prüfung von DE-015, Abschlussanzeige und Datum sind im Prüfpaket dokumentiert; kein PDF-Test.

## Nutzung und fachliche Rückmeldung

Die Anschlussvorschläge dienen der Unterrichtsplanung und fachlichen Gegenprüfung. Amtliche Lehrplanziele, Unterziele und Bemerkungen bleiben von didaktischen Feinzielen und Erfolgskriterien zu unterscheiden. Die Eignung für die konkrete Lerngruppe beurteilt die Lehrkraft.

**Lernhandlung/Aufgabe und Hilfsmittel bestimmt ausschließlich die Lehrkraft.** Sie werden nicht aus den Anschlusskarten vorgeschlagen oder übernommen. Der Feinziel-Übernahmebutton übernimmt nur Feinziel und Erfolgskriterium. Motivationsentwicklung wird nicht aus einer einzelnen Leistung oder bloßer Teilnahme abgeleitet oder benotet.

Für Rückmeldungen bitte Karten-ID bzw. Zielzeilen-ID, Schulart/Klassenstufe, Lehrplanstelle und die konkrete fachliche Frage oder Korrektur benennen. Besonders hilfreich sind Hinweise zu Lernzielebenen, Zielhandlungen, Voraussetzungen, stufenübergreifenden Anschlüssen und zu weit gefassten Zielausschnitten. Rückmeldungen können als [GitHub-Issue](https://github.com/geafaellt/LernzielKompass/issues) dokumentiert werden.

## Veröffentlichung und Weiterentwicklung

GitHub Pages ist **bereits eingerichtet und veröffentlicht**: [geafaellt.github.io/LernzielKompass](https://geafaellt.github.io/LernzielKompass/). Veröffentlicht wird der Branch `main` aus dem Repository-Stammverzeichnis `/` über die dortige `index.html`.

App 1.294 wurde bereits erfolgreich veröffentlicht. Der vorangehende dokumentierte Veröffentlichungsstand ist **App 1.295**, Deutsch-Modul `DE-2026-11-01.19`, mit angezeigtem Aktualisierungsdatum 01.11.2026. Die Veröffentlichung des App-Commits `4e7a121a47b7329c7dba37b5d8ad83a33c690365` ist durch den [erfolgreichen Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/41344565023) und die Liveprüfung in [DE-UZ-043](curriculum/deutsch/review_batch_043.json) dokumentiert.

DE-UZ-044 aktualisiert sieben bestehende Karten und veröffentlicht App 1.296, Deutsch-Modul `DE-2026-11-02.1`, mit Aktualisierungsdatum 02.11.2026. Die Veröffentlichung von Commit `e25a01f0b076581a1b5c60608b0313b410818aed` ist durch den [erfolgreichen Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/41406578192) und die Liveprüfung aller sieben geänderten Karten in [DE-UZ-044](curriculum/deutsch/review_batch_044.json) dokumentiert. Die gleichwertigen Node-Prüfungen dieses Pakets sind bestanden; der Python-Aufruf ist in dieser Umgebung wegen fehlender Xcode-Werkzeuge nicht verfügbar.

DE-UZ-045 prüft neun weitere zuvor zugeordnete Zeilen erstmals und die Hörverstehensfrage erneut. Sie bleibt offen; ihre beiden möglichen Lesarten sind dokumentiert. App 1.297, Modul `DE-2026-11-02.2`, präzisiert sieben bestehende Karten. Der [Pages-Lauf 41407924083](https://github.com/geafaellt/LernzielKompass/actions/runs/41407924083) veröffentlichte Commit `84ecd56b5ab1d0ce1d14119a07298c5ac37937e8` erfolgreich. Alle sieben geänderten Karten wurden live geöffnet; Zählstände und Prüfgrenzen stehen in [DE-UZ-045](curriculum/deutsch/review_batch_045.json).

DE-UZ-046 prüft elf weitere zuvor zugeordnete Zeilen erstmals und präzisiert acht vorhandene Karten. Die Hörverstehensfrage bleibt ohne neue Evidenz offen und wird nicht erneut gezählt. App 1.298, Modul `DE-2026-11-02.3`, wurde mit Commit `a1876eda7262d9852ba49d3368cd8bcf00dffbe5` im [Pages-Lauf 41425283078](https://github.com/geafaellt/LernzielKompass/actions/runs/41425283078) erfolgreich veröffentlicht. Liveprüfung aller acht geänderten Karten und Prüfgrenzen sind im [Prüfpaket DE-UZ-046](curriculum/deutsch/review_batch_046.json) dokumentiert.

DE-UZ-047 prüft zehn weitere zuvor zugeordnete Zeilen erstmals und präzisiert elf Karten. App 1.299, Modul `DE-2026-11-02.4`, trennt gemeinsame Inhalte und zusätzliche GS-Anforderungen deutlicher. Commit `0e6caccbf208e1b71e5687a6ceefba446186be6b` wurde im [Pages-Lauf 41426687552](https://github.com/geafaellt/LernzielKompass/actions/runs/41426687552) erfolgreich veröffentlicht. Alle elf geänderten Karten wurden in App 1.299 live geöffnet. Fortschritt und Prüfgrenzen stehen in [DE-UZ-047](curriculum/deutsch/review_batch_047.json).

DE-UZ-048 prüft dreizehn weitere zuvor zugeordnete Zeilen erstmals und präzisiert neun Karten. App 1.300, Modul `DE-2026-11-02.5`, unterscheidet insbesondere die Anforderungen an Wortarten, Satzarten und szenisches Gestalten. Commit `f927dd3749c6a908a22063c337b60b7f20f3e1aa` wurde im [Pages-Lauf 41445411424](https://github.com/geafaellt/LernzielKompass/actions/runs/41445411424) erfolgreich veröffentlicht. Alle neun geänderten Karten wurden live geöffnet. Fortschritt und Prüfgrenzen stehen in [DE-UZ-048](curriculum/deutsch/review_batch_048.json).

DE-UZ-049 prüft dreizehn weitere zuvor zugeordnete Zeilen erstmals, präzisiert neun Karten und korrigiert die Wort-/Satzebenen-Zuordnung mit der neuen Karte DE-180. App 1.301, Modul `DE-2026-11-02.6`, erhält alle vorhandenen IDs. Die Veröffentlichung über [Pages-Lauf 41447679721](https://github.com/geafaellt/LernzielKompass/actions/runs/41447679721) war erfolgreich; alle zehn betroffenen Karten wurden live geöffnet. Fortschritt und Prüfgrenzen stehen in [DE-UZ-049](curriculum/deutsch/review_batch_049.json).

DE-UZ-050 prüft zehn weitere zuvor zugeordnete GS4-Zeilen erstmals und präzisiert sieben Karten zu Schreibplanung, Appell, selbstbestimmtem Lesen, Textverstehen, Figurenwertung und Ortssage. DE-168 bleibt bestätigt. App1.302, Modul `DE-2026-11-02.7`, erhält alle Karten-IDs und Zuordnungen. Die Veröffentlichung über [Pages-Lauf 41455118962](https://github.com/geafaellt/LernzielKompass/actions/runs/41455118962) war erfolgreich; alle acht geprüften Karten wurden live geöffnet. Fortschritt und Prüfgrenzen stehen in [DE-UZ-050](curriculum/deutsch/review_batch_050.json).

DE-UZ-051 prüfte die letzten zehn zuvor zugeordneten Unterzielzeilen erstmals und präzisiert sieben Karten zu Leseerfahrungen, Textdeutung, digitalen Textprodukten, Vortrag, Szene und Kommunikationsrollen. DE-170 bleibt bestätigt. App 1.303, Modul `DE-2026-11-02.8`, erhält alle Karten-IDs und GS-Zuordnungen. Eine Anschlussfrage bleibt ungelöst. Die Veröffentlichung über [Pages-Lauf 41498527321](https://github.com/geafaellt/LernzielKompass/actions/runs/41498527321) war erfolgreich; alle acht geprüften Karten wurden live geöffnet. Fortschritt und Prüfgrenzen stehen in [DE-UZ-051](curriculum/deutsch/review_batch_051.json).

DE-UZ-052 entscheidet die letzte Hörverstehensfrage im ausdrücklich begrenzten literarischen Ausschnitt und ergänzt DE-015. App1.304, Modul `DE-2026-11-03.1`. Alle371 Unterzielzeilen und die23 dokumentierten Anschlussfragen sind geprüft bzw. entschieden; keine offene Anschlussfrage. Grenzen und Abschlussnachweise stehen in [DE-UZ-052](curriculum/deutsch/review_batch_052.json). [GitHub Pages](https://github.com/geafaellt/LernzielKompass/actions/runs/41661282109) erfolgreich; DE-015 und Abschlussanzeige live bestätigt. Die regelmäßige Einzelprüfung ist seit03.11.2026 pausiert.

Seit dem 01.11.2026 erfolgen Weiterentwicklungen ausschließlich in `geafaellt/LernzielKompass`, Branch `main`. Die [bisherige Sites-Prüfseite](https://lernzielkompass.dcxn2pwhpk.chatgpt.site) bleibt unverändert auf Site-Version 103 und ist nicht die aktuelle Veröffentlichung.

Für Änderungen an der App ist `dist/index.html` die Quelldatei; `index.html` ist der synchronisierte Pages-Einstieg. Vor einer App-Veröffentlichung:

```sh
python3 scripts/check-deutsch.py
python3 scripts/prepare-pages.py
python3 scripts/check-mathematik.py
```

Anschließend `dist/index.html` und `index.html` gemeinsam committen. `prepare-pages.py` synchronisiert die Dateien und setzt das Veröffentlichungsdatum in Berliner Zeit. Für die Neuerzeugung der Deutschdaten gilt die Reproduktionsfolge in der [Deutsch-Dokumentation](curriculum/deutsch/README.md). Reine Audit- oder README-Änderungen erfordern keine neue App-Version. Die verbindlichen Arbeitsregeln stehen in [AGENTS.md](AGENTS.md).

## Prüfnachweise zum Nachlesen

- [Mathematik: erster Prüfstand, Quellen und Fortsetzung](curriculum/mathematik/README.md)
- [Aktueller Deutsch-Fortschritt und nächster Prüfschritt](curriculum/deutsch/review_progress.json)
- [Deutsch-Zeilenprüfung mit Kartenbezug und Restumfang](curriculum/deutsch/row_audit.csv)
- [Deutsch-Prüfverlauf, technische Nachweise und Reproduktion](curriculum/deutsch/README.md) – chronologisch fortgeschrieben; ältere Abschnitte beschreiben historische Stände.
- [Jüngstes Prüfpaket DE-UZ-052](curriculum/deutsch/review_batch_052.json) und [aktuelle Deutschdaten](curriculum/deutsch/deutsch_module.json)
- [Sachunterricht: Daten, Quellen, Prüfverlauf und Freigabe der 21 ZA-Punkte](curriculum/sachunterricht/baseline.json) – für den Abschluss dieses Prüfumfangs sind `next_review` und `user_approval` vom 23.10.2026 maßgeblich; ältere Inventurtexte enthalten noch frühere offene Arbeitsschritte.
- [Gesicherte Deutsch-Quellenfassungen](curriculum/deutsch/sources/)


## Lernzielebenen im Vergleich · 19.11.2026

Die Anzeige verwendet für alle 407 Anschlusskarten (135 Sachunterricht, 178 Deutsch, 94 Mathematik) die belegenden Zielzeilen aus `curriculum/learning_levels.json`. Jeder Nachweis enthält die Lernzielebene, den Wortlaut, das Klassenstufenband und den Link zur amtlichen Zielzeile. Bei einer Unterzielzeile ohne Lernzielebene wird die nächste übergeordnete Zielzeile mit einer ausdrücklich ausgewiesenen Lernzielebene herangezogen. Die aufklappbaren Belege zeigen auch bei mehreren Zielankern die jeweilige Herkunft.

„Orientieren“, „Erleben“, „Entwickeln“, „Kennenlernen“, „Unterscheiden“ und weitere Zielhandlungen werden nicht als eigenständige Lernzielebenen angezeigt. Die erneute PDF-Prüfung korrigiert DE-112 auf Kennen und DE-113 auf Übertragen. Bei sieben Kartenseiten ist auch übergeordnet keine Lernzielebene aus der Begriffsübersicht ausgewiesen. Bei vier weiteren Mathematikkarten ist die Vererbung aus dem vorherigen Anwenden-Ziel anhand der Gliederung uneindeutig. Diese elf Fälle sind ausdrücklich gekennzeichnet. Die Einzelfallprüfung mit Seitenbelegen steht in [learning_levels_review.json](curriculum/learning_levels_review.json). Mehrere FSP-Stufenbänder werden bei den Bewertungsvorschlägen getrennt berücksichtigt.

Die ursprünglichen Zielformulierungen und vorhandenen Datenfelder bleiben als fachlicher Kontext erhalten. Für neue oder geänderte Anschlusskarten muss der Nachweis in `learning_levels.json` mitgeprüft werden. Die Prüfung `node scripts/check-learning-levels.cjs` kontrolliert alle Kartenseiten, die Quellenangaben und die Anzeige. `prepare-pages.py` bettet den geprüften Datenbestand ein.


Mathematik MA-091 ergänzt den qualitativen Seitenlängenvergleich MA-095 (95 Karten). Lernzielebenen Übertragen/Gestalten bleiben von Zielhandlungen getrennt. [Prüfpaket](curriculum/mathematik/review_batch_091.json); Daten-/Bereichsprüfungen, Lernzielebenen aller408 Karten und gezielte Browserprüfung bestanden. App 1.400 auf main veröffentlicht (e0970ac), [Pages erfolgreich](https://github.com/geafaellt/LernzielKompass/actions/runs/44610253325), Live-Datei bytegleich und Browserprüfungen auch öffentlich bestanden. Fortsetzung bei GS3-Zeichnen187450;23 Anschlussfragen bleiben offen.


Mathematik MA-092 ergänzt MA-096: Parallelogramm zeichnen / Rechteck darstellen, mit getrennten Lernzielebenen Übertragen/Gestalten.96 Karten; [Prüfpaket](curriculum/mathematik/review_batch_092.json). App1.401 auf main veröffentlicht(c23ce21), [Pages erfolgreich](https://github.com/geafaellt/LernzielKompass/actions/runs/44611569102), Live-Datei bytegleich. Daten-/Bereichsprüfungen sowie Lernzielebenen-Anzeige und gezielte Browserprüfungen lokal/live bestanden. Fortsetzung bei Ergänzen187451;23 Anschlussfragen bleiben offen.


Mathematik MA-093 ergänzt MA-097: Dreiecksumriss vervollständigen, ausdrücklich GS3 → FSP1/2.97 Karten; [Prüfpaket](curriculum/mathematik/review_batch_093.json). App1.402 auf main veröffentlicht(9a5835a), [Pages erfolgreich](https://github.com/geafaellt/LernzielKompass/actions/runs/44621694106), Live-Datei bytegleich. Daten-/Bereichsprüfungen sowie Lernzielebenen-Anzeige und gezielte Browserprüfungen lokal/live bestanden. Fortsetzung beim Fachbegriff Parallelogramm187452;23 Anschlussfragen bleiben offen.


Mathematik MA-094: Fachbegriff Parallelogramm187452 gegen beide FSP-Bänder abgegrenzt, kein hinreichend belegter direkter Fachwortanschluss.97 Karten und App1.402 unverändert. [Prüfpaket](curriculum/mathematik/review_batch_094.json); Fortsetzung bei Flächeninhalt/Umfang2027. Alle sechs Daten-/Bereichsprüfungen und die Audit-Konsistenzprüfung bestanden. Modul, Lernzielebenen-Daten und HTML bytegleich; kein neuer Browserlauf. Audit mit Commit311fdf5fe2f281b8fc25979405618eaff9982164 auf main veröffentlicht; [Pages-Lauf44630955851](https://github.com/geafaellt/LernzielKompass/actions/runs/44630955851) erfolgreich. Unveränderte Live-App1.402 bytegleich bestätigt(SHA256 0e98280797516efda8ea37e80525ee2582f18d1958225c1b113712fbd2175948).


Mathematik MA-095: Flächenvergleich187164 gegen beide FSP-Bänder untersucht; die Reichweite allgemeiner Größen-/Figuren- und Verpackungsvergleiche bleibt als Anschlussfrage offen. Lernzielebenen von Zielhandlungen getrennt und PDF-Spalten geprüft.97 Karten und App1.402 unverändert,24 Anschlussfragen. [Prüfpaket](curriculum/mathematik/review_batch_095.json); Fortsetzung187165. Alle sechs Daten-/Bereichsprüfungen und Audit-Konsistenzprüfung bestanden. Die automatisch aktualisierte Datumszeile wurde nach Prüfung als einzige HTML-Änderung für diese reine Auditveröffentlichung zurückgenommen; beide App-Dateien bleiben bytegleich. Kein neuer Browserlauf. Audit mit Commit471ce6d1e7bc2e71910b925d66ba2b127a4aaada auf main veröffentlicht; [Pages-Lauf44656090518](https://github.com/geafaellt/LernzielKompass/actions/runs/44656090518) erfolgreich. Unveränderte Live-App1.402 bytegleich bestätigt(SHA256 0e98280797516efda8ea37e80525ee2582f18d1958225c1b113712fbd2175948).


Mathematik MA-096 ergänzt MA-098: Rechteckfläche in zwei deckungsgleiche Spiegelhälften zerlegen, GS3 → FSP3/4. Lernzielebenen Einblick gewinnen/Kennen getrennt von Zielhandlungen. Flächenvergleich187164 als enger Teilanschluss nachgeprüft; allgemeine Vergleiche bleiben offen.98 Karten,23 Anschlussfragen; [Prüfpaket](curriculum/mathematik/review_batch_096.json). App1.403: Alle sechs Daten-/Bereichsprüfungen und Audit-Konsistenzprüfung bestanden. Gezielte Browserprüfung MA-002/011/098 einschließlich mobiler MA-098-Darstellung320px/390px bestanden; Geltungsbereich auf Karte, bei Zielen und im Planungsoutput sichtbar. Eigene Texte bleiben erhalten, Aufgaben/Hilfsmittel leer. Lernzielebenen-Anzeige aller411 Karten/822 Seiten bestanden; dies ist eine Struktur-/Darstellungsprüfung, keine neue fachliche Einzelprüfung aller Karten. Keine UI-Codeänderung und kein vollständiger98-Karten-Funktionslauf. App1.403 mit Commit3b26e6ff5616bf106d8f7f6f312ab6fbbcb37978 auf main veröffentlicht; [Pages-Lauf44669748044](https://github.com/geafaellt/LernzielKompass/actions/runs/44669748044) erfolgreich. Live-Datei bytegleich(SHA256 cf705d36b35ef6824791bd0649f1e99eee6dcc6d28a3434d274d1f0855134256). Gezielte Browserprüfung MA-002/011/098, mobile MA-098-Darstellung320px/390px und Lernzielebenen-Anzeige aller411 Karten/822 Seiten auch öffentlich bestanden.


Mathematik MA-097 ergänzt MA-099: spiegelbildliche Rechteckteile zusammensetzen, GS3 → FSP3/4. Lernzielebenen Einblick gewinnen/Kennen getrennt von Zielhandlungen.99 Karten,23 Anschlussfragen; [Prüfpaket](curriculum/mathematik/review_batch_097.json). App1.404: Alle sechs Daten-/Bereichsprüfungen und die Audit-Konsistenzprüfung bestanden. Gezielte Browserprüfung MA-002/098/099 einschließlich mobiler MA-099-Darstellung320px/390px bestanden; Geltungsbereich auf Karte, bei Zielen und im Planungsoutput sichtbar. Eigene Texte erhalten, Aufgaben/Hilfsmittel leer. Lernzielebenen-Anzeige aller412 Karten/824 Seiten bestanden; keine neue fachliche Einzelprüfung aller Karten. Keine UI-Codeänderung und kein vollständiger99-Karten-Funktionslauf. Veröffentlichung und Liveprüfung ausstehend.
