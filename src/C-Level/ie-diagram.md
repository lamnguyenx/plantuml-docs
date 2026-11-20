---
title: Ie Diagram — PlantUML Official Documentation
source: https://plantuml.com/ie-diagram
description: Official documentation for PlantUML Ie Diagram
---

# Information Engineering Diagrams

- Additional relations for the Information Engineering notation;
- An entity alias that maps to the class diagram class ;
- An additional visibility modifier * to identify mandatory attributes.

## Information Engineering Relations

| Type | Symbol |
| Zero or One | |o-- |
| Exactly One | ||-- |
| Zero or Many | }o-- |
| One or Many | }|-- |

```plantuml
@startuml
Entity01 }|..|| Entity02
Entity03 }o..o| Entity04
Entity05 ||--o{ Entity06
Entity07 |o--|| Entity08
@enduml
```

## Entities

```plantuml
@startuml
entity Entity01 {
  * identifying_attribute
  --
  * mandatory_attribute
  optional_attribute
}
@enduml
```

```plantuml
@startuml
entity Entity01 {
   optional attribute
   **optional bold attribute**
   * **mandatory bold attribute**
}
@enduml
```

## Complete Example

```plantuml
@startuml

' hide the spot
' hide circle

' avoid problems with angled crows feet
skinparam linetype ortho

entity "User" as e01 {
  *user_id : number <<generated>>
  --
  *name : text
  description : text
}

entity "Card" as e02 {
  *card_id : number <<generated>>
  sync_enabled: boolean
  version: number
  last_sync_version: number
  --
  *user_id : number <<FK>>
  other_details : text
}

entity "CardHistory" as e05 {
  *card_history_id : number <<generated>>
  version : number
  --
  *card_id : number <<FK>>
  other_details : text
}

entity "CardsAccounts" as e04 {
  *id : number <<generated>>
  --
  card_id : number <<FK>>
  account_id : number <<FK>>
  other_details : text
}


entity "Account" as e03 {
  *account_id : number <<generated>>
  --
  user_id : number <<FK>>
  other_details : text
}

entity "Stream" as e06 {
  *id : number <<generated>>
  version: number
  searchingText: string
  --
  owner_id : number <<FK>>
  follower_id : number <<FK>>
  card_id: number <<FK>>
  other_details : text
}


e01 }|..|| e02
e01 }|..|| e03

e02 }|..|| e05

e02 }|..|| e04
e03 }|..|| e04

e02 }|..|| e06
e03 }|..|| e06


@enduml
```
