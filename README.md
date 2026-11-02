# LernzielKompass

Der LernzielKompass unterstützt Lehrkräfte bei der Planung lernzieldifferenzierten Unterrichts im Förderschwerpunkt Lernen in Sachsen. Er stellt begrenzte Anschlussvorschläge zwischen Lehrplanzielen gegenüber und macht gemeinsame Lerngegenstände, unterschiedliche Operatoren sowie didaktisch konkretisierte Feinziele und Erfolgskriterien nachvollziehbar.

**[Veröffentlichte App öffnen](https://geafaellt.github.io/LernzielKompass/)** · **App 1.301** · **Fachlicher Deutsch-Prüfstand: DE-UZ-049 vom 02.11.2026**

Diese Übersicht wurde am 02.11.2026 mit den Projektnachweisen abgeglichen. Der Stand DE-UZ-041 / App 1.294 ist inzwischen fortgeschrieben. Maßgeblich für spätere Fortschritte sind die unten verlinkten Prüfdateien.

**Die App ist veröffentlicht und befindet sich in fachlicher Erprobung. Die Gesamtprüfung ist nicht abgeschlossen.** Eine vorhandene Karte oder technisch funktionierende Anzeige bedeutet weder vollständige Lehrplanabdeckung noch abgeschlossene fachliche Einzelprüfung aller zugeordneten Unterziele.

## Umfang der vorhandenen Lehrplanvergleiche

| Bereich | Vorhandener Umfang | Einordnung des Prüfstands |
| --- | --- | --- |
| Sachunterricht, Grundschule 1–4 | 135 Anschlusskarten; GS Sachunterricht ↔ FSP Deutsch-Heimatkunde/Sachunterricht, ausschließlich Stufenbänder 1/2 und 3/4; Datenbasis v2.46 | Der dokumentierte ZA-Prüfumfang wurde bearbeitet; die Projektverantwortliche hat die 21 ZA-Punkte am 23.10.2026 inhaltlich freigegeben. Das ist keine amtliche Freigabe und keine Aussage vollständiger Zieldeckung. Der Bestand bleibt bei den Deutsch-Erweiterungen unverändert. |
| Deutsch, Grundschule 1–4 | 178 Anschlusskarten; GS 1/2, 3 und 4 ↔ FSP Deutsch-Heimatkunde/Sachunterricht 1/2 und 3/4 | Quellenbasierter Abgleichsentwurf mit fortlaufender Einzelprüfung; aktueller Stand und Restumfang siehe unten. |
| Mathematik, Oberschule und weitere Fächer | In dieser veröffentlichten Fassung keine freigeschalteten Vergleiche | Mathematik und Oberschule sind in der Auswahl als „noch nicht geprüft“ deaktiviert. Sie gehören zum Entwicklungsziel, nicht zum bereits verfügbaren Prüfbestand. |

Die FSP-Stufenbänder werden nicht als Einzelklassen interpretiert. Stufenübergreifende Zuordnungen und notwendige Wahlbereiche sind zu beachten. Sekundarstufenanschlüsse gehören nicht zum aktuellen Deutsch-Abgleich.

Grundlagen sind die sächsischen Lehrpläne GS Deutsch (Fassung 2026), GS Sachunterricht (Überarbeitung 2019) und FSP Lernen Deutsch-Heimatkunde/Sachunterricht (2019). Der Sächsische Rechtschreibrahmen 2025 wird im Deutsch-Abgleich ergänzend zur fachlichen Abgrenzung herangezogen; er erzeugt keine zusätzlichen FSP-Ziele. Quellenanker und gesicherte Fassungen sind im Repository dokumentiert.

## Deutsch: erreichter Prüfstand und offene Arbeit

Quelle: [review_progress.json](curriculum/deutsch/review_progress.json), [Einzelprüfungen je Zielzeile](curriculum/deutsch/row_audit.csv) und [Prüfpaket DE-UZ-049](curriculum/deutsch/review_batch_049.json).

| Kennzahl | Stand DE-UZ-049 | Bedeutung |
| --- | ---: | --- |
| Vorhandene Deutsch-Karten | 178 | Begrenzte Anschlussvorschläge; keine Zahl vollständig geprüfter Kompetenzen. |
| GS-Zielblöcke mit Erstabgleich | 117 | Die Inventur enthält 488 GS- und 451 FSP-Zeilen. Erstabgleich und Inventur ersetzen keine Einzelprüfung. |
| Zuvor offene Unterzielzeilen erstmals geprüft | 241 | Diese erste Prüfphase ist abgearbeitet; Wiederprüfungen werden nicht erneut mitgezählt. |
| Unterzielzeilen ohne Karte | 137 | Zusammensetzung: 125 begründete Nichtanschlüsse, 11 belegte übergreifende Teilanschlüsse ohne Karte und eine offene Anschlussfrage. |
| Davon: begründete Nichtanschlüsse | 125 | Für den jeweils geprüften Zielausschnitt ist kein hinreichend belegter direkter Anschluss nachgewiesen; kein pauschaler Ausschluss jeder didaktischen Verbindung. |
| Davon: übergreifende Teilanschlüsse ohne Karte | 11 | Positive Belege aus übergreifenden Zielen; bewusst keine Operatorenkarte mit einem erfundenen oder entliehenen Tabellenoperator. |
| Offene Anschlussfragen / vorgemerkte Quellen-Nachprüfungen dieser Phase | 1 / 0 | Die früheren 22 Anschlussfragen sind begrenzt entschieden. Bei der Prüfung zuvor zugeordneter Zeilen kam die Frage zum vorbereitenden Aufbau von Hörverstehen (186303) hinzu. |
| Bereits zugeordnete Unterzielzeilen einzeln geprüft | 110 | Separat von den 241 zuvor offenen Zeilen gezählt. |
| Bereits zugeordnete Unterzielzeilen noch einzeln zu prüfen | **20** | Die offene Anschlussfrage bleibt bei neuer Evidenz vorrangig; diese Zuordnungen sind noch nicht vollständig fachlich gegengeprüft. |

Die Rechnung lautet **137 = 125 + 11 + 1**. Daneben sind 22 übergeordnete Zielblöcke ohne Karte gesondert erfasst; sie werden nicht als Unterziele mitgezählt. Karten, hierarchische Lehrplanzeilen und Zielblöcke sind unterschiedliche Zähleinheiten und erlauben keine einfache Abdeckungsquote.

**Nächster Prüfschritt:** `page908_186303` – „Aufbauen von Hörverstehen“, GS 1/2; Phase `uncertain_connections`. Ohne neue Evidenz zu dieser Anschlussfrage werden die 20 verbleibenden bereits zugeordneten Unterzielzeilen ab `page908_186901` (GS4 Planungsschritte) in Inventurreihenfolge geprüft. Eine Rückwärts-Einzelprüfung vom FSP-Lehrplan zur Grundschule ist nicht durchgeführt. Im Fortschrittsprotokoll bleibt `complete: false`.

## Was die Nachweise aussagen – und was noch offen ist

| Ebene | Belegt bzw. geprüft | Grenze |
| --- | --- | --- |
| Technische Daten- und Funktionsprüfung | Karten-IDs, Quellenreferenzen, Operatoranker, Stufenbänder, eingebettete Daten und JavaScript-Syntax; identische App-Dateien in `index.html` und `dist/index.html`. Dokumentierte Browserprüfungen umfassen Auswahl und Anzeige der neuen Karten DE-175–179 sowie der präzisierten Karte DE-021. Frühere Prüfungen betreffen unter anderem Fachwechsel, getrennte Entwürfe und Planvorschau. | Das belegt technische Konsistenz und die jeweils getesteten Abläufe, keine fachliche Vollständigkeit. Nicht alle Funktionen wurden mit jedem Prüfpaket erneut im Browser getestet. Ein erfolgreicher PDF-Download ist bislang nicht bestätigt. |
| Fachlich belegte Anschlussvorschläge | Einzelbegründungen, konkrete Quellenanker, unterschiedliche Anforderungen, Voraussetzungen und Restumfang stehen in den Prüfpaketen. Auch die 11 übergreifenden Teilanschlüsse ohne Karte sind positive fachliche Ergebnisse. | Ein Teilanschluss gilt nur für den ausdrücklich belegten Ausschnitt. Er bedeutet weder identische Leistungsanforderungen noch vollständige Abdeckung des GS-Ziels. Fehlende Karte bedeutet nicht automatisch fehlenden Anschluss. |
| Noch nicht abgeschlossene Prüfungen | 46 bereits zugeordnete Deutsch-Unterzielzeilen und eine neue Anschlussfrage bleiben zu prüfen; eine vollständige Rückwärts-Einzelprüfung ist nicht nachgewiesen. | Weder sämtliche Deutsch-Karten noch der gesamte Lehrplanvergleich dürfen als abschließend fachlich freigegeben bezeichnet werden. |

Die technische Prüfung `python3 scripts/check-deutsch.py` wurde für diese README-Aktualisierung am 02.11.2026 erfolgreich ausgeführt. Die Aussagen zu Browser- und Veröffentlichungstests stammen aus den verlinkten Prüfprotokollen; mit dieser Dokumentationsänderung wurde kein neuer Browser- oder PDF-Test durchgeführt.

## Nutzung und fachliche Rückmeldung

Die Anschlussvorschläge dienen der Unterrichtsplanung und fachlichen Gegenprüfung. Amtliche Lehrplanziele, Unterziele und Bemerkungen bleiben von didaktischen Feinzielen und Erfolgskriterien zu unterscheiden. Die Eignung für die konkrete Lerngruppe beurteilt die Lehrkraft.

**Lernhandlung/Aufgabe und Hilfsmittel bestimmt ausschließlich die Lehrkraft.** Sie werden nicht aus den Anschlusskarten vorgeschlagen oder übernommen. Der Feinziel-Übernahmebutton übernimmt nur Feinziel und Erfolgskriterium. Motivationsentwicklung wird nicht aus einer einzelnen Leistung oder bloßer Teilnahme abgeleitet oder benotet.

Für Rückmeldungen bitte Karten-ID bzw. Zielzeilen-ID, Schulart/Klassenstufe, Lehrplanstelle und die konkrete fachliche Frage oder Korrektur benennen. Besonders hilfreich sind Hinweise zu Operatoren, Voraussetzungen, stufenübergreifenden Anschlüssen und zu weit gefassten Zielausschnitten. Rückmeldungen können als [GitHub-Issue](https://github.com/geafaellt/LernzielKompass/issues) dokumentiert werden.

## Veröffentlichung und Weiterentwicklung

GitHub Pages ist **bereits eingerichtet und veröffentlicht**: [geafaellt.github.io/LernzielKompass](https://geafaellt.github.io/LernzielKompass/). Veröffentlicht wird der Branch `main` aus dem Repository-Stammverzeichnis `/` über die dortige `index.html`.

App 1.294 wurde bereits erfolgreich veröffentlicht. Der vorangehende dokumentierte Veröffentlichungsstand ist **App 1.295**, Deutsch-Modul `DE-2026-11-01.19`, mit angezeigtem Aktualisierungsdatum 01.11.2026. Die Veröffentlichung des App-Commits `4e7a121a47b7329c7dba37b5d8ad83a33c690365` ist durch den [erfolgreichen Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/41344565023) und die Liveprüfung in [DE-UZ-043](curriculum/deutsch/review_batch_043.json) dokumentiert.

DE-UZ-044 aktualisiert sieben bestehende Karten und veröffentlicht App 1.296, Deutsch-Modul `DE-2026-11-02.1`, mit Aktualisierungsdatum 02.11.2026. Die Veröffentlichung von Commit `e25a01f0b076581a1b5c60608b0313b410818aed` ist durch den [erfolgreichen Pages-Lauf](https://github.com/geafaellt/LernzielKompass/actions/runs/41406578192) und die Liveprüfung aller sieben geänderten Karten in [DE-UZ-044](curriculum/deutsch/review_batch_044.json) dokumentiert. Die gleichwertigen Node-Prüfungen dieses Pakets sind bestanden; der Python-Aufruf ist in dieser Umgebung wegen fehlender Xcode-Werkzeuge nicht verfügbar.

DE-UZ-045 prüft neun weitere zuvor zugeordnete Zeilen erstmals und die Hörverstehensfrage erneut. Sie bleibt offen; ihre beiden möglichen Lesarten sind dokumentiert. App 1.297, Modul `DE-2026-11-02.2`, präzisiert sieben bestehende Karten. Der [Pages-Lauf 41407924083](https://github.com/geafaellt/LernzielKompass/actions/runs/41407924083) veröffentlichte Commit `84ecd56b5ab1d0ce1d14119a07298c5ac37937e8` erfolgreich. Alle sieben geänderten Karten wurden live geöffnet; Zählstände und Prüfgrenzen stehen in [DE-UZ-045](curriculum/deutsch/review_batch_045.json).

DE-UZ-046 prüft elf weitere zuvor zugeordnete Zeilen erstmals und präzisiert acht vorhandene Karten. Die Hörverstehensfrage bleibt ohne neue Evidenz offen und wird nicht erneut gezählt. App 1.298, Modul `DE-2026-11-02.3`, wurde mit Commit `a1876eda7262d9852ba49d3368cd8bcf00dffbe5` im [Pages-Lauf 41425283078](https://github.com/geafaellt/LernzielKompass/actions/runs/41425283078) erfolgreich veröffentlicht. Liveprüfung aller acht geänderten Karten und Prüfgrenzen sind im [Prüfpaket DE-UZ-046](curriculum/deutsch/review_batch_046.json) dokumentiert.

DE-UZ-047 prüft zehn weitere zuvor zugeordnete Zeilen erstmals und präzisiert elf Karten. App 1.299, Modul `DE-2026-11-02.4`, trennt gemeinsame Inhalte und zusätzliche GS-Anforderungen deutlicher. Commit `0e6caccbf208e1b71e5687a6ceefba446186be6b` wurde im [Pages-Lauf 41426687552](https://github.com/geafaellt/LernzielKompass/actions/runs/41426687552) erfolgreich veröffentlicht. Alle elf geänderten Karten wurden in App 1.299 live geöffnet. Fortschritt und Prüfgrenzen stehen in [DE-UZ-047](curriculum/deutsch/review_batch_047.json).

DE-UZ-048 prüft dreizehn weitere zuvor zugeordnete Zeilen erstmals und präzisiert neun Karten. App 1.300, Modul `DE-2026-11-02.5`, unterscheidet insbesondere die Anforderungen an Wortarten, Satzarten und szenisches Gestalten. Commit `f927dd3749c6a908a22063c337b60b7f20f3e1aa` wurde im [Pages-Lauf 41445411424](https://github.com/geafaellt/LernzielKompass/actions/runs/41445411424) erfolgreich veröffentlicht. Alle neun geänderten Karten wurden live geöffnet. Fortschritt und Prüfgrenzen stehen in [DE-UZ-048](curriculum/deutsch/review_batch_048.json).

DE-UZ-049 prüft dreizehn weitere zuvor zugeordnete Zeilen erstmals, präzisiert neun Karten und korrigiert die Wort-/Satzebenen-Zuordnung mit der neuen Karte DE-180. App 1.301, Modul `DE-2026-11-02.6`, erhält alle vorhandenen IDs. Die Veröffentlichung über [Pages-Lauf 41447679721](https://github.com/geafaellt/LernzielKompass/actions/runs/41447679721) war erfolgreich; alle zehn betroffenen Karten wurden live geöffnet. Fortschritt und Prüfgrenzen stehen in [DE-UZ-049](curriculum/deutsch/review_batch_049.json).

Seit dem 01.11.2026 erfolgen Weiterentwicklungen ausschließlich in `geafaellt/LernzielKompass`, Branch `main`. Die [bisherige Sites-Prüfseite](https://lernzielkompass.dcxn2pwhpk.chatgpt.site) bleibt unverändert auf Site-Version 103 und ist nicht die aktuelle Veröffentlichung.

Für Änderungen an der App ist `dist/index.html` die Quelldatei; `index.html` ist der synchronisierte Pages-Einstieg. Vor einer App-Veröffentlichung:

```sh
python3 scripts/check-deutsch.py
python3 scripts/prepare-pages.py
```

Anschließend `dist/index.html` und `index.html` gemeinsam committen. `prepare-pages.py` synchronisiert die Dateien und setzt das Veröffentlichungsdatum in Berliner Zeit. Für die Neuerzeugung der Deutschdaten gilt die Reproduktionsfolge in der [Deutsch-Dokumentation](curriculum/deutsch/README.md). Reine Audit- oder README-Änderungen erfordern keine neue App-Version. Die verbindlichen Arbeitsregeln stehen in [AGENTS.md](AGENTS.md).

## Prüfnachweise zum Nachlesen

- [Aktueller Deutsch-Fortschritt und nächster Prüfschritt](curriculum/deutsch/review_progress.json)
- [Deutsch-Zeilenprüfung mit Kartenbezug und Restumfang](curriculum/deutsch/row_audit.csv)
- [Deutsch-Prüfverlauf, technische Nachweise und Reproduktion](curriculum/deutsch/README.md) – chronologisch fortgeschrieben; ältere Abschnitte beschreiben historische Stände.
- [Jüngstes Prüfpaket DE-UZ-049](curriculum/deutsch/review_batch_049.json) und [aktuelle Deutschdaten](curriculum/deutsch/deutsch_module.json)
- [Sachunterricht: Daten, Quellen, Prüfverlauf und Freigabe der 21 ZA-Punkte](curriculum/sachunterricht/baseline.json) – für den Abschluss dieses Prüfumfangs sind `next_review` und `user_approval` vom 23.10.2026 maßgeblich; ältere Inventurtexte enthalten noch frühere offene Arbeitsschritte.
- [Gesicherte Deutsch-Quellenfassungen](curriculum/deutsch/sources/)
