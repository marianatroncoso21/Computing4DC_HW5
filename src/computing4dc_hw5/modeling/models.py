from abc import ABCMeta, abstractmethod

from sklearn.linear_model import LogisticRegression


class Model(metaclass=ABCMeta):
    @abstractmethod
    def train(self, df):
        return NotImplementedError

    @abstractmethod
    def predict(self, df):
        return NotImplementedError


class LogisticModel(Model):
    def __init__(self, features, target):
        self._features = features
        self._target = target
        self.model = LogisticRegression(max_iter=1000)

    def train(self, df):
        self.model.fit(df[self._features], df[self._target])

    def predict(self, df):
        return self.model.predict_proba(df[self._features])[:, 1]
