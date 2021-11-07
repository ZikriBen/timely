import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MonitorHomeComponent } from './modules/monitor/components/monitor-home/monitor-home.component';

const routes: Routes = [
  { path: 'monitor-home', component: MonitorHomeComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}
