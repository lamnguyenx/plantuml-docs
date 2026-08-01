---
title: Faq Install — PlantUML Official Documentation
source: https://plantuml.com/faq-install
description: Official documentation for PlantUML Faq Install
---

# Local Installation notes

PlantUML News and information Installation notes Â Â Â Â

## Sequence Diagram
```
java -jar plantuml.jar -verbose sequenceDiagram.txt
```
```
@startuml
Alice -> Bob: test
@enduml
```

## Other Diagrams
```
java -jar plantuml.jar -testdot
```
```
@startuml
testdot
@enduml
```
```
java -jar plantuml.jar -verbose classDiagram.txt
```
```
@startuml
A <|-- B
@enduml
```
