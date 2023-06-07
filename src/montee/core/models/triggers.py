from dataclasses import dataclass
from enum import Enum
from typing import List

from montee.core.models.modal_tags import ModalTag


class EpistemicStrength(Enum):
    """The epistemic strength of a modal statement."""

    DESIRE = -3
    INTENTION = -2
    DEONTIC = -1
    DEFINITELY_NOT = 0
    UNLIKELY = 1
    POSSIBLY = 2
    PROBABLY = 3
    DEFINITELY = 4


@dataclass
class Trigger:
    """A word which triggers modality."""

    lemma: str
    modal_categories: List[str]
    strength: EpistemicStrength
    pos_tag: str

    def to_modal_tags(self) -> List[ModalTag]:
        tags = []

        if self.strength in {
            EpistemicStrength.UNLIKELY,
            EpistemicStrength.DEFINITELY_NOT,
        }:
            tags.append(ModalTag.LEXICAL_NEGATION)

        if "ATT_SAY" in self.modal_categories:
            tags.append(ModalTag.ATTITUDE_OF_SPEECH)

        if "ATT_THINK" in self.modal_categories:
            tags.append(ModalTag.ATTITUDE_OF_THOUGHT)

        if "MOD" in self.modal_categories:
            tags.append(ModalTag.MODAL)

        if "COND" in self.modal_categories:
            tags.append(ModalTag.CONDITIONAL)

        return tags
