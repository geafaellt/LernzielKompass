# Gemeinsame Lerngegenstände · Deutsch und Sachunterricht

Formulierungsprüfung DE-SU-LG-001, App 1.330, 08.11.2026. Alle 178 Deutsch- und 135 Sachunterrichtskarten wurden auf die Formulierung ihres gemeinsamen Lerngegenstandes geprüft. Keine wortgleichen Kopien der angezeigten Kartentitel. 25 Deutsch- und 100 Sachunterrichtsvorschläge wurden präzisiert; 153 beziehungsweise 35 bereits geeignete Vorschläge bleiben erhalten.

Der gemeinsame Lerngegenstand benennt eine Sache, Frage, einen Text, eine Situation oder eine fachliche Beziehung. Lernziele, Operatoren und Arbeitsaufträge werden davon unterschieden. Ein Textprogramm, eine Karte oder ein Verfahren kann selbst belegter Gegenstand sein; daraus folgt keine automatische Werkzeug- oder Aufgabenwahl. Geeignete Text- und Sachfragen werden nicht bloß umformuliert, um anders zu klingen. Gleiche Gegenstände bei unterschiedlichen Klassenstufen sind zulässig.

Bedingte Anschlüsse behalten ihre Voraussetzungen. Bei SU-028 und SU-061 bleibt es ausdrücklich bei einer methodischen Brücke zwischen verschiedenen Bezugsräumen. Wahlbereiche und konkrete gemeinsame Text-/Art-/Ortsauswahl werden nicht stillschweigend vorausgesetzt. Die Fachgrenzen und unterschiedlichen Zielnachweise auf den Karten gelten weiter.

## Daten und Reproduktion

`overrides.json` enthält ausschließlich die 125 redaktionell überarbeiteten didaktischen Formulierungen. Analog zur bestehenden Kartentitel-Ebene werden sie nach dem Laden der Fachmodule auf `shared_object_suggestion` angewandt. Damit verwenden Anzeige, Übernahme, Bewertungskontext und Planungsübersicht denselben Text. `scripts/prepare-pages.py` bettet die Datei ein und synchronisiert beide HTML-Einstiege. Der geschützte Sachunterrichtsbestand und der reproduzierbare Deutschbestand bleiben unverändert; die redaktionelle Ebene überlebt deren erneuten Aufbau.

`review_001.json` dokumentiert für alle 313 Karten Entscheidung, Vorher/Nachher, Begründung und bestehende Quellenreferenzen. Geprüft wurde die didaktische Formulierung innerhalb vorhandener Karten, keine vollständige neue amtliche Quellen- oder Anschlussprüfung. Keine neuen Zielzeilen, Anschlusskarten oder Operatoren; Fortschrittszähler bleiben unverändert. Mathematikvorschläge aus App 1.329 bleiben unverändert im Mathematikmodul.

Prüfung: `scripts/check-learning-objects.py` und `scripts/check-learning-objects-browser.cjs`, außerdem bestehende Deutsch-/Mathematik-/Zahlenraumprüfungen und Kartenauswahl. Der Browserdurchlauf prüft alle 313 Karten auf Anzeige, ausdrückliche Übernahme, Planungsoutput, leere Aufgaben-/Hilfsmittelfelder und unveränderte eigene Texte. Strukturelle Prüfungen ersetzen keine fachliche Beurteilung neuer Formulierungen. Veröffentlichungsnachweise stehen im Prüfpaket.

## Korrektur der Kartenauswahl

Der vollständige Browserdurchlauf deckte sechs zuvor nicht erreichbare Sachunterrichtskarten auf: SU-126, SU-132, SU-133, SU-135, SU-151 und SU-152. Der Filter verwendet jetzt die strukturierte Klassenangabe statt einer engen Schreibweisenprüfung im Quelltext. SU-020/SU-126 (Klasse 3) und SU-065 (Klasse 4) stehen unter „Übergreifende fachliche Ziele“. Bestehende Auswahlen dieser Karten werden dem richtigen Bereich zugeordnet; eigene Texte bleiben erhalten. Keine neue Karte und keine Änderung der curricularen Anker.
