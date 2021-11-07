export interface ActivityMonitor {
  minStop: number;
  timeOut: number;
  stops: number;
  startTotalTime: number;
  endTotalTime: number;
  totalTime: number;
  activeTime: number;
  nonActiveTime: number;
  percentage: number;
}
