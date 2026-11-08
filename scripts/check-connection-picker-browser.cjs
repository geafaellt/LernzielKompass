const {chromium}=require(process.env.LZK_PLAYWRIGHT||'playwright');
const assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {resolve}=require('node:path');
(async()=>{
 const browser=await chromium.launch({headless:true});
 try{
 const page=await browser.newPage({viewport:{width:1280,height:960}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.LZK_APP_URL||pathToFileURL(resolve('index.html')).href,{waitUntil:'domcontentloaded'});
 await page.locator('#runtimeStatus').waitFor({state:'hidden'});await page.locator('#startPlanning').click();
 const cards=page.locator('#connectionList .choice'),toggle=page.locator('#toggleConnectionPicker');
 for(const subject of ['Sachunterricht','Deutsch','Mathematik']){
  await page.selectOption('#subject',subject);await page.selectOption('#grade','1');
  const areas=await page.locator('#area option').evaluateAll(xs=>xs.map(x=>x.value).filter(Boolean));
  let ids=[];
  for(const area of areas){await page.selectOption('#area',area);ids=await page.locator('#topic option').evaluateAll(xs=>xs.map(x=>x.value).filter(Boolean));if(ids.length>1)break;}
  assert.ok(ids.length>1,subject);
  // No selection: accessible candidates, no misleading switching button.
  await page.selectOption('#topic','');await page.locator('#next').click();
  assert.equal(await cards.count(),ids.length);assert.equal(await toggle.isVisible(),false);
  await cards.first().click();assert.equal(await cards.count(),1);assert.equal(await cards.first().getAttribute('data-connection-id'),ids[0]);
  assert.equal(await toggle.innerText(),'anderen Anschluss wählen');assert.equal(await toggle.getAttribute('aria-expanded'),'false');
  await page.locator('#baseline').fill('Meine eigenen Lernvoraussetzungen');
  await page.locator('#next').click();await page.locator('#goalFSP').fill('Mein eigenes Feinziel');await page.locator('#taskFSP').fill('Meine eigene Aufgabe');await page.locator('#proofFSP').fill('Mein eigenes Kriterium');await page.locator('#prev').click();
  await toggle.focus();await page.keyboard.press('Enter');assert.equal(await cards.count(),ids.length);assert.equal(await toggle.getAttribute('aria-expanded'),'true');
  await toggle.click();assert.equal(await cards.count(),1);
  await toggle.click();await cards.nth(1).focus();await page.keyboard.press('Enter');
  assert.equal(await cards.count(),1);assert.equal(await cards.first().getAttribute('data-connection-id'),ids[1]);assert.equal(await page.locator('#topic').inputValue(),ids[1]);assert.equal(await toggle.getAttribute('aria-expanded'),'false');assert.equal(await page.evaluate(()=>document.activeElement.id),'toggleConnectionPicker');
  assert.equal(await page.locator('#baseline').inputValue(),'Meine eigenen Lernvoraussetzungen');
  for(const [id,value] of [['goalFSP','Mein eigenes Feinziel'],['taskFSP','Meine eigene Aufgabe'],['proofFSP','Mein eigenes Kriterium']])assert.equal(await page.locator('#'+id).inputValue(),value);
  await toggle.click();await page.locator('#next').click();await page.locator('#prev').click();assert.equal(await cards.count(),1);
  await page.locator('#prev').click();
 }
 await page.locator('#next').click();
 for(const width of [390,320]){await page.setViewportSize({width,height:844});for(const expanded of [false,true]){if(expanded)await toggle.click();assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),'mobile overflow');if(expanded)await toggle.click();}}
 await page.screenshot({path:'/tmp/lzk-connection-picker-mobile.png',fullPage:true});
 await page.setViewportSize({width:1280,height:960});await page.screenshot({path:'/tmp/lzk-connection-picker-desktop.png',fullPage:true});
 await toggle.click();await page.reload({waitUntil:'domcontentloaded'});await page.locator('#runtimeStatus').waitFor({state:'hidden'});await page.locator('#startPlanning').click();await page.locator('#next').click();assert.equal(await cards.count(),1);assert.equal(await toggle.getAttribute('aria-expanded'),'false');
 await page.locator('#prev').click();await page.selectOption('#area','');await page.locator('#next').click();assert.equal(await cards.count(),0);assert.equal(await toggle.isVisible(),false);
 // Exercise actual single-card combinations, if present in the current stock.
 await page.locator('#prev').click();let single=false;
 for(const grade of ['1','2','3','4']){await page.selectOption('#grade',grade);const areas=await page.locator('#area option').evaluateAll(xs=>xs.map(x=>x.value).filter(Boolean));for(const area of areas){await page.selectOption('#area',area);if(await page.locator('#topic option').count()===2){await page.locator('#next').click();assert.equal(await cards.count(),1);assert.equal(await toggle.isVisible(),false);single=true;break;}}if(single)break;}
 assert.ok(single,'single-card fixture');assert.deepEqual(errors,[]);
 console.log('PASS: selected card only, switch/collapse in all three subjects, no selection/empty/single, keyboard/focus, preserved teacher texts, navigation/reload and mobile 320/390.');
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
