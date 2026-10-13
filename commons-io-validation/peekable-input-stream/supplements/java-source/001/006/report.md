# Recovered generation configuration and chat provenance

Recorded on 2026-10-13 (UTC). This annotation corrects generation-provenance
claims after consulting the original local session records and the operator's
confirmation. It contributes no independent generation or measurement.

## Original claim and correction

The sealed generation metadata described the model and settings as unknown.
The historical JSON record also lacked a retained fresh-chat attestation. Those
fields describe what was captured in the original manifests, not the availability
of evidence in the original sessions.

Both initial generation turns used **GPT-6.1 Sol** (`gpt-6.1-sol`) with
**Extra High** reasoning effort (`xhigh`). Each generation started in a distinct
user-created chat with its own prompt attachment and without prior conversation
history. The operator confirmed that both chats were isolated and had no prior
context. Applicable working instructions and the assigned inputs were still part
of each generation's context.

## Parent records

| Generation | Original generation seal SHA-256 |
| --- | --- |
| json-001 | 482c9deffe47d4fc69f8fee5e4380610991893d447a38fe0ca6973baece488fd |
| java-source-001 | 28ac9b72af259f32261cb569e3ce65515007f3089213024d5065b60adcec9d5d |

Each registered copy of this annotation is linked by the preservation manager to
its own parent and exact seal. Original manifests, environment snapshots, reports,
test sources, execution records, and seals remain unchanged.

## Primary session evidence

The following are selected literal field values from the local JSONL records,
not inferred application defaults. Line numbers are one-based. Both app threads
are titled `Generate PeekableInputStream tests`; their distinct IDs identify them.

| Field or locator | JSON generation | Java-source generation |
| --- | --- | --- |
| Session ID | 01a13186-3cfe-7ae0-84e5-3023fde21d62 | 01a13245-fd2a-75a2-8cb3-b95edbb07071 |
| Initial generation turn ID | 01a13186-410f-7523-bc7d-006ab29d1d4c | 01a13246-00eb-78c1-8be4-c650aeecd821 |
| Session creation timestamp, line 1 | 2026-10-12T19:10:43.645Z | 2026-10-12T22:40:10.221Z |
| Initial turn-context timestamp, line 8 | 2026-10-12T19:10:46.436Z | 2026-10-12T22:40:14.068Z |
| `payload.model`, line 8 | gpt-6.1-sol | gpt-6.1-sol |
| `payload.effort`, line 8 | xhigh | xhigh |
| `payload.collaboration_mode.settings.reasoning_effort`, line 8 | xhigh | xhigh |
| `payload.originator`, line 1 | Codex Desktop | Codex Desktop |
| `payload.cli_version`, line 1 | 0.162.0-alpha.17.2 | 0.162.0-alpha.17.2 |
| `payload.thread_source`, line 1 | user | user |
| Initial prompt attachment, line 12 | c3caec6a-145d-4317-8bc9-c081b55d479c/Pasted text.txt | 440deb5a-7c09-49a5-9a02-9619c0f34970/Pasted text.txt |
| First generation final response | Line 152 | Line 271 |

JSON session file:
`C:/Users/edyko/.codex/sessions/2026/10/12/rollout-2026-10-12T15-10-43-01a13186-3cfe-7ae0-84e5-3023fde21d62.jsonl`.

Java-source session file:
`C:/Users/edyko/.codex/sessions/2026/10/12/rollout-2026-10-12T18-40-10-01a13245-fd2a-75a2-8cb3-b95edbb07071.jsonl`.

The session starts and initial prompts were inspected. The JSON generation's
first final response reports that no prohibited behavioral material was used;
the Java-source generation's first final response reports no prohibited exposure.
The Java-source sealed manifest also contains `isolation.freshChat: true`.
The operator's confirmation during this review supplies an explicit attestation
for both chats. This is procedural isolation, consistent with the study protocol.

The exact runtime version above is the session's `cli_version`; it is not a claim
about a separately identified desktop UI build. Unrecorded sampling parameters
and the original JSON freeze timestamp are not reconstructed from these fields.
The original WIT-UP analyzed JAR and producer revision remain unverified.

## Interpretation correction

The prompts did not prescribe a fixed test count. The generated suite sizes,
10 JSON cases and 20 Java-source cases, and their different assertions are study
outcomes to explain. Unequal suite size is not itself a violation of the protocol
or an independent uncontrolled generation setting. The report should examine
which available information, supported fixtures, and resulting assertions account
for the observed difference in mutant detection; this annotation does not claim
that their individual contributions have already been isolated.

There is one generation per source condition. The pilot therefore describes the
observed pair without estimating repeatability or general superiority. The
operator has deferred additional generations pending the professor's feedback.
No test, command, measurement, or pipeline outcome is reclassified by this
provenance correction.
