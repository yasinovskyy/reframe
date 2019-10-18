import pytest
import os
from reframe import Relation

@pytest.fixture
def country():
    dirname = os.path.dirname(__file__)
    country_csv_path = os.path.join(dirname, '../country.csv')
    return Relation(country_csv_path)

@pytest.fixture
def country_has_trump():
    dirname = os.path.dirname(__file__)
    country_sorted_csv_path = os.path.join(dirname, '../country_has_trump.csv')
    return Relation(country_sorted_csv_path)

def test_join(country, country_has_trump):
    country_joined = country.join(country_has_trump, left_col='code', right_col='code')
    for index, row in country_joined.iterrows():
        if row['code'] == 'USA':
            assert row['has_trump_as_president'] == True
        else:
            assert row['has_trump_as_president'] == False