---
title: Latex — PlantUML Official Documentation
source: https://plantuml.com/latex
description: Official documentation for PlantUML Latex
---

# LaTeX Support in PlantUML

PlantUML Plugins LaTeX Â Â Â Â

### Beta Version Notice

### How to Use LaTeX Generation

- Use the -tlatex flag when operating through the command line .
- Set format="latex" when configuring the Ant task .

#### Embedding in LaTeX Documents

## Class diagram example
```
@startuml
class Subscriber {
  subscriberId
}

class AccumUsage {
  subscriberId
}

class IpSession {
  ipAddress
  specificData
  sapcOriginStateId
  apnId
}

Subscriber "1" -[#blue]-> "1..*" IpSession
Subscriber "1" --> "0..1" AccumUsage
@enduml
```

## Sequence diagram example
```
@startuml
Bob -> Alice: hello
return Ok
@enduml
```

## Creating Links in LaTeX with the hyperref Package
```
@startuml
participant Bob   [[http://www.yahoo.com]]
participant Alice [[latex://resource-interaction]]
Bob -> Alice :    [[http://www.google.com]] hello
Bob -> Alice :    [[latex://resource-interaction]] interact
@enduml
```

## Links

- Q&A 1798 : Latex TikZ support
- Q&A 3558 : export to TikZ loses links
- Q&A 10761 : Latex export limitations (font size, hyperlinks, PNG in header, scaling image to page)
- Q&A 10788 : How to set Latex Font Size
- Latex PlantUML package (Oliver Kopp 2018-2023): home , Github , CTAN
- Stackoverflow 71409448 PlantUML in Latex
- TeX Exchange 428174 : Can I use the plantUML language in LaTeX?  Yes, and prerequisites to install are listed
