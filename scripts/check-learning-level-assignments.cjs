const assert=require('node:assert/strict');
const {resolve}=require('node:path');
const {pathToFileURL}=require('node:url');
const {chromium}=require(process.env.LZK_PLAYWRIGHT||'playwright');
const moduleData=require('../curriculum/mathematik/mathematik_module.json');
const levels=require('../curriculum/learning_levels.json');
(async()=>{
 const browser=await chromium.launch({headless:true});
 try{
  const page=await browser.newPage();const errors=[];page.on('pageerror',e=>errors.push(e.message));
  await page.goto(process.env.LZK_APP_URL||pathToFileURL(resolve('index.html')).href);
  await page.locator('#runtimeStatus').waitFor({state:'hidden'});
  await page.locator('#startPlanning').click();
  await page.selectOption('#subject','Mathematik');await page.selectOption('#grade','3');
  for(const id of ['MA-084','MA-085','MA-086','MA-090','MA-105']){
   const c=moduleData.connections.find(c=>c.id===id);
   assert.deepEqual(levels.cards[id].fsp.evidence,[]);
   assert.equal(levels.cards[id].fsp.assignment.level,'Kennen');
   await page.selectOption('#area',c.app_area);await page.selectOption('#topic',id);
   await page.locator('#next').click();
   assert.equal(await page.locator('#operatorComparisonFSP button').count(),0);
   assert.match(await page.locator('#operatorContextFSP').innerText(),/didaktisch/i);
   await page.locator('#next').click();
   assert.equal(await page.locator('#operatorFSP').innerText(),'Keine eigene Lernzielebene ausgewiesen');
   assert.match(await page.locator('#didacticLevelFSP').innerText(),/Kennen.*kein amtlicher Beleg/);
   assert.equal(await page.inputValue('#assessmentOperator'),'');
   assert.equal(await page.locator('#assessmentOperator option').filter({hasText:'im Zieltext ausgewiesen'}).count(),0);
   await page.locator('#next').click();await page.locator('#next').click();
   const official=page.locator('#output tr').filter({has:page.getByRole('rowheader',{name:'Lernzielebenen',exact:true})});
   assert.equal(await official.locator('td').nth(1).innerText(),'Keine eigene Lernzielebene ausgewiesen');
   const assigned=page.locator('#output tr').filter({has:page.getByRole('rowheader',{name:'Didaktische Kartenzuordnung',exact:true})});
   assert.match(await assigned.locator('td').nth(1).innerText(),/Kennen.*keine automatische fachliche Validierung/);
   for(const width of [320,390]){await page.setViewportSize({width,height:844});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));}
   for(let i=0;i<4;i++)await page.locator('#prev').click();
  }
  await page.selectOption('#topic','MA-084');
  await page.locator('#next').click();await page.locator('#next').click();await page.locator('#next').click();
  await page.selectOption('#assessmentOperator','Kennen');
  await page.locator('#assessmentGrade1').fill('Eigene erhaltene Abstufung');
  await page.reload();await page.locator('#startPlanning').click();
  for(let i=0;i<3;i++)await page.locator('#next').click();
  assert.equal(await page.inputValue('#assessmentOperator'),'Kennen');
  assert.equal(await page.inputValue('#assessmentGrade1'),'Eigene erhaltene Abstufung');
  assert.match(await page.locator('#assessmentHint').innerText(),/Manuell.*keine curriculare Zuordnung/);
  for(let i=0;i<3;i++)await page.locator('#prev').click();
  await page.selectOption('#area','MA-page912_1999');await page.selectOption('#topic','MA-113');
  await page.locator('#next').click();await page.locator('#next').click();
  assert.equal(await page.locator('#didacticLevelFSP').isVisible(),false);
  assert.equal(await page.locator('#operatorFSP').innerText(),'Beherrschen');
  assert.deepEqual(errors,[]);
  console.log('PASS: five didactic assignments separated from official levels in cards/goals/output; no automatic assessment claim; saved manual choice and teacher rubric preserved; mobile320/390; no leakage to MA-113.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
