const fs = require('fs');
const paths = ['outputs/20261011_lernzielkompass/site/dist/index.html', 'outputs/20261011_lernzielkompass/index.html'];
const additions = [
  {
    id: 'SU-012', theme: 'Jahreszeiten · Veränderungen in Natur und Pflanzenwelt',
    gs_anchor: 'GS Kl. 1/2 · LB 3 „Begegnungen mit Pflanzen und Tieren“; Kennen jahreszeitlicher Veränderungen in der Natur; typische Erscheinungen beobachten und vom Speziellen auf allgemeine Erscheinungen schließen.',
    gs_operator: 'Kennen; beobachten und verallgemeinern',
    fsp_anchor: 'FSP(L) Kl. 1/2 · DE-HKS LB 6 „Natur entdecken und erleben“; Kennen jahreszeitlicher Veränderungen; Jahreszeiten mit Blüten und Knospen, Vogelzug, Sommerwiese, Laubfärbung und Erntezeit, Frost und Schnee; Beobachtungen wiedergeben.',
    fsp_operator: 'Kennen; Beobachtungen wiedergeben',
    status: 'Geprüfter gemeinsamer Zielausschnitt · Zielhandlungen nicht deckungsgleich',
    source_ids: ['Q-GS-SU-GESAMT', 'Q-FSP-DEHKS-15'],
    fine_goals: [
      { track: 'Grundschule', goal: 'Die Lernenden können an einer ausgewählten Pflanze typische Veränderungen im Jahreslauf beobachten und eine Beobachtung einer Jahreszeit zuordnen.', criterion: 'Mindestens zwei beobachtete oder dokumentierte Veränderungen werden passend beschrieben und einer Jahreszeit zugeordnet.' },
      { track: 'FSP Lernen', goal: 'Die Lernenden können ausgewählte Naturbeobachtungen – etwa Knospen, Laubfärbung oder Frost – passenden Jahreszeiten zuordnen und eine Beobachtung wiedergeben.', criterion: 'Mindestens zwei Beobachtungen werden mithilfe von Realien, Bildern oder Wortkarten richtig zugeordnet und mündlich, bildlich oder durch Auswahl wiedergegeben.' }
    ],
    operator_relation: 'Beide Lernbereiche greifen jahreszeitliche Veränderungen auf. Die GS fordert gezielte Beobachtung und den Schluss vom Einzelfall auf typische Erscheinungen; der FSP-Anker listet exemplarische Erscheinungen und das Wiedergeben von Beobachtungen. Der gemeinsame Ausschnitt ist auf ausgewählte, tatsächlich beobachtete Naturveränderungen begrenzt.',
    review_note: 'Vogelzug, Nestbau und Brutpflege, Langzeitbeobachtungen sowie weitere Pflanzen- und Tierziele sind nur dann Teil der gemeinsamen Planung, wenn sie im konkreten Unterricht ausdrücklich ergänzt und gesondert geprüft werden.',
    content_review_required: true,
    app_review_message: 'Beide Lehrpläne greifen Jahreszeiten auf. Die GS-Zielhandlung des Verallgemeinerns und die FSP-Beispiele sind nicht vollständig gleich; wähle konkrete Beobachtungen aus.',
    shared_object_suggestion: 'Was verändert sich im Jahreslauf? Eine Pflanze beobachten'
  },
  {
    id: 'SU-013', theme: 'Bäume · Laub- und Nadelbäume unterscheiden',
    gs_anchor: 'GS Kl. 1/2 · LB 3 „Begegnungen mit Pflanzen und Tieren“; Beherrschen von grundlegendem Wissen über Bäume; fünf Vertreter der Laubbäume und drei Vertreter der Nadelbäume unterscheiden; Laub- und Nadelbaum vergleichen.',
    gs_operator: 'Beherrschen; Unterscheiden',
    fsp_anchor: 'FSP(L) Kl. 1/2 · DE-HKS LB 6 „Natur entdecken und erleben“; ausgewählte Pflanzenarten kennen; Laub- und Nadelbäume benennen, Gemeinsamkeiten und Unterschiede finden und wiedergeben.',
    fsp_operator: 'Kennen; benennen; Unterschiede und Gemeinsamkeiten wiedergeben',
    status: 'Geprüfter gemeinsamer Zielausschnitt · Artenumfang und Operatoren verschieden',
    source_ids: ['Q-GS-SU-GESAMT', 'Q-FSP-DEHKS-15'],
    fine_goals: [
      { track: 'Grundschule', goal: 'Die Lernenden können ausgewählte Laub- und Nadelbäume anhand von Blättern oder Nadeln unterscheiden und die Zuordnung mit einem Merkmal begründen.', criterion: 'Mindestens zwei Baumbeispiele werden passend zugeordnet; ein sichtbares Unterscheidungsmerkmal wird benannt oder in einer Skizze markiert.' },
      { track: 'FSP Lernen', goal: 'Die Lernenden können ausgewählte Bäume als Laub- oder Nadelbaum benennen oder zuordnen und ein gemeinsames oder unterscheidendes Merkmal wiedergeben.', criterion: 'Mindestens ein Laub- und ein Nadelbaum werden passend zugeordnet; ein Merkmal wird mündlich, bildlich oder durch Auswahl wiedergegeben.' }
    ],
    operator_relation: 'Der gemeinsame Zielkern – Laub- und Nadelbäume anhand ausgewählter Merkmale unterscheiden – ist explizit in beiden Lernbereichen verankert. Die GS fordert darüber hinaus das Beherrschen grundlegenden Baumwissens sowie eine größere Zahl von Arten; dies ist im FSP-Anker nicht gleichwertig enthalten.',
    review_note: 'Die im GS-Lehrplan geforderte Artenzahl (fünf Laub- und drei Nadelbäume), Baumteile, Jahresringe und Langzeitbeobachtungen sind zusätzliche Zielanteile und werden durch die Anschlussstelle nicht automatisch abgedeckt.',
    content_review_required: true,
    app_review_message: 'Gemeinsam ist das Unterscheiden von Laub- und Nadelbäumen. Artenzahl und zusätzliche GS-Zielanteile sind umfangreicher und müssen getrennt gesichert werden.',
    shared_object_suggestion: 'Laubbaum oder Nadelbaum? Bäume an Merkmalen erkennen'
  },
  {
    id: 'SU-014', theme: 'Getreide · Arten und ihre Verwendung als Grundnahrungsmittel',
    gs_anchor: 'GS Kl. 3 · LB 3 „Begegnungen mit Pflanzen und Tieren“; Kennen des Anbaus und der Verwendung von Getreide als Grundnahrungsmittel; drei Getreidearten unterscheiden; Verarbeitung vom Korn zum Brot.',
    gs_operator: 'Kennen; Unterscheiden',
    fsp_anchor: 'FSP(L) Kl. 3/4 · DE-HKS LB 6 „Natur entdecken und erleben“; weitere Pflanzen kennen; Getreidearten Roggen, Hafer, Gerste, Weizen und Mais benennen und unterscheiden; über Ernte früher und heute sprechen und eine Produktübersicht erstellen.',
    fsp_operator: 'Kennen; benennen und unterscheiden; zusammenhängend sprechen',
    status: 'Geprüfter gemeinsamer Zielausschnitt · Reichweite und Teilhandlungen verschieden',
    source_ids: ['Q-GS-SU-GESAMT', 'Q-FSP-DEHKS-27'],
    fine_goals: [
      { track: 'Grundschule', goal: 'Die Lernenden können drei ausgewählte Getreidearten anhand ihrer Merkmale unterscheiden und eine Verwendung als Nahrungsmittel benennen.', criterion: 'Drei Getreidearten werden passend zugeordnet; mindestens eine Verwendung wird korrekt angegeben.' },
      { track: 'FSP Lernen', goal: 'Die Lernenden können ausgewählte Getreidearten aus Realien- oder Bildmaterial benennen oder zuordnen und eine passende Verwendung einem Produkt zuordnen.', criterion: 'Mindestens zwei Getreidearten werden korrekt erkannt; eine passende Produktzuordnung wird hergestellt oder mündlich wiedergegeben.' }
    ],
    operator_relation: 'Beide Lehrpläne enthalten das Benennen und Unterscheiden konkreter Getreidearten; der FSP nennt fünf Beispiele und zusätzlich Ernte sowie Produktübersicht. Der GS-Anker verbindet das Thema stärker mit Anbau, Grundnahrungsmittel und Verarbeitung vom Korn zum Brot. Gemeinsam ist nur ein ausgewählter Arten- und Verwendungsabschnitt.',
    review_note: 'Kartoffelanbau, Pflanzenbestandteile, Verarbeitungsschritte sowie die vollständige Produktübersicht sind keine automatisch gemeinsamen Ziele. Kartoffel-Inhalte bleiben gesondert abzugleichen.',
    content_review_required: true,
    app_review_message: 'Getreidearten sind in beiden Plänen verankert; Anbau, Verarbeitung und die jeweiligen Artenumfänge unterscheiden sich. Begrenze den gemeinsamen Ausschnitt.',
    shared_object_suggestion: 'Getreide erkennen: vom Korn zu ausgewählten Lebensmitteln'
  },
  {
    id: 'SU-015', theme: 'Wasser · Zustandsänderungen und Wasserkreislauf',
    gs_anchor: 'GS Kl. 3 · LB 4 „Begegnung mit Phänomenen der unbelebten Natur“; Kennen von Zusammenhängen zwischen den Zustandsformen des Wassers; Zustandsänderungen untersuchen und Wissen auf den Wasserkreislauf in der Natur übertragen.',
    gs_operator: 'Kennen; Übertragen',
    fsp_anchor: 'FSP(L) Kl. 3/4 · DE-HKS LB 6 „Natur entdecken und erleben“; Einblick in die Phänomene Luft und Wasser; Untersuchungen mit Wasser; Einblick in den Kreislauf des Wassers mit Verdunstung, Wolken und Niederschlag.',
    fsp_operator: 'Einblick gewinnen',
    status: 'Geprüfter gemeinsamer Zielausschnitt · Operatoren deutlich verschieden',
    source_ids: ['Q-GS-SU-GESAMT', 'Q-FSP-DEHKS-27'],
    fine_goals: [
      { track: 'Grundschule', goal: 'Die Lernenden können an einem Versuch eine Zustandsänderung des Wassers beobachten und diese mit einem passenden Abschnitt des Wasserkreislaufs verbinden.', criterion: 'Eine beobachtete Zustandsänderung wird korrekt benannt und in einem einfachen Schema sachgerecht einer Phase des Wasserkreislaufs zugeordnet.' },
      { track: 'FSP Lernen', goal: 'Die Lernenden können die Abfolge Verdunstung – Wolkenbildung – Niederschlag mithilfe von Bildern oder Stützwörtern wiedergeben.', criterion: 'Mindestens zwei der drei Elemente werden in sinnvoller Reihenfolge ausgewählt oder wiedergegeben; Hilfen und Darstellungsform werden dokumentiert.' }
    ],
    operator_relation: 'Ein gemeinsamer Themenkern ist der Wasserkreislauf. Die GS verlangt Wissen über Zustandsformen und dessen Übertragung auf den Kreislauf; der FSP formuliert „Einblick gewinnen“ und nennt zentrale Kreislaufstationen. Diese Operatoren sind nicht gleichzusetzen und begründen keine lineare Rangfolge. Der gemeinsame Lerngegenstand muss die getrennten Zielhandlungen erhalten.',
    review_note: 'Die systematische Erklärung der Zustandsänderungen, der Temperaturabhängigkeit und die selbstständige Darstellung kausaler Zusammenhänge sind zusätzliche GS-Zielanteile. Der FSP-Zielanker umfasst außerdem weitere Wasseruntersuchungen, die hier nicht abgeglichen werden.',
    content_review_required: true,
    app_review_message: 'Der Wasserkreislauf ist gemeinsam verankert, die Operatoren und die verlangte fachliche Tiefe unterscheiden sich deutlich. Plane getrennte Zielhandlungen.',
    shared_object_suggestion: 'Wasser unterwegs: vom Verdunsten bis zum Niederschlag'
  }
];

for (const path of paths) {
  const html = fs.readFileSync(path, 'utf8');
  const match = html.match(/(<script id="curriculum-data" type="application\/json">)([\s\S]*?)(<\/script>)/);
  if (!match) throw new Error(`Curriculum data missing in ${path}`);
  const data = JSON.parse(match[2]);
  const ids = new Set(additions.map(item => item.id));
  data.connections = data.connections.filter(item => !ids.has(item.id));
  data.connections.push(...additions);
  const append = (planTest, levelTest, text) => {
    const item = data.curriculum_inventory.find(x => planTest(x) && levelTest(x));
    if (!item) throw new Error(`Inventory entry not found: ${text}`);
    if (!item.reviewed_candidates.includes(text)) item.reviewed_candidates += ` ${text}`;
  };
  append(x => x.plan === 'Grundschule Sachunterricht', x => x.level.includes('1/2'), 'LB 3 Jahreszeiten SU-012; LB 3 Bäume SU-013 abgeglichen.');
  append(x => x.plan === 'Grundschule Sachunterricht', x => x.level.includes('Klassenstufe 3'), 'LB 3 Getreide SU-014; LB 4 Wasserkreislauf SU-015 abgeglichen.');
  append(x => x.plan.includes('FSP Lernen'), x => x.level.includes('1/2'), 'LB 6 Jahreszeiten SU-012 und Bäume SU-013 abgeglichen.');
  append(x => x.plan.includes('FSP Lernen'), x => x.level.includes('3/4'), 'LB 6 Getreide SU-014 und Wasserkreislauf SU-015 abgeglichen.');
  data.review_log.push({ date: '2026-10-12', action: 'Vier weitere naturkundliche Anschlussstellen geprüft', result: 'SU-012 Jahreszeiten, SU-013 Laub- und Nadelbäume, SU-014 Getreidearten und SU-015 Wasserkreislauf. Zielhandlungen und Reichweiten wurden jeweils getrennt beschrieben; bei SU-015 sind die Operatoren ausdrücklich nicht gleichzusetzen.' });
  data.checked_on = '2026-10-12';
  const output = html.replace(match[0], match[1] + JSON.stringify(data) + match[3]).replaceAll('Datenstand Sachunterricht v0.10', 'Datenstand Sachunterricht v0.11');
  fs.writeFileSync(path, output);
}
