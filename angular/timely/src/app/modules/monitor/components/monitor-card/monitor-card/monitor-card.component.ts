import { Component, Input, OnInit } from '@angular/core';
import { ThemePalette } from '@angular/material/core';
import { ProgressSpinnerMode } from '@angular/material/progress-spinner';

@Component({
  selector: 'app-monitor-card',
  templateUrl: './monitor-card.component.html',
  styleUrls: ['./monitor-card.component.scss'],
})
export class MonitorCardComponent implements OnInit {
  constructor() {}
  @Input() totalTime: number;
  @Input() activeTime: number;
  @Input() nonActiveTime: number;
  @Input() percentage: number = 0;
  @Input() startTotalTime: number;
  @Input() endTotalTime: number;

  public value: number;

  ngOnInit(): void {
    if (this.percentage > 0) {
      this.value = this.percentage;
    }
  }
  color: ThemePalette = 'primary';
  mode: ProgressSpinnerMode = 'determinate';
}
