import { Component, OnInit } from '@angular/core';
import { MenuModel } from '../menu.model';
import { MenuService } from '../menu.service';

@Component({
  selector: 'app-menu-content',
  templateUrl: './menu-content.component.html',
  styleUrls: ['./menu-content.component.css']
})
export class MenuContentComponent implements OnInit {
  menuList: MenuModel[];
  constructor(private MenuService: MenuService) { }

  ngOnInit() {
    this.menuList = this.MenuService.getMenu();
  }

}
