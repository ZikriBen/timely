import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class FocusDataService {
  constructor(private _http: HttpClient) {}

  apiUrl: string = 'http://10.0.0.2:7750/';

  startFocus() {
    return this._http.get<any>(this.apiUrl + '/focus_on');
  }
  stopFocus() {
    return this._http.get<any>(this.apiUrl + '/focus_off');
  }
}
