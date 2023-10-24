import abc

from design_pattern.observer_pattern.observer import Observer


class Subject(abc.ABC):
    @abc.abstractmethod
    def register_observer(self, observer: Observer):
        pass

    @abc.abstractmethod
    def remover_observer(self, observer: Observer):
        pass

    @abc.abstractmethod
    def notify_observer(self):
        pass
