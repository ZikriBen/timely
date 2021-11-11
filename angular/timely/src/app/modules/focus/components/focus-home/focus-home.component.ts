import { Component, OnInit } from '@angular/core';
import { FocusDataService } from '../../services/focus-data.service';

@Component({
  selector: 'app-focus-home',
  templateUrl: './focus-home.component.html',
  styleUrls: ['./focus-home.component.scss'],
})
export class FocusHomeComponent implements OnInit {
  constructor(public focusDataService: FocusDataService) {}

  ngOnInit(): void {}
  StartFocus() {
    this.focusDataService.startFocus().subscribe((data) => {
      console.log(data);
    });
  }
  StopFocus() {
    this.focusDataService.stopFocus().subscribe((data) => {
      console.log(data);
    });
  }
}
