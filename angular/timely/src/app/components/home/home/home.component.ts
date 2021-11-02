import { Component, OnInit } from '@angular/core';
import { MonitorDataService } from 'src/app/services/monitor-data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(private monitorDataService:MonitorDataService) { }
public startTime:number;
public endTime:number;
public time:number;
public noChangedMadeTime:number;
public workTime:number;
public isLoading:boolean=false;
public status:string;
  ngOnInit(): void {
  }

  startMonitor(){
    this.time=null;
    this.workTime=null;
    this.noChangedMadeTime=null;


this.monitorDataService.startMonitor().subscribe(data=>{
if (data!=null) {
    this.isLoading=true;

}
        this.startTime=performance.now()

})



  }
stopMonitor(){
  this.endTime=performance.now();
  this.time=(this.endTime-this.startTime);
this.monitorDataService.stopMonitor().subscribe(data=>{
       if (data!=null){
       this.noChangedMadeTime = data.reduce(function (r, a) {
  r[0] = (r[0] || 0) + a[0];

  return r;
}, []);





       }
       this.workTime=this.time-(this.noChangedMadeTime*1000);
    this.isLoading=false;


})
}
statusMonitor(){
this.monitorDataService.statusMonitor().subscribe(data=>{
if (data!=null) {
  this.status=data;
}
})
}
}
