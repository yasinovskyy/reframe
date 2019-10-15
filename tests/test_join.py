import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def makePerson():
    data1 = {"id": [0, 1, 2], "firstName": ["Alice", "Bob", "Carol"], "lastName": ["Smith", "Johnson", "Williams"], "age": [86, 4, 37]}
    data2 = {"id": [0, 1, 2], "street": ["102 Day St", "5401 95th Ave", "810 Mulberry Ln"], "city": ["Atlanta", "Des Moines", "Eden Prairie"], "state": ["GA", "IA", "MN"]}
    person = pd.DataFrame(data=data1)
    address = pd.DataFrame(data=data2)
    return Relation(person, address)
'''
@pytest.fixture
def makeAddress():
    data2 = {"id": [0, 1, 2], "street": ["102 Day St", "5401 95th Ave", "810 Mulberry Ln"], "city": ["Atlanta", "Des Moines", "Eden Prairie"], "state": ["GA", "IA", "MN"]}
    address = pd.DataFrame(data=data2)
    return Relation(address)
'''
def test_join_expected1(makePerson):
    personInfo = makePerson.query("id").njoin(makePerson.query("id"))
    personInfo_expected = Relation("tests/test_join_expected1.csv", sep="|")
    assert personInfo.equals(personInfo_expected)

'''
def test_join_expected2(r):
    r = r.join(["age"])
    r_expected_2 = Relation("tests/test_join_expected2.csv", sep="|")
    assert r.equals(r_expected_2)

def test_join_expected3(r):
    r = r.join(["lastName"])
    r_expected_2 = Relation("tests/test_join_expected3.csv", sep="|")
    assert r.equals(r_expected_2)
'''
