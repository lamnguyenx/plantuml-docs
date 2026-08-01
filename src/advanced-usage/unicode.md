---
title: Unicode — PlantUML Official Documentation
source: https://plantuml.com/unicode
description: Official documentation for PlantUML Unicode
---

# Unicode

PlantUML Advanced usage Unicode Support Â Â Â Â

## Examples

```plantuml
@startuml
skinparam handwritten true
skinparam backgroundColor #EEEBDC

actor ä½¿ç¨è
participant "é ­ç­è" as A
participant "ç¬¬äºé¡" as B
participant "æå¾ä¸å èª²" as å¥çæ±è¥¿

ä½¿ç¨è -> A: å®æéé å·¥ä½
activate A

A -> B: åµå»ºè«æ±
activate B

B -> å¥çæ±è¥¿: åµå»ºè«æ±
activate å¥çæ±è¥¿
å¥çæ±è¥¿ --> B: éé å·¥ä½å®æ
destroy å¥çæ±è¥¿

B --> A: è«æ±åµå»º
deactivate B

A --> ä½¿ç¨è: åå®
deactivate A
@enduml
```

```plantuml
@startuml

(*) --> "è©å¹³å°"
--> === S1 ===
--> é èº¬åå¬ç¾
--> === S2 ===
--> éå¢ä¼æ³¢æ­¦å¨
--> (*)

skinparam backgroundColor #AAFFFF
skinparam activityStartColor red
skinparam activityBarColor SaddleBrown
skinparam activityEndColor Silver
skinparam activityBackgroundColor Peru
skinparam activityBorderColor Peru
@enduml
```

```plantuml
@startuml

skinparam usecaseBackgroundColor DarkSeaGreen
skinparam usecaseArrowColor Olive
skinparam actorBorderColor black
skinparam usecaseBorderColor DarkSlateGray

ä½¿ç¨è << äººé¡ >>
"ä¸»æ¸æåº«" as æ¸æåº« << æç¨ç¨å¼ >>
(èåµ) << ä¸æ¡¿ >>
"ä¸»æ°æ®ç" as (è´ä½) << åºæ¬ç >>

ä½¿ç¨è -> (èåµ)
ä½¿ç¨è --> (è´ä½)

æ¸æåº«  --> (è´ä½)
@enduml
```

```plantuml
@startuml
() "Î£ÏÎºÏÎ¬ÏÎ·Ï\nÎµÎ¯Î½Î±Î¹ ÏÎµÏÏÎ·Ï" as Î£ÏÎºÏÎ¬ÏÎ·Ï

Î£ÏÎºÏÎ¬ÏÎ·Ï - [Î ÏÎ·Î½Î¬ ÏÎ¿Î»ÎµÎ¼Î¿ÏÎ±ÏÎ®Ï]
[Î ÏÎ·Î½Î¬ ÏÎ¿Î»ÎµÎ¼Î¿ÏÎ±ÏÎ®Ï] ..> () ÎÎ¸Î®Î½Î± : ÎÏÏÎ­Ï Î¿Î¹ ÏÏÎ¬ÏÎµÎ¹Ï\nÎ´ÎµÎ½ ÏÎ·Î¼Î±Î¯Î½Î¿ÏÎ½ ÏÎ¯ÏÎ¿ÏÎ±
@enduml
```

## Charset
```
java -jar plantuml.jar -charset UTF-8 files.txt
```
```
<!-- Put images in c:/images directory -->
<target name="main">
<plantuml dir="./src" charset="UTF-8" />
```

## Using Unicode Character on PlantUML

- Special characters using &#XXXX; or <U+XXXX> form;
- Emoji using <:XXXXX:> or <:NameOfEmoji:> form.
