import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class MonitorDataService {

  constructor(private _http:HttpClient) { }

apiUrl:string="http://10.0.0.5:7750/";

startMonitor(){

    return this._http.get(this.apiUrl+'monitor_on');


}
stopMonitor(){
    return this._http.post<any>(this.apiUrl+'monitor_off',{});

}
statusMonitor(){
    return this._http.get<any>(this.apiUrl+'server_status');

  }
}
