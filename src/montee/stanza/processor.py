from typing import Optional

from stanza.pipeline.processor import Processor, register_processor

from montee.core.default_lexicon import load_default_lexicon
from montee.core.models.lexicons import Lexicon
from montee.core.montee import montee as core_montee
from montee.stanza.nodes import StanzaNode

@register_processor("montee")
class MonteeProcessor(Processor):
    """Processor that annotates modality spans based on a lexicon of trigger words."""

    _requires = set(["tokenize", "depparse"])
    _provides = set(["montee"])

    lexicon: Lexicon

    def __init__(self, lexicon: Optional[Lexicon]):
        if lexicon is None:
            lexicon = load_default_lexicon()

        self.lexicon = lexicon

    def process(self, doc):
        for sentence in doc.sents:
            nodes = [StanzaNode(sentence, word) for word in sentence.words]

            # Mutates `doc`
            core_montee(self.lexicon, nodes)

        return nodes
