const {chromium}=require(process.env.LZK_PLAYWRIGHT||'playwright');
const assert=require('node:assert/strict');
const {readFileSync}=require('node:fs');
const {pathToFileURL}=require('node:url');
const {resolve}=require('node:path');
const audit=JSON.parse(readFileSync('curriculum/learning_objects/review_001.json','utf8'));
(async()=>{const browser=await chromium.launch({headless:true});try{
 const page=await browser.newPage({viewport:{width:1280,height:960}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.LZK_APP_URL||pathToFileURL(resolve('index.html')).href,{waitUntil:'domcontentloaded'});await page.locator('#runtimeStatus').waitFor({state:'hidden'});await page.locator('#startPlanning').click();
 assert.equal(await page.title(),readFileSync('index.html','utf8').match(/<title>(.*?)<\/title>/)[1]);
 const result=await page.evaluate(async rows=>{
  const el=id=>document.getElementById(id),check=(ok,msg)=>{if(!ok)throw Error(msg)};
  const set=(id,val)=>{const e=el(id);check([...e.options].some(o=>o.value===val),'missing option '+id+': '+val);e.value=val;e.dispatchEvent(new Event('change',{bubbles:true}));};
  let total=0;
  for(const row of rows){
   const card=data.connections.find(c=>c.id===row.id);check(!!card,'missing '+row.id);
   set('subject',row.subject);set('grade',levelFor(card).split('/')[0]);set('area',connectionAreaKey(card));
   const own='Eigener Lerngegenstand vor '+row.id;el('learningObject').value=own;el('learningObject').dispatchEvent(new Event('input',{bubbles:true}));
   set('topic',row.id);check(el('learningObject').value===own,'overwritten draft '+row.id);
   el('next').click();await new Promise(requestAnimationFrame);
   check(el('learningObjectSuggestion').getClientRects().length>0,'not visible '+row.id);
   check(el('learningObjectSuggestion').textContent==='Didaktischer Vorschlag (kein amtlicher Lehrplantext): '+row.after,'wrong suggestion '+row.id);
   check(el('connectionList').querySelectorAll('.choice').length===1,'picker regression '+row.id);
   el('insertLearningObject').click();check(el('learningObject').value===row.after,'adoption '+row.id);
   for(let i=0;i<3;i++)el('next').click();
   const output=[...el('output').querySelectorAll('tr')].find(r=>r.querySelector('th')?.textContent==='Gemeinsamer Lerngegenstand');
   check(output?.querySelector('td')?.textContent===row.after,'plan output '+row.id);
   for(const id of ['taskGS','aidGS','taskFSP','aidFSP'])check(el(id).value==='','autofilled '+id+' '+row.id);
   for(let i=0;i<4;i++)el('prev').click();
   total++;
  }
  return total;
 },audit.cards);
 assert.equal(result,313);
 // Real keyboard use and draft persistence, including the newly worded selector.
 await page.locator('#next').click();await page.locator('#learningObject').fill('Mein eigener unveränderter gemeinsamer Lerngegenstand');
 await page.locator('#toggleConnectionPicker').focus();if(await page.locator('#toggleConnectionPicker').isVisible()){await page.keyboard.press('Enter');await page.locator('#connectionList .choice').first().click();assert.equal(await page.locator('#learningObject').inputValue(),'Mein eigener unveränderter gemeinsamer Lerngegenstand');}
 await page.reload({waitUntil:'domcontentloaded'});await page.locator('#runtimeStatus').waitFor({state:'hidden'});await page.locator('#startPlanning').click();assert.equal(await page.locator('#learningObject').inputValue(),'Mein eigener unveränderter gemeinsamer Lerngegenstand');await page.locator('#next').click();
 for(const width of [390,320]){await page.setViewportSize({width,height:844});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));}
 await page.locator('#learningObjectSuggestion').screenshot({path:'/tmp/lzk-ds-learning-object.png'});
 // Restore old drafts whose source context used to determine the wrong area.
 for(const [id,grade,oldArea,newArea] of [['SU-020','3','3-LB-4','3-GOALS'],['SU-065','4','4-LB-6','4-GOALS']]){
  await page.evaluate(({id,grade,oldArea})=>{const key='lernzielkompass_bewertung_entwurf',draft=JSON.parse(localStorage.getItem(key));draft.selectedId=id;draft.fields.subject='Sachunterricht';draft.fields.grade=grade;draft.fields.area=oldArea;draft.fields.learningObject='Unveränderter älterer Entwurf';draft.subjectDrafts.Sachunterricht.selectedId=id;Object.assign(draft.subjectDrafts.Sachunterricht.fields,{grade,area:oldArea,learningObject:'Unveränderter älterer Entwurf'});localStorage.setItem(key,JSON.stringify(draft));},{id,grade,oldArea});
  await page.reload({waitUntil:'domcontentloaded'});await page.locator('#runtimeStatus').waitFor({state:'hidden'});await page.locator('#startPlanning').click();
  assert.equal(await page.locator('#area').inputValue(),newArea);assert.equal(await page.locator('#topic').inputValue(),id);assert.equal(await page.locator('#learningObject').inputValue(),'Unveränderter älterer Entwurf');
  await page.selectOption('#subject','Deutsch');await page.selectOption('#subject','Sachunterricht');assert.equal(await page.locator('#topic').inputValue(),id);assert.equal(await page.locator('#learningObject').inputValue(),'Unveränderter älterer Entwurf');
 }
 assert.deepEqual(errors,[]);console.log('PASS: all 313 Deutsch/Sachunterricht suggestions visible, explicit adoption and planning output; selected-only picker, empty task/aid fields, preserved drafts, reload, migrated overarching-goal selections and mobile320/390.');
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
