from abc import ABC, abstractmethod

class IMonitor(ABC):

    @property
    @abstractmethod
    def running(self):
        pass

    @property
    @abstractmethod
    def total(self):
        pass

    @abstractmethod
    def monitoring_loop(self):
        pass

    @abstractmethod
    def start_monitor(self):
        pass

    @abstractmethod
    def stop_monitor(self):
        pass

    @abstractmethod
    def reset_monitor(self):
        pass

    @abstractmethod
    def calculate(self):
        pass

    
class TestMonitor(IMonitor):
    def __init__(self, total) -> None:
        self.__running = False
        self.__total = total
        
    def start_monitor(self):
        print("Started")

    def running(self):
        return self.__running
    
    def total(self):
        return self.__total

