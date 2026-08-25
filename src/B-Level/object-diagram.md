---
title: Object Diagram — PlantUML Official Documentation
source: https://plantuml.com/object-diagram
description: Official documentation for PlantUML Object Diagram
---

# Object Diagram

## Definition of objects

```plantuml
@startuml
object firstObject
object "My Second Object" as o2
@enduml
```

## Relations between objects

| Type | Symbol | Purpose |
| Extension | <|-- | Specialization of a class in a hierarchy |
| Implementation | <|.. | Realization of an interface by a class |
| Composition | *-- | The part cannot exist without the whole |
| Aggregation | o-- | The part can exist independently of the whole |
| Dependency | --> | The object uses another object |
| Dependency | ..> | A weaker form of dependency |

```plantuml
@startuml
object Object01
object Object02
object Object03
object Object04
object Object05
object Object06
object Object07
object Object08

Object01 <|-- Object02
Object03 *-- Object04
Object05 o-- "4" Object06
Object07 .. Object08 : some labels
@enduml
```

## Associations objects

```plantuml
@startuml
object o1
object o2
diamond dia
object o3

o1  --> dia
o2  --> dia
dia --> o3
@enduml
```

## Adding fields

```plantuml
@startuml

object user

user : name = "Dummy"
user : id = 123

@enduml
```

```plantuml
@startuml

object user1
object user2

user1 : name = "User A"
user2 : name = "User B"

user1 : id = 123
user2 : id = 456

@enduml
```

```plantuml
@startuml

object user {
  name = "Dummy"
  id = 123
}

@enduml
```

## Common features with class diagrams

- Hide attributes, methods...
- Defines notes
- Use packages
- Skin the output

## Map table or associative array

```plantuml
@startuml
map CapitalCity {
 UK => London
 USA => Washington
 Germany => Berlin
}
@enduml
```

```plantuml
@startuml
map "Map **Contry => CapitalCity**" as CC {
 UK => London
 USA => Washington
 Germany => Berlin
}
@enduml
```

```plantuml
@startuml
map "map: Map<Integer, String>" as users {
 1 => Alice
 2 => Bob
 3 => Charlie
}
@enduml
```

```plantuml
@startuml
object London

map CapitalCity {
 UK *-> London
 USA => Washington
 Germany => Berlin
}
@enduml
```

```plantuml
@startuml
object London
object Washington
object Berlin
object NewYork

map CapitalCity {
 UK *-> London
 USA *--> Washington
 Germany *---> Berlin
}

NewYork --> CapitalCity::USA
@enduml
```

```plantuml
@startuml
package foo {
    object baz
}

package bar {
    map A {
        b *-> foo.baz
        c =>
    }
}

A::c --> foo
@enduml
```

```plantuml
@startuml
object Foo
map Bar {
  abc=>
  def=>
}
object Baz

Bar::abc --> Baz : Label one
Foo --> Bar::def : Label two
@enduml
```

## Program (or project) evaluation and review technique (PERT) with map

```plantuml
@startuml PERT
left to right direction
' Horizontal lines: -->, <--, <-->
' Vertical lines: ->, <-, <->
title PERT: Project Name

map Kick.Off {
}
map task.1 {
    Start => End
}
map task.2 {
    Start => End
}
map task.3 {
    Start => End
}
map task.4 {
    Start => End
}
map task.5 {
    Start => End
}
Kick.Off --> task.1 : Label 1
Kick.Off --> task.2 : Label 2
Kick.Off --> task.3 : Label 3
task.1 --> task.4
task.2 --> task.4
task.3 --> task.4
task.4 --> task.5 : Label 4
@enduml
```

## Display JSON Data on Class or Object diagram

### Simple example

```plantuml
@startuml
class Class
object Object
json JSON {
   "fruit":"Apple",
   "size":"Large",
   "color": ["Red", "Green"]
}
@enduml
```
