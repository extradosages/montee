import pytest
import spacy

from montee.spacy.register import register as register_spacy


@pytest.fixture(scope="session")
def spacy_nlp():
    register_spacy()
    return spacy.load("en_core_web_sm")
