"""Build reviewed-scope German comparison proposals from versioned target inventories.
Each link is a manually selected, limited intersection; no whole-block equivalence.
"""
from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parent
GS=json.loads((ROOT/'gs_inventory.json').read_text());FSP=json.loads((ROOT/'fsp_inventory.json').read_text())
grows={r['id'].split('_')[-1]:r for r in GS['rows']}; frows={r['id'].split('_')[-1]:r for r in FSP['rows']}
blocks={b['id'].split('_')[-1]:b for a in GS['areas'] for b in a['blocks']}
terms=['Einblick gewinnen','Sich positionieren','Übertragen','Beherrschen','Anwenden','Kennen','Entwickeln','Verwenden']
def op(t):return next((x for x in terms if t.startswith(x)), 'Kein einheitlicher Operator ausgewiesen')
topics=[]
def T(key,title,gids,fids,obj,action,fg,limit,gsrows=()):
 topics.append(dict(key=key,title=title,gs=gids.split(),fsp=fids.split(),object=obj,action=action,fsp_goal=fg,limit=limit,gsrows=list(gsrows)))
# Oral communication: thematic FSP context is preserved in each shared object.
T('erzaehlen','Von einem gemeinsamen Schulfest erzählen','186271 186526','40282 40303 40291','Ein gemeinsam erlebtes Schulfest','den Ablauf des Festes in verständlicher Reihenfolge erzählen','Von einem gemeinsamen Schulfest in geordneter Folge erzählen und das gemeinsame Verhalten mit einem passenden Grund einschätzen.','FSP-Kontext: Klassengemeinschaft und Feste. Kein Beleg für sämtliche Erzählformen, Fachsprache oder den Einsatz einer Diktierfunktion.', ['186273','186527'])
T('sprechen-mittel','Stimme und Körpersprache im Theaterspiel','186281 186534 186847','40550 40556 40557 40558','Eine ausgewählte Szene aus einem gemeinsam gelesenen Märchen','Stimme und Körpersprache passend zu einer Rolle einsetzen','Den Inhalt der bekannten Szene auf ein szenisches Spiel übertragen und passende sprachliche Mittel, Mimik und Gestik einsetzen.','Nur bei tatsächlicher Wahl des FSP-Wahlbereichs 4. Keine vollständige Abdeckung von Sprachvarietäten.',['186282','186283','186535','186536'])
T('gespraech12','Bitten, danken, fragen und antworten','186287','39702 39708 39710 39711 39714','Eine Bitte um Hilfe im Klassenalltag','passende höfliche Sprachformen nennen und einer Gesprächssituation zuordnen','Gelernte Sprachformen des Bittens, Dankens, Fragens und Antwortens in vertrauten Situationen wiedergeben.','Formulierungen kennen ist nicht gleichbedeutend mit einer selbstständig entwickelten Gesprächskultur.',['186293'])
T('gespraech34','Gesprächsregeln und begründete Meinungen','186538 186849 186852 186840','40282 40289 40291','Eine Gesprächsregel für den Klassenrat','eine Gesprächsregel einhalten und die eigene Einschätzung mit einer Beobachtung begründen','Das Verhalten in einer konkreten Klassensituation einschätzen und die eigene Meinung dazu begründen.','FSP-Ziel: Positionierung zum Leben in der Klassengemeinschaft. Kein vollständiger Beleg für Fachsprache, digitale Gesprächsregeln oder sämtliche Gesprächsformen.',['186543','186546','186850','186842','186856','186858'])
T('vortrag12','Ein Jahreszeitengedicht vortragen','186295','39754 39768','Ein bekanntes Gedicht zur aktuellen Jahreszeit','ein geübtes kurzes Gedicht verständlich vortragen','Ein bekanntes Jahreszeitengedicht vortragen und seine Aussagen der passenden Jahreszeit zuordnen.','Gedichtvortrag ist unter dem FSP-Ziel zur zeitlichen Orientierung eingebunden. Kein eigenständiges FSP-Ziel zum systematischen Erlernen aller Präsentationsstrategien.',['186297'])
T('vortrag34','Literarische Texte vortragen','186548 186859 186994','40480 40484 40485','Ein ausgewählter kurzer literarischer Text','einen vorbereiteten Text verständlich und passend zum Inhalt vortragen','Den bekannten literarischen Text nach Vorbereitung ausdrucksvoll lesen und seinen Inhalt wiedergeben.','Präsentationsplanung, digitale Produktion und selbstständige Strategieauswahl sind nicht vollständig abgedeckt.',['186549','186862','186995'])
T('zuhoeren12','Einem Märchen gezielt zuhören','186299','39869 39876 39879','Ein gemeinsam gehörtes kurzes Märchen','nach einem Hörauftrag eine wesentliche Information aus dem Märchen wiedergeben','Dem Märchen zielgerichtet zuhören und einen wesentlichen Inhalt wiedergeben.','Keine vollständige Gleichsetzung aller Zuhörstrategien, Hörbedingungen und Reflexionsanforderungen.',['186303','186305','186307','186310','186312'])
T('zuhoeren34','Literarischen Hörtext verstehen','186557 186867','40480 40483 40485','Eine kurze vorgelesene Geschichte','wichtige Informationen aus der Geschichte wiedergeben und eine Schlussfolgerung am Gehörten begründen','Der bekannten Geschichte aktiv zuhören und ihren Inhalt verständlich wiedergeben.','FSP belegt Zuhören und Inhaltswiedergabe; versteckte Informationen, Absicht und begründete Schlussfolgerungen sind weitergehende GS-Anforderungen.',['186563','186568','186871'])
T('schrift12','Lauttreue Wörter lesbar schreiben','186315','39267 39274 39281 39286','Beschriftungen zu vertrauten Gegenständen im Klassenraum','ausgewählte Buchstaben und lauttreue Wörter formklar schreiben','Bekannte Laut-Buchstaben-Beziehungen auf das Schreiben weiterer lauttreuer Wörter übertragen.','FSP 1/2: Druckschrift als Erstschrift; kein Beherrschen der Schulausgangsschrift. Wahrnehmungsübungen sind unterstützende Voraussetzungen, kein Ersatz für das Schreibziel.',['186323','186326'])
T('schrift34','Schulausgangsschrift lesbar nutzen','186327 186584 186874','40126 40127','Eine kurze handschriftliche Mitteilung','eine kurze Mitteilung lesbar und zunehmend flüssig schreiben','Bekannte Buchstabenverbindungen der Schulausgangsschrift auf eine neue kurze Mitteilung übertragen und lesbar schreiben.','FSP verlangt Transfer auf Schreiben; GS-Beherrschen verlangt Routine. Individuelle Handschrift und digitale Schreibwerkzeuge sind nicht vollständig durch diesen Ausschnitt belegt.',['186328','186585','186875'])
T('gross12','Großschreibung und Satzschlusszeichen entdecken','186330','39375 39379 39380','Kurze Sätze über Gegenstände im Klassenraum','Nomen und Satzanfänge groß schreiben und ein passendes Satzschlusszeichen benennen','Die erarbeiteten Regeln zur Großschreibung von Substantiven und Satzanfängen sowie zu Satzschlusszeichen wiedergeben.','Nur dieser orthografische Ausschnitt; keine pauschale Abdeckung des Rechtschreibrahmens, der Nominalgruppen oder aller Wortbildungsregeln.',['186339','186340','186341','186342','186343'])
T('gross34','Groß- und Kleinschreibung in Sätzen','186330 186879','40219 40221 40223','Sätze zu einer neuen Bildszene aus dem Klassenalltag','die Groß- und Kleinschreibung ausgewählter Nomen, Verben und Adjektive untersuchen und richtig verwenden','Gelernte Regeln zur Großschreibung von Substantiven und Satzanfängen sowie zur Kleinschreibung von Verben und Adjektiven auf neue Sätze anwenden.','Keine Gleichsetzung mit satzinterner Großschreibung aller nominalisierten Wortarten; diese FSP-Zielzeile nennt Substantive, Verben und Adjektive.',['186339','186340','186341','186881','186882'])
T('schreibbesonderheit','Besondere Sprech- und Schreibweisen vergleichen','186589','40226','Wortpaare mit einem ausgewählten Rechtschreibphänomen, etwa Hund – Hunde','eine erarbeitete Besonderheit der Sprech- und Schreibweise an Modellwörtern erläutern','An ausgewählten Wörtern Unterschiede zwischen Sprechen und Schreiben entdecken.','FSP nennt Auslautverhärtung, Doppelkonsonanten und weitere Phänomene als Bemerkungen; kein Beleg einer systematisch beherrschten Rechtschreibstrategie. Auswahl genau festlegen.',['186592','186594'])
T('abschreiben12','Wörter und Sätze abschreiben','186346','39267 39290','Eine kurze Beschriftung für ein Klassenplakat','eine eingeübte Abschreibfolge beschreiben und erproben','Bekannte Schreibverfahren beim Abschreiben neuer lauttreuer Wörter oder kurzer Sätze nutzen.','Nur Abschreiben; keine vollständige Gleichsetzung von Selbstkontrolle, Fehlerdiagnose und Strategiewahl.')
T('abschreiben34','Abschreibverfahren gezielt nutzen','186346 186604 186885','40126 40135 40142 40144','Ein kurzer Textabschnitt für ein Klassenplakat','eine eingeübte Abschreibfolge nutzen und die Schreibschritte erläutern','Eine erarbeitete Schreibfolge auf das Abschreiben eines vergleichbaren Textabschnitts übertragen.','GS 4 Anwenden verlangt eine neue Anforderung mit selbstständiger Verfahrenswahl; FSP Übertragen bleibt im vergleichbaren Kontext.')
T('wortschatz12','Häufige Inhaltswörter richtig schreiben','186347','39267 39305 39307 39311','Ein kleiner gemeinsamer Wortschatz aus dem Klassenalltag','vereinbarte häufige Inhaltswörter richtig schreiben','Bekannte Schreibweisen auf ausgewählte klassenbezogene oder individuelle lauttreue Wörter übertragen.','Gemeinsame Wörter vorab festlegen; FSP 1/2 ist hier auf lauttreue Wörter begrenzt. Keine identische Wortliste oder Fehlerquote vorgeschrieben.',['186348','186349'])
T('wortschatz34','Klassenbezogene und individuelle Wörter sichern','186347 186605 186886','40126 40148','Ein gemeinsamer Wortschatz für das aktuelle Unterrichtsthema','vereinbarte häufige Inhaltswörter sicher richtig schreiben','Erarbeitete Schreibweisen in vergleichbaren Wort- und Satzaufgaben nutzen.','Wortumfang und Auswahl sind didaktische Festlegungen; kein automatisches Gleichsetzen mit dem gesamten GS-Wortschatz.',['186348','186349','186609','186610','186888','186889'])
T('funktion12','Ausgewählte Funktionswörter schreiben','186350','39267 39308','Ausgewählte kurze Funktionswörter in einfachen Sätzen','die vereinbarten Funktionswörter richtig schreiben','Erarbeitete Schreibweisen auf ausgewählte lauttreue Funktionswörter in vergleichbaren Sätzen übertragen.','FSP 1/2 ausdrücklich Auswahl; keine vollständige Beherrschung der GS-Funktionswortliste.')
T('funktion34','Funktionswörter in Sätzen sichern','186350 186606 186890','40126 40148','Ein festgelegter Satz kurzer Funktionswörter','die vereinbarten Funktionswörter richtig schreiben','Erarbeitete Funktionswörter in vergleichbaren Schreibaufgaben richtig verwenden.','Nur vereinbarter Ausschnitt; keine vollständige Gleichsetzung mit allen GS-Funktionswörtern.')
T('alphabet','Wörter alphabetisch ordnen','186352','40098 40102','Wortkarten für ein kleines Klassenwörterverzeichnis','Wörter nach dem Anfangsbuchstaben alphabetisch ordnen','Die erarbeitete Buchstabenfolge wiedergeben und Wörter nach dem ersten Buchstaben ordnen.','Stufenübergreifend: GS 1/2 ↔ FSP 3/4. FSP Kennen ist keine routinierte alphabetische Ordnung nach mehreren Buchstaben.')
T('woerterbuch','Ein Wort im Wörterverzeichnis suchen','186353 186612 186895','40098 40104','Ein ausgewähltes Wort im kindgerechten Wörterverzeichnis','ein gesuchtes Wort im Wörterverzeichnis finden','Die erarbeitete Suchfolge im Wörterverzeichnis wiedergeben und an einem vertrauten Beispiel nutzen.','FSP belegt keinen vollständigen Umgang mit Zweit-/Drittbuchstaben, Grundformbildung, gesonderten Wortteilen oder digitalen Rechtschreibhilfen.',['186355','186357','186358'])
T('mitteilung','Schreiben als Mitteilung erleben','186360 186618','39316','Eine kurze Nachricht an die Klasse','die Bedeutung einer kurzen Nachricht für ihren Empfänger erläutern','Eine eigene kurze Mitteilung als Möglichkeit des freien Schreibens erproben.','FSP 1/2: Einblick in freies Schreiben; keine vollständige Textproduktionskompetenz. Digitale Kommunikationsformen nicht gleichgesetzt.',['186363','186365'])
T('textplanung','Ein eigenes Buch planen','186369 186620 186899','39934 39938 39941 39945 39947','Ein kleines selbst hergestelltes Bilder- oder Wörterbuch','Ideen und Material für das eigene Buch sammeln und in eine sinnvolle Reihenfolge bringen','Erarbeitete Schrittfolgen auf die Herstellung eines eigenen Buches anwenden: Thema wählen, Material sammeln und Seiten ordnen.','Nur bei gewähltem FSP-WB2. Die Buchherstellung ist kein vollständiger FSP-Beleg für textsortenübergreifende Schreibplanung.',['186372','186373','186623','186624','186901'])
T('einladung','Eine Einladung verfassen','186380 186631','40320 40323','Eine Einladung zu einer gemeinsamen Klassenveranstaltung','eine verständliche Einladung für einen festgelegten Empfänger formulieren','Gelernte sprachliche Mittel und Formen auf eine Einladung zu einem neuen Anlass anwenden.','Der FSP-Anschluss gilt für die Gebrauchsform Einladung; keine pauschale Abdeckung kreativen, produktiven oder kooperativen Schreibens.',['204803','186637'])
T('textschreiben','Eigene Gedanken schriftlich mitteilen','186902','40126 40150','Eine kurze schriftliche Mitteilung im Klassenbriefkasten','eine verständliche Mitteilung mit eigener begründeter Meinung verfassen','Erarbeitete Schreibweisen auf eine eigene kurze Mitteilung übertragen.','Gemeinsam ist die Mitteilung. Begründete Appelle, sämtliche Schreibformen und vollständige Textsortensicherheit sind auf FSP-Seite damit nicht belegt.',['186903','186904'])
T('schriftzeichen','Schrift und Symbole als Informationsträger','186397','39201 39205 39207','Schrift und Symbole im Schulhaus','Schrift und Symbole als Informationsträger erkennen','Bekannte Bilder, Symbole und Schriftzeichen ihren Informationen zuordnen.','Logographemisches Wiedererkennen ist noch kein alphabetisches Lesen.',['186399','186400'])
T('lesen12','Wörter und kleine Texte erlesen','186401 186418 186668 186914','39247 39253 39256 39259 39266','Ein kurzer, altersangemessener Text zum gemeinsamen Unterrichtsthema','Wörter und kurze Sätze sinnverstehend lesen','Bekannte Laut-Buchstaben-Beziehungen auf unbekannte Wörter und einen kleinen Text übertragen und den Sinn wiedergeben.','FSP 1/2: deutlich begrenzter Textumfang; GS 3/4 daher stufenübergreifend. Reines Vorlesen durch andere ersetzt den Nachweis eigenen Lesens nicht.',['186409','186411','186414','186420','186422','186670','186916'])
T('lesen34','In Sinnzusammenhängen lesen','186401 186418 186668 186914','40107 40111 40114 40116','Ein kurzer Sachtext zum gemeinsamen Unterrichtsthema','einen Text flüssig und in sinnvollen Einheiten lesen','Erarbeitete Lesefertigkeiten auf einen unbekannten kleinen Text übertragen und Sinneinheiten beim Lesen beachten.','FSP-Textlänge und sprachliche Komplexität bleiben begrenzt; keine pauschale Gleichsetzung mit GS-Leseflüssigkeit oder selbstständiger Wahl von Leseförderverfahren.',['186414','186416','186417','186420','186421','186670','186916'])
T('sinn12','Eine Textinformation finden','186425','39247 39266','Eine zentrale Information in einem kurzen Bild-Text-Angebot','eine Information im Text finden und in eigenen Worten wiedergeben','Einen kleinen unbekannten Text erlesen und eine inhaltliche Frage mit Textbezug beantworten.','FSP-Sinnerfassung deckt weder das gesamte GS-Strategierepertoire noch das Verknüpfen aller Informationen ab.',['186430','186431','186436'])
T('sinn34','Wesentliches im Text erschließen','186425 186672 186673 186922 186923','40107 40119 40120 40123','Ein kurzer Text mit klar erkennbarer Hauptaussage','wesentliche Textinformationen finden und mit einer passenden Textstelle verbinden','Einen unbekannten kleinen Text erlesen, eine Sinneinheit erkennen und eine wesentliche Information mit Texthilfe wiedergeben.','Nur Sinnerfassung und wesentliche Informationen. Widersprüchliche Aussagen, digitale Navigation, Strategieauswahl und weitergehende Interpretation sind nicht vollständig belegt.',['186430','186431','186432','186433','186434','186436','186699','186703','186927','186933','186934','186935'])
T('literatur12','Ein Märchen erschließen','186442 186450 186459','39869 39879','Ein gemeinsam ausgewähltes Märchen','Inhalte und eine auffällige Eigenschaft des Märchens beschreiben','Einen wesentlichen Inhalt des gehörten oder gelesenen Märchens wiedergeben.','Nur literarischer Ausschnitt; keine vollständige Typologie von Sach-, Gebrauchs- und digitalen Texten. FSP fordert hier keinen umfassenden Gattungsvergleich.',['186443','186455','186456'])
T('literatur34','Kinderliteratur verstehen','186442 186450 186459 186707 186726 186733 186943 186944 186973 186985','40480 40482 40485','Ein gemeinsam gewählter literarischer Text, etwa Märchen oder Fabel','Handlung, Figuren und ein wesentliches Textmerkmal erläutern','Den Inhalt eines erarbeiteten literarischen Textes wiedergeben und handelnde Figuren benennen.','Fabeln und Ortssagen stehen auf FSP-Seite als Beispiele in den Bemerkungen; kein verbindlicher FSP-Auftrag zur vollständigen Gattungsanalyse. Comics sind nicht ausdrücklich ausgewiesen.',['186443','186455','186456','186711','186729','186730','186731','186945','186975','186978'])
T('medienangebot','Ein Kinderbuch auswählen und vorstellen','186447 186717 186953','40480 40482 40486','Ein ausgewähltes Kinderbuch aus der Bibliothek','ein Kinderbuch anhand von Inhalt und eigenen Interessen auswählen und die Auswahl erläutern','Ein bekanntes Kinderbuch in Grundzügen vorstellen und eine Bibliothek als Zugang zu Büchern kennenlernen.','Kein vollständiger Beleg für Verlagswissen, sämtliche Medienquellen oder Glaubwürdigkeitsprüfung von Informationen. Buchvorstellung ist im FSP eine Bemerkung.',['186448','186449','186721','186725','186965','186968'])
T('digital12','Mit einem Textprogramm schreiben','186460','39318 39327 39329 39335 39341','Eine digitale Beschriftung für ein Klassenprodukt','elementare Bedienhandlungen beim digitalen Schreiben erproben','Sprachwissen beim Schreiben einer neuen kurzen Beschriftung im Textprogramm anwenden und Zeichen löschen oder den Text drucken.','Kein vollständiger Anschluss für Wikis, Podcasts, Suchmaschinen, Risiken oder sämtliche Gerätefunktionen.',['186464'])
T('digital34','Digitale Werkzeuge für ein Textprodukt','186460 186739 186987','40153 40157 40159 40162 40163','Ein kurzer Text für ein digitales Klassenplakat','ein einfaches Textprodukt mit einem digitalen Schreibwerkzeug gestalten','Erarbeitete Bedienhandlungen eines Textprogramms wiedergeben und beim Schreiben eines kurzen Textes nutzen.','Nur Schreibwerkzeug. Kritische Informationsprüfung, Datenschutz, Fake News, Nutzungsreflexion und umfassende Medienproduktion bleiben getrennt.',['186464','186745','186990'])
T('praesentation12','Eine Szene spielen','186466','39967 39969 39970 39974 39976','Eine kurze Szene aus einem vertrauten Märchen','eine mögliche szenische Darstellung erproben','Den Inhalt des bekannten Märchens auf ein szenisches Spiel übertragen.','Nur bei Wahl des FSP-WB3; kein vollständiger Anschluss sämtlicher Präsentationsformen.',['186470'])
T('praesentation34','Literatur szenisch gestalten','186466 186746 186994','40550 40556 40557 40558 40559 40560','Eine ausgewählte Szene eines gemeinsamen Textes','eine Szene mithilfe von Stimme, Mimik und Gestik darstellen','Den bekannten Textinhalt auf eine szenische Darstellung übertragen und die eigene Rolle passend gestalten.','Nur bei Wahl des FSP-WB4. Kein vollständiger Nachweis von digitalen Präsentationen und Portfolioarbeit.',['186470','186749','186999'])
T('recherche','Sachinformationen zu einer Einrichtung gewinnen','186734 186986','40395 40397 40399','Informationen über die örtliche Bibliothek als öffentliche Einrichtung','Informationen aus zwei geeigneten Medien zur Einrichtung einholen und vergleichen','Mithilfe einer passenden Quelle Informationen zur Einrichtung gewinnen und eine wichtige Information wiedergeben.','Gemeinsamer Gegenstand muss eine öffentliche oder soziale Einrichtung sein. FSP fordert keine allgemeine Suchmaschinenkompetenz oder systematische Quellenbewertung.',['186737'])
T('sprachhandeln','Höfliche Sprachformen passend einsetzen','186477 186769 187008','39702 39708 39710 39711 39714','Eine Bitte oder Entschuldigung im Schulalltag','eine sprachliche Form passend zur Absicht und zum Gegenüber auswählen und ihre Wirkung erläutern','Gelernte Sprachformen des Bittens oder Entschuldigens in vertrauten Situationen wiedergeben.','FSP 1/2: keine explizite Sprachwirkungsanalyse; nur gemeinsamer situativer Ausschnitt. Sprichwörter, Mehrdeutigkeit, Werbung und Politik nicht mitabgedeckt.',['186478','186777','187009','187010'])
T('kommunikation','Mündlich und schriftlich einladen','186482 186778 187011','40320 40323','Eine mündliche und eine schriftliche Einladung zum selben Anlass','Unterschiede einer mündlichen und schriftlichen Einladung anhand des Empfängers erklären','Gelernte Gebrauchsformen auf eine mündliche und schriftliche Einladung zu einem neuen Anlass anwenden.','FSP-Gebrauchsformen sind belegt; keine vollständige Theorie mündlicher/schriftlicher Kommunikation, keine Chat- oder Emoji-Analyse.',['186483','186484','186781','187015'])
T('wortarten12','Nomen und Verben entdecken','186488','39344 39350 39351 39357 39360 39362 39364','Wörter zu Menschen, Dingen und Tätigkeiten im Klassenraum','Merkmale von Nomen und Verben nennen und an Wörtern zeigen','Erste Unterschiede zwischen Tätigkeitswörtern und Namenwörtern entdecken und passende Beispiele zuordnen.','Nur Nomen, Verb und begleitender Artikel; Adjektive und Nominalgruppen sind in FSP1/2 damit nicht abgedeckt.',['186489','186490','186493','186494','186495','186497'])
T('wortarten34','Wortarten an Beispielen unterscheiden','186488 186788 187020','40166 40169 40171 40173 40175 40177 40179 40182 40185','Wörter und kurze Sätze zu einer gemeinsamen Bildszene','Nomen, Verben und Adjektive anhand erarbeiteter Merkmale unterscheiden','Erarbeitete Merkmale von Nomen, Verben und Adjektiven wiedergeben und an bekannten Wörtern zeigen.','FSP Kennen umfasst nicht sämtliche GS-Merkmale: Prädikatfunktion, Steigerung, Zeitformen und systematische Nominalgruppenanalyse getrennt prüfen.',['186489','186493','186500'])
T('pronomen','Personalpronomen kennenlernen','186789','40192','Namen und Personalpronomen in kurzen Sätzen','die Funktion eines Personalpronomens an einem Satz erklären','Personalpronomen in einfachen Sätzen als Stellvertreter entdecken.','Nur Personalpronomen; kein Anschluss für Präteritum, Adjektivsteigerung oder vollständige Subjektanalyse.',['186801','186802','186803'])
T('wortschatzerweiterung','Ober- und Unterbegriffe bilden','186810 187033','40351 40355','Lebensmittel für ein gemeinsames Pausenfrühstück','Lebensmittelwörter passenden Oberbegriffen zuordnen und die Ordnung begründen','Lebensmittel durch Ober- und Unterbegriffe ordnen und damit eine begründete Auswahl für das Frühstück unterstützen.','FSP-Positionierung zu Ernährungsgewohnheiten ist der Rahmen. Keine vollständige Gleichsetzung mit Wortfamilien, Wortfeldern oder Mehrdeutigkeit.',['186813'])
T('satzarten12','Aussagen, Fragen und Aufforderungen entdecken','186509','39372','Aussage, Frage und Aufforderung zur selben Klassensituation','Satzarten und typische Satzschlusszeichen an bekannten Beispielen unterscheiden','Aussage-, Frage- und Aufforderungssätze anhand von Sprechmelodie und Satzzeichen kennenlernen.','Keine vollständige Abdeckung von Nominalgruppen, Erweiterungsprobe, Subjekt und Prädikat.',['186510','186511'])
T('satzarten34','Satzarten situationsgerecht verwenden','186509','40199','Eine neue Gesprächssituation im Klassenraum','Aussage, Frage und Aufforderung zielgerichtet formulieren und unterscheiden','Gelernte Satzarten in einer neuen Situation mündlich und schriftlich passend verwenden.','Nur Satzarten; GS3/4 fordert zusätzlich Satzglieder, Proben und Erweiterungen, die hier nicht belegt sind.',['186510','186511'])
T('rede','Wörtliche Rede erkennen','186815','40202 40204 40208','Ein kurzer Dialog aus einem gemeinsamen Lesetext','wörtliche Rede mit vorangestelltem Begleitsatz untersuchen und passende Zeichen setzen','Wörtliche Rede im Text anhand von Doppelpunkt und Anführungszeichen entdecken und mit verteilten Rollen lesen.','FSP Einblick ist kein Beleg für selbstständig korrektes Verschriften sämtlicher Formen wörtlicher Rede.',['186819'])
T('position','Zum Verhalten einer Märchenfigur Stellung nehmen','186938','39882 39888 39891','Eine ausgewählte Handlung einer Märchenfigur','eine Bewertung der Figurenhandlung anhand einer Textstelle begründen','Das Verhalten einer Märchenfigur einschätzen und die eigene Meinung mit einem passenden Grund ausdrücken.','Stufenübergreifend GS4 ↔ FSP1/2. Nur Figurenverhalten, keine allgemeine Bewertung sämtlicher sprachlicher Mittel.',['186942'])
from additional_topics import append
append(T)
from batch_002_topics import append as append_batch002
append_batch002(T)
from batch_003_topics import append as append_batch003
append_batch003(T)
from batch_004_topics import append as append_batch004
append_batch004(T)
from batch_006_topics import append as append_batch006
append_batch006(T)
from batch_008_topics import append as append_batch008
append_batch008(T)
from batch_009_topics import append as append_batch009
append_batch009(T)
from batch_010_topics import append as append_batch010
append_batch010(T)
from batch_016_topics import append as append_batch016
append_batch016(T)
from batch_018_topics import append as append_batch018
append_batch018(T)
from batch_019_topics import append as append_batch019
append_batch019(T)
from batch_020_topics import append as append_batch020
append_batch020(T)
from batch_021_topics import append as append_batch021
append_batch021(T)
from batch_026_review import append as append_batch026
append_batch026(T)
from batch_027_review import append as append_batch027
append_batch027(T)
from batch_028_review import append as append_batch028
append_batch028(T)
from batch_029_review import append as append_batch029
append_batch029(T)
from batch_030_review import append as append_batch030
append_batch030(T)
from batch_032_review import append as append_batch032
append_batch032(T)
from batch_033_review import append as append_batch033
append_batch033(T)
from batch_034_review import append as append_batch034
append_batch034(T)
from batch_035_review import append as append_batch035
append_batch035(T)
from batch_037_review import append as append_batch037
append_batch037(T)
from batch_038_review import append as append_batch038
append_batch038(T)
from batch_039_review import append as append_batch039
append_batch039(T)
from batch_041_review import append as append_batch041
append_batch041(T)
from batch_043_review import append as append_batch043
append_batch043(T)
# Explicit exclusions instead of inventing equivalent FSP goals.
exclusions={
 '187034':'Der FSP-Anker zu Satzarten belegt nicht die für GS4 konkretisierten Satzergänzungen. Satzarten sind als stufenübergreifende Wiederaufnahme von GS1/2 gesondert verfügbar.',
 '186344':'Rechtschreibstrategien des GS-Rechtschreibrahmens sind nicht als gleichwertiges systematisches Strategierepertoire im FSP1–4 ausgewiesen. Lautanalyse, Silbenstruktur und Schreibverfahren sind Vorläufer/Teilausschnitte, nicht die gesamte Strategieanforderung.',
 '186602':'FSP-Sprachwissen, Schreibverfahren und Einblick in Sprech-/Schreibunterschiede belegen nicht den systematischen Transfer aller GS-Rechtschreibstrategien.',
 '186883':'Kein Beleg für routiniertes Beherrschen des gesamten GS-Rechtschreibstrategierepertoires in DE-HKS1–4.',
 '186351':'FSP nennt besondere Schreibungen als Beispiele zu einem Einblicksziel, trennt aber nicht ausdrücklich regelgeleitete Schreibungen von echten Merkschreibungen des GS-Rechtschreibrahmens.',
 '186611':'Vokalverdopplung und Dehnungs-h im FSP sind keine pauschalen Merkwörter: Ihre Funktion muss jeweils geprüft werden. Keine fachlich gesicherte Gleichsetzung der GS-Merkschreibungen.',
 '186893':'Das FSP-Einblicksziel zur unterschiedlichen Sprech-/Schreibweise weist kein Beherrschen des GS-Wissens über nicht regelgeleitete Schreibungen aus.',
 '186388':'DE-HKS1–4 enthält Schreiben und Lernkontrolle, aber keinen gleichwertigen spezifischen Zielanker zur kriteriengeleiteten Überarbeitung vollständiger Texte. Didaktisch möglich, hier keine eigenständige Anschlusskarte.',
 '186651':'Kriteriengeleitete Textüberarbeitung, Schreibkonferenz und digitale Revision sind nicht als entsprechender FSP-Zielkomplex belegt. Der übergreifende Kontrollbeleg ist positiv berücksichtigt; der genaue Anschluss der Selbstkontrolle (186659) bleibt nach DE-UZ-031 offen.',
 '186912':'Routinierte Überarbeitung eigener und fremder Texte ist durch FSP-Schreibverfahren und freies Schreiben nicht hinreichend belegt.',
 '186485':'Mehrsprachigkeit und kulturelle Vielfalt erscheinen im FSP in thematischen Bemerkungen; ein systematisches Untersuchen sprachlicher Vielfalt ist kein entsprechendes explizites FSP-Ziel.',
 '186782':'Regionalsprache, Sprachvergleich und Gebärdensprache nicht als entsprechender FSP-Primarstufen-Zielkomplex belegt. Achtung von Vielfalt ist keine sprachsystematische Untersuchung.',
 '187018':'Transferwissen über Sprachvarietäten und Anglizismen ist nicht durch FSP-Hinweise auf kulturelle Vielfalt belegt.',
 '186503':'Das Erlesen von Wortbausteinen im FSP ist rezeptiv; es belegt keine produktive Wortbildung durch Zusammensetzung und Ableitung.',
 '186806':'FSP-Wortbausteine beim Lesen sind keine gleichwertige Zielanforderung zum produktiven Transfer von Wortbildung.',
 '187031':'Kein spezifischer FSP1–4-Zielanker für routiniertes Beherrschen produktiver Wortbildung belegt.',
 '186506':'Wortschatzerweiterung als allgemeines FSP-Ziel ersetzt keinen konkreten Zielbeleg zum Bilden von Wortfamilien und Wortfeldern.',
 '187021':'Perfekt, Futur I, zweiteilige Verbformen und Nomenveränderung sind im geprüften FSP-Primarstufenplan nicht entsprechend ausgewiesen. Allgemeine Verbveränderbarkeit ist keine vollständige Abdeckung.'
}
for id,b in blocks.items():
 if b['target'].startswith('Verwenden der Fachbegriffe:'):
  exclusions[id]='Die Fachbegriffsliste wird nicht als Ganzes gleichgesetzt. Einzelne gemeinsame Begriffe (z. B. Buchstabe, Wort, Satz oder Wortart) werden in passenden Sachkarten benutzt. Weitere Begriffe der GS-Liste sind nicht als entsprechender vollständiger FSP-Begriffsbestand ausgewiesen; genaue Einzelfallprüfung bleibt erforderlich.'
criteria={'erzaehlen': 'Die Ereignisse sind zeitlich geordnet; eine Einschätzung des gemeinsamen Verhaltens wird mit einem konkreten Beispiel begründet.', 'sprechen-mittel': 'Stimme und mindestens ein körperliches Ausdrucksmittel passen erkennbar zur gewählten Rolle und Szene.', 'gespraech12': 'Eine passende Bitte oder Entschuldigung wird verständlich formuliert und der vertrauten Situation zugeordnet.', 'gespraech34': 'Eine eigene Einschätzung wird durch eine konkrete Beobachtung zum Gesprächsverhalten begründet.', 'vortrag12': 'Das Gedicht wird verständlich vorgetragen; mindestens eine Aussage wird zutreffend einer Jahreszeit zugeordnet.', 'vortrag34': 'Der vorbereitete Vortrag berücksichtigt Sinnabschnitte; eine Frage zum Inhalt wird zutreffend beantwortet.', 'zuhoeren12': 'Eine zentrale Handlung wird nach dem Hören zutreffend wiedergegeben; vereinbarte Bildhilfen sind zulässig.', 'zuhoeren34': 'Die wesentlichen Ereignisse werden nach dem Hören in nachvollziehbarer Reihenfolge wiedergegeben.', 'schrift12': 'Die ausgewählten Wörter sind lauttreu aufgebaut und die Buchstaben eindeutig erkennbar.', 'schrift34': 'Buchstabenverbindungen sind erkennbar, Wörter lesbar und Wortgrenzen deutlich.', 'gross12': 'Die Regeln für Substantive, Satzanfänge und Satzschlusszeichen werden an bekannten Beispielen zutreffend gezeigt.', 'gross34': 'Die ausgewählten neuen Sätze zeigen passende Groß- bzw. Kleinschreibung; die zugrunde gelegte Regel ist erkennbar.', 'schreibbesonderheit': 'An einem ausgewählten Wortpaar wird eine konkrete Abweichung von Sprech- und Schreibweise wahrgenommen oder markiert.', 'abschreiben12': 'Die vereinbarte Abschreibfolge wird nachvollziehbar ausgeführt; Buchstabenfolge und Wortgrenzen bleiben erhalten.', 'abschreiben34': 'Der neue Textabschnitt wird nach der erarbeiteten Folge abgeschrieben; die vereinbarten Kontrollschritte sind sichtbar.', 'wortschatz12': 'Die vorab ausgewählten lauttreuen Wörter werden vollständig und mit richtiger Buchstabenfolge geschrieben.', 'wortschatz34': 'Die vereinbarten Wörter werden auch in einer vergleichbaren Satzaufgabe richtig geschrieben.', 'funktion12': 'Die ausgewählten lauttreuen Funktionswörter werden in kurzen vergleichbaren Sätzen richtig geschrieben.', 'funktion34': 'Die vorab vereinbarten Funktionswörter werden in der Schreibaufgabe richtig eingesetzt und geschrieben.', 'alphabet': 'Die ausgewählten Wörter stehen nach ihrem ersten Buchstaben in alphabetischer Reihenfolge.', 'woerterbuch': 'Das vereinbarte Wort wird mithilfe der erarbeiteten Suchfolge im Wörterverzeichnis aufgefunden.', 'mitteilung': 'Die kurze Nachricht enthält eine eigene erkennbare Mitteilungsabsicht und einen verständlichen Inhalt.', 'textplanung': 'Thema, Materialauswahl und Seitenfolge passen zusammen; die Herstellungsschritte werden nachvollziehbar umgesetzt.', 'einladung': 'Anlass, Empfänger sowie die für den konkreten Anlass nötigen Angaben sind verständlich enthalten.', 'textschreiben': 'Die eigene Mitteilung ist verständlich und enthält einen für den Empfänger erkennbaren Inhalt.', 'schriftzeichen': 'Bekannte Schriftzeichen oder Symbole werden ihrer Bedeutung zugeordnet; bloßes Bildraten wird vom Lesen unterschieden.', 'lesen12': 'Ausgewählte Wörter werden selbst erlesen; eine Frage zum Sinn des kleinen Textes wird zutreffend beantwortet.', 'lesen34': 'Der kleine unbekannte Text wird selbst erlesen; sinnvolle Wortgruppen sind erkennbar und eine Inhaltsfrage wird beantwortet.', 'sinn12': 'Eine passende Textinformation wird gefunden und mit einer Frage oder einem Bild zutreffend verbunden.', 'sinn34': 'Eine wesentliche Information wird wiedergegeben und mit einem passenden Abschnitt des Textes verbunden.', 'literatur12': 'Eine zentrale Handlung des Märchens wird in eigenen Worten oder einer passenden Bildfolge wiedergegeben.', 'literatur34': 'Handlung und handelnde Figuren werden in Grundzügen zutreffend wiedergegeben; keine vollständige Gattungsanalyse verlangt.', 'medienangebot': 'Ein bekanntes Buch wird mit Titel oder eindeutiger Kennzeichnung und einer zutreffenden Inhaltsangabe vorgestellt.', 'digital12': 'Die kurze Beschriftung wird im Textprogramm eingegeben; ein vereinbarter Bearbeitungsschritt gelingt.', 'digital34': 'Die erarbeitete Bedienfolge wird gezeigt und ein kurzer lesbarer Text im Schreibprogramm erstellt.', 'praesentation12': 'Rollenhandlung und sprachliche Gestaltung sind auf den Inhalt der bekannten Szene bezogen.', 'praesentation34': 'Die Szene bleibt inhaltlich nachvollziehbar; die eigene Rolle wird mit passenden Ausdrucksmitteln gestaltet.', 'recherche': 'Eine zutreffende Information über die Einrichtung wird aus einer benannten Quelle entnommen und wiedergegeben.', 'sprachhandeln': 'Die gewählte Formulierung passt zur Bitte oder Entschuldigung in der vertrauten Situation.', 'kommunikation': 'Die Einladung enthält die für den Anlass nötigen Informationen und passt zur mündlichen bzw. schriftlichen Form.', 'wortarten12': 'Ausgewählte Namenwörter und Tätigkeitswörter werden unterschieden und mit passenden Beispielen verbunden.', 'wortarten34': 'Ausgewählte Nomen, Verben und Adjektive werden mithilfe erarbeiteter Merkmale richtig zugeordnet.', 'pronomen': 'Ein Personalpronomen wird in einem einfachen Satz erkannt und einer passenden Person zugeordnet.', 'wortschatzerweiterung': 'Lebensmittelwörter sind sinnvoll geordnet; eine Auswahl für das Frühstück wird mit einem passenden Grund erläutert.', 'satzarten12': 'Eine Aussage, Frage oder Aufforderung wird anhand eines bekannten Beispiels erkannt.', 'satzarten34': 'Aussage, Frage und Aufforderung passen zur neuen Situation; beim Schreiben werden passende Schlusszeichen verwendet.', 'rede': 'Eine Stelle wörtlicher Rede wird erkannt; die Rollen beim Lesen sind zutreffend unterschieden.', 'position': 'Eine erkennbare Einschätzung der Figurenhandlung wird mit einem passenden Grund aus der Geschichte gestützt.'}
registry=json.loads((ROOT/'id_registry.json').read_text())
for t in topics:
 for gid in t['gs']:
  key=t['key']+':'+gid
  if key not in registry:registry[key]='DE-'+str(max(int(x.split('-')[1]) for x in registry.values())+1).zfill(3)
(ROOT/'id_registry.json').write_text(json.dumps(registry,indent=2))
connections=[];sources={};associations={};usedrows=set()
source_meta={'gs':('Grundschule Deutsch','2004/2009/2019/2025/2026'),'fsp':('FSP Lernen Deutsch-Heimatkunde/Sachunterricht','2005/2010/2019')}
def source(r,track):
 sid='Q-DE-'+r['id'];sources[sid]={'id':sid,'title':source_meta[track][0]+' · '+r['grade']+' · '+r['target'],'version':source_meta[track][1],'url':r['url'],'checked_on':'2026-10-30'};return sid
context={
 'Verwenden':('den benannten Fachbegriff im passenden Zusammenhang benutzen','Der Fachbegriff wird zutreffend auf das vereinbarte Beispiel bezogen.'),
 'Entwickeln':('individuelle Fortschritte an passenden Aufgaben zeigen','Die Beobachtung beschreibt einen konkreten Fortschritt gegenüber dem dokumentierten Ausgangsstand.'),
 'Einblick gewinnen':('erproben und erste Beobachtungen dazu äußern','Eine zutreffende Beobachtung bzw. ein nachvollziehbarer erster Zugang wird sichtbar; kein Routinenachweis.'),
 'Kennen':('im erarbeiteten Kontext zeigen und erläutern','Die vereinbarte Kenntnis wird an einem bekannten Beispiel fachlich richtig wiedergegeben.'),
 'Übertragen':('auf einen vergleichbaren, noch nicht bearbeiteten Fall übertragen','Das Gelernte wird bei verändertem Beispiel mit erkennbar gleicher Grundstruktur passend genutzt.'),
 'Beherrschen':('sicher und routiniert ausführen','Die vereinbarte Handlung gelingt in mehreren kurzen Durchgängen flüssig und zuverlässig.'),
 'Anwenden':('bei einer neuen Anforderung mit selbst gewähltem Vorgehen nutzen','Die neue Anforderung wird erkannt, ein geeignetes Vorgehen ausgewählt und sachgerecht umgesetzt.'),
 'Sich positionieren':('mit einem nachvollziehbaren Grund beurteilen','Eine erkennbare Position wird durch einen passenden Grund bzw. eine Beobachtung gestützt.')}
for t in topics:
 fr=[frows[i] for i in t['fsp']];f=fr[0];fop=op(f['target']);band=f['grade']; assert all(r['grade']==band for r in fr)
 for gid in t['gs']:
  g=grows[gid];gop=op(g['target']);a=next(a for a in GS['areas'] if a['id']==g['area_id'])
  cid=registry[t['key']+':'+gid]; selected_rows=[r for i,r in grows.items() if i in t['gsrows'] and r['parent_target_id']==g['id']]
  # The parent and selected children are traced separately; other children remain outside the card.
  supports=[g]+selected_rows
  associations.setdefault(gid,[]).append(cid)
  usedrows.update(r['id'] for r in supports)
  ids=[source(r,'gs') for r in supports]+[source(r,'fsp') for r in fr]
  prefix,crit=context.get(gop,('am festgelegten Beispiel zeigen','Die festgelegte Lernhandlung ist beobachtbar.'))
  ggoal='Die Lernenden können '+t['action']+'. Anforderungsniveau: '+gop+' – '+prefix+'.'
  iswahl='Wahlbereich' in f['area'];gsband='1/2' if g['grade']=='1/2' else '3/4'
  scope='Gemeinsamer Zielausschnitt: '+t['object']+'. '+t['limit']
  c={'id':cid,'subject':'Deutsch','theme':t['title'],'app_area':'DE-'+g['area_id'],
     'gs_anchor':f"GS Deutsch Kl. {g['grade']} · {a['title']}; {g['target']}"+(('; Konkretisierung: '+'; '.join(r['target'] for r in selected_rows)) if selected_rows else ''),
     'gs_operator':gop,'fsp_anchor':f"FSP(L) Kl. {band} · DE-HKS {f['area']}; {f['target']}"+('; Zielausschnitt: '+'; '.join(r['target'] for r in fr[1:]) if len(fr)>1 else ''),
     'fsp_operator':fop,'status':'Abgleichsvorschlag · begrenzter Zielausschnitt'+(' · FSP-Wahlbereich erforderlich' if iswahl else ''),
     'review_status':'quellenbasiert_gepruefter_entwurf','user_approval':False,
     'source_ids':list(dict.fromkeys(ids)),'gs_target_ids':[r['id'] for r in supports],'fsp_target_ids':[r['id'] for r in fr],
     'fine_goals':[{'track':'Grundschule','goal':ggoal,'criterion':crit+' Inhaltlicher Bezug: '+t['object']+'.'},{'track':'FSP Lernen','goal':'Die Lernenden können: '+t['fsp_goal'],'criterion':criteria.get(t['key'], t['fsp_goal']+' Die beschriebene Handlung wird am vereinbarten Beispiel beobachtet.')+' Die konkrete Materialmenge und erlaubte Hilfen legt die Lehrkraft vorab fest.'}],
     'task_suggestions':{'GS':'Bearbeite folgenden Gegenstand: '+t['object']+'. Auftrag: '+t['action']+'. '+prefix.capitalize()+'.','FSP':t['fsp_goal']+' Material: '+t['object']+'.'},
     'aid_suggestions':{'GS':'Aufgabe und Umfang vorab festlegen; Hilfen entsprechend dem Ziel zulassen.','FSP':'Bei Bedarf Bild-/Wortkarten, Stützwörter oder eine gegliederte Textvorlage. Hilfen dürfen den geforderten Lese-, Schreib- oder Begründungsnachweis nicht ersetzen.'},
     'shared_object_suggestion':t['object'],'operator_relation':f'GS: {gop}; FSP: {fop}. Der FSP-Operator gehört zum genannten übergeordneten Ziel und wird nur innerhalb seines Sach- bzw. Textkontextes verwendet. '+t['limit'],
     'review_note':scope,'app_review_message':scope+' Feinziele, Aufgaben und Erfolgskriterien sind didaktische Vorschläge; keine amtlichen Formulierungen.', 'content_review_required':True,
     'stage_alignment':{'relation':'same-band' if gsband==band else 'cross-band','gs_anchor_grade':g['grade'],'gs_curriculum_band':gsband,'fsp_curriculum_bands':[band],'basis':'GS-Klassenstufe/-band und FSP-Lehrplanband getrennt; FSP-Band ist kein Einzeljahrgang.'}}
  connections.append(c)
# Explicit corrections from the source review, preserving stable card IDs.
from review_corrections import correct
correct(connections)
from batch_002_topics import refine
refine(connections)
from batch_003_topics import refine as refine_batch003
refine_batch003(connections)
from batch_004_topics import refine as refine_batch004
refine_batch004(connections)
from batch_005_review import refine as refine_batch005
refine_batch005(connections)
from batch_006_topics import refine as refine_batch006
refine_batch006(connections)
from batch_007_review import refine as refine_batch007
refine_batch007(connections)
from batch_008_topics import refine as refine_batch008
refine_batch008(connections)
from batch_009_topics import refine as refine_batch009
refine_batch009(connections)
from batch_010_topics import refine as refine_batch010
refine_batch010(connections)
from batch_011_review import refine as refine_batch011
refine_batch011(connections)
from batch_012_review import refine as refine_batch012
refine_batch012(connections)
from batch_014_review import refine as refine_batch014
refine_batch014(connections)
from batch_015_review import refine as refine_batch015
refine_batch015(connections)
from batch_016_topics import refine as refine_batch016
refine_batch016(connections)
from batch_018_topics import refine as refine_batch018
refine_batch018(connections)
from batch_019_topics import refine as refine_batch019
refine_batch019(connections)
from batch_020_topics import refine as refine_batch020
refine_batch020(connections)
from batch_021_topics import refine as refine_batch021
refine_batch021(connections)
from batch_022_review import refine as refine_batch022
refine_batch022(connections)
from batch_025_review import refine as refine_batch025
refine_batch025(connections)
from batch_026_review import refine as refine_batch026
refine_batch026(connections)
from batch_027_review import refine as refine_batch027
refine_batch027(connections)
from batch_028_review import refine as refine_batch028
refine_batch028(connections)
from batch_029_review import refine as refine_batch029
refine_batch029(connections)
from batch_030_review import refine as refine_batch030
refine_batch030(connections)
from batch_031_review import refine as refine_batch031
refine_batch031(connections)
from batch_032_review import refine as refine_batch032
refine_batch032(connections)
from batch_033_review import refine as refine_batch033
refine_batch033(connections)
from batch_034_review import refine as refine_batch034
refine_batch034(connections)
from batch_035_review import refine as refine_batch035
refine_batch035(connections)
from batch_036_review import refine as refine_batch036
refine_batch036(connections)
from batch_037_review import refine as refine_batch037
refine_batch037(connections)
from batch_038_review import refine as refine_batch038
refine_batch038(connections)
from batch_039_review import refine as refine_batch039
refine_batch039(connections)
from batch_041_review import refine as refine_batch041
refine_batch041(connections)
from batch_043_review import refine as refine_batch043
refine_batch043(connections)
from batch_044_review import refine as refine_batch044
refine_batch044(connections)
from batch_045_review import refine as refine_batch045
refine_batch045(connections)
from batch_046_review import refine as refine_batch046
refine_batch046(connections)
from batch_047_review import refine as refine_batch047
refine_batch047(connections)
# Recompute coverage after refinements that may remove unsupported row links.
usedrows={rid for c in connections for rid in c['gs_target_ids']}
# Synchronize reviewed row coverage and new source anchors before assembling the audit.
for c in connections:
 if c['id'] in ['DE-004','DE-007','DE-148','DE-149','DE-012','DE-016','DE-150','DE-020','DE-151','DE-025','DE-114','DE-152','DE-045','DE-123','DE-153','DE-154','DE-155','DE-062','DE-079','DE-156','DE-157','DE-072','DE-083','DE-087','DE-089','DE-158','DE-159','DE-160','DE-092','DE-095','DE-161','DE-101','DE-162','DE-102','DE-108','DE-013','DE-017','DE-163','DE-164','DE-165','DE-166','DE-167','DE-168','DE-169','DE-170','DE-171','DE-172','DE-173','DE-174','DE-021','DE-175','DE-176','DE-177','DE-178','DE-179','DE-001','DE-003','DE-006','DE-011','DE-015','DE-018','DE-115','DE-019','DE-022','DE-023','DE-030','DE-031','DE-039','DE-117','DE-042','DE-044','DE-047','DE-050','DE-051','DE-055','DE-118','DE-119','DE-052','DE-056','DE-059','DE-060','DE-065','DE-066','DE-068','DE-069','DE-078','DE-081','DE-082']:
  usedrows.update(c['gs_target_ids'])
  for rid in c['gs_target_ids']: source(grows[rid.split('_')[-1]], 'gs')
  for rid in c['fsp_target_ids']: source(frows[rid.split('_')[-1]], 'fsp')
for sid in ["Q-DE-page908_186528","Q-DE-page146_39579","Q-DE-page146_39597","Q-DE-page146_39600","Q-DE-page908_186530","Q-DE-page908_186540","Q-DE-page908_186542"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186551","Q-DE-page908_186552","Q-DE-page908_186553","Q-DE-page146_40545","Q-DE-page146_40546","Q-DE-page146_40547","Q-DE-page146_40548","Q-DE-page908_186561","Q-DE-page908_186562"]:
 sources[sid]['checked_on']='2026-11-01'
sources['Q-DE-FSP34-SCHRIFT-GLIEDERUNG']={"id":"Q-DE-FSP34-SCHRIFT-GLIEDERUNG","title":"FSP Lernen Deutsch-Heimatkunde/Sachunterricht · Klassenstufen 3/4 · Übergreifende Ziele: schriftliche Arbeiten übersichtlich gliedern","version":"2005/2010/2019","url":"https://www.schulportal.sachsen.de/lplandb/lehrplan/146","checked_on":"2026-11-01"}
for sid in ["Q-DE-page908_186566","Q-DE-page908_186569","Q-DE-page908_186586","Q-DE-page146_40146","Q-DE-page908_186588","Q-DE-FSP34-SCHRIFT-GLIEDERUNG"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186589","Q-DE-page908_186591","Q-DE-page908_186592","Q-DE-page908_186594","Q-DE-page146_40226","Q-DE-page908_186597","Q-DE-page908_186600","Q-DE-page146_40218","Q-DE-page908_186599","Q-DE-page908_186601","Q-DE-page146_40202","Q-DE-page146_40204"]:
 sources[sid]['checked_on']='2026-11-01'
sources['Q-DE-FSP34-SCHREIBANLASS']={"id":"Q-DE-FSP34-SCHREIBANLASS","title":"FSP Lernen Deutsch-Heimatkunde/Sachunterricht · Klassenstufen 3/4 · Übergreifende Ziele: Schreibanlass berücksichtigen","version":"2005/2010/2019","url":"https://www.schulportal.sachsen.de/lplandb/lehrplan/146","checked_on":"2026-11-01"}
for sid in ["Q-DE-page908_186620","Q-DE-page908_186623","Q-DE-page908_186624","Q-DE-page146_39934","Q-DE-page146_39938","Q-DE-page146_39941","Q-DE-page146_39944","Q-DE-page146_39945","Q-DE-page146_39947","Q-DE-page908_186631","Q-DE-page908_186645","Q-DE-page908_186646","Q-DE-page908_186648","Q-DE-page146_40488","Q-DE-page908_186622","Q-DE-page908_186625","Q-DE-page146_40320","Q-DE-page146_40323","Q-DE-FSP34-SCHREIBANLASS","Q-DE-page908_186634","Q-DE-page146_40126","Q-DE-page146_40150","Q-DE-page908_186636","Q-DE-page146_40531","Q-DE-page146_40532","Q-DE-page146_40541"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186668","Q-DE-page908_186670","Q-DE-page146_39247","Q-DE-page146_39253","Q-DE-page146_39256","Q-DE-page146_39259","Q-DE-page146_39266","Q-DE-page146_40107","Q-DE-page146_40111","Q-DE-page146_40114","Q-DE-page146_40116"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186673","Q-DE-page908_186699","Q-DE-page908_186703","Q-DE-page146_40107","Q-DE-page146_40119","Q-DE-page146_40120","Q-DE-page146_40123","Q-DE-page908_186717","Q-DE-page908_186721","Q-DE-page908_186723","Q-DE-page908_186725","Q-DE-page146_40480","Q-DE-page146_40482","Q-DE-page146_40486","Q-DE-page908_186707","Q-DE-page908_186712","Q-DE-page146_40320","Q-DE-page146_40323","Q-DE-page908_186722","Q-DE-page146_40395","Q-DE-page146_40396","Q-DE-page146_40397"]:
 sources[sid]['checked_on']='2026-11-01'
sources['Q-DE-FSP-GRUNDLAGEN-MEDIENBILDUNG']={"id":"Q-DE-FSP-GRUNDLAGEN-MEDIENBILDUNG","title":"FSP Lernen · Grundlagen · Ziele und Aufgaben: Medienbildung, eigene mediale Wirkungen und Alternativen","version":"2005/2010/2019","url":"https://www.schulportal.sachsen.de/lplandb/lehrplan/146","checked_on":"2026-11-01"}
for sid in ["Q-DE-page908_186726","Q-DE-page908_186729","Q-DE-page908_186730","Q-DE-page908_186731","Q-DE-page146_40480","Q-DE-page146_40482","Q-DE-page146_40485","Q-DE-page908_186739","Q-DE-page908_186745","Q-DE-page146_40153","Q-DE-page146_40157","Q-DE-page146_40159","Q-DE-page146_40162","Q-DE-page146_40163","Q-DE-page908_186746","Q-DE-page908_186749","Q-DE-page146_40550","Q-DE-page146_40556","Q-DE-page146_40557","Q-DE-page146_40558","Q-DE-page146_40559","Q-DE-page146_40560","Q-DE-page908_186734","Q-DE-page908_186737","Q-DE-page146_40395","Q-DE-page146_40396","Q-DE-page146_40397","Q-DE-page146_40399","Q-DE-page908_186750","Q-DE-page146_39950","Q-DE-page908_186743","Q-DE-page908_186744","Q-DE-page146_40324","Q-DE-page146_40326","Q-DE-page146_40332","Q-DE-FSP-GRUNDLAGEN-MEDIENBILDUNG","Q-DE-page908_186728","Q-DE-page146_39882","Q-DE-page146_39888","Q-DE-page146_39891"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186769","Q-DE-page908_186770","Q-DE-page908_186777","Q-DE-page146_39702","Q-DE-page146_39708","Q-DE-page146_39710","Q-DE-page146_39711","Q-DE-page146_39714","Q-DE-page908_186778","Q-DE-page908_186781","Q-DE-page146_40320","Q-DE-page146_40323","Q-DE-page908_186771","Q-DE-page908_186774","Q-DE-page908_186776","Q-DE-page146_40463","Q-DE-page146_40475","Q-DE-page146_40476","Q-DE-page146_40478"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186789","Q-DE-page908_186801","Q-DE-page908_186802","Q-DE-page908_186803","Q-DE-page146_40192","Q-DE-page146_40194","Q-DE-page908_186805","Q-DE-page146_40463","Q-DE-page146_40470","Q-DE-page146_40472"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186810","Q-DE-page908_186813","Q-DE-page146_40351","Q-DE-page146_40354","Q-DE-page146_40355","Q-DE-page908_186815","Q-DE-page908_186819","Q-DE-page146_40202","Q-DE-page146_40204","Q-DE-page146_40208"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186859","Q-DE-page908_186862","Q-DE-page146_40480","Q-DE-page146_40482","Q-DE-page146_40484","Q-DE-page146_40485","Q-DE-page908_186867","Q-DE-page908_186869","Q-DE-page908_186870","Q-DE-page908_186871","Q-DE-page146_40483","Q-DE-page908_186840","Q-DE-page908_186843","Q-DE-page146_40241","Q-DE-page146_40244","Q-DE-page146_40250","Q-DE-page908_186849","Q-DE-page908_186851","Q-DE-page908_186864","Q-DE-page908_186865","Q-DE-page146_40545","Q-DE-page146_40546","Q-DE-page146_40547","Q-DE-page146_40548"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186874","Q-DE-page908_186877","Q-DE-page146_40153","Q-DE-page146_40159","Q-DE-page146_40163","Q-DE-page908_186899","Q-DE-page908_186900","Q-DE-page146_40320","Q-DE-page146_40323","Q-DE-FSP34-SCHREIBANLASS","Q-DE-page908_186902","Q-DE-page908_186904","Q-DE-page908_186906","Q-DE-page908_186908","Q-DE-page146_40488"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186994","Q-DE-page908_187000","Q-DE-page146_39950","Q-DE-page908_186953","Q-DE-page908_186965","Q-DE-page908_186969","Q-DE-page146_40324","Q-DE-page146_40326","Q-DE-page146_40332","Q-DE-FSP-GRUNDLAGEN-MEDIENBILDUNG","Q-DE-page908_186944","Q-DE-page908_186947","Q-DE-page146_40320","Q-DE-page146_40322"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186538","Q-DE-page908_186544","Q-DE-page146_40305","Q-DE-page146_40307","Q-DE-page146_40309","Q-DE-page146_40317","Q-DE-page908_186769","Q-DE-page908_186771","Q-DE-page908_186772","Q-DE-page146_40463","Q-DE-page146_40470","Q-DE-page146_40472","Q-DE-page908_186789","Q-DE-page908_186793","Q-DE-page908_186795","Q-DE-page146_40166","Q-DE-page146_40175","Q-DE-page146_40177"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186810","Q-DE-page908_186811","Q-DE-page146_40107","Q-DE-page146_40109","Q-DE-page146_40116","Q-DE-page908_186867","Q-DE-page908_186870","Q-DE-page908_186872","Q-DE-page146_40395","Q-DE-page146_40396","Q-DE-page146_40397","Q-DE-page146_40399","Q-DE-page146_40401","Q-DE-page146_40403","Q-DE-page908_186987","Q-DE-page908_186993","Q-DE-page146_40282","Q-DE-page146_40294","Q-DE-page146_40299","Q-DE-page908_187011","Q-DE-page908_187013","Q-DE-page146_40305","Q-DE-page146_40307","Q-DE-page146_40309","Q-DE-page146_40310","Q-DE-page146_40317","Q-DE-page908_187021","Q-DE-page908_187030","Q-DE-page146_40463","Q-DE-page146_40470","Q-DE-page146_40472","Q-DE-page908_186874","Q-DE-page908_186875","Q-DE-page146_40126","Q-DE-page146_40127"]:
 sources[sid]['checked_on']='2026-11-01'
for sid in ["Q-DE-page908_186271","Q-DE-page908_186273","Q-DE-page146_40282","Q-DE-page146_40303","Q-DE-page146_40291","Q-DE-page146_40294","Q-DE-page908_186281","Q-DE-page908_186282","Q-DE-page908_186283","Q-DE-page146_40550","Q-DE-page146_40556","Q-DE-page146_40557","Q-DE-page146_40558","Q-DE-page908_186287","Q-DE-page908_186293","Q-DE-page146_39702","Q-DE-page146_39708","Q-DE-page146_39710","Q-DE-page146_39711","Q-DE-page146_39714","Q-DE-page908_186295","Q-DE-page908_186297","Q-DE-page146_39754","Q-DE-page146_39768","Q-DE-page146_39765","Q-DE-page908_186299","Q-DE-page908_186305","Q-DE-page908_186307","Q-DE-page908_186310","Q-DE-page908_186312","Q-DE-page146_39869","Q-DE-page146_39876","Q-DE-page146_39879","Q-DE-page146_39874","Q-DE-page908_186315","Q-DE-page908_186323","Q-DE-page908_186326","Q-DE-page146_39267","Q-DE-page146_39274","Q-DE-page146_39281","Q-DE-page146_39286","Q-DE-page908_186317","Q-DE-page908_186318","Q-DE-page908_186319","Q-DE-page908_186320","Q-DE-page146_39179","Q-DE-page146_39185","Q-DE-page146_39187"]:
 sources[sid]['checked_on']='2026-11-02'
for sid in ["Q-DE-page908_186327","Q-DE-page908_186328","Q-DE-page146_40126","Q-DE-page146_40127","Q-DE-page908_186330","Q-DE-page908_186339","Q-DE-page908_186340","Q-DE-page908_186341","Q-DE-page908_186342","Q-DE-page908_186343","Q-DE-page146_39375","Q-DE-page146_39379","Q-DE-page146_39380","Q-DE-page146_40219","Q-DE-page146_40221","Q-DE-page146_40223","Q-DE-page908_186347","Q-DE-page908_186348","Q-DE-page908_186349","Q-DE-page146_39267","Q-DE-page146_39305","Q-DE-page146_39307","Q-DE-page146_39311","Q-DE-page146_40148","Q-DE-page908_186353","Q-DE-page908_186355","Q-DE-page908_186357","Q-DE-page908_186358","Q-DE-page146_40098","Q-DE-page146_40104","Q-DE-page908_186331","Q-DE-page908_186332","Q-DE-page908_186333","Q-DE-page146_39201","Q-DE-page146_39209","Q-DE-page146_39211","Q-DE-page146_39212","Q-DE-page146_39214","Q-DE-page146_39216","Q-DE-page146_39232","Q-DE-page146_39234"]:
 sources[sid]['checked_on']='2026-11-02'
for sid in ["Q-DE-page908_186360","Q-DE-page908_186363","Q-DE-page908_186365","Q-DE-page146_39316","Q-DE-page908_186369","Q-DE-page908_186372","Q-DE-page908_186373","Q-DE-page146_39934","Q-DE-page146_39938","Q-DE-page146_39941","Q-DE-page146_39945","Q-DE-page146_39947","Q-DE-page146_39944","Q-DE-page908_186380","Q-DE-page908_204803","Q-DE-page146_40320","Q-DE-page146_40323","Q-DE-page908_186397","Q-DE-page908_186399","Q-DE-page908_186400","Q-DE-page146_39201","Q-DE-page146_39205","Q-DE-page146_39207","Q-DE-page146_39204","Q-DE-page908_186401","Q-DE-page908_186409","Q-DE-page908_186411","Q-DE-page908_186414","Q-DE-page146_39247","Q-DE-page146_39253","Q-DE-page146_39256","Q-DE-page146_39259","Q-DE-page146_39266","Q-DE-page908_186416","Q-DE-page908_186417","Q-DE-page146_40107","Q-DE-page146_40111","Q-DE-page146_40114","Q-DE-page146_40116","Q-DE-page146_40109","Q-DE-page908_186408","Q-DE-page146_39209","Q-DE-page146_39211","Q-DE-page146_39212","Q-DE-page146_39214","Q-DE-page146_39216","Q-DE-page146_39232","Q-DE-page146_39234","Q-DE-page908_186412"]:
 sources[sid]['checked_on']='2026-11-02'
for sid in ["Q-DE-page908_186418","Q-DE-page908_186420","Q-DE-page908_186422","Q-DE-page146_39247","Q-DE-page146_39253","Q-DE-page146_39256","Q-DE-page146_39259","Q-DE-page146_39266","Q-DE-page908_186421","Q-DE-page146_40107","Q-DE-page146_40111","Q-DE-page146_40114","Q-DE-page146_40116","Q-DE-page146_40109","Q-DE-page908_186425","Q-DE-page908_186430","Q-DE-page908_186431","Q-DE-page908_186436","Q-DE-page908_186432","Q-DE-page908_186433","Q-DE-page908_186434","Q-DE-page146_40119","Q-DE-page146_40120","Q-DE-page146_40123","Q-DE-page908_186442","Q-DE-page908_186443","Q-DE-page146_39869","Q-DE-page146_39879","Q-DE-page146_39874","Q-DE-page908_186450","Q-DE-page908_186455","Q-DE-page908_186456","Q-DE-page146_40480","Q-DE-page146_40482","Q-DE-page146_40485","Q-DE-page908_186447","Q-DE-page908_186448","Q-DE-page908_186449","Q-DE-page146_40486","Q-DE-page908_186460","Q-DE-page908_186464","Q-DE-page146_39318","Q-DE-page146_39327","Q-DE-page146_39329","Q-DE-page146_39335","Q-DE-page146_39341","Q-DE-page146_40153","Q-DE-page146_40157","Q-DE-page146_40159","Q-DE-page146_40162","Q-DE-page146_40163"]:
 sources[sid]['checked_on']='2026-11-02'
# Teacher-owned planning fields: never publish automatic task or aid suggestions.
for card in connections:
 card.pop('task_suggestions', None)
 card.pop('aid_suggestions', None)
# Apply editorial titles after all historical review patches.
card_titles=json.loads((ROOT.parent/'card_titles.json').read_text())
for card in connections:
 if card['id'] in card_titles:
  card['theme']=card_titles[card['id']]
# Use plain curriculum terminology in all card text after historical patches.
def clarify_curriculum_terms(value):
 if isinstance(value, str):
  return value.replace('Beide Elternziele', 'Beide übergeordneten Lehrplanziele').replace('des Elternziels', 'des übergeordneten Lehrplanziels').replace('dem anderen GS-Elternziel', 'dem anderen übergeordneten GS-Lehrplanziel')
 if isinstance(value, list):
  return [clarify_curriculum_terms(item) for item in value]
 if isinstance(value, dict):
  return {key: clarify_curriculum_terms(item) for key, item in value.items()}
 return value
connections=clarify_curriculum_terms(connections)
# Every goal block gets an explicit outcome; no unreviewed block silently disappears.
audit=[]
for a in GS['areas']:
 for b in a['blocks']:
  id=b['id'].split('_')[-1];cs=associations.get(id,[])
  if not cs and id not in exclusions: raise ValueError('Missing decision '+id+' '+b['target'])
  audit.append({'gs_target_id':b['id'],'grade':a['grade'],'area_id':a['id'],'target':b['target'],'outcome':'begrenzter Anschluss' if cs else 'kein hinreichend belegter direkter Anschluss','connection_ids':cs,'reason':('Nur die ausdrücklich benannten Ausschnitte; keine Gleichsetzung des gesamten Zielblocks.' if cs else exclusions[id]),'uncovered_child_ids':[r['id'] for r in b['rows'][1:] if r['id'] not in usedrows], 'residual_status':'Unterziele außerhalb der ausgewählten Ausschnitte bleiben separat prüfbar; kein Vollabdeckungsanspruch.'})
source_list=list(sources.values())
source_list.append({'id':'Q-DE-RSR-2025','title':'Sächsischer Rechtschreibrahmen für die Grundschule','version':'2025','url':'https://www.schulportal.sachsen.de/lplandb/material/513/JfY9HcZHEdq5jhm8t45J','checked_on':'2026-11-01'})
for c in connections:
 if c['app_area'] in ['DE-page908_186313','DE-page908_186520','DE-page908_186831'] and 'Q-DE-RSR-2025' not in c['source_ids']:c['source_ids'].append('Q-DE-RSR-2025')
module={'schema_version':'deutsch-1.0','version':'DE-2026-11-02.4','checked_on':'2026-11-02','status':'Abgleichsentwurf zur fachlichen Erprobung','scope':'GS Deutsch 1/2, 3, 4 (2026) ↔ FSP DE-HKS 1/2, 3/4 (2019). Keine Sekundarstufenanschlüsse.','sources':source_list,'connections':connections,'target_audit':audit,'areas':[{'id':'DE-'+a['id'],'grades':a['grade'].split('/'),'title':a['title'].replace('Lernbereich: ',''),'grade_band':a['grade']} for a in GS['areas']], 'inventory_counts':{'gs_rows':len(GS['rows']),'gs_goal_blocks':len(audit),'fsp_rows':len(FSP['rows'])},'limitations':['Alle 117 GS-Zielblöcke sind mit einem Erstabgleichsergebnis erfasst. Das ist kein abgeschlossener zielzeilenweiser Vollabgleich.','Nicht ausgewählte Unterziele sind als Restumfang nachvollziehbar; Einzelne Unterziele sind noch nicht abschließend gegengeprüft.','Lehrplanziel, Unterziel und Bemerkung sind in den Inventuren getrennt. Didaktische Vorschläge sind als solche markiert.']}
(ROOT/'deutsch_module.json').write_text(json.dumps(module,ensure_ascii=False,indent=2))
print(len(connections),'Karten;',len(audit),'Zielblöcke;',len(exclusions),'Abgrenzungen')
