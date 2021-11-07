import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { MonitorDataService } from 'src/app/modules/monitor/services/monitor-data.service';
import { ActivityMonitor } from '../../../../monitor/models/activity-monitor';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  constructor(private monitorDataService: MonitorDataService) {}

  public isLoading: boolean = false;
  public activityMonitor: ActivityMonitor;
  ngOnInit(): void {}

  startMonitor() {
    this.monitorDataService.startMonitor().subscribe((data) => {
      if (data != null) {
        console.log(data);

        this.isLoading = true;
      }
    });
  }
  stopMonitor() {
    this.monitorDataService.stopMonitor().subscribe((data) => {
      if (data != null) {
        this.activityMonitor = data;
        console.log(this.activityMonitor);
      }
      this.isLoading = false;
    });
  }
  statusMonitor() {
    this.monitorDataService.statusMonitor().subscribe((data) => {
      if (data != null) {
      }
    });
  }
}
