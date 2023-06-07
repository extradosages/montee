import pytest
import stanza

from montee.stanza.register import register as register_stanza


@pytest.fixture(scope="session")
def stanza_nlp():
    register_stanza()
    return stanza.Pipeline("en", processors="tokenize, pos, lemma, depparse")
