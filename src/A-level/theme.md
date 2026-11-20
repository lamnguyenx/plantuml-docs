---
title: Theme — PlantUML Official Documentation
source: https://plantuml.com/theme
description: Official documentation for PlantUML Theme
---

# Themes

```plantuml
@startuml
!theme spacelab
class Example {
  Theme spacelab
}
@enduml
```

```plantuml
@startuml
!theme spacelab
a -> b
b -> c
@enduml
```

## List of available themes

- Gallery of all official PlantUML themes .
- Examples of some Puml Themes made by Brett Schwarz on the Theme Gallery .

```plantuml
@startuml
help themes
@enduml
```

```plantuml
@startjson
%get_all_theme()
@endjson
```

## Coloring message with some procedures included on some theme

- $success("<msg>")
- $failure("<msg>")
- $warning("<msg>")

```plantuml
@startuml
!theme spacelab
Bob -> Alice :  hello
Bob <- Alice :  $success("success: hello B.")
Bob -x Alice :  $failure("failure")
Bob ->> Alice : $warning("warning")
@enduml
```

## Local themes
```
!theme foo from /path/to/themes/folder
```

## Themes from the Internet
```
!theme amiga from https://raw.githubusercontent.com/plantuml/plantuml/tree/master/src/main/resources/themes
```
