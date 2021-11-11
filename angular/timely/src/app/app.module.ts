import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { HeaderComponent } from './modules/core/components/header/header.component';
import { HomeComponent } from './modules/core/components/home/home/home.component';
import { MonitorHomeComponent } from './modules/monitor/components/monitor-home/monitor-home.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MonitorSettingComponent } from './modules/monitor/components/monitor-setting/monitor-setting/monitor-setting.component';
import { MonitorDataComponent } from './modules/monitor/components/monitor-data/monitor-data/monitor-data.component';
import { MonitorCardComponent } from './modules/monitor/components/monitor-card/monitor-card/monitor-card.component';

import { MonitorHistoryComponent } from './modules/monitor/components/monitor-history/monitor-history.component';

import { MaterialModule } from 'src/material.module';
import { FocusHomeComponent } from './modules/focus/components/focus-home/focus-home.component';
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
    FocusHomeComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    MaterialModule,
    FormsModule,
  ],
  providers: [HttpClient, HttpClientModule],
  bootstrap: [AppComponent],
})
export class AppModule {}
