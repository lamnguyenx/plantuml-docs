---
title: Teoz — PlantUML Official Documentation
source: https://plantuml.com/teoz
description: Official documentation for PlantUML Teoz
---

# Current "Puma" architecture

PlantUML News and information Teoz architecture Â Â Â Â

## Toward "Teoz" architecture

```plantuml
@startuml
!pragma teoz true
Alice -> Bob : hello
& Bob -> Charlie : hi
@enduml
```

## Anchors and Duration

```plantuml
@startuml
!pragma teoz true

{start} Alice -> Bob : start doing things during duration
Bob -> Max : something
Max -> Bob : something else
{end} Bob -> Alice : finish

{start} <-> {end} : some time

@enduml
```

## Pragma "teoz"
```
java -jar plantuml.jar -Pteoz=true
```

[Ref. GH-582 ]

## Nested boxes for sequence diagrams

```plantuml
@startuml
!pragma teoz true
box "component"
  box "sub1"
    participant a
  endbox
  box "sub2"
    participant b
  endbox
end box
@enduml
```

```plantuml
@startuml
!pragma teoz true
box "component"
  box "sub1\n\n"
    participant a
    box "subsub1"
      participant suba
    end box
  endbox
  box "sub2"
    participant b
  endbox
end box
@enduml
```
