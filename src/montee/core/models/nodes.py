from __future__ import annotations
from typing import List, Optional, Protocol

from montee.core.models.modal_tags import ModalTag


class Node(Protocol):
    """A protocol for a wrapper interface to an annotatable node in a parse tree."""

    id: int
    """
    A quasi-unique identifier for a node.
    
    A node id must be unique only within a given parse tree. Montee routines have
    undefined behavior otherwise.
    """

    # Write protocols
    def add_modal_trigger(self, modal_trigger: Node) -> None:
        """Annotate the node with a reference to a modal trigger for the node."""
        raise NotImplementedError

    def add_modal_tag(self, modal_tag: ModalTag) -> None:
        """Annotate the node with a modal tag."""
        raise NotImplementedError

    # Read protocols
    def get_modal_triggers(self) -> List[Node]:
        """
        Retrieve all modal trigger references the node is currently annotated with.
        """
        raise NotImplementedError

    def get_modal_tags(self) -> List[ModalTag]:
        """Retrieve all modal tags the node is currently annotated with."""
        raise NotImplementedError

    def get_text(self) -> str:
        """Retrieve the text associated with the node."""
        raise NotImplementedError

    def get_lemma(self) -> str:
        """Retrieve the lemma associated with the node."""
        raise NotImplementedError

    def get_part_of_speech(self) -> str:
        """Retrieve the part of speech tag associated with the node."""
        raise NotImplementedError

    def get_dependency_relation(self) -> str:
        """
        Retrieve the dependency relation in the parse tree for which the node is a
        dependent.
        """
        raise NotImplementedError

    def is_past_participle(self) -> bool:
        """Does the node wrap the past participle of a verb?"""
        raise NotImplementedError

    def get_governor(self) -> Optional[Node]:
        """Retrieve the governor (head) of the node in the dependency parse tree."""
        raise NotImplementedError

    def get_dependents(self) -> List[Node]:
        """
        Retrieve the dependents (children) of the node in the dependency parse tree.
        """
        raise NotImplementedError

    # Hashing, so I can put them in sets
    def __hash__(self):
        return hash(self.id)
