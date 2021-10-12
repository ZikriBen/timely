import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MonitorDataService {

  constructor(private _http:HttpClient) { }

apiUrl:string="https://localhost:44312/api/Products";

startMonitor(){
    return this._http.get(this.apiUrl);

}
stopMonitor(){
    return this._http.get(this.apiUrl);

}
}
