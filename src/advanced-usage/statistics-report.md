---
title: Statistics Report — PlantUML Official Documentation
source: https://plantuml.com/statistics-report
description: Official documentation for PlantUML Statistics Report
---

# Enable statistics

PlantUML Advanced usage Statistics Report Â Â Â Â

- Use -enablestats flag in the command line
- Use enablestats="true" setting with the ANT task
- Globally set the environment variable PLANTUML_STATS to true
- Call OptionFlags.getInstance().setEnableStats(true) from your Java code

## Statistics Report

## Java Integration API

```plantuml
@startuml
class StatsUtil {
{static} +Stats getStats()
}
interface Stats {
+StatsTable getLastSessions()
+StatsTable getCurrentSessionByDiagramType()
+StatsTable getCurrentSessionByFormat()
+StatsTable getAllByDiagramType()
+StatsTable getAllByFormat()
}
StatsUtil -> Stats: build
Stats o--> "5" StatsTable: contains
enum StatsColumn {
SESSION_ID
VERSION
PARSED_COUNT
...
}
interface StatsTable {
+ Collection<StatsColumn> getColumnHeaders()
+ List<StatsLine> getLines()
}
StatsTable o-> StatsColumn: headers
StatsTable *--> StatsLine: contains
interface StatsLine {
}
interface StatsLine {
+Collection<StatsColumn> getColumnHeaders()
+Object getValue(StatsColumn column)
}
StatsLine o--> StatsColumn: headers
@enduml
```
