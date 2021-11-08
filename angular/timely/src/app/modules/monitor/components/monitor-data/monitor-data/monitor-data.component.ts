import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ActivityMonitor } from '../../../models/activity-monitor';
import { LocalStorageService } from '../../../services/local-storage.service';
import { MonitorDataService } from '../../../services/monitor-data.service';

@Component({
  selector: 'app-monitor-data',
  templateUrl: './monitor-data.component.html',
  styleUrls: ['./monitor-data.component.scss'],
})
export class MonitorDataComponent implements OnInit {
  constructor(
    private monitorDataService: MonitorDataService,
    public localStorageService: LocalStorageService,
    private router: Router
  ) {}
  public isLoading: boolean = false;
  public activityMonitors: ActivityMonitor[];
  public activityMonitor: ActivityMonitor;

  public startTime: any;
  ngOnInit(): void {
    if (this.localStorageService.getItem('activityMonitor') === null) {
      this.activityMonitors = [];
    } else {
      this.activityMonitors = JSON.parse(
        this.localStorageService.getItem('activityMonitor')
      );
    }
  }
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
        this.activityMonitors.push(data);
        this.localStorageService.setItem(
          'activityMonitor',
          JSON.stringify(this.activityMonitors)
        );
        console.log(this.activityMonitors);
      }
      this.isLoading = false;
    });
  }

  moveToHistory() {
    this.router.navigate(['/monitor-history']);
  }
}
