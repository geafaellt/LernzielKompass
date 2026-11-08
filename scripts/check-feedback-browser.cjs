const {chromium}=require(process.env.LZK_PLAYWRIGHT||'playwright');
const assert=require('node:assert/strict');
const {readFileSync}=require('node:fs');
const {pathToFileURL}=require('node:url');
const {resolve}=require('node:path');
(async()=>{const browser=await chromium.launch({headless:true});try{
 const page=await browser.newPage({viewport:{width:1200,height:900}}),errors=[],remote=[];
 page.on('pageerror',e=>errors.push(e.message));page.on('request',r=>{if(r.url().includes('tally.so'))remote.push(r.url())});
 await page.goto(process.env.LZK_APP_URL||pathToFileURL(resolve('index.html')).href,{waitUntil:'domcontentloaded'});
 await page.locator('#runtimeStatus').waitFor({state:'hidden'});
 const config=await page.locator('#feedback-config').textContent();assert.match(JSON.parse(config).form_url,/^https:\/\/tally\.so\/r\/[A-Za-z0-9]+$/);
 assert.equal(await page.locator('#openFeedback').isVisible(),true);
 await page.locator('#openFeedback').click();assert.equal(await page.locator('#feedbackDialog').isVisible(),true);
 const link=page.locator('#feedbackLink');assert.equal(await link.getAttribute('href'),JSON.parse(config).form_url);assert.equal(await link.getAttribute('rel'),'noopener noreferrer');assert.equal(await link.getAttribute('target'),'_blank');
 assert.equal(await page.locator('#feedbackDialog input,#feedbackDialog textarea,#feedbackDialog iframe').count(),0);
 await page.keyboard.press('Escape');assert.equal(await page.locator('#feedbackDialog').isVisible(),false);assert.equal(await page.locator('#openFeedback').evaluate(e=>e===document.activeElement),true);
 await page.locator('#startPlanning').click();await page.locator('#learningObject').evaluate(e=>{e.value='Eigene Planung bleibt privat';e.dispatchEvent(new Event('input',{bubbles:true}))});
 await page.locator('#openFeedback').click();assert.equal(await page.locator('#feedbackDialog').isVisible(),true);await page.locator('#closeFeedback').click();assert.equal(await page.locator('#learningObject').inputValue(),'Eigene Planung bleibt privat');
 for(const width of [390,320]){await page.setViewportSize({width,height:844});await page.locator('#openFeedback').click();assert.ok(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));if(width===390)await page.screenshot({path:'/tmp/lzk-feedback-mobile.png'});await page.keyboard.press('Escape')}
 assert.deepEqual(remote,[]);assert.deepEqual(errors,[]);
 const html=readFileSync('index.html','utf8');assert.ok(!html.includes('lernzielkompass@gmx.de'));
 console.log('PASS: feedback on start/planner, valid private-recipient-free link, no background requests, no draft transfer, keyboard/focus and mobile 320/390. External submission/email requires live verification.');
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
