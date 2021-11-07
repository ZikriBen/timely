import { Component, OnInit } from '@angular/core';
import { ActivityMonitor } from '../../models/activity-monitor';
import { MonitorDataService } from '../../services/monitor-data.service';

@Component({
  selector: 'app-monitor-home',
  templateUrl: './monitor-home.component.html',
  styleUrls: ['./monitor-home.component.scss'],
})
export class MonitorHomeComponent implements OnInit {
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
