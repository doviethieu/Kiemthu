import pytest
from movie_ticket import movie_ticket

def test_invalid_age():
    with pytest.raises(ValueError):
        movie_ticket(-1, 21)

def test_invalid_time():
    with pytest.raises(ValueError):
        movie_ticket(20, 25)

def test_child_before_22():
    assert movie_ticket(10, 21) == 50000

def test_child_after_22():
    assert movie_ticket(10, 23) == 40000

def test_adult_before_22():
    assert movie_ticket(25, 21) == 100000

def test_adult_after_22():
    assert movie_ticket(30, 23) == 80000

def test_senior_before_22():
    assert movie_ticket(65, 20) == 70000

def test_senior_after_22():
    assert movie_ticket(70, 23) == 56000
