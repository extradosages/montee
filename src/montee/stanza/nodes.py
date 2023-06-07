from typing import List, Optional

from stanza.models.common.doc import Sentence, Word

from montee.core.models.modal_tags import ModalTag
from montee.core.models.nodes import Node


class StanzaNode(Node):
    _sentence: Sentence
    _word: Word

    def __init__(self, sentence: Sentence, word: Word):
        self._sentence = sentence
        self._word = word
    
    def add_modal_tag(self, modal_tag: ModalTag) -> None:
        self._word._modal_tags += [modal_tag]

    def add_modal_trigger(self, modal_trigger: Node) -> None:
        self._word._modal_triggers += [modal_trigger]

    def get_modal_tags(self) -> List[ModalTag]:
        return self._word._modal_tags

    def get_modal_triggers(self) -> List[Node]:
        return self._word._modal_triggers

    def get_text(self) -> str:
        return self._word.text

    def get_lemma(self) -> str:
        lemma = self._word.lemma
        if lemma is None:
            raise RuntimeError(
                "Word processed with stanza pipeline without lemmatization"
            )
        return lemma
    
    def get_part_of_speech(self) -> str:
        return self._word.upos

    def get_dependency_relation(self) -> str:
        relation = self._word.deprel
        if relation is None:
            raise RuntimeError(
                "Word processed with stanza pipeline without dependency parsing"
            )
        return relation

    def is_past_participle(self) -> bool:
        word = self._word
        if word.feats is None:
            return False
        is_verb = word.upos == "VERB"
        is_past_tense = "Tense=Past" in word.feats
        is_participle = "VerbForm=Part" in word.feats
        return is_verb and is_past_tense and is_participle

    def get_governor(self) -> Optional[Node]:
        one_based_index = self._word.head
        if not isinstance(one_based_index, int):
            return None
        if one_based_index == 0:
            return None
        index = one_based_index - 1
        governor = self._sentence.words[index]
        return StanzaNode(self._sentence, governor)

    def get_dependents(self) -> List[Node]:
        one_based_index = self._word.id
        return [
            StanzaNode(self._sentence, word)
            for word in self._sentence.words
            if word.head == one_based_index
        ]

    def __repr__(self):
        return self._word.text
