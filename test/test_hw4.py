import datetime

import pandas as pd
import pytest

from computing4dc_hw5.hw4 import (
    count_simba,
    get_day_month_year,
    compute_distance
)

#1. Tests for count_simba function
def test_count_simba():
    data = [
        "Simba and Nala are lions.",
        "I laugh in the face of danger.",
        "Hakuna matata",
        "Timon, Pumba and Simba are friends, but Simba could eat the other two."
    ]
    assert count_simba(data) == 3


def test_count_simba_empty_list():
    assert count_simba([]) == 0


def test_count_simba_no_matches():
    assert count_simba(["Timon", "Pumba"]) == 0


#2. Tests for get_day_month_year function
def test_get_day_month_year_values():
    dates = [datetime.date(1992, 12, 18), datetime.date(2018, 7, 30)]
    result = get_day_month_year(dates)
    expected = pd.DataFrame(
        {"day": [18, 30], "month": [12, 7], "year": [1992, 2018]}
    )
    pd.testing.assert_frame_equal(result, expected, check_dtype=False)


def test_get_day_month_year_columns_and_shape():
    dates = [datetime.date(2016, 7, 16)]
    result = get_day_month_year(dates)
    assert list(result.columns) == ["day", "month", "year"]
    assert result.shape == (1, 3)


def test_get_day_month_year_integer_dtype():
    result = get_day_month_year([datetime.date(2009, 12, 26)])
    for col in ["day", "month", "year"]:
        assert pd.api.types.is_integer_dtype(result[col])


# 3. Tests for compute_distance function:
def test_compute_distance_returns_one_value_per_pair():
    pairs = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
    result = compute_distance(pairs)
    assert isinstance(result, list)
    assert len(result) == 2
    assert all(d > 0 for d in result)


def test_compute_distance_same_point_returns_zero():
    assert compute_distance([((41.30, 2.17), (41.30, 2.17))]) == [0.0]


def test_compute_distance_empty_list():
    assert compute_distance([]) == []


def test_compute_distance_invalid_latitude():
    with pytest.raises(ValueError):
        compute_distance([((91, 0), (0, 0))])