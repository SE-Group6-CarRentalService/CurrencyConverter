import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import {CarListComponent} from "./car-list/car-list.component";
import {LocationMapComponent} from "./location-map/location-map.component";
import {RentalSystemComponent} from "./rental-system/rental-system.component";
import {UserSettingsComponent} from "./user-settings/user-settings.component";
import {UserLoginComponent} from "./user-login/user-login.component";
import {RentalCheckoutComponent} from "./rental-checkout/rental-checkout.component";

const routes:Routes = [
  {path: 'cars', component: CarListComponent},
  {path: 'locations', component: LocationMapComponent},
  {path: 'rentals', component: RentalSystemComponent},
  {path: 'user', component: UserSettingsComponent},
  {path: 'login', component: UserLoginComponent},
  {path: 'checkout', component: RentalCheckoutComponent}
]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports : [RouterModule]
})
export class AppRoutingModule { }
