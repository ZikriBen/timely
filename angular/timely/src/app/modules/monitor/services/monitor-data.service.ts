import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ActivityMonitor } from '../models/activity-monitor';

@Injectable({
  providedIn: 'root',
})
export class MonitorDataService {
  constructor(private _http: HttpClient) {}

  apiUrl: string = 'http://10.0.0.2:7750/';

  startMonitor() {
    return this._http.get<string>(this.apiUrl + 'monitor_on');
  }
  stopMonitor() {
    return this._http.get<ActivityMonitor>(this.apiUrl + 'monitor_off');
  }
  statusMonitor() {
    return this._http.get<any>(this.apiUrl + 'server_status');
  }
}
