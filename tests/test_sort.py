import pytest
import os
from reframe import Relation

@pytest.fixture
def country():
    dirname = os.path.dirname(__file__)
    country_csv_path = os.path.join(dirname, '../country.csv')
    return Relation(country_csv_path)

@pytest.fixture
def country_sorted():
    dirname = os.path.dirname(__file__)
    country_sorted_csv_path = os.path.join(dirname, '../country_sorted.csv')
    return Relation(country_sorted_csv_path)

def test_sort(country, country_sorted):
    country = country.sort(['code'], ascending=True)
    assert country.reset_index(drop=True).equals(country_sorted)