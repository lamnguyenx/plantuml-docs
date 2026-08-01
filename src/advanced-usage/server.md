---
title: Server — PlantUML Official Documentation
source: https://plantuml.com/server
description: Official documentation for PlantUML Server
---

# PlantUML Server

PlantUML Plugins HTTP Server Â Â Â Â

## Interactive interface
```
@startuml
Bob -> Alice : hello
@enduml
```

## Specify an initial diagram

## Metadata

## Web service mode

## PNG service

## SVG service

## ASCII Art service

## Image Map service
```
@startuml
participant Bob [[http://plantuml.com]]
Bob -> Alice : [[http://forum.plantuml.net]] hello
@enduml
```
```
<map id="plantuml_map" name="plantuml_map">
<area shape="rect" id="id1" href="http://forum.plantuml.net" title="http://forum.plantuml.net" alt="" coords="38,50,199,65"/>
<area shape="rect" id="id2" href="http://plantuml.com" title="http://plantuml.com" alt="" coords="8,3,50,116"/>
</map>
```

## Proxy service

- RESOURCE is the complete URL of the document which contains the diagram description (with the @startxxx and @endxxx tags), it could be a .html or a .txt file.
- INDEX is optional, it specifies the occurrence (starting at 0) of the diagram description that will be parsed when there are more than one diagram descriptions in the remote document. It defaults to zero.
- FORMAT is optional, it specifies the format to return. Supported values are: png , svg , eps , epstext and txt . Default is png ,

## Installation of the PlantUML Server

## Source code
