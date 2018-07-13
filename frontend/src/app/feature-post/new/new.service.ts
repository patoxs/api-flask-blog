import { Injectable } from '@angular/core';
import { NewModel } from './new.model';

@Injectable()
export class NewService {
  newFrontPage: NewModel[] = [
    new NewModel('assets/images/posts/features/1.jpg', 'politics', 'U.S. House Chamber Closed After Unknown Material', 'August 6, 2015', 1456, 32),
    new NewModel('assets/images/posts/features/2.jpg', 'sports', 'Philip Rivers: I’m going to be a Charger, wherever we are', 'August 6, 2015', 1456, 32),
    new NewModel('assets/images/posts/features/3.jpg', 'money', 'U.S. Flag Raised Over Embassy in Republic of Cuba', 'August 6, 2015', 1456, 32),
    new NewModel('assets/images/posts/features/4.jpg', 'world', 'Death Toll in Chinese Port Blasts Rises to 104', 'August 6, 2015', 1456, 32)
  ];

  constructor() { }

  getNewFrontPage() {
    return this.newFrontPage.slice();
  }

}
