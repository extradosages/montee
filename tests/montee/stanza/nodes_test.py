from copy import deepcopy

import pytest
from stanza.models.common.doc import Document

from montee.core.models.modal_tags import ModalTag
from montee.stanza.nodes import StanzaNode


@pytest.fixture
def sentence(stanza_nlp, text):
    doc: Document = stanza_nlp(text)  # type: ignore
    return doc.sentences[0]


@pytest.fixture
def sentence_with_past_participle(stanza_nlp, text_with_past_participle):
    doc: Document = stanza_nlp(text_with_past_participle)  # type: ignore
    return doc.sentences[0]


@pytest.fixture
def node0(sentence):
    return StanzaNode(sentence, sentence.words[0])


@pytest.fixture
def node1(sentence):
    return StanzaNode(sentence, sentence.words[1])


@pytest.fixture
def node4(sentence):
    return StanzaNode(sentence, sentence.words[4])


@pytest.fixture
def node5(sentence_with_past_participle):
    return StanzaNode(
        sentence_with_past_participle, sentence_with_past_participle.words[2]
    )


def test_get_modal_tags_empty_by_default(node0: StanzaNode):
    assert node0.get_modal_tags() == []


def test_get_modal_tags_returns_set_modal_tags(node0: StanzaNode):
    new_modal_tag = ModalTag.MODAL
    new_word = deepcopy(node0._word)
    new_word._modal_tags = [new_modal_tag]  # type: ignore
    assert new_word._modal_tags == [new_modal_tag]  # type: ignore
    new_node = StanzaNode(node0._sentence, new_word)
    assert new_node.get_modal_tags() == [new_modal_tag]


def test_governor_is_none_for_root_node(node4: StanzaNode):
    assert node4.get_governor() is None


def test_governor_returns_correct_word(node1: StanzaNode):
    governor = node1.get_governor()
    assert governor is not None
    assert isinstance(governor, StanzaNode)
    assert governor.get_text() == "text"


def test_dependents_returns_no_dependents_for_leaf_node(
    node1: StanzaNode,
):
    assert node1.get_dependents() == []


def test_dependents_returns_correct_dependents(node4):
    dependents = node4.get_dependents()
    assert len(dependents) == 5
    assert dependents[0].get_text() == "This"
    assert dependents[1].get_text() == "is"
    assert dependents[2].get_text() == "a"
    assert dependents[3].get_text() == "test"
    assert dependents[4].get_text() == "."


def test_is_past_participle_is_correct(node5):
    assert node5.is_past_participle()
