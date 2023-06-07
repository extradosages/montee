from typing import List

from montee.core.counterfactuals import is_counterfactual
from montee.core.models.lexicons import Lexicon
from montee.core.models.modal_tags import ModalTag
from montee.core.models.nodes import Node


def _is_ancestor(node: Node, potential_descendent: Node, visited=None) -> bool:
    """
    Checks if there's a path from the start node to the end node in the graph.
    Uses a DFS-like approach to check for the path.
    """
    if visited is None:
        visited = set()

    if node == potential_descendent:
        return True
    if node in visited:
        return False

    visited.add(node)

    for node in node.get_dependents():
        if _is_ancestor(node, potential_descendent, visited):
            return True

    return False


def _get_local_triggers(
    trigger_nodes: List[Node], node: Node
) -> List[Node]:
    """
    Checks if there's a path from the node to any of the previously tagged nodes.
    If there is, assigns the modal tags of the target node to the source node.
    """
    local_triggers = set()

    for potential_descendent in trigger_nodes:
        if _is_ancestor(node, potential_descendent):
            local_triggers.add(potential_descendent)

    return list(local_triggers)


def montee(
    lexicon: Lexicon,
    nodes: List[Node],
) -> List[Node]:
    """
    Tags a list of nodes with their modality.
    """
    trigger_nodes = set()

    for node in nodes:
        trigger = lexicon.match(node)
        if trigger is not None:
            for modal_tag in trigger.to_modal_tags():
                node.add_modal_tag(modal_tag)
            trigger_nodes.add(node)
        if is_counterfactual(node):
            node.add_modal_tag(ModalTag.COUNTERFACTUAL)
            trigger_nodes.add(node)

    for node in nodes:
        local_triggers = _get_local_triggers(trigger_nodes, node)
        for trigger in local_triggers:
            node.add_modal_trigger(trigger)

    return nodes
