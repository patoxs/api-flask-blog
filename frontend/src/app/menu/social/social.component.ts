import { Component, OnInit } from '@angular/core';
import { SocialService } from './social.service';
import { SocialModel } from './social.model';

@Component({
  selector: 'app-social',
  templateUrl: './social.component.html',
  styleUrls: ['./social.component.css'],
  providers: [SocialService]
})
export class SocialComponent implements OnInit {
  iconList: SocialModel[];
  constructor(private SocialService: SocialService) { }

  ngOnInit() {
    this.iconList = this.SocialService.getSocialIcons();
  }

}
