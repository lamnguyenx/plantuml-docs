---
title: Link — PlantUML Official Documentation
source: https://plantuml.com/link
description: Official documentation for PlantUML Link
---

# Format definition

#### Simple link

- [[http://plantuml.com]]
- [[]] (empty link)

#### Link with optional label

#### Link with optional tooltip

#### Only tooltip

#### Only tooltip and label

#### URL authentication

## Links contained curly bracket

```plantuml
@startuml
[[link{with_bracket}&id=10]]:Some activity\n(with link with brackets)\n""link{with_bracket}&id=10"";
[["link{with_bracket}"{}]]:Some activity\n(with link with brackets and empy tooltip)\n"""link{with_bracket}"{}"";
[["link{with_bracket}"{with tooltip}]]:Some activity\n(with link finished by brackets and tooltip)\n"""link{with_bracket}"{with tooltip}"";
[["link{with_bracket}&id=10"{with tooltip}]]:Some activity\n(with link with brackets and tooltip)\n"""link{with_bracket}&id=10"{with tooltip}"";
@enduml
```

## Links in sequence diagram

```plantuml
@startuml
actor Bob [[http://plantuml.com/sequence]]
actor "This is [[http://plantuml.com/sequence Alice]] actor" as Alice
Bob -> Alice [[http://plantuml.com/start]] : hello
note left [[http://plantuml.com/start]]
  a note with a link
end note
Alice -> Bob : hello with [[http://plantuml.com/start{Tooltip for message} some link]]
note right [[http://plantuml.com/start]] : another note
note left of Bob
You can use [[http://plantuml.com/start links in notes]] also.
end note
@enduml
```

## Links in class diagram

```plantuml
@startuml
class Car [[http://plantuml.com/link]]
class Wheel [[http://plantuml.com/sequence]]
note left [[http://plantuml.com]]
foo
end note
Car *-- Wheel [[http://plantuml.com/class]] : has some
@enduml
```

```plantuml
@startuml
class Car {
  - Some field [[[http://plantuml.com]]]
  Some method() [[[http://plantuml.com/link]]]
}
@enduml
```

```plantuml
@startuml
Object <|-- Foo

class Foo {
  + Object[]   [[[http://www.google.com]]]
  + methods1() [[[http://www.yahoo.com/A1{Some explainations about this method}]]]
  + methods2() [[[http://www.yahoo.com/A2]]]
}
  
class Foo2 {
  + methods1() [[[http://www.yahoo.com/B1]]]
  + methods2() [[[http://www.yahoo.com/B2]]]
}
  
class Object [[http://www.yahoo.com]]
@enduml
```

## Links in activity diagram

### On activity label

```plantuml
@startuml
start
[[http://plantuml.com]]:Some activity;
:Some [[http://plantuml.com link]];
end
@enduml
```

### On partition

```plantuml
@startuml
start
partition "[[http://plantuml.com partition_name]]" {
    :read doc. on [[http://plantuml.com plantuml_website]];
    :test diagram;
}
end
@enduml
```

## Link in State diagram

- local link on a word
- or link on the entire state shape

```plantuml
@startuml
state state1 [[http://plantuml.com/link]]
state state2 [[http://plantuml.com/state{this is a tooltip\nand a link to "plantuml/state"}]]
state2 : a global link\nand a tooltip
note left [[http://plantuml.com]]
a note
and a link
to ""plantuml.com""
end note
state3 : a local link to [[http://plantuml.com plantuml]]

state1 --> state2
state2 --> state3
@enduml
```

## Links in Network diagram (nwdiag)

```plantuml
@startnwdiag
network Network {
  Server [description="A [[http://plantuml.com link]] on nwdiag"];
}
@endnwdiag
```

## Links in JSON/YAML diagram

### JSON

```plantuml
@startjson
{
"@fruit": "Apple",
"$size": "Large",
"Appli.": "A [[http://plantuml.com link]] on JSON"
}
@endjson
```

### YAML

```plantuml
@startyaml
@fruit: Apple
$size: Large
Appli.: A [[http://plantuml.com link]] on YAML
@endyaml
```

## Links in notes

```plantuml
@startuml
:Foo:
note left of Foo [[http://www.google.com]]
This is a note
end note

note right of Foo
Yet another link to [[http://www.google.com]] as demo.
You can also [[http://www.yahoo.fr specify a text]] for the link.
And even [[http://www.yahoo.fr{This is a tooltip} add a tooltip]] to the link.
end note
@enduml
```

## Links with explicit URL directive

### On sequence diagram

```plantuml
@startuml
Bob -> Alice : ok
url of Bob is [[http://www.google.com]]
@enduml
```

### On class diagram

```plantuml
@startuml
skinparam topurl http://www.google.com
Dog --|> Mammal
url of Mammal is [[/search]]
url of Dog is [[http://www.yahoo.com{This is Dog}]]
Dog o-- Cat
Cat --|> Mammal
@enduml
```

### On usecase diagram

```plantuml
@startuml
actor Mamal
usecase Dog

url of Mamal is [[http://www.google.com]]
url of Dog is [[http://www.yahoo.com{This is Dog}]]
@enduml
```

### On component or deployment diagram

```plantuml
@startuml
node Mamal
component Dog

url of Mamal is [[http://www.google.com]]
url of Dog is [[http://www.yahoo.com{This is Dog}]]
@enduml
```

## Links in arrow (or Hyperlinks in link or connection)

### Class diagram

```plantuml
@startuml
class Car 
Car "1" *-- "*" Wheel : [[http://plantuml.com/class-diagram has some]]
@enduml
```

```plantuml
@startuml
class Car 
Car "1" *-- "*" Wheel [[http://plantuml.com/class-diagram]] : has some
@enduml
```

### Component or Deployment diagram

FIXME FIXME

```plantuml
@startuml
node Car 
Car *-- Wheel [[http://plantuml.com/deployment-diagram]] : has some
@enduml
```

### State diagram

FIXME FIXME

```plantuml
@startuml
state Car
state CarWithWheel
Car -> CarWithWheel [[http://plantuml.com/state-diagram]] : Add wheel to car
@enduml
```

## Specific SkinParameter for Link

### hyperlinkColor

```plantuml
@startuml
:hyperlinkColor setting, by default;
:[[http://plantuml.com]];
@enduml
```

```plantuml
@startuml
skinparam hyperlinkColor red
:hyperlinkColor setting;
:[[http://plantuml.com]];
@enduml
```

### hyperlinkUnderline

```plantuml
@startuml
skinparam hyperlinkUnderline false
:hyperlinkColor setting;
:[[http://plantuml.com]];
@enduml
```

```plantuml
@startuml
skinparam hyperlinkUnderline 1
:hyperlinkColor setting;
:[[http://plantuml.com]];
@enduml
```

```plantuml
@startuml
skinparam hyperlinkUnderline 5
:hyperlinkColor setting;
:[[http://plantuml.com]];
@enduml
```

### topurl

```plantuml
@startmindmap

skinparam topurl https://plantuml.com/

* [[index PlantUML website]]
** [[sequence-diagram Sequence]]
** [[mindmap-diagram MindMap]]
** [[wbs-diagram WBS]]
** ...
@endmindmap
```

## Other SkinParameter for Link

- Specific SkinParameter for SVG

## Using (global) style

### Without style (by default)

```plantuml
@startuml
title test on HyperlinkColor [[test link]]

 class test <<normal>> {
  * aaa
  + [[normal model]]
  - bb
 }
 
  class test_with_stereo AS "[[http://www.plantuml.com test]]" <<red>> {
  * aaa
  + [[red model]]
  - bb
 }
@enduml
```

### With style

```plantuml
@startuml
<style>
.red {
  HyperlinkColor #FF0000
}
</style>

title test on HyperlinkColor [[test link]]

 class test <<normal>> {
  * aaa
  + [[normal model]]
  - bb
 }
 
  class test_with_stereo AS "[[http://www.plantuml.com test]]" <<red>> {
  * aaa
  + [[red model]]
  - bb
 }
@enduml
```
