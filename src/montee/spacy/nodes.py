from __future__ import annotations
from typing import List, Optional 

from spacy.tokens import Doc, Token

from montee.core.models.modal_tags import ModalTag
from montee.core.models.nodes import Node


class SpacyNode(Node):
    _doc: Doc
    _token: Token

    def __init__(self, doc: Doc, token: Token):
        self.id = token.i
        self._doc = doc
        self._token = token

    def add_modal_trigger(self, modal_trigger: SpacyNode) -> None:
        self._token._.modal_triggers.append(modal_trigger._token)

    def add_modal_tag(self, modal_tag: ModalTag) -> Node:
        self._token._.modal_tags.append(modal_tag)

    def get_modal_triggers(self) -> List[Node]:
        return self._token._.modal_triggers

    def get_modal_tags(self) -> List[ModalTag]:
        return self._token._.modal_tags

    def get_text(self) -> str:
        return self._token.text

    def get_lemma(self) -> str:
        return self._token.lemma_
    
    def get_part_of_speech(self) -> str:
        return self._token.pos_

    def get_dependency_relation(self) -> str:
        return self._token.dep_

    def is_past_participle(self) -> bool:
        is_participle = self._token.tag_ == "VBN"
        return is_participle

    def get_governor(self) -> Optional[Node]:
        if self._token.head == self._token:
            return None
        return SpacyNode(self._doc, self._token.head)

    def get_dependents(self) -> List[Node]:
        return [SpacyNode(self._doc, child) for child in self._token.children]

    def __repr__(self):
        return self._token.text
