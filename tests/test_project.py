import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def r():
    data_real = {"firstName": ["Alice", "Bob", "Carol"], "lastName": ["Smith", "Johnson", "Williams"], "age": [86, 4, 37]}
    df = pd.DataFrame(data=data_real)
    return Relation(df)

def test_project_expected1(r):
    r = r.project(["firstName"])
    r_expected_2 = Relation("tests/test_project_expected1.csv", sep="|")
    assert r.equals(r_expected_2)

def test_project_expected2(r):
    r = r.project(["age"])
    r_expected_2 = Relation("tests/test_project_expected2.csv", sep="|")
    assert r.equals(r_expected_2)

def test_project_expected3(r):
    r = r.project(["lastName"])
    r_expected_2 = Relation("tests/test_project_expected3.csv", sep="|")
    assert r.equals(r_expected_2)

