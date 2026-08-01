---
title: Tinymce — PlantUML Official Documentation
source: https://plantuml.com/tinymce
description: Official documentation for PlantUML Tinymce
---

# TinyMCE Editor

PlantUML Plugins TinyMCE Â Â Â Â

## Demo

<p>You can click on "<strong>UML</strong>" button in the toolbar to add a new diagram.</p>
<p>You can also select an image, and click on this same button to <em>edit</em> the diagram.</p>
<p><img style="display: block; margin-left: auto; margin-right: auto;" src="http://www.plantuml.com/plantuml/img/SyfFKj2rKt3CoKnE1G00" alt="Bob -> Alice" /></p>
<p>You can also select a text diagram, and then click on "<strong>UML</strong>" button to generate the diagram:</p>
<p>Â </p>
<p>@startuml</p>
<p>class Foo</p>
<p>@enduml</p>
<p>Â </p>
<p><span style="text-decoration: underline;">Very easy to used and to integrate.</span></p>

## Installation

1. Download TinyMCE package
(for example, TinyMCE 3.5.7 ).
2. Unzip it somewhere and move tiny_mce directory to a dedicated place, for example in htdocs/tiny_mce/ .
3. Download plantumlPluginForTinyMCE.zip file
4. Unzip this file to htdocs/tiny_mce/plugins directory
5. Check that in htdocs/tiny_mce/plugins/plantuml directory, you have the following files: htdocs/tiny_mce/plugins/plantuml img/ js/ langs/ dialog.htm editor_plugin.js editor_plugin_src.js
6. Add the following code into your HTML pages, in the <head> section: <!-- TinyMCE -->
<script type="text/javascript" src="tiny_mce/tiny_mce.js"></script>
<script type="text/javascript">
	tinyMCE.init({
		mode : "textareas",
		theme : "advanced",
theme_advanced_buttons2 : "justifyleft,justifycenter,justifyright,justifyfull,separator,numlist,bullist,outdent,indent,separator,forecolor,backcolor,separator,hr,link,unlink,image,code,separator,plantuml",
		plugins : 'plantuml',   
	});
</script>
<!-- /TinyMCE -->
7. Add the following code into your HTML pages, somewhere in the <body> section: <textarea id="elm1" name="elm1" rows="24" cols="80" style="width: 80%">
	</textarea>
8. Load your HTML file in your browser & enjoy.
