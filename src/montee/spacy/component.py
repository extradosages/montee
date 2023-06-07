from typing import Optional

from spacy.lang.en import English

from montee.core.default_lexicon import load_default_lexicon
from montee.core.models.lexicons import Lexicon
from montee.core.montee import montee as core_montee
from montee.spacy.nodes import SpacyNode
from montee.spacy.register import register


class MonteeComponent:
    lexicon: Lexicon

    def __init__(self, lexicon: Optional[Lexicon]):
        register()

        if lexicon is None:
            lexicon = load_default_lexicon()

        self.lexicon = lexicon

    def __call__(self, doc):
        # Wrap all tokens in the node api
        nodes = [SpacyNode(doc, token) for token in doc]

        # Mutates `doc`
        core_montee(self.lexicon, nodes)

        return doc


@English.factory("montee", default_config={"lexicon": None})
def montee(nlp, name, lexicon: Optional[Lexicon]):
    return MonteeComponent(lexicon)
