import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { HeaderComponent } from './modules/core/components/header/header.component';
import { HomeComponent } from './modules/core/components/home/home/home.component';
import { MonitorHomeComponent } from './modules/monitor/components/monitor-home/monitor-home.component';
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatSliderModule } from '@angular/material/slider';
import { MatButtonModule } from '@angular/material/button';
import { MonitorSettingComponent } from './modules/monitor/components/monitor-setting/monitor-setting/monitor-setting.component';
import { MonitorDataComponent } from './modules/monitor/components/monitor-data/monitor-data/monitor-data.component';
import { MonitorCardComponent } from './modules/monitor/components/monitor-card/monitor-card/monitor-card.component';
import { MatCardModule } from '@angular/material/card';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MonitorHistoryComponent } from './modules/monitor/components/monitor-history/monitor-history.component';
import { MatGridListModule } from '@angular/material/grid-list';
import { ScrollingModule } from '@angular/cdk/scrolling';
import { MatSidenavModule } from '@angular/material/sidenav';
@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    MonitorHomeComponent,
    MonitorSettingComponent,
    MonitorDataComponent,
    MonitorCardComponent,
    MonitorHistoryComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    MatSliderModule,
    MatButtonModule,
    MatCardModule,
    MatProgressSpinnerModule,
    MatGridListModule,
    ScrollingModule,
    MatSidenavModule,
  ],
  providers: [HttpClient, HttpClientModule],
  bootstrap: [AppComponent],
})
export class AppModule {}
