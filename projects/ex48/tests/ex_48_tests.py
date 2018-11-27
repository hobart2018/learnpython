from nose.tools import *
from ex48 import lexicon
from ex48.parser import *

def test_direction():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb','eat')])
def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop','in'),
                          ('stop', 'of')])

def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
    result = lexicon.scan("bear princess")
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess')])

def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ('number', 91234)])

def test_errors():
    assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', 'bear'),
                          ('error','IAS'),
                          ('noun', 'princess')])
def test_peek():
    assert_equal(peek(lexicon.scan("kill the bear")), "verb")

def test_match():
    assert_equal(match(lexicon.scan("kill the bear"),'verb'), ('verb', 'kill'))
    assert_equal(match(lexicon.scan("kill the bear"),'none'), None)

def test_parse_verb():
    word_list = lexicon.scan("of kill the bear")
    assert_equal(parse_verb(word_list), ('verb', 'kill'))

    wrong_word_list = lexicon.scan("I kill the bear")
    assert_raises(ParserError, parse_verb, wrong_word_list)

def test_parse_object():
    word_list_noun = lexicon.scan("of princess the bear")
    assert_equal(parse_object(word_list_noun), ('noun', 'princess'))

    word_list_direction = lexicon.scan("north of princess the bear")
    assert_equal(parse_object(word_list_direction), ('direction', 'north'))

    wrong_word_list = lexicon.scan("I kill the bear")
    assert_raises(ParserError, parse_object, wrong_word_list)

def test_parse_sentence():
    word_list_noun = lexicon.scan("princess kill the bear")
    sentence_noun=parse_sentence(word_list_noun)
    assert_equal(sentence_noun.subject, 'princess')
    assert_equal(sentence_noun.verb, 'kill')
    assert_equal(sentence_noun.object,'bear')

    word_list_verb = lexicon.scan("kill the bear")
    sentence_verb=parse_sentence(word_list_verb)
    assert_equal(sentence_verb.subject, 'player')
    assert_equal(sentence_verb.verb, 'kill')
    assert_equal(sentence_verb.object, 'bear')

    wrong_word_list = lexicon.scan("I kill the bear")
    assert_raises(ParserError, parse_sentence, wrong_word_list)
