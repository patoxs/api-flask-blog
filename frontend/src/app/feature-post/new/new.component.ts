import { Component, OnInit } from '@angular/core';
import { NewService } from './new.service';
import { NewModel } from './new.model';

@Component({
  selector: 'app-new',
  templateUrl: './new.component.html',
  styleUrls: ['./new.component.css'],
  providers: [NewService]
})
export class NewComponent implements OnInit {
  news: NewModel[];
  constructor(private newService: NewService) { }

  ngOnInit() {
    this.news = this.newService.getNewFrontPage();
    console.log(this.news);
  }

}
