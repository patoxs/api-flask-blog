import { Component, OnInit } from '@angular/core';
import { MenuModel } from './menu.model';
import { MenuService } from './menu.service';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css'],
  providers: [MenuService]
})
export class MenuComponent implements OnInit {
  menuList: MenuModel[];
  constructor(private MenuService: MenuService) { }

  ngOnInit() {

  }

}
