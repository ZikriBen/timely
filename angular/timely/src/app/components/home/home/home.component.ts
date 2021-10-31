import { Component, OnInit } from '@angular/core';
import { MonitorDataService } from 'src/app/services/monitor-data.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  constructor(private monitorDataService:MonitorDataService) { }

  ngOnInit(): void {
  }

  startMonitor(){
this.monitorDataService.startMonitor().subscribe(data=>{
        console.log(data)
})



  }
stopMonitor(){
this.monitorDataService.stopMonitor().subscribe(data=>{
       if (data!=null){
         console.log(JSON.stringify(data) )
       }

})
}
statusMonitor(){
this.monitorDataService.statusMonitor().subscribe(data=>{
        console.log(data)

})
}
}