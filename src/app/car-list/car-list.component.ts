import { Component, OnInit } from '@angular/core';
import {CarOverview} from "../model/CarOverview";
import {Cars} from "../mockdata/mock-carlist";

@Component({
  selector: 'app-car-list',
  templateUrl: './car-list.component.html',
  styleUrls: ['./car-list.component.css']
})
export class CarListComponent implements OnInit {

  constructor() { }

  cars = Cars;

  ngOnInit(): void {
  }

}
