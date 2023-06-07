from dataclasses import dataclass
from typing import List

from montee.core.models.nodes import Node
from montee.core.models.triggers import Trigger


@dataclass
class Lexicon:
    triggers: dict[str, Trigger]

    def __init__(self, triggers: List[Trigger]):
        self.triggers = {
            (trigger.lemma, trigger.pos_tag): trigger 
            for trigger in triggers
        }

    def __contains__(self, item: str):
        return item in self.triggers

    def match(self, node: Node) -> Trigger | None:
        lemma = node.get_lemma()
        pos_tag = node.get_part_of_speech()
        return self.triggers.get((lemma, pos_tag), None)
