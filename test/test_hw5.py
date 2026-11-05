import math

import pytest

from computing4dc_hw5.hw5 import (
    Card,
    Circle,
    Deck,
    Patient,
    PlaneFigure,
    Rectangle,
    Triangle,
)

# Exercise 1: Patient


def test_patient_stores_name():
    p = Patient("Ana", ["fever", "cough"])
    assert p.name == "Ana"


def test_patient_stores_symptoms():
    p = Patient("Ana", ["fever", "cough"])
    assert p.symptoms == ["fever", "cough"]


def test_patient_tests_start_empty():
    p = Patient("Ana", ["fever", "cough"])
    assert p.tests == {}


def test_add_test():
    p = Patient("Ana", ["fever", "cough"])
    p.add_test("covid", True)
    assert p.tests == {"covid": True}


def test_has_covid_positive_test():
    p = Patient("Ana", ["fever", "cough"])
    p.add_test("covid", True)
    assert p.has_covid() == 0.99


def test_has_covid_negative_test():
    p = Patient("Ana", ["fever", "cough"])
    p.add_test("covid", False)
    assert p.has_covid() == 0.01


def test_has_covid_without_test():
    p = Patient("Ana", ["fever", "cough"])
    assert p.has_covid() == pytest.approx(0.25)


# Exercise 2: Card and Deck


def test_card_stores_suit():
    c = Card("Hearts", "A")
    assert c.suit == "Hearts"


def test_card_stores_value():
    c = Card("Hearts", "A")
    assert c.value == "A"


def test_card_repr():
    c = Card("Hearts", "A")
    assert repr(c) == "A of Hearts"


def test_deck_starts_with_52_cards():
    d = Deck()
    assert len(d.cards) == 52


def test_deck_shuffle_keeps_52_cards():
    d = Deck()
    d.shuffle()
    assert len(d.cards) == 52


def test_deck_draw_removes_one_card():
    d = Deck()
    d.draw()
    assert len(d.cards) == 51


def test_deck_draw_returns_a_card():
    d = Deck()
    card = d.draw()
    assert isinstance(card, Card)


def test_deck_draw_empty_deck_returns_none():
    d = Deck()
    d.cards = []
    assert d.draw() is None


# Exercise 3: PlaneFigure and its children


def test_plane_figure_cannot_be_created():
    with pytest.raises(TypeError):
        PlaneFigure()


def test_triangle_perimeter():
    t = Triangle(4, 3, 5, 3)
    assert t.compute_perimeter() == 12


def test_triangle_surface():
    t = Triangle(4, 3, 5, 3)
    assert t.compute_surface() == 6


def test_rectangle_perimeter():
    r = Rectangle(4, 3)
    assert r.compute_perimeter() == 14


def test_rectangle_surface():
    r = Rectangle(4, 3)
    assert r.compute_surface() == 12


def test_circle_perimeter():
    c = Circle(1)
    assert c.compute_perimeter() == pytest.approx(2 * math.pi)


def test_circle_surface():
    c = Circle(1)
    assert c.compute_surface() == pytest.approx(math.pi)
