const {chromium}=require(process.env.LZK_PLAYWRIGHT||'playwright');
const assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {resolve}=require('node:path');
const {readFileSync}=require('node:fs');
(async()=>{
 const browser=await chromium.launch({headless:true});
 try{
 const page=await browser.newPage({viewport:{width:1280,height:960}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 const url=process.env.LZK_APP_URL||pathToFileURL(resolve('index.html')).href;
 await page.goto(url,{waitUntil:'domcontentloaded'});await page.locator('#runtimeStatus').waitFor({state:'hidden'});
 assert.equal(await page.title(),readFileSync('index.html','utf8').match(/<title>(.*?)<\/title>/)[1]);
 assert.equal(await page.locator('#startPage').isVisible(),true);
 for(const selector of ['#planner','#subject','#next','#fspInfo','#backToStart'])assert.equal(await page.locator(selector).isVisible(),false,selector);
 assert.equal(await page.locator('#introPanel').isVisible(),false);
 assert.equal(await page.locator('.model-track').count(),2);
 assert.equal(await page.locator('.model-track li').count(),8);
 const model=await page.locator('.connection-model').innerText();
 for(const word of ['Curriculare Anschlussstelle','Gemeinsamer Lerngegenstand','Lernvoraussetzungen','Ressourcen','Barrieren','Scaffolding','Kriterien zum Feinziel','gemeinsame Sicherung'])assert.ok(model.includes(word),word);
 assert.ok((await page.locator('#startPage').innerText()).split(/\s+/).length<230,'Landing must remain concise');
 assert.equal(await page.getByRole('button',{name:'Jetzt lernzieldifferent planen',exact:true}).isEnabled(),true);
 await page.screenshot({path:'/tmp/lzk-startpage-desktop.png',fullPage:true});
 await page.locator('.start-about > summary').click();assert.equal(await page.locator('#introPanel').isVisible(),true);
 await page.locator('.start-about > summary').click();
 await page.locator('#startPlanning').focus();await page.keyboard.press('Enter');
 assert.equal(await page.locator('#startPage').isVisible(),false);
 assert.equal(await page.locator('#subject').isVisible(),true);
 assert.equal(await page.evaluate(()=>document.activeElement.id),'selectionHeading');
 await page.selectOption('#subject','Mathematik');await page.selectOption('#area','MA-page912_1751');await page.selectOption('#topic','MA-030');
 await page.locator('#next').click();await page.locator('#baseline').fill('Eigene Lernvoraussetzungen bleiben erhalten');
 await page.locator('#next').click();await page.locator('#goalFSP').fill('Mein eigenes Feinziel');await page.locator('#taskFSP').fill('Meine eigene Aufgabenentscheidung');
 const draft=await page.evaluate(()=>localStorage.getItem('lernzielkompass_bewertung_entwurf'));
 await page.locator('#backToStart').click();assert.equal(await page.locator('#startPage').isVisible(),true);assert.equal(await page.locator('#planner').isVisible(),false);assert.equal(await page.evaluate(()=>document.activeElement.id),'welcomeHeading');
 assert.equal(await page.evaluate(()=>localStorage.getItem('lernzielkompass_bewertung_entwurf')),draft);
 await page.locator('#startPlanning').click();assert.equal(await page.locator('#selectionHeading').isVisible(),true);assert.equal(await page.locator('#topic').inputValue(),'MA-030');assert.equal(await page.locator('#goalFSP').inputValue(),'Mein eigenes Feinziel');
 await page.reload({waitUntil:'domcontentloaded'});await page.locator('#runtimeStatus').waitFor({state:'hidden'});
 assert.equal(await page.locator('#startPage').isVisible(),true);assert.equal(await page.locator('#subject').isVisible(),false);assert.equal(await page.evaluate(()=>localStorage.getItem('lernzielkompass_bewertung_entwurf')),draft);
 for(const width of [390,320]){
  await page.setViewportSize({width,height:844});assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth+1));
  if(width===390)await page.screenshot({path:'/tmp/lzk-startpage-mobile.png',fullPage:true});
 }
 await page.locator('#startPlanning').click();assert.equal(await page.locator('#selectionHeading').isVisible(),true);
 await page.locator('#next').click();await page.locator('#next').click();assert.equal(await page.locator('#goalFSP').inputValue(),'Mein eigenes Feinziel');assert.equal(await page.locator('#taskFSP').inputValue(),'Meine eigene Aufgabenentscheidung');
 await page.emulateMedia({media:'print'});assert.equal(await page.locator('#startPage').isVisible(),false);assert.equal(await page.locator('#backToStart').isVisible(),false);
 const noJs=await browser.newPage({javaScriptEnabled:false});await noJs.goto(url,{waitUntil:'domcontentloaded'});assert.equal(await noJs.locator('#planner').isVisible(),false);assert.equal(await noJs.locator('#startPlanning').isDisabled(),true);assert.equal(await noJs.locator('#runtimeStatus').isVisible(),true);await noJs.close();
 assert.deepEqual(errors,[]);
 console.log('PASS: landing gate, concise supplied model, keyboard/focus, start selection, return/reload draft preservation, mobile320/390, print and no-JS fallback.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exitCode=1});
