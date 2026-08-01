---
title: Ditaa — PlantUML Official Documentation
source: https://plantuml.com/ditaa
description: Official documentation for PlantUML Ditaa
---

# Ditaa

PlantUML Advanced usage Ditaa diagram Â Â Â Â

```plantuml
@startditaa
+--------+   +-------+    +-------+
|        +---+ ditaa +--> |       |
|  Text  |   +-------+    |diagram|
|Document|   |!magic!|    |       |
|     {d}|   |       |    |       |
+---+----+   +-------+    +-------+
    :                         ^
    |       Lots of work      |
    +-------------------------+
@endditaa
```

## Generalisation (of @start/@end tag)

## Option supported by PlantUML

- -E or --no-separation to remove separator
- -S or --no-shadows to remove shadow
- scale=<XYZ> to scale up or down the diagram

### Without option

```plantuml
@startditaa
+---------+  /--------\   +-------+
| cBLU    +--+cAAA    +---+Version|
|         |  |  Data  |   |   V3  |
|    +----+  |  Base  |   |cRED{d}|
|    |cPNK|  |     {s}|   +-------+
|    |    |  \---+----/
+----+----+    
@endditaa
```

### Remove separator

```plantuml
@startditaa < -E
+---------+  /--------\   +-------+
| cBLU    +--+cAAA    +---+Version|
|         |  |  Data  |   |   V3  |
|    +----+  |  Base  |   |cRED{d}|
|    |cPNK|  |     {s}|   +-------+
|    |    |  \---+----/
+----+----+    
@endditaa
```

### Remove shadow or scale diagram

```plantuml
@startditaa < --no-shadows, scale=0.7
+---------+  /--------\   +-------+
| cBLU    +--+cAAA    +---+Version|
|         |  |  Data  |   |   V3  |
|    +----+  |  Base  |   |cRED{d}|
|    |cPNK|  |     {s}|   +-------+
|    |    |  \---+----/
+----+----+    
@endditaa
```

## Tags

| Tag | Description |
| {c} | Choice or Decision |
| {d} | Document - Symbol representing a document |
| {io} | Input/Output - Symbol representing input/output |
| {mo} | Manual operation |
| {o} | Ellipse |
| {s} | Storage - Symbol representing a form of storage, like a database or a hard disk. |
| {tr} | Trapezoid |

```plantuml
@startditaa
+------+------+------+------+------+------+------+
| c {c}|d {d} |io{io}|mo{mo}|o{o}  |s{s}  |tr{tr}|
+------+------+------+------+------+------+------+
@endditaa
```

## More documentation

- ditaa.sourceforge.net
- github.com/stathissideris/ditaa
