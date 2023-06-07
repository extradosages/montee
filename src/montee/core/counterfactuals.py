from montee.core.models.nodes import Node


def is_counterfactual(node: Node) -> bool:
    """
    Check if a node in a dependency graph represents a counterfactual.

    This function identifies counterfactuals based on two patterns:
    1. If the node is "had" and it is an auxiliary of a verb in past participle
        form.
    2. If the node is "if" and it governs a "had" node that is an auxiliary of
        a verb in past participle form.
    """

    head = node.get_governor()
    # Check if the node is "had" and it is an auxiliary of a verb in past
    # participle form.
    if (
        node.get_text().lower() == "had"
        and node.get_dependency_relation() == "aux"
        and head is not None
        and head.is_past_participle()
    ):
        return True

    # Check if the node is "if" and it governs a "had" node that is an auxiliary
    # of a verb in past participle form.
    if node.get_text().lower() == "if":
        for child in node.get_dependents():
            child_head = child.get_governor()
            if (
                child.get_text().lower() == "had"
                and child.get_dependency_relation() == "aux"
                and child_head is not None
                and child_head.is_past_participle()
            ):
                return True

    # If neither condition is met, the node does not represent a counterfactual.
    return False
