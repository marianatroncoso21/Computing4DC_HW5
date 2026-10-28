from abc import ABCMeta, abstractmethod


class Preprocessor(metaclass=ABCMeta):
    """Interface for every preprocessing step."""

    @abstractmethod
    def transform(self, df):
        raise NotImplementedError