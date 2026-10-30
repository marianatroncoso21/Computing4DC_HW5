from abc import ABCMeta, abstractmethod

import pandas as pd
from sklearn.model_selection import train_test_split


class DataLoader(metaclass=ABCMeta):
    @abstractmethod
    def load(self):
        return NotImplementedError


class CSVLoader(DataLoader):
    def __init__(self, path):
        self.path = path

    def load(self):
        df = pd.read_csv(self.path)
        train, test = train_test_split(df, test_size=0.2, random_state=42)
        return train, test
