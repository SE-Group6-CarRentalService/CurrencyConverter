import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { CarListComponent } from './car-list/car-list.component';
import { UserSettingsComponent } from './user-settings/user-settings.component';
import { LocationMapComponent } from './location-map/location-map.component';
import { RentalSystemComponent } from './rental-system/rental-system.component';
import { AppRoutingModule } from './app-routing.module';
import { UserLoginComponent } from './user-login/user-login.component';
import { RentalCheckoutComponent } from './rental-checkout/rental-checkout.component';

@NgModule({
  declarations: [
    AppComponent,
    CarListComponent,
    UserSettingsComponent,
    LocationMapComponent,
    RentalSystemComponent,
    UserLoginComponent,
    RentalCheckoutComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    NgbModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
