from montee.core.default_lexicon import load_default_lexicon

def test_default_lexicon_can_be_loaded():
    lexicon = load_default_lexicon()
    assert len(lexicon.triggers) == 523