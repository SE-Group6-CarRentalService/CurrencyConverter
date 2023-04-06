import {Component, Inject, Input, OnInit} from '@angular/core';
import {Cars} from "../mockdata/mock-carlist";
import {Router} from "@angular/router";
import {CarOverview} from "../model/CarOverview";

@Component({
  selector: 'app-car-list',
  templateUrl: './car-list.component.html',
  styleUrls: ['./car-list.component.css']
})
export class CarListComponent implements OnInit {

  constructor( private router: Router) { }

  cars = Cars;

  ngOnInit(): void {
  }

  checkout(car:CarOverview){
    if (car.rented){
      console.log("Already rented")
    }else {
      this.router.navigate(['/checkout'], {
        queryParams: {
          car : encodeURIComponent(JSON.stringify(car))
        }
      })
    }
  }
}


