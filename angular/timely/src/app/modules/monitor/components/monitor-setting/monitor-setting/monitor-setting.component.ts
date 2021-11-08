import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-monitor-setting',
  templateUrl: './monitor-setting.component.html',
  styleUrls: ['./monitor-setting.component.scss'],
})
export class MonitorSettingComponent implements OnInit {
  constructor() {}
  public isLoading: boolean = false;

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
