import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MonitorHistoryComponent } from './modules/monitor/components/monitor-history/monitor-history.component';
import { MonitorHomeComponent } from './modules/monitor/components/monitor-home/monitor-home.component';

const routes: Routes = [
  { path: 'monitor-home', component: MonitorHomeComponent },
  { path: 'monitor-history', component: MonitorHistoryComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
