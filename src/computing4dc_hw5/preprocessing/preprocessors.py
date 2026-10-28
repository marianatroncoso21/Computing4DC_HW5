from .base import Preprocessor


class DropNaRows(Preprocessor):
    """Step 6b: remove the rows with NaN in the given columns."""

    def __init__(self, columns):
        self._columns = columns

    def transform(self, df):
        return df.dropna(subset=self._columns)


class FillNaWithMean(Preprocessor):
    """Step 6c: fill the NaN of the given columns with the column mean."""

    def __init__(self, columns):
        self._columns = columns

    def transform(self, df):
        df = df.copy()
        for column in self._columns:
            df[column] = df[column].fillna(self._compute_mean(df, column))
        return df

    def _compute_mean(self, df, column):
        return df[column].mean()