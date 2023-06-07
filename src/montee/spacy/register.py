from spacy.tokens import Token


def register():
    if not Token.has_extension("modal_tags"):
        Token.set_extension("modal_tags", default=[])
    if not Token.has_extension("modal_triggers"):
        Token.set_extension("modal_triggers", default=[])
