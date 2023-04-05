import { Component, OnInit } from '@angular/core';
import {FAQs} from "../mockdata/mock-faqs";

@Component({
  selector: 'app-faq',
  templateUrl: './faq.component.html',
  styleUrls: ['./faq.component.css']
})
export class FaqComponent implements OnInit {

  constructor() { }

  faqs = FAQs;

  ngOnInit(): void {
  }

}
