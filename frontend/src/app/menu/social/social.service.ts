import { Injectable } from '@angular/core';
import { SocialModel } from './social.model';

@Injectable()
export class SocialService {
  socialIcons: SocialModel[] = [
    new SocialModel('#', 'google-plus'),
    new SocialModel('#', 'twitter'),
    new SocialModel('#', 'facebook'),
    new SocialModel('#', 'vk'),
    new SocialModel('#', 'youtube-play')
  ];

  constructor() {}

  getSocialIcons() {
    return this.socialIcons.slice();
  }
}
