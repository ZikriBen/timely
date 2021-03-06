import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
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
  public times: number[] = [1, 2, 3, 4, 5, 6, 7, 8];
  //monitor Setting Controls
  public monitorSetting: FormGroup;
  // public totalTime: FormControl;
  // public minStop: FormControl;

  ngOnInit(): void {
    this.monitorSetting = new FormGroup({
      totalTime: new FormControl(this.times),
    });
  }
}
