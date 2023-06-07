from enum import Enum


class ModalTag(Enum):
    """Modal tags."""

    MODAL = "MODAL"
    """
    Represents a modal verb, which is used to indicate likelihood, ability, permission,
    or obligation. Modal tags annotate speech tokens which have been modified by the
    corresponding modal verbs.

    Example: In the sentence "She **might** come to the party", the word "come" is
    tagged as MODAL.
    """

    ATTITUDE_OF_SPEECH = "ATTITUDE_OF_SPEECH"
    """
    Represents an attitude or sentiment expressed through the mode of speech, including
    doubt, certainty, necessity, etc. Modal tags annotate speech tokens which have been
    modified by the corresponding attitude of speech.

    Example: In the sentence "I **think** it's going to rain", the phrase "it's going to
    rain" is tagged as ATTITUDE_OF_SPEECH.
    """

    ATTITUDE_OF_THOUGHT = "ATTITUDE_OF_THOUGHT"
    """
    Represents an attitude or sentiment expressed through the mode of thought, including
    belief, opinion, speculation, etc.
    Modal tags annotate speech tokens which have been modified by the corresponding
    attitude of thought.

    Example: In the sentence "I **guess** she won't come", the phrase "she won't come"
    is tagged as ATTITUDE_OF_THOUGHT.
    """

    CONDITIONAL = "CONDITIONAL"
    """
    Represents a conditional mood that is used to speak of an event whose realization is
    dependent upon another condition. Modal tags annotate speech tokens which have been
    modified by the corresponding conditional mood.

    Example: In the sentence "**If** it rains, we'll stay at home", the phrase "we'll
    stay at home" is tagged as CONDITIONAL.
    """

    COUNTERFACTUAL = "COUNTERFACTUAL"
    """
    Represents a counterfactual mood or conditional, which is used to speculate about
    what could have happened in a different world or under different circumstances.
    Modal tags annotate speech tokens which have been modified by the corresponding
    counterfactual mood.

    Example: In the sentence "**If** I were rich, I would travel the world", the phrase
    "I would travel the world" is tagged as COUNTERFACTUAL.
    """

    LEXICAL_NEGATION = "LEXICAL_NEGATION"
    """
    Represents lexical negation, which is a way of negating or denying something through
    the use of specific words like "not", "no", "never", etc. Modal tags annotate speech
    tokens which have been modified by the corresponding lexical negation.

    Example: In the sentence "I do **not** like spinach", the word "like" is tagged as
    LEXICAL_NEGATION.
    """

    NEGATION = "NEGATION"
    """
    Represents negation, which is a grammatical construction that contradicts some or
    all of a sentence's meaning. Modal tags annotate speech tokens which have been
    modified by the corresponding negation.

    Example: In the sentence "I **don't think** that's a good idea", the phrase "that's
    a good idea" is tagged as NEGATION.
    """
