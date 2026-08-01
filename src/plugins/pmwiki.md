---
title: Pmwiki — PlantUML Official Documentation
source: https://plantuml.com/pmwiki
description: Official documentation for PlantUML Pmwiki
---

# PmWiki integration

PlantUML Plugins PmWiki Â Â Â Â

## Description

## Installation
```
include_once("$FarmD/cookbook/pmplantuml.php");
```

## Usage

## Patch of pmplantuml.php
```
--- pmplantuml_php.txt  2020-02-01 20:07:10.000000000 +0000
+++ pmplantuml.php      2023-09-15 15:06:02.711068260 +0000
@@ -34,22 +34,24 @@
 function doplantuml($str) {
        global $KPV, $KeepToken;

-       $str = preg_replace( "/$KeepToken(\\d+?)$KeepToken/e", '$KPV[$1]', $str);
+       $str = PPRE( "/$KeepToken(\\d+?)$KeepToken/", '$KPV[$1]', $str[0]);
+       // pmwiki can insert vspace when a blank line is present
+       $str = preg_replace( "<<:vspace>>", "", $str);
        $str = preg_replace( "/>/", ">", $str);
        $str = preg_replace( "/</", "<", $str);

-       $url = "http://www.plantuml.com/plantuml/img/";
+       $url = "http://www.plantuml.com/plantuml/png/";
        $url .= encodep($str);
        return Keep('<img src='.$url.' />');
 }

 Markup('plantuml',
        'fulltext',
-       '/(@start\w+.*?@end\w+)/sexi',
-       'doplantuml("$1")');
+       '/(@start\w+.*?@end\w+)/sxi',
+       "doplantuml");

 function encodep($text) {
-     $data = utf8_encode($text);
+     $data = $text;
      $compressed = gzdeflate($data, 9);
      return encode64($compressed);
 }
```
