from repeated_word import repeated_word

def test_exists():
    assert repeated_word

def test_empty_string():
    str = ''
    assert repeated_word(str) == None

def test_string_one_word():
    str = 'one word'
    assert repeated_word(str) == None

def test_string_no_repeat():
    str = 'the zen of python says simple is better than complex'
    assert repeated_word(str) == None

def test_string_brief():
    str = "Once upon a time, there was a brave princess who..."
    assert repeated_word(str) == 'a'

def test_string_lengthy():
    str = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    assert repeated_word(str) == 'it'