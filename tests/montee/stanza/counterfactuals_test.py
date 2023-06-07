from stanza.models.common.doc import Document

from montee.core.counterfactuals import is_counterfactual
from montee.stanza.nodes import StanzaNode


def test_check_cf_positive_1(stanza_nlp):
    # In this sentence, the word "had" is part of a counterfactual structure.
    doc: Document = stanza_nlp(
        "They would have gone, had they gotten their things together in time."
    )  # type: ignore
    sentence = doc.sentences[0]
    word = sentence.words[5]
    node = StanzaNode(sentence, word)

    assert is_counterfactual(node)


def test_check_cf_positive_2(stanza_nlp):
    # In this sentence, the word "had" is part of a counterfactual structure.
    doc: Document = stanza_nlp(
        "They would have gone, had they had transportation."
    )  # type: ignore
    sentence = doc.sentences[0]
    word = sentence.words[5]
    node = StanzaNode(sentence, word)

    assert is_counterfactual(node)


def test_check_cf_negative(stanza_nlp):
    # In this sentence, the word "had" is not part of a counterfactual structure.
    doc: Document = stanza_nlp("They had a good time at the party.")  # type: ignore
    sentence = doc.sentences[0]
    word = sentence.words[1]
    node = StanzaNode(sentence, word)

    assert not is_counterfactual(node)


def test_check_cf_if_had_positive(stanza_nlp):
    # In this sentence, the word "had" is part of a counterfactual structure following
    # "if".
    doc: Document = stanza_nlp(
        "If they had listened to me, none of this would have happened."
    )  # type: ignore
    sentence = doc.sentences[0]
    word = sentence.words[2]
    node = StanzaNode(sentence, word)

    assert is_counterfactual(node)


def test_check_cf_if_had_negative(stanza_nlp):
    # In this sentence, the word "listened" follows "if", but there is no "had" to make
    # it a counterfactual.
    doc: Document = stanza_nlp(
        "If they listened to me more often, things like this wouldn't happen."
    )  # type: ignore
    sentence = doc.sentences[0]
    word = sentence.words[2]
    node = StanzaNode(sentence, word)

    assert not is_counterfactual(node)
