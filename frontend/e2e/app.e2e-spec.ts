import { EbPage } from './app.po';

describe('eb App', () => {
  let page: EbPage;

  beforeEach(() => {
    page = new EbPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
