const {chromium}=require(process.env.LZK_PLAYWRIGHT||'playwright');
const assert=require('node:assert/strict');
const {pathToFileURL}=require('node:url');
const {resolve}=require('node:path');
const data=require(resolve('curriculum/fsp-rueckwaerts/teacher_info.json'));
(async()=>{
 const browser=await chromium.launch({headless:true});
 try{
 const page=await browser.newPage({viewport:{width:1280,height:900}}),errors=[];
 page.on('pageerror',e=>errors.push(e.message));
 await page.goto(process.env.LZK_APP_URL||pathToFileURL(resolve('index.html')).href,{waitUntil:'domcontentloaded'});
 await page.locator('#runtimeStatus').waitFor({state:'hidden'});
 await page.selectOption('#subject','Mathematik');
 await page.locator('#next').click();
 await page.locator('#baseline').fill('Mein unveränderter Lehrkraftentwurf');
 const before=await page.evaluate(()=>({storage:JSON.stringify(localStorage),subject:document.getElementById('subject').value,topic:document.getElementById('topic').value,baseline:document.getElementById('baseline').value}));
 assert.equal(await page.locator('#fspInfo').evaluate(e=>e.open),false);
 await page.locator('#fspInfo > summary').focus();await page.keyboard.press('Enter');
 assert.equal(await page.locator('#fspInfo').evaluate(e=>e.open),true);
 assert.equal(await page.locator('.fsp-info-case').count(),10);
 assert.equal(await page.locator('#fspInfo .fsp-info-group').count(),3);
 for(const item of data.items){
  const article=page.locator(`[data-finding-id="${item.id}"]`);
  assert.equal(await article.locator(':scope > a').getAttribute('href'),item.fsp_evidence[0].url);
  await article.locator('summary').click();
  assert.equal(await article.locator('blockquote').count(),item.fsp_evidence.length+item.gs_comparators.length);
  for(const row of [...item.fsp_evidence,...item.gs_comparators])assert.ok(await article.locator(`a[href="${row.url}"]`).count());
  assert.ok((await article.innerText()).includes(item.interpretation));
 }
 for(const [subject,count] of [['Deutsch',2],['Sachunterricht',5],['Mathematik',3],['',10]]){
  await page.selectOption('#fspInfoSubject',subject);assert.equal(await page.locator('.fsp-info-case').count(),count);
 }
 const links=await page.locator('#fspInfo a').evaluateAll(nodes=>nodes.map(a=>({href:a.href,target:a.target,rel:a.rel})));
 assert.ok(links.length>50);for(const a of links){assert.match(a.href,/^https:\/\/www\.schulportal\.sachsen\.de\/lplandb\/lehrplan\/\d+#page\d+_\d+$/);assert.equal(a.target,'_blank');assert.ok(a.rel.includes('noopener'));}
 assert.deepEqual(await page.evaluate(()=>({storage:JSON.stringify(localStorage),subject:document.getElementById('subject').value,topic:document.getElementById('topic').value,baseline:document.getElementById('baseline').value})),before);
 await page.locator('#fspInfo').scrollIntoViewIfNeeded();
 await page.screenshot({path:'/tmp/lzk-fsp-info-desktop.png'});
 await page.setViewportSize({width:390,height:844});await page.selectOption('#fspInfoSubject','Mathematik');
 await page.locator('[data-finding-id="M-01"] summary').click();await page.locator('[data-finding-id="M-01"]').scrollIntoViewIfNeeded();
 assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=window.innerWidth+1));
 await page.screenshot({path:'/tmp/lzk-fsp-info-mobile.png'});
 await page.emulateMedia({media:'print'});assert.equal(await page.locator('#fspInfo').isVisible(),false);await page.emulateMedia({media:'screen'});
 await page.reload();await page.locator('#runtimeStatus').waitFor({state:'hidden'});assert.equal(await page.locator('#baseline').inputValue(),'Mein unveränderter Lehrkraftentwurf');
 assert.deepEqual(errors,[]);
 console.log('PASS: all 10 cases and excerpt links, classifications, keyboard, filters, mobile layout, print exclusion and draft preservation.');
 }finally{await browser.close();}
})().catch(e=>{console.error(e);process.exit(1)});
