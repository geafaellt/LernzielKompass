const {chromium} = require(process.env.LZK_PLAYWRIGHT || 'playwright');
const assert = require('node:assert/strict');
const {pathToFileURL} = require('node:url');
const {resolve} = require('node:path');
const {readFileSync} = require('node:fs');
const moduleData = require(resolve('curriculum/mathematik/mathematik_module.json'));
(async () => {
 const browser = await chromium.launch({headless:true});
 try {
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  const base = process.env.LZK_APP_URL || pathToFileURL(resolve('index.html')).href;
  await page.goto(base, {waitUntil:'domcontentloaded'});
  await page.locator('#runtimeStatus').waitFor({state:'hidden'});
  await page.locator('#startPlanning').click();
  assert.equal(await page.title(),readFileSync(resolve('index.html'),'utf8').match(/<title>(.*?)<\/title>/)[1]);
  await page.selectOption('#subject','Mathematik');
  for (const grade of ['1','2','3','4']) {
   await page.selectOption('#grade',grade);
   const areas = moduleData.areas.filter(a=>a.grades.includes(grade));
   assert.equal(await page.locator('#area option').count(),areas.length+1);
   for (const area of areas) {
    await page.selectOption('#area',area.id);
    const cards=moduleData.connections.filter(c=>c.app_area===area.id);
    assert.equal(await page.locator('#topic option').count(), cards.length+1);
    if(!cards.length) assert.match(await page.locator('#coverage').innerText(),/Abgleich bleibt offen/);
    for (const card of cards) {
     const previousObject=await page.inputValue('#learningObject');
     await page.selectOption('#topic',card.id);
     assert.equal(await page.inputValue('#learningObject'),previousObject,'Card selection must preserve teacher text');
     assert.notEqual(card.shared_object_suggestion,card.theme);
     assert.equal(await page.locator('#learningObjectSuggestion').innerText(),'Didaktischer Vorschlag (kein amtlicher Lehrplantext): '+card.shared_object_suggestion);
     if (card.fsp_scope) {
      await page.locator('#next').click();
      await page.locator('#insertLearningObject').click();
      assert.equal(await page.inputValue('#learningObject'),card.shared_object_suggestion);
      assert.equal(await page.locator('#operatorRelationNote').isVisible(),false);
      assert.equal(await page.locator('#reviewWarning').isVisible(),false);
      await page.locator('#connectionNotes > summary').click();
      if(card.number_range_alignment)assert.ok((await page.locator('#connectionNotes').innerText()).includes(card.number_range_alignment.notice));
      await page.locator('#connectionNotes > summary').click();
      assert.equal(await page.locator('#fspScopeDetails').isVisible(),true);
      assert.ok((await page.locator('#fspScopeDetails').innerText()).includes(card.fsp_scope.summary));
      assert.deepEqual(await page.locator('#fspScopeDetails a').evaluateAll(as=>as.map(a=>a.href)),card.fsp_scope.source_ids.map(id=>moduleData.sources.find(s=>s.id===id).url));
      await page.locator('#next').click();
      assert.equal(await page.locator('#fspScopeGoals').isVisible(),true);
      assert.ok((await page.locator('#fspScopeGoals').innerText()).includes(card.fsp_scope.planning_rule));
      for (const [suffix,goal] of [['GS',card.fine_goals[0]],['FSP',card.fine_goals[1]]]) {
       await page.locator('#apply'+suffix).click();
       assert.equal(await page.inputValue('#goal'+suffix),goal.goal);
       assert.equal(await page.inputValue('#proof'+suffix),goal.criterion);
       assert.equal(await page.inputValue('#task'+suffix),'');
       assert.equal(await page.inputValue('#aid'+suffix),'');
      }
      await page.locator('#next').click();
      await page.locator('#next').click();
      const objectRow=page.locator('#output tr').filter({hasText:'Gemeinsamer Lerngegenstand'});
      assert.equal(await objectRow.count(),1);
      assert.equal(await objectRow.locator('td').innerText(),card.shared_object_suggestion);
      const scopeRow=page.locator('#output tr').filter({hasText:'FSP-Zahlenraum / Geltungsbereich'});
      assert.equal(await scopeRow.count(),1);
      assert.ok((await scopeRow.innerText()).includes(card.fsp_scope.summary));
      for(let i=0;i<4;i++)await page.locator('#prev').click();
     }
     assert.match(await page.locator('#connectionDetail').innerText(), card.stage_alignment.relation==='cross-band' ? /Stufenübergreifend/ : /Stufenband passend/);
     for (const [suffix,op] of [['GS',card.gs_operator],['FSP',card.fsp_operator]]) {
      assert.equal(await page.locator('#operatorComparison'+suffix+' button').innerText(),op);
     }
     assert.deepEqual(await page.locator('#sourceList a').evaluateAll(as=>as.map(a=>a.href)),
        card.source_ids.map(id=>moduleData.sources.find(s=>s.id===id).url));
    }
   }
  }
  const card = moduleData.connections.find(c=>c.id==='MA-007');
  await page.selectOption('#area',card.app_area);
  await page.selectOption('#topic',card.id);
  await page.locator('#applyGS').evaluate(el=>el.click());
  await page.locator('#applyFSP').evaluate(el=>el.click());
  for (const suffix of ['GS','FSP']) {
   assert.equal(await page.inputValue('#task'+suffix),'');
   assert.equal(await page.inputValue('#aid'+suffix),'');
   assert.notEqual(await page.inputValue('#goal'+suffix),'');
   assert.notEqual(await page.inputValue('#proof'+suffix),'');
  }
  await page.selectOption('#subject','Deutsch');
  await page.selectOption('#area',await page.locator('#area option').nth(1).getAttribute('value'));
  assert.ok(await page.locator('#topic option').count()>1);
  assert.equal(await page.locator('#fspScopeDetails').getAttribute('hidden'),'');
  assert.equal(await page.locator('#fspScopeGoals').getAttribute('hidden'),'');
  assert.equal(await page.inputValue('#goalGS'),'');
  await page.selectOption('#subject','Sachunterricht');
  await page.selectOption('#area',await page.locator('#area option').nth(1).getAttribute('value'));
  assert.ok(await page.locator('#topic option').count()>1);
  assert.equal(await page.locator('#fspScopeDetails').getAttribute('hidden'),'');
  assert.equal(await page.locator('#fspScopeGoals').getAttribute('hidden'),'');
  await page.selectOption('#subject','Mathematik');
  assert.equal(await page.inputValue('#grade'),'4');
  assert.equal(await page.inputValue('#topic'),card.id);
  assert.equal(await page.inputValue('#goalGS'),card.fine_goals[0].goal);
  await page.reload({waitUntil:'domcontentloaded'});
  await page.locator('#startPlanning').click();
  assert.equal(await page.inputValue('#subject'),'Mathematik');
  assert.equal(await page.inputValue('#topic'),card.id);
  await page.locator('#next').click();
  await page.locator('#next').click();
  await page.locator('#prev').click();
  await page.locator('#learningObject').fill('Mein eigener gemeinsamer Lerngegenstand');
  await page.locator('#next').click();
  await page.locator('#goalFSP').fill('Eigener unveränderter Entwurf');
  await page.locator('#taskFSP').fill('Eigene Aufgabenentscheidung');
  await page.locator('#prev').click();
  await page.locator('#prev').click();
  await page.selectOption('#topic','MA-018');
  assert.equal(await page.inputValue('#learningObject'),'Mein eigener gemeinsamer Lerngegenstand');
  assert.equal(await page.inputValue('#goalFSP'),'Eigener unveränderter Entwurf');
  assert.equal(await page.inputValue('#taskFSP'),'Eigene Aufgabenentscheidung');
  await page.reload({waitUntil:'domcontentloaded'});
  await page.locator('#startPlanning').click();
  assert.equal(await page.inputValue('#learningObject'),'Mein eigener gemeinsamer Lerngegenstand');
  assert.equal(await page.inputValue('#goalFSP'),'Eigener unveränderter Entwurf');
  assert.equal(await page.inputValue('#taskFSP'),'Eigene Aufgabenentscheidung');
  await page.locator('#next').click();
  await page.setViewportSize({width:390,height:844});
  assert.equal(await page.locator('#fspScopeDetails').isVisible(),true);
  assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth));
  if(process.env.LZK_SCOPE_SCREENSHOT)await page.locator('#fspScopeDetails').screenshot({path:process.env.LZK_SCOPE_SCREENSHOT});
  assert.deepEqual(errors,[]);
  console.log('PASS: '+moduleData.connections.length+' mathematics cards: shared-object display/adoption/output and preserved teacher learning-object text; visible scope in cards/goals/output, source links, goal adoption, empty task/aid fields, unchanged teacher drafts, subject isolation and mobile layout.');
 } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
