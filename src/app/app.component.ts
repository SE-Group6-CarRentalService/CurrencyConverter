import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'CarRentalFE';

  minDate: Date;
  dateRange : String = '';
  carChoice : String = '';


  constructor() {
    this.minDate = new Date();
  }
}
