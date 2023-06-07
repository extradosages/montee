import pytest
# from stanza.models.common.doc import Word

from montee.stanza.register import register


# @pytest.fixture(autouse=True)
# def word_extensions():
#     yield
#     Word.remove_property("modal_tags")
#     Word.remove_property("modal_triggers")


@pytest.fixture
def word0(stanza_nlp, text):
    doc = stanza_nlp(text)
    sentence = doc.sentences[0]
    return sentence.words[0]


# def test_extensions_are_not_normally_accessible(word0):
#     assert not hasattr(word0, "_modal_tags")
#     assert not hasattr(word0, "_modal_triggers")


def test_extensions_are_accessible_after_registration(word0):
    register()

    assert word0._modal_tags == []
    assert word0._modal_triggers == []
