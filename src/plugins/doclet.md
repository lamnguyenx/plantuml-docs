---
title: Doclet — PlantUML Official Documentation
source: https://plantuml.com/doclet
description: Official documentation for PlantUML Doclet
---

# New Doclet

PlantUML Plugins Doclet Â Â Â Â

## UMLDoclet

- Declare the nl.talsmasoftware.umldoclet.UMLDoclet class to be used by javadoc (will by default also delegate to Standard doclet, so all-in-one).
- All customizable options will become documented on the github page before the 1.0.0 release.

## Old legacy doclet

- @note : can be used to add a note to a class
- @assoc : Pattern: <cardinality> - <cardinality> <associated class> (no spaces)
- @navassoc : Pattern: <cardinality> - <cardinality> <associated class> (no spaces)
- @depend : Pattern: <cardinality> - <cardinality> <associated class> (no spaces)
- @overrideAssoc : can be used to mark a field-declaration not to export its association.

- createPackages : Default value is false
- showPublicMethods : Default value is true
- showPublicConstructors : Default value is true
- showPublicFields : Default value is true

## Ant-Script example
```
<project>
<target name="main">
<javadoc doclet="de.mallox.doclet.PlantUMLDoclet"
docletpath="plantUmlDoclet.jar"
access="private"
additionalparam=
"-J-DdestinationFile=uml.txt -J-DcreatePackages=false -J-DshowPublicMethods=true -J-DshowPublicConstructors=false -J-DshowPublicFields=true"
>
<packageset dir="src">
<include name="**"/>
</packageset>
</javadoc>

<java jar="plantuml.jar" fork="true" maxmemory="128m">
<arg value="uml.txt"/>
</java>
</target>
</project>
```

## Image example

## Source example
```
package demo;

class Controller {}
class EmbeddedAgent {}
class PowerManager {}

/**
* @extends Controller
* @extends EmbeddedAgent
* @navassoc - - 1..* PowerManager
* @note this is a note
*/
class SetTopController implements URLStreamHandler {
public String name;

int authorizationLevel;
void startUp() {}
void shutDown() {}
void connect() {}
}

/** @depend - friend - SetTopController */
class ChannelIterator {}

interface URLStreamHandler {
void OpenConnection();
void parseURL();
void setURL();
void toExternalForm();
}
```
