import pytest


@pytest.fixture
def text():
    return "This is a test text."


@pytest.fixture
def text_with_past_participle():
    return "We have tested the texts."
