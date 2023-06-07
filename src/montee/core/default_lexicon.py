from csv import reader
from importlib import resources
from typing import List

import montee.data as data
from montee.core.models.lexicons import Lexicon
from montee.core.models.triggers import EpistemicStrength, Trigger


def load_default_lexicon() -> Lexicon:
    """Load the default lexicon."""
    triggers: List[Trigger] = []

    with resources.open_text(data, "default_lexicon.csv") as file:
        rows = reader(file)
        for row in rows:
            lemma = row[0]
            modal_categories = row[1].split()
            strength = EpistemicStrength(int(row[2]))
            pos_tag = row[3]
            trigger = Trigger(
                lemma=lemma,
                modal_categories=modal_categories,
                strength=strength,
                pos_tag=pos_tag,
            )
            triggers.append(trigger)

    return Lexicon(triggers=triggers)
