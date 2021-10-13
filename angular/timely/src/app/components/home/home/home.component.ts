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

})
  }
stopMonitor(){
this.monitorDataService.stopMonitor().subscribe(data=>{

})
}

}