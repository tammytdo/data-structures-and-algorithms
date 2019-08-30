# Adding a key/value to your hashtable results in the value being in the data structure
# Retrieving based on a key returns the value stored
# Successfully returns null for a key that does not exist in the hashtable
# Successfully handle a collision within the hashtable
# Successfully retrieve a value from a bucket within the hashtable that has a collision
# Successfully hash a key to an in-range value

import pytest
from hashtable import HashTable

def test_exists():
    assert HashTable

@pytest.mark.skip()
def test_get_missing():
    ht = HashTable()


    # do this or test for return of None if you go that way
    with pytest.raises(ValueError):
        ht.get('spam')

@pytest.mark.skip()
def test_add():
    ht = HashTable()
    ht.add('spam','eggs')

    assert ht.get('spam') == 'eggs'

@pytest.mark.skip()
def test_contains():
    ht = HashTable()
    ht.add('spam','eggs')
    assert ht.contains('spam')

@pytest.mark.skip()
def test_not_contains():
    ht = HashTable()
    assert not ht.contains('spam')

def test_hash_same():
    ht = HashTable()
    assert ht.hash('taco') == ht.hash('taco')

def test_hash_in_range():
    ht = HashTable()
    assert  0 <= ht.hash('eggs') < len(ht.buckets)


def test_hash_different():
    ht = HashTable()
    assert not ht.hash('taco') == ht.hash('bell')


@pytest.mark.skip()
def test_collision():
    ht = HashTable()
    ht.add('spam','spammy stuff')
    ht.add('maps', 'mappy stuff')
    assert ht.get('spam') == 'spammy stuff'
    assert ht.get('maps') == 'mappy stuff'

