# Informationen für Lehrkräfte: FSP-Inhalte und GS-Gegenbezüge

App 1.322 ergänzt einen separaten Informationsbereich mit Fachfilter, zehn Fällen, direkt verlinkten amtlichen Lehrplanauszügen und aufklappbaren GS-Gegenbezügen. Er verändert keine Anschlusskarten, Feinziele, Kriterien, Entwürfe oder Fortsetzungspunkte. Aufgaben und Hilfsmittel werden nicht ergänzt. Der Bereich wird nicht in den Planungsoutput übernommen und beim Drucken ausgeblendet.

`review_001.json` enthält die geprüften Quellenzeilen. `teacher_info.json` übernimmt diese unverändert und ergänzt Titel und fachliche Einordnungen aus `offene_inhalte_2026-11-07.md`. `fsp_source_inventory.json` dokumentiert das gesichtete FSP-Korpus, keine abgeschlossene Einzelprüfung. Zwei konkrete Spezifizierungen, sechs Teil- oder wahlabhängige Bezüge und zwei Abgrenzungsfälle dürfen nicht als zehn vollständige Inhaltslücken gezählt werden. Andere Grundschulfächer sind nicht vollständig geprüft.

`assets/fsp-info.js` rendert ausschließlich Informationen und greift nicht auf den Planungszustand oder gespeicherte Lehrkraftentwürfe zu. Quellen werden in einem neuen Tab geöffnet. Zielwortlaut und übergeordnetes Hauptziel sind getrennt; die Bemerkungsfälle zeigen ausdrücklich die Bemerkung. Die Ausgangsdateien werden direkt in das HTML eingebettet, sodass die Übersicht auch lokal ohne zusätzliche Netzabrufe funktioniert. Die amtlichen Quellenlinks benötigen eine Internetverbindung.

Reproduktion und Prüfung:

1. `python3 scripts/update-fsp-info.py` (wird auch durch `scripts/prepare-pages.py` aufgerufen).
2. `python3 scripts/update-mathematik.py`, `python3 scripts/check-deutsch.py`, `python3 scripts/prepare-pages.py`, `python3 scripts/check-mathematik.py`, `python3 scripts/test-mathematik-scope.py`, `python3 scripts/check-fsp-info.py`.
3. `node scripts/check-mathematik-browser.cjs` und `node scripts/check-fsp-info-browser.cjs`; `LZK_APP_URL` setzt bei Bedarf die öffentlich ausgelieferte App.

Veröffentlichungsnachweise stehen in `release_001.json`.
