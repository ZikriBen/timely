import { Component, OnInit } from '@angular/core';
import { ActivityMonitor } from '../../models/activity-monitor';
import { LocalStorageService } from '../../services/local-storage.service';

@Component({
  selector: 'app-monitor-history',
  templateUrl: './monitor-history.component.html',
  styleUrls: ['./monitor-history.component.scss'],
})
export class MonitorHistoryComponent implements OnInit {
  public activityMonitors: ActivityMonitor[];

  constructor(private localStorageService: LocalStorageService) {}

  ngOnInit(): void {
    if (this.localStorageService.getItem('activityMonitor') !== null) {
      this.activityMonitors = JSON.parse(
        this.localStorageService.getItem('activityMonitor')
      );
    }
  }
}
