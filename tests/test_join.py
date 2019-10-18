import pandas as pd
import pytest
from reframe import Relation

@pytest.fixture
def makePerson():
    #data1 = {"id": [0, 1, 2], "firstName": ["Alice", "Bob", "Carol"], "lastName": ["Smith", "Johnson", "Williams"], "age": [86, 24, 37]}
    data1 = {"id": [0, 1], "firstName": ["Alice", "Bob"], "lastName": ["Smith", "Johnson"]}
    person = pd.DataFrame(data=data1)
    return Relation(person)

@pytest.fixture
def makeAddress():
    #data2 = {"id": [0, 1, 2], "street": ["102 Day St", "5401 95th Ave", "810 Mulberry Ln"], "city": ["Atlanta", "Des Moines", "Eden Prairie"], "state": ["GA", "IA", "MN"]}
    data2 = {"id": [0, 1], "city": ["Atlanta", "Des Moines"], "state": ["GA", "IA"]}
    address = pd.DataFrame(data=data2)
    return Relation(address)

@pytest.fixture
def makeAge():
    data3 = {"id": [0,1], "age": [86, 24]}
    age = pd.DataFrame(data=data3)
    return Relation(age)

@pytest.fixture
def makeContact():
    data4 = {"id": [0,1], "email": ["thesmiths@homestead.com", "bobby@site.com"], "phone": ["555-107-1234", "868-402-7539"]}
    contact = pd.DataFrame(data=data4)
    return Relation(contact)

def test_join_expected1(makePerson, makeAddress):
    personInfo = makePerson.njoin(makeAddress)
    personInfo_expected = Relation("tests/test_join_expected1.csv", sep="|")
    assert personInfo.equals(personInfo_expected)

def test_join_expected2(makePerson, makeAge):
    personInfo = makePerson.njoin(makeAge)
    personInfo_expected = Relation("tests/test_join_expected2.csv", sep="|")
    assert personInfo.equals(personInfo_expected)

def test_join_expected3(makePerson, makeContact):
    personInfo = makePerson.njoin(makeContact)
    print(personInfo)
    personInfo_expected = Relation("tests/test_join_expected3.csv", sep="|")
    print(personInfo_expected)
    assert personInfo.equals(personInfo_expected)

