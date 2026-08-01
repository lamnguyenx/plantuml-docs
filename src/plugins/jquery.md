---
title: Jquery — PlantUML Official Documentation
source: https://plantuml.com/jquery
description: Official documentation for PlantUML Jquery
---

# JQuery integration

PlantUML Plugins JQuery Â Â Â Â

```plantuml
@startuml
class foo
@enduml
```
```
<head>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="[[jquery_plantuml.js|jquery_plantuml.js]]"></script>
<!-- rawdeflate.js is implicity used by jquery_plantuml.js -->
</head>
```

## How does it works?

- JQuery simply parses the html source file on loading,
- Then all uml descriptions are transformed into links to plantuml.com site. (like for Javascript integration .)

## Complete source example
```
<html>
<head>
<script type="text/javascript" src="jquery.js"></script>
<script type="text/javascript" src="[[jquery_plantuml.js|jquery_plantuml.js]]"></script>
<!-- rawdeflate.js is implicity used by jquery_plantuml.js -->
</head>

<body>
<p>Example</p>
<hr>
<img uml="
class foo
">
<hr>
<img uml="
class foo
">

</body>
</html>
```
