import pytest

from montee.core.montee import montee
from montee.core.default_lexicon import load_default_lexicon
from montee.spacy.nodes import SpacyNode


@pytest.fixture(scope="session")
def doc(spacy_nlp, text):
    return spacy_nlp(text)


@pytest.fixture(scope="session")
def lexicon():
    return load_default_lexicon()


def test_tag_modality(lexicon, doc):
    nodes = [SpacyNode(doc, token) for token in doc]
    montee(lexicon, nodes)
    assert False
