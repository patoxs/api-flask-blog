import { MenuModel } from '../menu/menu.model';

export class FooterService {
  footerMenu: MenuModel[] = [
    new MenuModel('#', 'Mauro', [
      new MenuModel('#', 'Politics', []),
      new MenuModel('#', 'Sports', []),
      new MenuModel('#', 'Money', []),
      new MenuModel('#', 'World', []),
    ]),
    new MenuModel('#', 'sports', [
      new MenuModel('#', 'NFL', []),
      new MenuModel('#', 'MLB', []),
      new MenuModel('#', 'NBA', []),
      new MenuModel('#', 'NHL', []),
      new MenuModel('#', 'NCAAF', []),
      new MenuModel('#', 'NCAAB', []),
    ]),
    new MenuModel('#', 'life', [
      new MenuModel('#', 'People', []),
      new MenuModel('#', 'Movies', []),
      new MenuModel('#', 'Music', []),
      new MenuModel('#', 'TV', []),
      new MenuModel('#', 'Books', []),
    ]),
    new MenuModel('#', 'money', [
      new MenuModel('#', 'Markets', []),
      new MenuModel('#', 'Business', []),
      new MenuModel('#', 'Personal', []),
      new MenuModel('#', 'Cars', []),
      new MenuModel('#', 'Careers', []),
    ]),
    new MenuModel('#', 'tech', [
      new MenuModel('#', 'Politics', []),
      new MenuModel('#', 'Sports', []),
      new MenuModel('#', 'Money', []),
      new MenuModel('#', 'World', []),
    ]),
    new MenuModel('#', 'politics', [
      new MenuModel('#', 'Australia', []),
      new MenuModel('#', 'Canada', []),
      new MenuModel('#', 'France', []),
      new MenuModel('#', 'Germany', []),
      new MenuModel('#', 'Poland', []),
      new MenuModel('#', 'Ukraine', []),
    ]),
    new MenuModel('#', 'travel', [
      new MenuModel('#', 'Business', []),
      new MenuModel('#', 'Experience', []),
      new MenuModel('#', 'Destinations', []),
      new MenuModel('#', 'Flights', []),
      new MenuModel('#', 'Cruises', []),
      new MenuModel('#', 'Deals', []),
    ]),
    new MenuModel('#', 'opinion', [
      new MenuModel('#', 'BBC', []),
      new MenuModel('#', 'CNN', []),
      new MenuModel('#', 'Forbs', []),
    ]),
    new MenuModel('#', 'investing', [
      new MenuModel('#', 'Our', []),
      new MenuModel('#', 'Charity', []),
      new MenuModel('#', 'Business', []),
      new MenuModel('#', 'Help', []),
      new MenuModel('#', 'Contact', []),
    ]),
    new MenuModel('#', 'lifestyle', [
      new MenuModel('#', 'Freelance', []),
      new MenuModel('#', 'Travel', []),
      new MenuModel('#', 'Sport', []),
      new MenuModel('#', 'Money', []),
    ]),
    new MenuModel('#', 'business', [
      new MenuModel('#', 'Ideas', []),
      new MenuModel('#', 'Investors', []),
      new MenuModel('#', 'Offers', []),
    ]),
    new MenuModel('#', 'video', [
      new MenuModel('#', 'Nation', []),
      new MenuModel('#', 'World', []),
      new MenuModel('#', 'Politics', []),
      new MenuModel('#', 'Have', [])
    ]),

  ];

  constructor(){}

  getFooter(){
    return this.footerMenu.slice();
  }
}
