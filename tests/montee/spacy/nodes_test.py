import pytest

from montee.core.models.modal_tags import ModalTag
from montee.spacy.nodes import SpacyNode


@pytest.fixture
def doc(spacy_nlp, text):
    return spacy_nlp(text)


@pytest.fixture
def doc_with_past_participle(spacy_nlp, text_with_past_participle):
    return spacy_nlp(text_with_past_participle)


def test_spacy(doc):
    assert False


@pytest.fixture
def node1(doc):
    return SpacyNode(doc, doc[0])


@pytest.fixture
def node2(doc):
    return SpacyNode(doc, doc[1])


@pytest.fixture
def node3(doc):
    return SpacyNode(doc, doc[4])


@pytest.fixture
def node4(doc_with_past_participle):
    return SpacyNode(doc_with_past_participle, doc_with_past_participle[2])


def test_modal_tags_empty_by_default(node1: SpacyNode):
    assert node1.get_modal_tags() == []


def test_modal_tags_returns_set_modal_tags(node1: SpacyNode):
    new_modal_tag = ModalTag.MODAL
    node1._token._.modal_tags = [new_modal_tag]
    assert node1.get_modal_tags() == [new_modal_tag]


def test_governor_is_none_for_root_node(node2: SpacyNode):
    assert node2.get_governor() is None


def test_governor_returns_correct_word(node2: SpacyNode):
    governor = node2.get_governor()
    assert governor is not None
    assert isinstance(governor, SpacyNode)
    assert governor.get_text() == "This"


def test_dependents_returns_no_dependents_for_leaf_node(node2: SpacyNode):
    assert node2.get_dependents() == []


def test_dependents_returns_correct_dependents(node3: SpacyNode):
    dependents = node3.get_dependents()
    assert len(dependents) == 2
    assert dependents[0].get_text() == "a"
    assert dependents[1].get_text() == "test"


def test_is_past_participle_is_correct(node4: SpacyNode):
    assert node4.is_past_participle()
