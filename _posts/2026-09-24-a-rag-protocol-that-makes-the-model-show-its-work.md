---
title: "A RAG protocol that makes the model show its work"
description: >-
  A short, evidence-first protocol for using retrieval-augmented generation
  without letting a language model turn an unsupported answer into a finding.
date: 2026-09-24 07:00:00 -0600
project: method
status: published
tier: A
claims:
citations:
summary: >-
  The model is used for bounded transformations, while code controls search,
  evidence, verification, abstention and the run log.
---

Retrieval-augmented generation is not a citation system by itself. It gives a model more text;
the protocol has to make that text accountable.

This is the method used in
[KIT Scientific Research RAG](https://github.com/polarizetech/kit-scientific-research-rag):

## Pipeline

- **Plan:** turn the question into sub-questions, search terms and falsification queries.
- **Discover:** search the available literature providers and record providers that did not answer.
- **Acquire:** fetch accessible full text through the paper library.
- **Index:** split the text into passages with stable evidence IDs.
- **Retrieve and rerank:** combine lexical and semantic search, then select the passages to inspect.
- **Extract:** record the passage, source, direction, population, study role and a verbatim quote.
- **Synthesise:** let the model draft only from evidence IDs that were actually retrieved.
- **Critique:** search again for null results, opposing results and failed replications; do not merely
  ask the model to reconsider its own draft.
- **Verify:** check quotes and numbers in code, then judge each claim against its cited passage.
- **Render and log:** print bibliographic metadata from stored records and save the searches,
  passages, model versions, verdicts and limits.

## Rules

- The model fills bounded, schema-constrained forms. Code controls the sequence.
- A paper's existence and a passage's support for a claim are separate checks.
- A quote must occur in the stored passage.
- A number in a claim must occur in its cited evidence, with a matching unit where the field
  declares units.
- A citation must be an evidence ID from the run; the model does not type the bibliography.
- A passage describing another paper is a pointer, not independent first-hand evidence.
- Verifier disagreement is reported as disputed, not averaged away.
- Failed claims are removed and counted in the limits.
- "No opposing result was retrieved" is a statement about the search, not about the literature.
- Retrieved papers are data, not instructions. Text addressed to an AI reader is excluded when
  detected.
- A run's own output is never indexed as a source for a later run.

## Extending it

The engine is domain-neutral. A domain package supplies the rules that the engine cannot know:

- which study designs count as evidence;
- which sources are authoritative;
- which units are equivalent;
- which species, preparation or outcome gaps limit generalisation.

The domain is recorded in the run log. Adding a neuroscience, cardiovascular or vestibular
extension changes the field rules without forking retrieval, verification or logging.

## Limits

This does not make a language model truthful. It reduces the paths by which unsupported claims
enter an answer and makes the remaining uncertainty visible.

It does not recover missing figures or supplements, make closed papers available, or guarantee
that a verifier is right. When another model writes the answer through the repository's MCP
evidence tools, only the deterministic checks apply (evidence ids, quotes and numbers); whether a
passage supports a claim is judged only inside the pipeline. A useful result can still be
**insufficient evidence**.

## Update — 2026-09-24

The repository is now public and linked above. Before publishing, the code was brought into line
with this description: a claim whose number does not occur in its source is now removed rather
than marked disputed, and the MCP evidence tools now apply the quote and number checks too.
