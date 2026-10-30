from abc import ABCMeta, abstractmethod

class Feature(metaclass=ABCMeta):
    """Interface for every feature: all of them must implement transform()."""

    @abstractmethod
    def transform(self, df):
        raise NotImplementedError