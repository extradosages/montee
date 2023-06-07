from __future__ import annotations
from typing import List, Optional

from montee.core.models.modal_tags import ModalTag
from montee.core.models.nodes import Node


class MockNode(Node):
    _text: str
    _lemma: str
    _relation: str
    _modal_tags: List[ModalTag]
    _governor: Optional[MockNode]
    _dependents: List[MockNode]

    def __init__(
        self, text: str, lemma: str, relation: str, modal_tags: List[ModalTag]
    ):
        self._text = text
        self._lemma = lemma
        self._modal_tags = modal_tags
        self._relation = relation
        self._governor = None
        self._dependents = []

    def set_governor(self, governor: Optional[MockNode]):
        self._governor = governor

    def set_dependents(self, dependents: List[MockNode]):
        self._dependents = dependents

    def get_lemma(self) -> str:
        return self._lemma

    def get_text(self) -> str:
        return self._text

    def get_dependency_relation(self) -> str:
        return self._relation

    def modal_tags(self) -> List[ModalTag]:
        return self._modal_tags

    def get_governor(self) -> MockNode | None:
        return self._governor

    def get_dependents(self) -> List[MockNode]:
        return self._dependents
