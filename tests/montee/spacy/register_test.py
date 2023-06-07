import pytest
from spacy.tokens import Token

from montee.spacy.register import register


@pytest.fixture(autouse=True)
def token_extensions():
    yield
    Token.remove_extension("modal_tags")
    Token.remove_extension("modal_triggers")


@pytest.fixture(scope="session")
def token0(spacy_nlp, text) -> Token:
    doc = spacy_nlp(text)
    return doc[0]


def test_extensions_are_not_normally_accessible(token0):
    assert not Token.has_extension("modal_tags")
    assert not Token.has_extension("modal_triggers")
    assert not hasattr(token0._, "modal_tags")
    assert not hasattr(token0._, "modal_triggers")


def test_extensions_are_accessible_after_registration(token0):
    register()

    assert token0._.modal_tags == []
    assert token0._.modal_triggers == []
