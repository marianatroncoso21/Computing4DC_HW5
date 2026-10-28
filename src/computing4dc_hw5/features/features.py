from .base import Feature

class BMIFeature(Feature):
    """Adds a column with Body Mass Index: weight (kg) / height (m)^2."""

    def __init__(self, new_column="bmi_calc"):
        self._new_column = new_column

    def transform(self, df):
        df = df.copy()
        df[self._new_column] = self._compute_bmi(df["height"], df["weight"])
        return df

    def _compute_bmi(self, height_cm, weight_kg):
        height_m = height_cm / 100
        return weight_kg / height_m ** 2

class GenderEncoder(Feature):
    """Adds a 0/1 column from gender (1 = female, 0 = male)."""

    def __init__(self, new_column="is_female"):
        self._new_column = new_column

    def transform(self, df):
        df = df.copy()
        df[self._new_column] = self._encode_gender(df["gender"])
        return df

    def _encode_gender(self, gender):
        return (gender == "F").astype(int)