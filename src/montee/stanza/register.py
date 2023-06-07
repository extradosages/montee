from stanza.models.common.doc import Word

_is_registered: bool = False


def is_registered() -> bool:
    return _is_registered


def register():
    global _is_registered
    if _is_registered:
        return
    Word.add_property("modal_tags", default=[])
    Word.add_property("modal_triggers", default=[])
    _is_registered = True
