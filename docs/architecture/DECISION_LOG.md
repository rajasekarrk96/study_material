# STATUS: FROZEN
**Effective Date**: 2026-08-06
**Version**: v2.3

---

# ARCHITECTURAL DECISION LOG

## ADR 1: Renaming Change Requests to Content Proposals
- **Context**: Change requests initially only targeted updates to existing lessons. However, contributors will also need to suggest new lessons, topics, quizzes, tags, or media assets.
- **Decision**: Rename the model `ChangeRequest` to `ContentProposal`. This broadens the entity to encompass any proposed change, new content, or deletions.
- **Consequences**: Editorial tables (`ContentProposal`, `ContentProposalSection`) are named uniformly to support high scalability.

## ADR 2: Decoupled Draft Content Layer
- **Context**: Storing proposals directly for every micro-edit generates high database write overhead and pollutes the review history.
- **Decision**: Introduce a distinct draft layer (`DraftLessonSection`). Contributor edits save instantly to drafts. A proposal is generated only when draft suggestions are ready to be packaged for merge review.
- **Consequences**: Simplifies continuous auto-save for users without creating spam reviews.

## ADR 3: Media Library and Search Index Bounded Separation
- **Context**: Embedding raw files or links inside Markdown notes leads to broken files and duplications. Direct searches on Markdown content are slow.
- **Decision**: Decoupled media assets into standard library tables (`Media`, `MediaFolder`). Decoupled markdown content into structured indexing chunks (`SearchDocument`, `SearchChunk`) for performant searching and future vector indexing support.
- **Consequences**: Knowledge data is fully clean and decoupled from delivery/student constraints.
