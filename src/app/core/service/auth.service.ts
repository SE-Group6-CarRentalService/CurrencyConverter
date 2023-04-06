import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {LoginDto} from "../model/login-dto";
import {AuthenticationDto} from "../model/authentication-dto";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  url = 'http://localhost:8080/';

  constructor(private http : HttpClient) {

  }

  login(loginDto : LoginDto) : Observable<AuthenticationDto>{
    return this.http.post<AuthenticationDto>(this.url + 'v1/customers/login', loginDto);
  }

  isLoggedIn() : Boolean{
    return false;
  }
}
