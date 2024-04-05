 const {test, expect} = require('@playwright/test');

 test('First Playwright Test', async ({browser,page}) =>
 {

    // chorme - plugins / cookies
    /* default configuration, better call page if do not need any special configuration of the new context
        const context = await browser.newContext();
        const page = await context.newPage();
    */
    await page.goto("https://rahulshettyacademy.com/locatorspractice/");
    // get title - assertion
    console.log(await page.title());

 });

 test('Google test', async ({page}) => 
 {

    await page.goto("https://google.com")
    console.log(await page.title());
    await expect(page).toHaveTitle("Google");

 });

