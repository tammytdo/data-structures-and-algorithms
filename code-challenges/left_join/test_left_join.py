from left_join import left_join
from hashtable import HashTable

import pytest

@pytest.fixture
def empty_ht():
    ht = HashTable()

    return HashTable()

@pytest.fixture()
def synonyms():
    ht = HashTable()
    ht.add('fond', 'enamored')
    ht.add('diligent', 'employed')
    ht.add('outfit', 'garb')

    return ht

@pytest.fixture()
def antonyms():
    ht = HashTable()
    ht.add('fond', 'averse')
    ht.add('diligent', 'idle')
    ht.add('guide', 'follow')

    return ht

def test_exists():
    assert left_join

def test_empty_hashtables():
    ht1 = HashTable()
    ht2 = HashTable()
    assert left_join(ht1, ht2) == []

def test_empty_hashtable_1(empty_ht, antonyms):
    assert left_join(empty_ht, antonyms) == []

def test_empty_hashtable_2(synonyms, empty_ht):
    assert left_join(empty_ht, synonyms) == []

def test_ht_1_get(synonyms):
    assert synonyms.get('fond') == 'enamored'
    assert synonyms.get('diligent') == 'employed'


def test_left_join(synonyms, antonyms):
    assert left_join(synonyms, antonyms) == [['fond', 'enamored', 'averse'], ['diligent', 'employed', 'idle'], ['outfit', 'garb', None]]


# def test_():
#     assert