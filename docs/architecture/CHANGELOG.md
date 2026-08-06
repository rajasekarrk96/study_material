# STATUS: FROZEN
**Effective Date**: 2026-08-06
**Version**: v2.3

---

# CHANGELOG

## [v2.3] — 2026-08-06
### Added
- Bounded context design (Separation of Knowledge, Curriculum, and Platform Layers).
- Media Library support (`Media`, `MediaFolder`, `MediaTag`, `MediaReference`).
- Decoupled Search Index structures (`SearchDocument`, `SearchChunk`, `SearchKeyword`).
- Roadmap nodes and prerequisite edge structures (`RoadmapNode`, `RoadmapEdge`).
- Draft layer saving tables (`DraftLessonSection`).
- Proposal checklists, AI generated source metadata tracking, and quality score breakdowns.
- Dynamic `PermissionMatrix` and user enrollment mappings (`UserCourse`).

### Changed
- Renamed all `ChangeRequest` references to `ContentProposal` to cover insertions and configurations.
