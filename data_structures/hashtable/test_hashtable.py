import pytest
from hashtable import HashTable

def test_exists():
    assert HashTable

def test_get_empty():
    ht = HashTable()

    with pytest.raises(ValueError):
        ht.get('')

def test_get_missing():
    ht = HashTable()

    with pytest.raises(ValueError):
        ht.get('coffee')

def test_add():
    ht = HashTable()
    ht.add('coffee', 'brew')

    assert ht.get('coffee') == 'brew'

def test_contains_one():
    ht = HashTable()
    ht.add('coffee', 'brew')

    assert ht.contains('coffee')

def test_contains_many():
    ht = HashTable()
    ht.add('coffee', 'brew')
    ht.add('tea', 'steep')
    ht.add('juice', 'press')
    assert ht.contains('tea')

def test_not_contains():
    ht = HashTable()
    assert not ht.contains('coconut water')
    assert not ht.contains('kombucha')

def test_hash_same():
    ht = HashTable()
    assert ht.hash('coffee') == ht.hash('eeffoc')
    assert ht.hash('tea') == ht.hash('aet')
    assert ht.hash('juice') == ht.hash('iuejc')

def test_hash_in_range():
    ht = HashTable()
    assert  0 <= ht.hash('coffee') < len(ht.buckets)
    assert 0 <= ht.hash('juice') < len(ht.buckets)

def test_hash_different():
    ht = HashTable()
    assert not ht.hash('coffee') == ht.hash('tea')
    assert not ht.hash('tea') == ht.hash('juice')

def test_collision():
    ht = HashTable()
    ht.add('coffee', 'brew')
    ht.add('offeec', 'nonsense')
    ht.add('tea', 'steep')
    ht.add('eat', 'bite')

    assert ht.get('coffee') == 'brew'
    assert ht.get('offeec') == 'nonsense'
    assert ht.get('tea') == 'steep'
    assert ht.get('eat') == 'bite'
