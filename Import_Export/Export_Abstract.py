from abc import ABCMeta, abstractmethod


class Export_Abstract:
    @abstractmethod
    def exportToFile(self):
        pass