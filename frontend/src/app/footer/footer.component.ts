import { Component, OnInit } from '@angular/core';
import { MenuModel } from '../menu/menu.model';
import { FooterService } from './footer.service';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css'],
  providers: [FooterService]
})
export class FooterComponent implements OnInit {
  footerMenu: MenuModel[];
  constructor(private FooterService: FooterService) { }

  ngOnInit() {
    this.footerMenu = this.FooterService.getFooter();
  }

}
