# LernzielKompass

Der LernzielKompass unterstützt Lehrkräfte bei der Planung lernzieldifferenzierten Unterrichts im Förderschwerpunkt Lernen in Sachsen. Er stellt begrenzte Anschlussvorschläge zwischen Lehrplanzielen gegenüber und macht gemeinsame Lerngegenstände, die Lernzielebenen und konkreten Zielhandlungen sowie didaktisch konkretisierte Feinziele und Erfolgskriterien nachvollziehbar.

Lernzielebenen wie „Kennen“ oder „Anwenden“ beschreiben die Anforderungen eines Lehrplanziels. Aufgabenoperatoren wie „nenne“ oder „erkläre“ geben die konkrete Tätigkeit in einer Aufgabe vor. Die bestehenden technischen Feldnamen `gs_operator`, `fsp_operator` und `operator_relation` bleiben aus Kompatibilitätsgründen erhalten. Die Felder können auch Zielhandlungen und Hinweise aus der konkreten Zielzeile enthalten. Gespeicherte Bewertungsentwürfe behalten ihre bisherigen Schlüssel.

**[Veröffentlichte App öffnen](https://geafaellt.github.io/LernzielKompass/)** · **App 1.431** · **Fachlicher Deutsch-Prüfstand: DE-UZ-052 vom 03.11.2026**

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
| Mathematik, Grundschule 1–4 | 124 begrenzte Anschlüsse;95 stufenbandpassend,29 stufenübergreifend | MA-130, App1.431:24 offene Anschlussfragen, Einzelprüfung unvollständig. Fortsetzung GS3 strukturierte Aufgabenformate187201. [Fortschritt](curriculum/mathematik/review_progress.json) · [Prüfpaket](curriculum/mathematik/review_batch_130.json). |
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


Mathematik MA-097 ergänzt MA-099: spiegelbildliche Rechteckteile zusammensetzen, GS3 → FSP3/4. Lernzielebenen Einblick gewinnen/Kennen getrennt von Zielhandlungen.99 Karten,23 Anschlussfragen; [Prüfpaket](curriculum/mathematik/review_batch_097.json). App1.404: Alle sechs Daten-/Bereichsprüfungen und die Audit-Konsistenzprüfung bestanden. Gezielte Browserprüfung MA-002/098/099 einschließlich mobiler MA-099-Darstellung320px/390px bestanden; Geltungsbereich auf Karte, bei Zielen und im Planungsoutput sichtbar. Eigene Texte erhalten, Aufgaben/Hilfsmittel leer. Lernzielebenen-Anzeige aller412 Karten/824 Seiten bestanden; keine neue fachliche Einzelprüfung aller Karten. Keine UI-Codeänderung und kein vollständiger99-Karten-Funktionslauf. App1.404 mit Commit8bdb31f1c7268b6229c3d740ede67a1ea35da152 auf main veröffentlicht; [Pages-Lauf44688597423](https://github.com/geafaellt/LernzielKompass/actions/runs/44688597423) erfolgreich. Live-Datei bytegleich(SHA256 96be4972143e69b03898064a1e84327af578d91072be986bcc50b51ce3a5aa03). Gezielte Browserprüfung MA-002/098/099, mobile MA-099-Darstellung320px/390px und Lernzielebenen-Anzeige aller412 Karten/824 Seiten auch öffentlich bestanden.


Mathematik MA-098 ergänzt MA-100: gleich große Teilflächen bis100 auszählen, GS3 → FSP3/4. GS-Flächenmaßdeutung von FSP-Anzahlbestimmung und Lernzielebenen von Zielhandlungen getrennt.100 Karten,23 Anschlussfragen; [Prüfpaket](curriculum/mathematik/review_batch_098.json). App1.405: Alle sechs Daten-/Bereichsprüfungen und die Audit-Konsistenzprüfung bestanden. Gezielte Browserprüfung MA-087/099/100 einschließlich mobiler MA-100-Darstellung320px/390px bestanden; Geltungsbereich auf Karte, bei Zielen und im Planungsoutput sichtbar. Eigene Texte erhalten, Aufgaben/Hilfsmittel leer. Lernzielebenen-Anzeige aller413 Karten/826 Seiten bestanden; keine neue fachliche Einzelprüfung aller Karten. Keine UI-Codeänderung und kein vollständiger100-Karten-Funktionslauf. App1.405 mit Commitb03ad838651acbe36e955787111ef54744048c0c auf main veröffentlicht; [Pages-Lauf44691360865](https://github.com/geafaellt/LernzielKompass/actions/runs/44691360865) erfolgreich. Live-Datei bytegleich(SHA256 79874145676d679f4bd43eb344fcf3a51f0c379f29f24a4b0dc0c3df31c16d10). Gezielte Browserprüfung MA-087/099/100, mobile MA-100-Darstellung320px/390px und Lernzielebenen-Anzeige aller413 Karten/826 Seiten auch öffentlich bestanden.


Mathematik MA-099: Schätzen187168 im Flächen-/Umfangskontext geprüft; konkrete Umfangsanschlussfrage offen.100 Karten,24 Anschlussfragen; [Prüfpaket](curriculum/mathematik/review_batch_099.json). Reiner Audit, App1.405 unverändert. Alle sechs Daten-/Bereichsprüfungen und Audit-Konsistenzprüfung bestanden. Modul, Lernzielebenen-Daten und HTML bytegleich; kein neuer Browserlauf. Audit mit Commite73d3760e88c7317639d6557156ae8ca571575ae auf main veröffentlicht; [Pages-Lauf44697849566](https://github.com/geafaellt/LernzielKompass/actions/runs/44697849566) erfolgreich. Unveränderte Live-App1.405 bytegleich bestätigt(SHA256 79874145676d679f4bd43eb344fcf3a51f0c379f29f24a4b0dc0c3df31c16d10).


Mathematik MA-100: gesicherten Entwurf einmalig integriert. MA-101 vergleicht ganze Randlängen zweier Dreiecksbegrenzungen; bis100 als didaktischer Rechenrahmen.101 Karten,31 Anschlussfragen,191 Inventurzeilen. [Prüfpaket](curriculum/mathematik/review_batch_100.json). App1.406: Alle sechs Daten-/Bereichsprüfungen und Audit-Konsistenzprüfung bestanden. Gezielte Browserprüfung MA-064/067/101 einschließlich mobiler MA-101-Darstellung320px/390px bestanden. Geltungsbereich auf Karte, bei Zielen und im Planungsoutput sichtbar; eigene Entwürfe erhalten, Aufgaben/Hilfsmittel leer. Lernzielebenen-Anzeige aller414 Karten/828 Seiten bestanden; keine neue fachliche Einzelprüfung aller Karten. Keine UI-Codeänderung und kein vollständiger101-Karten-Funktionslauf. App1.406 mit Commit697055bab44439b3fe447f8365e4d97d7071c9d4 auf main veröffentlicht; [Pages-Lauf44727254718](https://github.com/geafaellt/LernzielKompass/actions/runs/44727254718) erfolgreich. Live-Datei bytegleich(SHA256 55a4a657dec347faa4bf9d9b77bf9d992d9879309b3bdea57e0a9401169de7d5). Gezielte Browserprüfung MA-064/067/101, mobile MA-101-Darstellung320px/390px und Lernzielebenen-Anzeige aller414 Karten/828 Seiten auch öffentlich bestanden.


Mathematik MA-101: Eigenschaften und Fachbegriffe von Körpernetzen geprüft.2034 als konkrete Anschlussfrage offen,2035 direkter Fachwort-Nichtanschluss.101 Karten unverändert,32 Anschlussfragen. [Prüfpaket](curriculum/mathematik/review_batch_101.json). Reiner Audit; App1.406 unverändert. Alle sechs Daten-/Bereichsprüfungen und Audit-Konsistenzprüfung bestanden. Alle101 Karten, Modul, Lernzielebenen-Daten und HTML unverändert; kein neuer Browserlauf. Audit mit Commit353498f4d92c4ad5738aa9e9075c8306c0b5fac1 auf main veröffentlicht; [Pages-Lauf44775758080](https://github.com/geafaellt/LernzielKompass/actions/runs/44775758080) erfolgreich. Unveränderte Live-App1.406 bytegleich bestätigt(SHA256 55a4a657dec347faa4bf9d9b77bf9d992d9879309b3bdea57e0a9401169de7d5).


Mathematik MA-102: begrenzter Pyramiden-Quader-Vergleich MA-102; drei offene Fragen mit Restumfang geklärt, keine neuen Erstprüfungen.102 Karten,29 Anschlussfragen. [Prüfpaket](curriculum/mathematik/review_batch_102.json). App1.407: Alle sechs Daten-/Bereichsprüfungen und Audit-Konsistenzprüfung bestanden. Gezielte Browserprüfung MA-084/095/102 einschließlich mobiler MA-102-Darstellung320px/390px bestanden; Geltungsbereich auf Karte, bei Zielen und im Planungsoutput sichtbar, eigene Texte erhalten und Aufgaben/Hilfsmittel leer. Lernzielebenen-Anzeige aller415 Karten/830 Seiten bestanden; keine neue fachliche Einzelprüfung aller Karten. Keine UI-Codeänderung und kein vollständiger102-Karten-Funktionslauf. App1.407 mit Commit77c4c2e037e1e3a440d5e8384acb611d859aabfa auf main veröffentlicht; [Pages-Lauf44777080601](https://github.com/geafaellt/LernzielKompass/actions/runs/44777080601) erfolgreich. Live-Datei bytegleich(SHA256 90ae7cea29dc09e8519bb81f975d41a128e508dc7fc7df59f9ffb4f2bfe882b9). Gezielte Browserprüfung MA-084/095/102, mobile MA-102-Darstellung320px/390px und Lernzielebenen-Anzeige aller415 Karten/830 Seiten auch öffentlich bestanden.


Mathematik MA-103: begrenzter Kegel-Zylinder-Vergleich. Zwei Fragen mit Restumfang geklärt, keine neuen Erstprüfungen.103 Karten,27 Anschlussfragen. [Prüfpaket](curriculum/mathematik/review_batch_103.json). App1.408: Datenprüfungen und lokale Lernzielebenenprüfung bestanden. Veröffentlicht mit b5c89ef1834cf5d141c3b480067c38a49419fd93; [Pages44950269901](https://github.com/geafaellt/LernzielKompass/actions/runs/44950269901) erfolgreich. Live-HTML bytegleich; gezielter Live-Browserlauf einschließlich Mobilansicht bestanden. Keine UI-Codeänderung; kein vollständiger103-Karten-Funktionstest. Lernzielebenen aller416 Karten/832 Seiten lokal bestanden; zusätzlicher Live-Gesamtlauf wegen Browserstart-Zeitlimit mit EGL/GPU-Initialisierungsfehler nicht abgeschlossen. Zielgerichteter Live-Lauf einschließlich MA-103-Kennen/Anwenden und Mobilansicht bestanden. Weitergehende Restumfänge bleiben offen.


Mathematik MA-104: bekannte Pyramidenform bei verändertem Blickwinkel wiedererkennen; begrenzter Anschluss mit getrenntem übergreifendem Sichtwechselbeleg.104 Karten,26 Fragen. [Prüfpaket](curriculum/mathematik/review_batch_104.json). App1.409: Datenprüfungen, gezielter lokaler/Live-Browserlauf und Lernzielebenenanzeige417 Karten/834 Seiten bestanden. Veröffentlicht mit ea082073e453203087e5012da729ea12c95d00b7; [Pages45011489623](https://github.com/geafaellt/LernzielKompass/actions/runs/45011489623) erfolgreich. Live-HTML bytegleich. Keine UI-Codeänderung; kein vollständiger104-Karten-Funktionstest. Alle103 Bestandskarten unverändert. Lernzielebenenanzeige aller417 Karten/834 Seiten lokal und live geprüft; keine neue vollständige semantische Bestandsprüfung. Weitergehende Restumfänge bleiben offen.


Mathematik MA-105: Netzherstellung/-zeichnung/-prüfung2033 als begründeter Nichtanschluss; Netzeigenschaften2034 bleiben separat offen.25 Anschlussfragen,104 Karten; App1.409 unverändert. [Prüfpaket](curriculum/mathematik/review_batch_105.json). Datenprüfungen und Bestandserhalt bestanden; Auditcommit cf34442a048b33728c27639288e35acee39f76a7 auf main veröffentlicht. [Pages45012244520](https://github.com/geafaellt/LernzielKompass/actions/runs/45012244520) erfolgreich; unveränderte Live-App1.409 bytegleich bestätigt. Kein neuer Browserlauf für reine Auditänderungen; entsprechende Live-Prüfungen in MA-104 bestanden.


Mathematik MA-106: quadratische Würfelseitenflächen bei vorgegebener Netzzuordnung.105 Karten,24 Anschlussfragen. [Prüfpaket](curriculum/mathematik/review_batch_106.json). App1.410: Auf main veröffentlicht mit28343d285ad4a1915d71414ad3b4afdac26b3f7e; [Pages45041439907](https://github.com/geafaellt/LernzielKompass/actions/runs/45041439907) erfolgreich. Ausgelieferte App1.410 bytegleich. Datenprüfungen, gezielter Browserlauf und Lernzielebenenanzeige aller418 Karten/836 Seiten lokal und live bestanden. Keine UI-Codeänderung; kein vollständiger neuer Funktionstest aller105 Mathematikkarten. Alle104 Bestandskarten unverändert. Weitergehende Restumfänge und24 Anschlussfragen bleiben offen.


Mathematik MA-107: eigenes spiegelgleiches Bandornament entwickeln und fortsetzen.106 Karten,25 Anschlussfragen. [Prüfpaket](curriculum/mathematik/review_batch_107.json). App1.411: Auf main veröffentlicht mit8a8993f895f68ccae6bfae03dbf1a593acd549af; [Pages45042409919](https://github.com/geafaellt/LernzielKompass/actions/runs/45042409919) erfolgreich. Ausgelieferte App1.411 bytegleich. Datenprüfungen, gezielter Browserlauf und Lernzielebenenanzeige aller419 Karten/838 Seiten lokal und live bestanden. Keine UI-Codeänderung; kein vollständiger neuer Funktionstest aller106 Mathematikkarten. Alle105 Bestandskarten unverändert. Weitergehende Restumfänge und25 Anschlussfragen bleiben offen.


Mathematik MA-108: Fachwortzeile187180 für gespiegelt/gedreht/verschoben getrennt geprüft; kein hinreichend belegter direkter aktiver Fachwortanschluss. Inhaltliche Symmetrieanschlüsse bleiben erhalten.25 Anschlussfragen,106 Karten; App1.411 unverändert. [Prüfpaket](curriculum/mathematik/review_batch_108.json). Datenprüfungen und Bestandserhalt bestanden; Auditcommit ff77384acb48efdd5a2da85521054c35a1192235 auf main veröffentlicht. [Pages45107484071](https://github.com/geafaellt/LernzielKompass/actions/runs/45107484071) erfolgreich; unveränderte Live-App1.411 nach dem Build bytegleich bestätigt. Kein neuer Browserlauf für reine Auditänderungen; entsprechende Prüfungen inMA-107 bestanden.


Mathematik MA-109: gleiche Verschiebung im eigenen Bandmuster als didaktischer Teilanschluss.107 Karten,25 Fragen; Drehsymmetrie bleibt offen. [Prüfpaket](curriculum/mathematik/review_batch_109.json). App1.412: Sechs Datenprüfungen sowie gezielte lokale und Live-Browserprüfungen bestanden, einschließlich420 Karten/840 Lernzielebenen-Seiten. Appcommit 8bd7fe5cd4d01437c27f91b9fccdb41b5b7a4d0e auf main veröffentlicht. [Pages45142667257](https://github.com/geafaellt/LernzielKompass/actions/runs/45142667257) erfolgreich; Live-App1.412 bytegleich bestätigt. Keine UI-Codeänderung und kein vollständiger Funktionslauf aller107 Mathematikkarten; keine vollständige neue semantische Bestandsprüfung.


Mathematik MA-110: halbe Drehung im eigenen Ornament als didaktischer Teilanschluss.108 Karten,24 Fragen; weiter bei GS3-Zahldarstellungen2038. [Prüfpaket](curriculum/mathematik/review_batch_110.json). App1.413: Sechs Datenprüfungen sowie gezielte lokale und Live-Browserprüfungen bestanden, einschließlich421 Karten/842 Lernzielebenen-Seiten. Appcommit 8d416b6b5412fd203d131ffb6708a68179c637e0 auf main veröffentlicht. [Pages45143879980](https://github.com/geafaellt/LernzielKompass/actions/runs/45143879980) erfolgreich; Live-App1.413 bytegleich bestätigt. Keine UI-Codeänderung und kein vollständiger Funktionslauf aller108 Mathematikkarten; keine vollständige neue semantische Bestandsprüfung.


Mathematik MA-111: Anzahl/Position und numerische Kennzeichnung in GS3 getrennt zugeordnet.110 Karten,24 Fragen; weiter bei2040/2041. [Prüfpaket](curriculum/mathematik/review_batch_111.json). App1.414: Sechs Datenprüfungen sowie gezielte lokale und Live-Browserprüfungen bestanden,einschließlich423 Karten/846 Lernzielebenen-Seiten. Appcommit 9577a38dac2a19eee9e9bc6dbc0283764733a72c auf main veröffentlicht. [Pages45170618379](https://github.com/geafaellt/LernzielKompass/actions/runs/45170618379) erfolgreich; Live-App1.414 bytegleich bestätigt. Keine UI-Codeänderung und kein vollständiger Funktionslauf aller110 Mathematikkarten; keine vollständige neue semantische Bestandsprüfung.


Mathematik MA-112: Ziffernzahlen lesen/sprechen/schreiben in GS3, begrenzter Anschluss aufMA-111 an FSP3/4. GS bis1000/FSP bis100, beide Lernzielebenen Beherrschen. Zwei alte Fragen zur schriftlichen Zahlwortform entschieden;111 Karten,22 offene Fragen. [Prüfpaket](curriculum/mathematik/review_batch_112.json). Weiter bei2044. App1.415: Datenprüfungen und gezielter Funktionsbrowser lokal/live bestanden; Lernzielebenen aller424 Karten/848 Seiten geprüft. Veröffentlicht mit f26f818c5ca0a036120a2d17facb662937c3b108; [Pages45196696515](https://github.com/geafaellt/LernzielKompass/actions/runs/45196696515) erfolgreich. Live-HTML bytegleich, SHA256 b7316d3f0d0c6244152e94b01bc3f105e0d263afbcdc49d36e6e2945a94f3e3b. Keine vollständige erneute Funktions- oder semantische Prüfung sämtlicher Bestandskarten.


Mathematik MA-113: Bildliche Mengendarstellung ↔ Zahl in GS3 aufMA-112 begrenzt zugeordnet, GS bis1000/FSP3/4 bis100, beide Lernzielebenen Beherrschen.112 Karten,22 offene Fragen; weiter bei187183/187184. [Prüfpaket](curriculum/mathematik/review_batch_113.json). App1.416: Datenprüfungen und gezielter Funktionsbrowser lokal/live bestanden; Lernzielebenen aller425 Karten/850 Seiten geprüft. Veröffentlicht mit d8a5de4875e2e314b5ce6eeccf657f72d471b359; [Pages45198458109](https://github.com/geafaellt/LernzielKompass/actions/runs/45198458109) erfolgreich. Live-HTML bytegleich, SHA256 4e76d06fb268bf02a1ff190cf07afef8bc27f91ed14cff234096f847bfebadb0. Keine vollständige erneute Funktions- oder semantische Prüfung sämtlicher Bestandskarten.


Mathematik MA-114: dekadische Stellenwertanteile in GS3 begrenzt zugeordnet (GS1000/FSP3/4 bis100).113 Karten,22 Fragen. Didaktische Kennen-Zuordnungen erhalten und von amtlichen Ebenen getrennt angezeigt. [Prüfpaket](curriculum/mathematik/review_batch_114.json). App1.417: Daten- und lokale sowie Live-Browserprüfungen bestanden; auf main veröffentlicht, Pages erfolgreich und ausgelieferte App bytegleich bestätigt.


MA-114 veröffentlicht: App1.417, Commit `2a6f3ad2a857c72ca54dad9fe463a50a903aedd5`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45225266673). Live-App bytegleich (SHA-256 `35da2131fd75e26540b828b4b08561f80ad79fac21666295d6778e5396ad2c02`). Alle sechs Datenprüfungen sowie vollständige Mathematik-Browserprüfung, Ebenenprüfung und didaktische Zuordnungsprüfung lokal und live bestanden. Bestehende Lehrkrafttexte und manuelle Bewertungen erhalten. Nächster Schritt: erneute Einzelprüfung187185/187186;22 Anschlussfragen und weitergehende Restumfänge offen. Kein Gesamtabschluss behauptet.


Mathematik MA-116: Vorgänger/Nachfolger und begrenzende Nachbarzehner fürGS3 mitGS1000/FSP100 ergänzt.115 Karten,22 Fragen. [Prüfpaket](curriculum/mathematik/review_batch_116.json). App1.418: Daten- und lokale sowie Live-Browserprüfungen bestanden; auf main veröffentlicht, Pages erfolgreich und ausgelieferte App bytegleich bestätigt.


MA-116 veröffentlicht: App1.418, Commit `ea65b3a0ecdd3b0b5b38da6310cd52b2c172f034`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45333697589). Live-App bytegleich, SHA-256 `d471c118ef44c66791b9f3e8d02359cf96b9559527218bb49747ce49bb586d6c`. Alle sechs Datenprüfungen, vollständige Mathematik-Browserprüfung115Karten und Ebenenprüfung428Karten/856Seiten lokal/live bestanden. Nächster Schritt187189 (Doppelte/Hälfte), danach187190/187191.22 offene Anschlussfragen und weitergehende Restumfänge; kein Gesamtabschluss.


Mathematik MA-117: Doppelte/halbe Anzahlen inGS3 begrenzt zugeordnet; GS Beherrschen bis1000/FSP Einblick gewinnen, Grenze100 didaktisch ausBandziel.116 Karten,22 Fragen. [Prüfpaket](curriculum/mathematik/review_batch_117.json). App1.419 auf main veröffentlicht; Pages erfolgreich, ausgelieferte App bytegleich und gezielte Mathematik-/vollständige Ebenen-Browserprüfung lokal/live bestanden.


MA-117 veröffentlicht: App1.419, Commit `0a8a6c9ea19a24771accbffa26ff80f78c1ea4ca`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45347849381). Live-App bytegleich, SHA-256 `b90c5a2c46c942861fd28f4a34a91e3d1d2a5d17ac9e249bfa99571a02705fa7`. Alle sechs Datenprüfungen, gezielte MathematikprüfungMA-011/116 mit bestehenden Regressionen und vollständige Ebenenprüfung429Karten/858Seiten lokal/live bestanden. Keine UI-Codeänderung und kein erneuter vollständiger Mathematikfunktionslauf aller116Karten. Nächster Schritt187190 (Runden), danach187191.22 offene Anschlussfragen und weitergehende Restumfänge; kein Gesamtabschluss.


Mathematik MA-119: Zahlvergleich in Bild-/Zifferndarstellung ergänzt (beide Beherrschen; GS1000/FSP100).117 Karten,22 Fragen. [Prüfpaket](curriculum/mathematik/review_batch_119.json). App1.420: Sechs Datenprüfungen und vollständige Mathematik-/Ebenen-Browserprüfungen lokal bestanden. Veröffentlichung und Liveprüfung bestanden.


MA-119 veröffentlicht: App1.420, Commit `ef0e9ae054f54ab2a6b460e8f88308f4ec983006`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45378166283). Live-App bytegleich, SHA-256 `7da7ef8eb811aa53408c744790a042e8070ffa1934cf5fa81f559a7c8cbca964`. Alle sechs Datenprüfungen, vollständige Mathematikprüfung117Karten und Ebenenprüfung430Karten/860Seiten lokal/live bestanden. Nächster Schritt2052/2055, danach187192–187196;7 neue Inventurzeilen noch ungeprüft.22 Anschlussfragen und weitere Restumfänge bleiben offen, kein Gesamtabschluss.


Mathematik MA-120: Stellenwertdarstellung GS-Anwenden/FSP-Beherrschen getrennt (GS1000/FSP100).118 Karten,22 Fragen. [Prüfpaket](curriculum/mathematik/review_batch_120.json). App1.421: sechs Datenprüfungen, vollständige Mathematikprüfung118Karten und Ebenenprüfung431Karten/862Seiten lokal und live bestanden; Veröffentlichung geprüft.


MA-120 veröffentlicht: App1.421, Commit `c8c521288c79277a6a20658aff9fc44dcdc12c9b`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45561240383). Live-App bytegleich, SHA-256 `ca6c0b2f519541d5d7c3edc044b93f5e6a7c38913e72131d2a2ff50c13692aed`. Alle sechs Datenprüfungen, vollständige Mathematikprüfung118Karten und Ebenenprüfung431Karten/862Seiten lokal/live bestanden. Nächster Schritt187192, danach187193–187196;2052 nur Kontext,2055 begrenzt geprüft.22 Anschlussfragen und weitere Restumfänge bleiben offen, kein Gesamtabschluss.


Mathematik MA-121: wertgleiches dekadisches Bündeln/Entbündeln, GS-Anwenden/FSP-Beherrschen, Grenzen1000/100.119 Karten,22 Fragen. [Prüfpaket](curriculum/mathematik/review_batch_121.json). App1.422: sechs Datenprüfungen, vollständige Mathematikprüfung119Karten und Ebenenprüfung432Karten/864Seiten lokal und live bestanden; Veröffentlichung geprüft.


MA-121 veröffentlicht: App1.422, Commit `0fcce47c31f9d60df3a07345eb4e951f3a055a99`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45564353973). Live-App bytegleich, SHA-256 `200ff6edb6c85e30c476594e7fa56da7ad6a62f70ed8e339e273387a6354b0b3`. Alle sechs Datenprüfungen, vollständige Mathematikprüfung119Karten und Ebenenprüfung432Karten/864Seiten lokal/live bestanden. Nächster Schritt187193/187194, danach187195/187196;187192 begrenzt geprüft.22 Anschlussfragen und weitere Restumfänge bleiben offen, kein Gesamtabschluss.


Mathematik MA-122: Stellenwertprinzip und platzbewahrende Null auf bestehenderMA-118 präzisiert; GS-Anwenden/FSP-Beherrschen, Grenzen1000/100.119 Karten,22 Fragen. [Prüfpaket](curriculum/mathematik/review_batch_122.json). App1.423: Prüfungen und Veröffentlichung bestanden.

MA-122: Alle sechs Datenprüfungen sowie die vollständige Mathematikprüfung (119 Karten) und Ebenenprüfung (432 Karten/864 Seiten) lokal und live bestanden; Veröffentlichung geprüft.


MA-122 veröffentlicht: App1.423, Commit `b72d4166ae0d57aa1e8121559250beb7674c2ca0`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45581369916). Live-App bytegleich, SHA-256 `91753285b5ffd8de86e107fbd339fb4295e1adc5e781b5f699475b664012a36d`. Alle sechs Datenprüfungen, vollständige Mathematikprüfung119Karten und Ebenenprüfung432Karten/864Seiten lokal/live bestanden. Nächster Schritt187195, danach187196;187193/187194 einzeln auf bestehenderMA-118 begrenzt geprüft.22 Anschlussfragen und weitere Restumfänge bleiben offen, kein Gesamtabschluss.


Mathematik MA-123: Darstellungsvernetzung187195 auf bestehenderMA-118 präzisiert; GS-Anwenden/FSP-Beherrschen, Grenzen1000/100.119 Karten,22 Fragen. [Prüfpaket](curriculum/mathematik/review_batch_123.json). App1.424: Prüfungen und Veröffentlichung bestanden.

MA-123: Alle sechs Datenprüfungen sowie die vollständige Mathematikprüfung (119 Karten) und Ebenenprüfung (432 Karten/864 Seiten) lokal und live bestanden; Veröffentlichung geprüft.


MA-123 veröffentlicht: App1.424, Commit `dc45dbda1326188d93f693f4ddfe2f5f0271c482`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45602993519). Live-App bytegleich, SHA-256 `e8eefa57412bbad597ceb0273937cf0443c8fc0b008c197695d3169d4fc361c4`. Alle sechs Datenprüfungen, vollständige Mathematikprüfung119Karten und Ebenenprüfung432Karten/864Seiten lokal/live bestanden. Nächster Schritt187196;187195 einzeln auf bestehenderMA-118 für den beidseitigen Darstellungswechsel begrenzt geprüft.22 Anschlussfragen und weitere Restumfänge bleiben offen, kein Gesamtabschluss.


Mathematik MA-124: Fachbegriffe187196 Tausender/Runden ohne hinreichend belegten direkten Anschluss in beiden FSP-Bändern entschieden. GS-Lernzielebene Anwenden, Zielhandlung Verwenden getrennt.119 Karten,22 Fragen; Fortsetzung2064/2065. [Prüfpaket](curriculum/mathematik/review_batch_124.json). App1.425: lokal und live bestanden; Veröffentlichung geprüft.


MA-124 veröffentlicht: App1.425, Commit `1dbdcbeec24f79de8e39066259cc7bef296cbc51`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45725808667). Live-App bytegleich, SHA-256 `ec0daa549e8848e43db9b794218eb8bab44700a9e6b110b54d5cd50773ab0ab7`. Alle sechs Datenprüfungen, gezielte MathematikprüfungMA-118/119 und Ebenenprüfung432Karten/864Seiten lokal/live bestanden. Der vollständige Mathematik-Funktionstest wurde lokal mehrfach ausgeführt, blieb wegen Klick-/Scroll-Zeitlimits unvollständig und wird auch live nicht als bestanden behauptet. Kein UI-Code geändert. Nächster Schritt2064/2065;187196 für Tausender/Runden ohne hinreichenden direkten Anschluss entschieden.22 Anschlussfragen und weitere Restumfänge bleiben offen, kein Gesamtabschluss. Nachweis abgeschlossen am26.11.2026.


Mathematik MA-125: Addition/Subtraktion in Teilschritten2065 begrenzt aufMA-120, beide amtlichen Lernzielebenen Übertragen, Zahlenräume1000/100.120 Karten,22 Fragen. [Prüfpaket](curriculum/mathematik/review_batch_125.json). App1.426: Lokale und gezielte Liveprüfungen bestanden; Veröffentlichung geprüft.


MA-125 veröffentlicht: App1.426, Commit `157144fe682a55976e028405e29ec9b685e8fee8`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45765415982). Live-App bytegleich, SHA-256 `589a5691f06a76867ff817197c68db87a7b96c855c3ed7cbdec9e58f9db7ea19`. Sechs Datenprüfungen, gezielte MathematikprüfungMA-032/089/120 und Ebenenprüfung433Karten/866Seiten lokal/live bestanden. Kein neuer vollständiger Funktionslauf aller120 Mathematikkarten, keine UI-Codeänderung. Nächster Schritt187197;2065 erstmals für den Teilschrittweg begrenzt geprüft,2064 nur Kontext.120 Karten,22 offene Anschlussfragen,15 ganze Nichtanschlüsse und220 Inventurzeilen. Kein Gesamtabschluss.


Mathematik MA-126: Rechenwegreflexion187197 im FSP-Wahlbereich Tierwelt begrenzt aufMA-121; amtlichGS Übertragen/FSP Anwenden. GS1000/FSP100 (didaktisch aus Bandziel).121 Karten,22 Fragen. [Prüfpaket](curriculum/mathematik/review_batch_126.json). App1.427: Lokale und gezielte Liveprüfungen bestanden; Veröffentlichung geprüft.


MA-126 veröffentlicht: App1.427, Commit `5fd452dfbb6dba6b8b4c605c894dff091e19111f`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45789271925). Live-App bytegleich, SHA-256 `e52ea2746dac3f51c851f8ae79c874192fa04696edeb4f0e0df3d4561c22b9c7`. Sechs Datenprüfungen, gezielte MathematikprüfungMA-037/120/121 und Ebenenprüfung434Karten/868Seiten lokal/live bestanden. Kein neuer vollständiger Funktionslauf aller121Mathematikkarten, keine UI-Codeänderung. Nächster Schritt: Restumfang187197 (Notationsformen/Pflichtbereich); Rechenwegreflexion im Tierwelt-Wahlbereich erstmals begrenzt geprüft,2064 nur Kontext.121 Karten,22 offene Anschlussfragen,15 ganze Nichtanschlüsse und220 Inventurzeilen. Kein Gesamtabschluss.


Mathematik MA-127: Beschreiben eigener Teilschrittwege aus187197 auf bestehenderMA-120 ergänzt, beiderseits amtlich Übertragen. Zahlenräume1000/100 ausdrücklich belegt.121 Karten,22 Fragen; keine neue Karte oder Erstzählung. [Prüfpaket](curriculum/mathematik/review_batch_127.json). App1.428: Lokale und gezielte Liveprüfungen bestanden; Veröffentlichung geprüft.


MA-127 veröffentlicht: App1.428, Commit `8bafdc5bdd3bd125b64037c019efe45a156520af`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45795739745). Live-App bytegleich, SHA-256 `68232affad658e502af6660c72a236fc1b2cc14f21903999af55ac2c2e9552b8`. Sechs Datenprüfungen, gezielte MathematikprüfungMA-037/120/121 und Ebenenprüfung434Karten/868Seiten lokal/live bestanden. Kein neuer vollständiger Funktionslauf aller121Mathematikkarten, keine UI-Codeänderung. Nächster Schritt: Restumfang187197 (Variantenabwägung/Notationsformen35509); eigene Rechenwege auf bestehenderMA-120 ergänzt, keine neue Karte oder Erstzählung,2064 nur Kontext.121 Karten,22 offene Anschlussfragen,15 ganze Nichtanschlüsse und220 Inventurzeilen. Kein Gesamtabschluss.

Mathematik MA-128: Pflichtbereichsabwägung aufMA-122, GS Übertragen/FSP Einblick gewinnen. GS1000/FSP100 didaktisch abgeleitet.122 Karten,23 Fragen; keine neue Erstzählung. Sechs Datenprüfungen, gezielte KartenprüfungMA-120/121/122 und Ebenenprüfung435Karten/870Seiten lokal und live bestanden; Veröffentlichung geprüft.


MA-128 veröffentlicht: App1.429, Commit `c91459564407a258c6ecb57459ba2016b6d4e7ff`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45814581876). Live-App bytegleich, SHA-256 `02b357f87f027a436dda8d0ae89d44686dd77983c76f5e23576a14e1143b2eb6`. Sechs Datenprüfungen, gezielte MathematikprüfungMA-120/121/122 und Ebenenprüfung435Karten/870Seiten lokal/live bestanden. Kein neuer vollständiger Funktionslauf aller122Mathematikkarten, keine UI-Codeänderung. Nächster Schritt: Umkehroperation187198; Rest187197 zu Notationen/breiteren Vergleichen ausdrücklich im Fragenregister gesichert.122 Karten,23 offene Anschlussfragen,15 ganze Nichtanschlüsse und220 Inventurzeilen. Keine neue Erstzählung187197; kein Gesamtabschluss. Deutsch-Abschluss unverändert.

Mathematik MA-129: Umkehrkontrolle von Addition/Subtraktion aufMA-123, beide amtlich Übertragen. GS1000/FSP100 ausdrücklich; Fehler-/Kontrollwerte eingeschlossen.123 Karten,23 Fragen; eine Erstprüfung187198. Sechs Datenprüfungen, gezielte KartenprüfungMA-038/120/123 und Ebenenprüfung436Karten/872Seiten lokal und live bestanden; Veröffentlichung geprüft.


MA-129 veröffentlicht: App1.430, Commit `efc397ede77a78f47d6334db20aa01648a18828a`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45816040398). Live-App bytegleich, SHA-256 `604af20f644a204425fb04ec1598c0da09552f194c9386ae3ffa598f50b2dfd7`. Sechs Datenprüfungen, gezielte MathematikprüfungMA-038/120/123 und Ebenenprüfung436Karten/872Seiten lokal/live bestanden. Kein neuer vollständiger Funktionslauf aller123Mathematikkarten, keine UI-Codeänderung. Nächster Schritt: arithmetische Muster187199 mit187200/187201.123 Karten,23 offene Anschlussfragen,15 ganze Nichtanschlüsse und220 Inventurzeilen. Eine Erstprüfung187198; kein Gesamtabschluss. Deutsch-Abschluss unverändert.

Mathematik MA-130: gleichschrittige Zahlenfolgen aufMA-124, amtlich GS Übertragen/FSP Beherrschen. GS1000/FSP100 ausdrücklich; weiterführende Regeln als Restfrage gesichert.124 Karten,24 Fragen; zwei Erstprüfungen187199/187200. Sechs Datenprüfungen, gezielte KartenprüfungMA-016/039/124 und Ebenenprüfung437Karten/874Seiten lokal und live bestanden; Veröffentlichung geprüft.


MA-130 veröffentlicht: App1.431, Commit `320a421d433275d81c98b5abd80a7ae869ea7923`, [erfolgreicher Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/45824996936). Live-App bytegleich, SHA-256 `270475af09ad97dd70753b6c913b4dfe1d7d3a5bc03af19fbe996de31bc6e3bb`. Sechs Datenprüfungen, gezielte MathematikprüfungMA-016/039/124 und Ebenenprüfung437Karten/874Seiten lokal/live bestanden. Kein neuer vollständiger Funktionslauf aller124Mathematikkarten, keine UI-Codeänderung. Nächster Schritt: strukturierte Aufgabenformate187201.124 Karten,24 offene Anschlussfragen,15 ganze Nichtanschlüsse und220 Inventurzeilen. Zwei Erstprüfungen187199/187200; eine gemeinsame weiterführende Regelfrage einmal gezählt. Kein Gesamtabschluss. Deutsch-Abschluss unverändert.
