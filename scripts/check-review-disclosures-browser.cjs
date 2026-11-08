const {chromium}=require(process.env.LZK_PLAYWRIGHT||'playwright');
const assert=require('node:assert/strict');
const {readFileSync}=require('node:fs');
const {pathToFileURL}=require('node:url');
const {resolve}=require('node:path');
const cards=[...JSON.parse(readFileSync('curriculum/sachunterricht/baseline.json')).connections.map(c=>({...c,subject:'Sachunterricht'})),...require(resolve('curriculum/deutsch/deutsch_module.json')).connections,...require(resolve('curriculum/mathematik/mathematik_module.json')).connections];
(async()=>{const browser=await chromium.launch({headless:true});try{
 const page=await browser.newPage({viewport:{width:1280,height:960}}),errors=[];page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.LZK_APP_URL||pathToFileURL(resolve('index.html')).href,{waitUntil:'domcontentloaded'});await page.locator('#runtimeStatus').waitFor({state:'hidden'});await page.locator('#startPlanning').click();
 assert.equal(await page.title(),readFileSync('index.html','utf8').match(/<title>(.*?)<\/title>/)[1]);
 const counts=await page.evaluate(async expected=>{
  const e=id=>document.getElementById(id),check=(v,m)=>{if(!v)throw Error(m)},norm=s=>s.replace(/\s+/g,' ').trim();
  const set=(id,value)=>{const el=e(id);check([...el.options].some(o=>o.value===value),'missing '+id+': '+value);el.value=value;el.dispatchEvent(new Event('change',{bubbles:true}))};
  let deduped=0;
  for(const c of expected){
   const current=data.connections.find(x=>x.id===c.id);set('subject',c.subject);set('grade',levelFor(current).split('/')[0]);set('area',connectionAreaKey(current));set('topic',c.id);e('next').click();await new Promise(requestAnimationFrame);
   const notes=e('connectionNotes'),sources=e('connectionSources');check(!notes.open&&!sources.open,'disclosures default closed '+c.id);check(!notes.hidden&&!sources.hidden,'missing disclosure '+c.id);
   check(!document.querySelector('[data-step="1"] .notice.warning'),'yellow banner '+c.id);
   notes.querySelector('summary').click();sources.querySelector('summary').click();check(notes.open&&sources.open,'cannot expand '+c.id);
   const text=norm(notes.textContent);check(text.includes(norm(c.operator_relation)),'relation lost '+c.id);
   const warning=c.content_review_required?(c.app_review_message||c.review_note||'Prüfe vor der Auswahl den konkreten gemeinsamen Zielausschnitt.'):'';
   if(warning)check(text.includes(norm(warning)),'boundary lost '+c.id);
   if(warning&&norm(c.operator_relation).includes(norm(warning))){check(e('reviewWarning').hidden&&e('reviewWarning').textContent==='','duplicate '+c.id);deduped++;}
   const links=[...e('sourceList').querySelectorAll('a')];check(links.length===c.source_ids.length,'sources missing '+c.id);
   const sm=new Map(data.sources.map(s=>[s.id,s.url]));check(links.every((a,i)=>a.href===sm.get(c.source_ids[i])&&a.target==='_blank'&&a.rel.includes('noopener')),'source URL '+c.id);
   e('operatorComparisonGS').querySelector('button').click();check(!e('operatorMeaning').hidden,'operator help missing '+c.id);check(!e('operatorMeaning').querySelector('a'),'duplicated sources in definition '+c.id);
   if(c.fsp_scope){const scope=e('fspScopeDetails');check(!scope.hidden,'scope hidden '+c.id);check(scope.textContent.includes(c.fsp_scope.planning_rule),'planning limit lost '+c.id);const proof=scope.querySelector('details');check(proof&&!proof.open&&proof.querySelectorAll('a').length===c.fsp_scope.source_ids.length,'scope evidence '+c.id);proof.querySelector('summary').click();check(proof.open,'scope proof not expandable '+c.id);}
   e('learningObject').value='Eigener Text bleibt';e('learningObject').dispatchEvent(new Event('input',{bubbles:true}));
   e('prev').click();
  }
  return {total:expected.length,deduped};
 },cards);
 assert.equal(counts.total,cards.length);assert.equal(counts.deduped,cards.filter(c=>c.content_review_required&&c.app_review_message&&c.operator_relation.replace(/\s+/g,' ').includes(c.app_review_message.replace(/\s+/g,' '))).length);
 // Switch to a known mathematics example and exercise real keyboard disclosure controls.
 await page.selectOption('#subject','Mathematik');await page.selectOption('#grade','1');await page.selectOption('#area','MA-page912_1751');await page.selectOption('#topic','MA-032');await page.locator('#next').click();
 // A same-card render preserves a deliberate open state; close explicitly for the visual/default checks.
 for(const selector of ['#connectionNotes','#connectionSources'])await page.locator(selector).evaluate(e=>e.open=false);
 assert.equal(await page.locator('#operatorRelationNote').isVisible(),false);assert.equal(await page.locator('#sourceList a').first().isVisible(),false);assert.equal(await page.locator('#fspScopeDetails').isVisible(),true);
 await page.locator('#connectionNotes > summary').focus();await page.keyboard.press('Enter');assert.equal(await page.locator('#operatorRelationNote').isVisible(),true);assert.equal(await page.locator('#reviewWarning').isVisible(),false);await page.keyboard.press('Enter');
 await page.locator('#connectionSources > summary').focus();await page.keyboard.press('Space');assert.equal(await page.locator('#sourceList a').first().isVisible(),true);await page.keyboard.press('Space');
 await page.locator('#operatorComparisonGS button').first().click();assert.equal(await page.locator('#operatorMeaning').isVisible(),true);
 await page.locator('#learningObject').fill('Eigener unveränderter Text');await page.locator('#toggleConnectionPicker').click();await page.locator('#connectionList .choice').first().click();assert.equal(await page.locator('#learningObject').inputValue(),'Eigener unveränderter Text');assert.equal(await page.locator('#operatorMeaning').isVisible(),false);assert.equal(await page.locator('#connectionSources').getAttribute('open'),null);
 await page.screenshot({path:'/tmp/lzk-compact-desktop.png',fullPage:true});
 for(const width of [390,320]){await page.setViewportSize({width,height:844});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));if(width===390)await page.screenshot({path:'/tmp/lzk-compact-mobile.png',fullPage:true});}
 await page.reload({waitUntil:'domcontentloaded'});await page.locator('#runtimeStatus').waitFor({state:'hidden'});await page.locator('#startPlanning').click();assert.equal(await page.locator('#learningObject').inputValue(),'Eigener unveränderter Text');await page.locator('#next').click();assert.equal(await page.locator('#connectionNotes').getAttribute('open'),null);
 await page.locator('#prev').click();await page.selectOption('#area','');await page.locator('#next').click();assert.equal(await page.locator('#connectionNotes').isVisible(),false);assert.equal(await page.locator('#connectionSources').isVisible(),false);
 assert.deepEqual(errors,[]);console.log(`PASS: all ${counts.total} cards retain relation/boundary/source evidence in collapsed disclosures; ${counts.deduped} duplicate warnings removed; operator help, visible FSP limits, keyboard, switching/reload, drafts, empty selection and mobile320/390.`);
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
