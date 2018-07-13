import { Injectable } from '@angular/core';
import { MenuModel } from './menu.model';

@Injectable()
export class MenuService {
  menuList: MenuModel[] = [
    new MenuModel('#', 'Home', []),
    new MenuModel('#', 'All Pages', [
      new MenuModel('#', 'Home 2', []),
      new MenuModel('#', 'About', []),
      new MenuModel('#', 'Coming Soon', []),
      new MenuModel('#', 'Elements', []),
      new MenuModel('#', 'Typography', []),
      new MenuModel('#', 'Font Awesome', []),
      new MenuModel('#', 'Header Styles', []),
      new MenuModel('#', 'Single Blog', []),
      new MenuModel('#', '404', [])
    ]),
    new MenuModel('#', 'Gallery', []),
    new MenuModel('#', 'Author', []),
    new MenuModel('#', 'Contact', []),
    new MenuModel('#', 'Subscribe', [])
  ];

  constructor() { }

  getMenu() {
    return this.menuList.slice();
  }

}
