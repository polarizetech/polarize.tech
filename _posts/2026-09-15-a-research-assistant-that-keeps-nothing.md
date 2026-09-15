---
title: "A research assistant that keeps nothing"
description: >-
  zdr-research-chat: a voice research assistant where the model, embeddings,
  speech-to-text and text-to-speech all run on one machine — how the
  zero-retention claim is checked, and the four places it deliberately is not true.
date: 2026-09-15 07:00:00 -0600
project: method
status: published
tier: A
claims:
citations:
image: /assets/posts/locked-laptop.jpg
image_alt: >-
  A closed laptop lying on brick paving, wrapped crosswise in a heavy chain held
  shut with a padlock.
image_credit: Santeri Viinamäki
image_license: CC BY-SA 4.0
image_license_url: https://creativecommons.org/licenses/by-sa/4.0/
image_source_url: https://commons.wikimedia.org/wiki/File:Locked_computer_laptop.jpg
summary: >-
  Most private AI is private because a vendor promises not to look. This stack is
  private because the conversation never leaves the machine — a property checked
  with a socket listing rather than a policy. It keeps a git-tracked research
  journal, answers by voice from a phone, and ships a firewall, because the machine
  it was built on turned out to be answering strangers.
---

A tool write-up. zdr-research-chat is the research assistant behind this site: a chat and
voice interface to a language model where every component that touches the conversation runs
on the author's own machine. Built for work that produces a written record.

## What runs where

| function | runs on | leaves the machine |
|---|---|---|
| language model | Ollama, host-native, on the GPU | no |
| embeddings | Ollama, host-native | no |
| chat interface and retrieval | Open WebUI, in a container | no |
| vector store | Qdrant, in a container | no |
| speech-to-text | faster-whisper, inside Open WebUI | no |
| text-to-speech | Kokoro, host-native | no |
| phone access | Tailscale private network, HTTPS | encrypted end to end between own devices |
| journal | a local git repository | only on push, to its own private remote |

The model and the voice synthesis run outside containers because containers on Apple Silicon
cannot reach the GPU. Everything else is in containers and bound to loopback.

## Checking the claim

Zero retention is stated as something to verify, not something to trust. Three checks:

1. **List live connections during a conversation.** Nothing in the chat path should connect
   anywhere but the local machine.
2. **Turn off Wi-Fi.** Chat, retrieval, speech-to-text and text-to-speech keep working. Only
   phone access and journal pushes need a network.
3. **Read the switches.** Open WebUI's telemetry, analytics, update check and web search are
   off in the environment file. Qdrant's usage statistics are off in the compose file.

**The Qdrant switch was missing until 2026-09-15.** Qdrant ships with usage statistics on,
and the stack never turned them off, so one of its two containers was sending anonymised
usage data while the documentation said telemetry was off. Found while checking this write-up
against the code rather than the README. The switch is now set, and the repository's
self-check fails if it is ever removed.

## Where it deliberately is not zero-retention

Four exceptions, each off unless switched on, each documented in the file that makes the
request.

| tool | reaches | sends |
|---|---|---|
| literature search | OpenAlex, Europe PMC, Crossref, DANDI | search terms and DOIs |
| web search | DuckDuckGo | the query; disabled in the shipped config, and per chat when enabled |
| air quality | OpenAQ, and a geocoder if given a place name | coordinates or the place name |
| video transcripts | YouTube | a public video id |

None of these sees the conversation. A search query is still data, and those services log
requests like any website.

## A tier, not a slogan

"Zero data retention" describes where the stack is pointed, not the code. Every model,
embedding, speech and voice backend is a URL. The deployment declares which tier it is in:

| tier | means | checkable how |
|---|---|---|
| local | every backend on this machine | a connection listing during a conversation |
| self-hosted | own hardware, own jurisdiction | own network |
| managed zero-retention | a vendor with a contractual guarantee | not checkable — a contract, not a measurement |
| cloud | no guarantee | — |

Only `local` can be verified from the machine itself. It is the default.

## The journal

The assistant can make three kinds of write — a finding, a theory update, a session log —
into a separate git repository.

- **Only on an explicit request** ("log that", "save this"). Otherwise the write is refused
  and the assistant says nothing was written.
- **One commit per write, append-only.** No amend, no rebase, no force-push, no whole-file
  rewrite. The history of a theory file is the history of the thinking.
- **The container never runs git.** The tool writes the file and queues a request; a
  committer on the host turns each request into one commit. A crashed container cannot leave
  a repository half-written.

## Literature: the model only asks

In the literature tool the model's whole job is to turn a request into search terms and pick
a function. The archive ranks the results. The tool draws titles, authors, abstracts and
retraction notices straight from the archive's records into a panel. The model is told the
reader can already see the panel and not to restate it.

**A citation on screen never passed through the model**, so the model cannot misquote it.
Tools that place a language model between the reader and the paper are deliberately not
used. The archives are a fixed allowlist of four hosts, enforced in code.

## Memory is the design constraint

On a 16 GB machine the model shares memory with the containers, the embedding model and the
operating system. If the machine is swapping, the model is too big, and no quantisation
setting recovers it. A smaller model that fits in memory beats a larger one that pages.

Two further rules from running it:

- **Avoid models that reason before calling a tool.** Journal writes and searches are tool
  calls; a model that thinks at length before each one turns a voice exchange into a wait.
- **Raise the context length.** The runtime's default context is small enough that a system
  prompt plus a few tool definitions can silently push the tools out.

## Why a firewall ships with it

A laptop can hold a publicly routable address with no router in front of it. Then every
service listening on all interfaces is on the open internet — including a model server that
must listen beyond loopback so the containers can reach it.

On the machine this was built on, that was not hypothetical. Counted from the model server's
own access log: **1,009 successful inference requests from 160 addresses outside any private
or tailnet range**, 5,985 outside requests in all, between 15 August and 9 September 2026.
The last is on 9 September, the day a default-deny firewall for the public interface was
committed. Local requests continue in the same log after it.

So the firewall travels with the stack: loopback, the tailnet and the container bridge stay
open, the public interface does not. A network check reports in one line whether a newly
joined network is hiding the machine or exposing it.

## Limits

- **An 8B-class model on a laptop is not a frontier model.** The trade is capability for
  being usable with material that should not be uploaded.
- **macOS on Apple Silicon only**, 16 GB minimum. The GPU paths assume it.
- **Tailscale's coordination service sees device metadata**, not content.
- **The four exceptions above are real egress** whenever they are switched on.
