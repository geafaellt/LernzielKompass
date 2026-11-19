const assert = require('node:assert/strict');
const {readFileSync} = require('node:fs');
const {resolve} = require('node:path');
const {pathToFileURL} = require('node:url');
const {chromium} = require(process.env.LZK_PLAYWRIGHT || 'playwright');
const levels = require('../curriculum/learning_levels.json');
const cards = [
 ...require('../curriculum/sachunterricht/baseline.json').connections,
 ...require('../curriculum/deutsch/deutsch_module.json').connections,
 ...require('../curriculum/mathematik/mathematik_module.json').connections
];
assert.deepEqual(Object.keys(levels.cards).sort(), cards.map(c=>c.id).sort());
for (const card of cards) {
 for (const side of ['gs','fsp']) {
  const entry=levels.cards[card.id][side];
  assert.ok(entry.evidence.length || entry.note, card.id);
  for (const item of entry.evidence) {
   assert.ok(levels.levels.includes(item.level), card.id);
   assert.ok(item.target.toLowerCase().startsWith(item.level.toLowerCase()+' '),card.id);
   assert.ok(item.url.endsWith('#'+item.row_id),card.id);
  }
 }
}
const values=(id,side)=>levels.cards[id][side].evidence.map(e=>e.level);
assert.deepEqual(values('SU-011','gs'),['Kennen']);
assert.deepEqual(values('SU-036','gs'),['Einblick gewinnen']);
assert.deepEqual(values('SU-052','fsp'),['Sich positionieren']);
assert.deepEqual(values('SU-066','fsp'),['Einblick gewinnen']);
assert.deepEqual(values('SU-133','gs'),['Kennen']);
assert.deepEqual(values('DE-115','fsp'),[]);
assert.deepEqual(values('MA-084','fsp'),[]);
(async()=>{
 const browser=await chromium.launch({headless:true});
 try {
  const page=await browser.newPage();
  const errors=[];
  page.on('pageerror',error=>errors.push(error.message));
  await page.goto(process.env.LZK_APP_URL || pathToFileURL(resolve('index.html')).href);
  await page.locator('#runtimeStatus').waitFor({state:'hidden'});
  const checks=await page.evaluate(()=>{
   const results=[];
   for(const card of data.connections) {
    renderOperatorComparison(card);
    for(const side of ['gs','fsp']) {
     const suffix=side==='gs'?'GS':'FSP';
     const shown=[...document.querySelectorAll('#operatorComparison'+suffix+' button')].map(b=>b.textContent);
     const expected=[...new Set(levelEvidence(card,side).map(e=>e.level))];
     results.push({id:card.id,side,shown,expected});
    }
   }
   // Text fields must never be interpreted as level evidence.
   const sample={...data.connections[0],gs_operator:'Orientieren; Erleben; kein Kennen; Kennenlernen'};
   renderOperatorComparison(sample);
   results.push({id:'text injection',shown:[...document.querySelectorAll('#operatorComparisonGS button')].map(b=>b.textContent),expected:['Kennen']});
   return results;
  });
  for(const check of checks)assert.deepEqual(check.shown,check.expected,check.id+' '+check.side);
  await page.reload();
  await page.locator('#startPlanning').click();
  for(const subject of ['Sachunterricht','Deutsch','Mathematik']) {
   await page.selectOption('#subject',subject);
   await page.selectOption('#grade','1');
   const area=await page.locator('#area option').evaluateAll(options=>options.find(o=>o.value)?.value);
   await page.selectOption('#area',area);
   const topic=await page.locator('#topic option').evaluateAll(options=>options.find(o=>o.value)?.value);
   await page.selectOption('#topic',topic);
   await page.locator('#next').click();
   await page.getByRole('heading',{name:'Lernzielebenen im Vergleich'}).waitFor();
   await page.locator('#operatorComparisonGS button').first().click();
   assert.equal(await page.locator('#operatorMeaning').isVisible(),true);
   await page.locator('#prev').click();
  }
  assert.deepEqual(errors,[]);
  console.log('PASS: '+cards.length+' Karten, 814 Kartenseiten, amtliche Belege, Ausschluss von Zielhandlungen, Quellenvererbung und Fachwechsel.');
 } finally {await browser.close();}
})().catch(error=>{console.error(error);process.exitCode=1;});
