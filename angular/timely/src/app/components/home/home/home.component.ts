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

  ngOnInit(): void {
  }

  startMonitor(){
this.monitorDataService.startMonitor().subscribe(data=>{
        console.log(data)
        // if (data!=null) {

        // this.startTime=performance.now()
        // console.log(this.startTime+' im start  ')
        // }
})



  }
stopMonitor(){
this.monitorDataService.stopMonitor().subscribe(data=>{
       if (data!=null){
         console.log(JSON.stringify(data) )

        //  this.endTime=(performance.now()-this.startTime);
        //  this.endTime/=1000;
        //  Math.round(this.endTime);
        //  console.log(this.endTime+'im finishe')
       }

})
}
statusMonitor(){
this.monitorDataService.statusMonitor().subscribe(data=>{
        console.log(data)

})
}
}
