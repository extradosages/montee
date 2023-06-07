# montee

Montee is a python library that implements a variant of the algorithm detailed in the 2021 paper [Modality and Negation in Event Extraction](https://arxiv.org/abs/2109.09393) and provides plugins for [spacy](https://spacy.io/) and [stanza](https://stanfordnlp.github.io/stanza/) to allow the algorithm to be used as part of both their nlp pipelines.

The original algorithm uses combinatory categorical grammar parses as semantic graphs underlying annotations; in order to easily integrate with popular python nlp libraries this library uses simpler dependency parse trees instead.

## Linguistic modality

From the original paper (slightly modified):
> Linguistic modality is frequently used in natural language to express uncertainty with respect to events and states. Downstream NLP tasks that depend on knowing whether an event actually occurred, such as Knowledge Graph construction, Fact-checking, Question Answering and Entailment Graph construction, can benefit from understanding modality. Such information is crucial in the medical domain, for instance, where it facilitates more accurate Information Extraction and search for radiology reports. Similarly, if we pose a question in the socio-political domain, such as _Did the protesters attack the police?_, our answer will be different depending on the evidence that the system has observed: _Protesters attacked the police_ \[yes\] or _Protesters are unlikely to have attacked the police_ \[uncertain\].

## Notes
I lack the expertise in nlp to asses the correctness of the original paper or my implementation, so I strongly encourage users to review the source code and to open issues and create pull requests.

Yeah, I thought about calling this `montee-python` but there's [already a library](https://monte-python.readthedocs.io/en/latest/) making that catchy reference.
