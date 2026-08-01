---
title: Old News — PlantUML Official Documentation
source: https://plantuml.com/old-news
description: Official documentation for PlantUML Old News
---

# Some RSS flows

PlantUML News and information What's New ? (Full) Â Â Â Â

- Â Recent activities on the Q&A forum
- Â Recent questions and answers on the Q&A forum

- Jun 9, 2026 : @plantuml/mcp-js is now available on npm: a pure Node.js local MCP server for PlantUML. Built on TeaVM , it runs entirely in Node with no Java required, and exposes PlantUML to AI assistants through the Model Context Protocol.
- Jun 8, 2026 : Minor bug fixes and improvements (V1.2026.6).
- May 27, 2026 : Minor bug fixes and improvements (V1.2026.5).
- May 26, 2026 :
	PlantUML is now available on npm as @plantuml/core Thanks to TeaVM , the engine runs entirely in the browser and can be imported straight from a CDN, with no server and no Java.
- May 20, 2026 : Minor bug fixes and improvements (V1.2026.4).
- May 11, 2026 : PlantUML activity diagrams used as executable workflows for Claude Code skills ,
	a creative new use case where the diagram is the skill rather than just documenting it. Antony Marcano reports going from 24 prohibitive clauses in prose to only 11 in PlantUML form, for equivalent behavior.
	(See also the Stagentic Promptbook plugin.)
- May 8, 2026 : Minor bug fixes and improvements (V1.2026.3).
- Apr 8, 2026 : qpr: A lightweight shell script to render PlantUML diagrams via Docker with optional terminal display.
- Mar 23, 2026 : Explore the new js-PlantUML editors, all running entirely in your browser.
- Feb 27, 2026 : Minor bug fixes and improvements (V1.2026.2).
- Feb 11, 2026 : Client-Side is coming
- Jan 18, 2026 : Minor bug fixes and improvements (V1.2026.1).
- Jan 9, 2026 : Minor bug fixes and improvements (V1.2026.0).
- Nov 17, 2025 : Beta testing of Chart Diagram. (Many thanks to David Fyfe for its great contribution!)
- Nov 4, 2025 : Minor bug fixes and improvements (V1.2025.10).
- Oct 18, 2025 : Minor bug fixes and improvements (V1.2025.9).
- Oct 11, 2025 :
	We are currently redesigning the PlantUML command-line options. Your feedback is very valuable at this stage! We invite you to test to let us know what feels clear (or confusing).
- Oct 4, 2025 : Minor bug fixes and improvements (V1.2025.8).
- Sep 10, 2025 : Minor bug fixes and improvements (V1.2025.7). Versions V1.2025.5 and V1.2025.6 were never actually released due to the OSSRH end-of-life and shutdown .
	  This had absolutely no impact on end users or developers, but it required some sensitive updates to our internal GitHub CI pipelines.
	  Everything is now back to normal, and we expect to resume our regular release schedule.
- June 28, 2025 : Minor bug fixes and improvements (V1.2025.4).
- June 1, 2025 : Minor bug fixes and improvements (V1.2025.3).
- May 18, 2025 : A real-world example of how Large Language Models can assist in developing custom tooling for step-by-step playback of PlantUML sequence diagrams, 
	authored by Unmesh Joshi and featured on Martin Fowler's blog. (Thanks to Andreas Studer for pointing this out).
- March 5, 2025 : Minor bug fixes and improvements (V1.2025.2).
- February 16, 2025 : Minor bug fixes and improvements (V1.2025.1).
- February 1, 2025 : Updated version of the PlantUML Language Reference Guide to V1.2025.0.
- January 7, 2025 : Minor bug fixes and improvements (V1.2025.0).
- November 18, 2024 : Visit the PlantUML Themes Gallery! (Many thanks to Johannes Thorn for its contribution!)
- November 15, 2024 : Minor bug fixes and improvements (V1.2024.8).
- October 16, 2024 :
Developed by Xiaoqi Zhao , you can explore the new PlantUML course on Udemy or watch it on YouTube . (Huge congratulations and thanks to Xiaoqi for this contribution!)
- September 9, 2024 : Minor bug fixes and improvements (V1.2024.7).
- July 6, 2024 : Minor bug fixes and improvements (V1.2024.6). Eclipse Layout Kernel is now integrated in the main library.
- May 26, 2024 : Minor bug fixes and improvements (V1.2024.5). (Thanks and congratulation to Jim Nelson !)
- April 6, 2024 : Minor bug fixes and improvements (V1.2024.4).
- February 14, 2024 : Minor bug fixes and improvements (V1.2024.2).
- February 1, 2024 : How mix all diagram type and make sub-diagram.
- February 1, 2024 : Minor bug fixes and improvements (V1.2024.0).
- December 12, 2023 : Minor bug fixes and improvements (V1.2023.13).
- October 20, 2023 : Minor bug fixes and improvements (V1.2023.12).
- September 24, 2023 : Upgrade PlantUML Language Reference Guide to V1.2023.11
- September 13, 2023 : Minor bug fixes and improvements (V1.2023.11).
- July 12, 2023 : Minor bug fixes and improvements (V1.2023.10).
- June 13, 2023 : Minor bug fixes and improvements (V1.2023.9). ALLOW_PLANTUML_INCLUDE has now been removed. Please use security profile instead.
- May 21, 2023 : Minor bug fixes and improvements (V1.2023.8).
- May 13, 2023 :
	Thanks to Eric Vantillard , the MIT version is available
	on Maven Central Repository .
- May 12, 2023 : Minor bug fixes and improvements (V1.2023.7).
- April 18, 2023 : Minor bug fixes and improvements (V1.2023.6).
- March 24, 2023 : Minor bug fixes and improvements (V1.2023.5).
- March 20, 2023 :
	You can try the new official Discord server.
- March 9, 2023 : Improve backward compatibility about package and namespace simplification (V1.2023.4).
- March 7, 2023 :
	You can now try the pure Javascript PlantUML implementation!
- February 26, 2023 : Package and namespace simplification (V1.2023.2).
- February 2, 2023 : Important change about package and namespace Starting with version 1.2023.2 (which is online as a beta), PlantUML handles differently namespaces and packages. There won't be any difference between namespaces and packages anymore: both keywords are now synonymous. The drawing is slightly different, because we now also draw intermediate packages .
Note that this is not a final choice , it depends on the feedback from users. Packages now involve the definition of a namespace, as in any ordinary programming language.
The default separator is the dot (.) but can be changed using the set separator X directive.
You can also disable namespace management using set separator none , in which case you get back a behavior similar to older versions of PlantUML. The parser is also slightly more strict. You now have to declare an element before adding a note on it, for example. Usually we try to make improvements that don't break backwards compatibility.
Here we were forced to put in a more consistent behavior, which unfortunately might break your old diagrams.
However, the addition of the set separator none should fix it, if necessary. That leaves the drawing part, and let's see how you react here. You can open issues on github or react on the forum , depending on which tool you prefer.
- January 29, 2023 : Minor bug fixes and improvements (V1.2023.1).
- January 9, 2023 : Minor bug fixes and improvements (V1.2023.0).
- December 8, 2022 :
	Documentation about Extended BackusâNaur Form diagram.
- December 6, 2022 : Minor bug fixes and improvements (V1.2022.14).
- November 19, 2022 : Minor bug fixes and improvements (V1.2022.13).
- October 23, 2022 : Minor bug fixes and improvements (V1.2022.12).
- October 3, 2022 : Render PlantUML diagrams in Slack channels.
- September 25, 2022 : Minor bug fixes and improvements (V1.2022.8).
- August 23, 2022 :
	Use inline SVG sprite.
- August 22, 2022 : Minor bug fixes and improvements (V1.2022.7).
- June 21, 2022 : Minor bug fixes and improvements (V1.2022.6).
- April 30, 2022 : Minor bug fixes and improvements (V1.2022.5).
- April 9, 2022 : Minor bug fixes and improvements (V1.2022.4).
- March 29, 2022 : Minor bug fixes and improvements (V1.2022.3).
- March 5, 2022 : New default theme and CSS styles (V1.2022.2).
- February 25, 2022 : Make PlantUML diagrams easily accessible from markdown, GitHub flavored.
- February 16, 2022 : You can restore the old theme using skin rose directive.
- February 10, 2022 : Next versions of PlantUML will slightly change the default theme. This website reflects the new default theme.
	We hope you will like it. The online server will be updated accordingly in the incoming days.
- February 1, 2022 : Minor bug fixes and improvements (V1.2022.1).
- January 14, 2022 : Get inspired by what people are doing on GitHub with PlantUML.
- January 11, 2022 : Minor bug fixes and improvements (V1.2022.0).
- December 13, 2021 : PlantUML is not affected by the log4j vulnerability.
- December 8, 2021 : Emojis from Twemoji available (V1.2021.16).
- November 30, 2021 : Minor bug fixes and improvements (V1.2021.15).
- November 12, 2021 : Minor bug fixes and improvements (V1.2021.14).
- November 1, 2021 : Minor bug fixes and improvements (V1.2021.13).
- October 5, 2021 : Minor bug fixes and improvements (V1.2021.12).
- October 2, 2021 : Minor bug fixes and improvements (V1.2021.11).
- September 17, 2021 : PlantUML Docker is now up to date. Many thanks to Mubarak Imam for his great work on this topic!
- August 30, 2021 : Minor bug fixes and improvements (V1.2021.10).
- August 26, 2021 : Release 1.1.26 of the PlantUML Eclipse Plugin with ELK support. (Thanks Hallvard !)
- July 26, 2021 : Give a color on PlantUML for github/linguist
- July 25, 2021 : Minor bug fixes and improvements (V1.2021.9).
- June 26, 2021 : Minor bug fixes and improvements (V1.2021.8).
- June 3, 2021 :
	You can now connect Astah and PlantUML .
	(Thanks to Shintaro Hosoai for his work)
- May 23, 2021 : Minor bug fixes and improvements (V1.2021.7) and two new builtin functions to reverse colors.
- May 14, 2021 : Introducing new !theme feature (V1.2021.6). (Thanks to Brett Schwarz for his work)
- April 28, 2021 :
	Supporting Eclipse Layout Kernel in addition of GraphViz/dot: What do you think about it?
- April 25, 2021 : Minor bug fixes and improvements (V1.2021.5).
- April 14, 2021 : New release 1.1.25 of the PlantUML Eclipse Plugin .
	(Thanks to Hallvard TrÃ¦tteberg for his work!)
- April 4, 2021 : Minor bug fixes and improvements (V1.2021.4). (Thanks to LoÃ¯c PÃ©ron for the code about quarterly and yearly print scale to gantt diagram )
- March 22, 2021 : Minor bug fixes and improvements (V1.2021.3).
- March 7, 2021 : Minor bug fixes and improvements (V1.2021.2).
- February 2, 2021 : Minor bug fixes and improvements (V1.2021.1).
- January 10, 2021 : Add support for YAML data (V1.2021.0). (Thanks to Piotr for the suggestion)
- December 21, 2020 : Fix annoying regression about GraphViz diagrams under Windows (V1.2020.26).
- December 18, 2020 : Minor bug fixes and improvements (V1.2020.24).
- December 13, 2020 : Minor bug fixes and improvements (V1.2020.23).
- December 9, 2020 : PlantUML Language Reference Guide finally updated!
- December 6, 2020 : Minor bug fixes and improvements (V1.2020.22).
- November 30, 2020 : Easily display your JSON data (V1.2020.21).
- November 21, 2020 : Minor bug fixes and improvements (V1.2020.20).
- October 12, 2020 : Official release of PlantUML PicoWebServer.
- October 12, 2020 : Minor bug fixes and improvements (V1.2020.19).
- September 30, 2020 : Minor bug fixes and improvements (V1.2020.18).
- September 19, 2020 : Minor bug fixes and improvements (V1.2020.17).
- August 29, 2020 : Information about GraphViz version 2.44: you may have to run dot -c in a command line to finalize the installation.
- August 23, 2020 :
	Several new features in gantt diagram (V1.2020.16). Default colors have been changed. ( You can use styles to retrieve old colors ).
- June 28, 2020 : Minor bug fixes and improvements (V1.2020.15).
- June 20, 2020 : Minor bug fixes and improvements (V1.2020.14).
- June 13, 2020 : Minor bug fixes and improvements (V1.2020.13).
- June 6, 2020 : Minor bug fixes and improvements (V1.2020.12).
- June 2, 2020 : The Hitchhikerâs Guide to PlantUML is out! Big credit to Crashedmind for his wonderfull work!
- May 30, 2020 : How to deploy PlantUML safely.
- May 30, 2020 : Minor bug fixes and improvements (V1.2020.11).
- May 27, 2020 : Sysdream is about to make some code audit on PlantUML. We hope they won't find anything too bad.
- May 17, 2020 : Use keyword arguments with the preprocessor (V1.2020.10). (Thanks to Crashedmind for the suggestion !)
- May 10, 2020 : Minor bug fixes and improvements (V1.2020.9).
- April 26, 2020 : Minor bug fixes and improvements (V1.2020.8).
- April 19, 2020 : Introducing procedure in preprocessor (V1.2020.7). You may have to replace some !function declaration
	to !procedure declaration in your diagrams if you use some advanced features of the preprocessor. We are really sorry about that.
	This is an easy change that is important to keep the preprocessor consistent.
- April 19, 2020 : Upgrade of the online server.
- April 5, 2020 : Minor bug fixes and improvements (V1.2020.6).
- March 19, 2020 : Minor bug fixes and improvements (V1.2020.5).
- March 19, 2020 : Due to legal issues, rollback to the regular license (V1.2020.4).
- March 17, 2020 : Minor bug fixes and improvements (V1.2020.3).
- March 17, 2020 : We have updated our software license to Coronavirus license.
- March 15, 2020 : As a politician, community leader or business leader, you have the power and the responsibility to read THIS.
- March 1, 2020 : Highlighted periods in timing diagrams (V1.2020.2).
- February 16, 2020 : Few Gantt diagram improvements (V1.2020.1).
- January 26, 2020 : There is yet another poll about default separator .
- January 26, 2020 : Help us by beta-testing the incoming packages/namespaces feature .
- January 12, 2020 : Minor bug fixes and improvements (V1.2020.0).
- December 10, 2019 : Minor bug fixes and improvements (V1.2019.13).
- December 6, 2019 : New release of the PlantUML Eclipse Plugin .
	(Thanks to Hallvard TrÃ¦tteberg for his work!)
- November 3, 2019 : Minor bug fixes and improvements (V1.2019.12) and Kubernetes-icons included in PlantUML Standard Library
- October 28, 2019 : UML visualisation for Git repositories.
- September 22, 2019 : Minor bug fixes and improvements (V1.2019.11).
- September 14, 2019 : Minor bug fixes and improvements (V1.2019.10).
- August 26, 2019 : Minor bug fixes and improvements (V1.2019.9).
- July 15, 2019 :
	Following the great suggestions from Richard Goodwin , we have started to add some styling features in PlantUML. Specifications are still in progess.
	If you are interested, you can contribute to our discussions on the new #style slack channel . (Thanks again Richard!)
- July 13, 2019 : Minor bug fixes and improvements (V1.2019.8).
- July 1, 2019 : July 2019, PlantUML elected as Sourceforge Community Choice Project of the Month.
- June 24, 2019 : Minor bug fixes and improvements (V1.2019.7).
- May 24, 2019 : The new V2 preprocessor is officially released.
- April 24, 2019 : Beta testing of the new V2 preprocessor.
- April 20, 2019 : Minor bug fixes and improvements (V1.2019.5).
- April 6, 2019 :
	Nice article about Markdown native diagrams with PlantUML .
	Here is a request for better integration in GitLab .
	And here another one for GitHub .
- March 29, 2019 :
	New Work Breakdown Structure diagram and minor bug fixes and improvements.
- March 10, 2019 : Enhancement in MindMap diagram and minor bug fixes and improvements.
- March 1, 2019 : Enhancement in timing diagram and support for MindMap diagram
- February 13, 2019 : New version of the PlantUML Language Reference Guide.
- February 9, 2019 : Minor bug fixes and improvements.
- February 4, 2019 : New release of the Eclipse plugin .
	(Bug fixes and new features: diagram text selector).
- January 17, 2019 : Collaborative tool for website design .
- January 16, 2019 : New website design
- January 13, 2019 : Minor bug fixes and improvements.
- December 21, 2018 : Minor bug fixes and improvements.
- November 26, 2018 : New network diagrams .
	(Credit to Takeshi Komiya )
- October 21, 2018 : Fix !include issue introduced with V1.2018.11
- September 22, 2018 : Building custom library
- August 26, 2018 : Minor bug fixes and improvements.
- July 27, 2018 : Minor bug fixes and improvements.
- June 24, 2018 : Minor bug fixes and improvements.
- June 11, 2018 : New release of PlantUML Standard Library.
- May 21, 2018 : Minor bug fixes and improvements.
- May 5, 2018 : Minor bug fixes and improvements.
- May 1, 2018 : Minor bug fixes and improvements.
- April 12, 2018 : New Gantt diagram features.
- April 5, 2018 : Minor bug fixes and improvements.
- March 9, 2018 : Minor bug fixes and improvements.
- January 28, 2018 : Use order directive to change participant order .
- January 26, 2018 :
	Find inspiration with Real World PlantUML .
	(Credit to Yuki Furuyama )
- January 4, 2018 : Connector in Activity Diagram Beta .
- December 11, 2017 : Minor bug fixes and improvements.
- November 12, 2017 : Minor bug fixes and improvements.
- October 17, 2017 : Forum migrated to a newer version.
- October 7, 2017 : Minor bug fixes and improvements.
- September 17, 2017 :
	We apologize to all people that have post messages on the Q&A forum recently. A lot of messages were not published until now because of some internal error. We understand that it has
	been frustrating for you and we are really sorry about that! The good news is that everything is working now but you still have to be patient :
	we have a lot of questions to answer to!
- September 3, 2017 : Minor bug fixes and improvements.
- August 22, 2017 : New release of PlantUML Eclipse with newpage directive support.
	(Thanks to Hallvard TrÃ¦tteberg for his work) Important note: You may have to refresh/reload your previously defined update site .
- July 3, 2017 : New archimate features.
- June 5, 2017 : Minor bug fixes and improvements.
- May 10, 2017 : Minor bug fixes and improvements.
- May 4, 2017 : PlantUML Renderer on Wordpress. (Thanks to Todd Halfpenny his great job!)
- May 2, 2017 : PlantUML available on Docker. (Many thanks to David Ducatel for setting up this!)
- April 26, 2017 : Final Versioning Scheme deployed.
- April 19, 2017 : Minor bug fixes and improvements.
- April 7, 2017 : Minor bug fix when splitting diagrams.
- April 6, 2017 : The PlantUML Eclipse now supports hyperlinks! (Thanks to Hallvard TrÃ¦tteberg for his work)
- April 5, 2017 : Minor bug fixes and improvements.
- March 25, 2017 :
	Please vote to validate PlantUML future versioning scheme.
- March 21, 2017 :
	Changing versioning scheme and Minor bug fixes and improvements.
- March 15, 2017 : Minor bug fixes and improvements.
- March 12, 2017 : Use hyperlinks and URL in your diagrams .
- February 26, 2017 : Add padding in Sequence Diagram .
	(Thanks to Scherzer Helmut for his suggestions and tests)
- February 16, 2017 : Simplified arrowColor skinparameter following poll about syntax simplification .
- February 15, 2017 : Update Timing Diagrams .
- February 6, 2017 : Update documentation about Eclipse Plugin .
	(Thanks to Hallvard TrÃ¦tteberg for his work)
- February 1, 2017 : New Timing Diagrams as beta feature .
- January 22, 2017 : Poll about skinparam arrow syntax simplification .
- January 21, 2017 : Minor bug fixes and improvements.
- December 21, 2016 : Reverse colors for black background environment.
- December 14, 2016 : Generate statistics about your PlantUML Usage.
- December 8, 2016 : Use crowfoot into your database diagrams.
	(Thanks for lesswood for the idea and the code!)
- December 1, 2016 : Use Ascii Math into your diagram.
- November 19, 2016 : Minor bug fixes and improvements.
- November 4, 2016 : Date and default parameter value in preprocessing. (Thanks to Serge Wenger and Johannes Brunen for their useful suggestions.)
- October 10, 2016 : New enhanced Java Doclet. (Thanks to Gerald Boersma fo his work!)
- September 29, 2016 : Minor bug fixes and improvements.
- September 6, 2016 : A coffee with Jordi Cabot (from MOdeling LAnguages)
- August 25, 2016 : Minor bug fixes and improvements.
- July 26, 2016 : Minor bug fixes and improvements.
- July 4, 2016 : Minor bug fixes and improvements.
- June 19, 2016 : Some more skinparam for Sequence Diagrams.
- June 16, 2016 :
	Please vote to choose default arrow's thickness for Sequence Diagram. The thickness goes from 1 to 1,5 so the difference is really tiny.
- June 8, 2016 : Lucidchart lets you create and edit your sequence diagrams by entering text.
- June 2, 2016 : Dedicate photo or picture set in algorithmic stone.
- May 31, 2016 : Minor bug fixes and improvements.
- May 19, 2016 : Adding floating note to Activity Beta Diagram (Thanks to Ali Saad from Transvalor for the suggestion).
- May 11, 2016 : Adding long description to deployment diagram.
- May 1, 2016 :
	Updated PlantUML Web Server with Tweet button which renders UML diagram inside Twitter .
- April 23, 2016 : Running PlantUML without Graphviz/Dot dependency
- April 4, 2016 : Minor bug fixes and improvements.
- March 6, 2016 : Minor bug fixes and improvements.
- February 8, 2016 : Some success in porting Graphviz/DOT to Java!
- February 7, 2016 : Minor bug fixes and improvements.
- January 30, 2016 :
	Fix a regression about packages links and few other changes .
- January 26, 2016 : Integration with Fitnesse Wiki .
- January 9, 2016 : Use sprites in stereotypes (Thanks to Jean-Marie Kubek from Institut National Universitaire Champollion for the code and the idea).
- December 21, 2015 : TexWriting.com is now integrating an online UML editor
	(Thanks to Florian MÃ¼ller).
- November 15, 2015 : Minor bug fixes and improvements.
- November 1, 2015 : Minor bug fixes and improvements.
- September 28, 2015 : Minor bug fixes and improvements.
- September 6, 2015 : Use unicode in creole engine and minor bug fixes and improvements.
- August 5, 2015 : Minor bug fixes and improvements.
- July 11, 2015 : New stop and resume feature for automatic numbering. (Thanks to Jean-Baptiste Laurent for the suggestion).
- June 20, 2015 : Minor bug fixes and improvements.
- June 7, 2015 : Add end keyword in Activity Diagram Beta. (Thanks to Radhakrishnan Mohan for the suggestion).
- May 31, 2015 : Use trees for hierarchical structure. (Thanks to Evren Esat Ãzkan for the suggestion).
- May 3, 2015 : Bug fix in preprocessor .
- April 20, 2015 : Generate handwritten diagrams (Many thanks to
	Adrian Vogt for the suggestion and its code!).
- April 7, 2015 : Use of guillemet in Stereotypes (Thanks to
	Mark George for the suggestion).
- March 20, 2015 : Integration with NodeBB Forum (Thanks to Connor Hillen ).
- March 15, 2015 : Specify colors for individual components.
- February 14, 2015 : Minor bug fixes and improvements.
- February 2, 2015 : Future enhancements in Sequence Diagrams with Teoz layout engine.
- January 28, 2015 : New version of the Word Template. (Thanks to Adriaan van den Brand for his works)
- January 14, 2015 : Minor bug fixes and improvements.
- January 8, 2015 :
	We support Freedom of Speech : implementation of Je Suis Charlie command.
- January 5, 2015 : Minor bug fixes and improvements.
- December 10, 2014 : New !includeurl feature in preprocessing. (Thanks to Nicolas Jouanin for his code)
- December 3, 2014 : Minor bug fixes and improvements.
- October 26, 2014 : You can contribute to Wikipedia.
- October 23, 2014 : Minor bug fixes and improvements.
- October 2, 2014 : Updated version of the PlantUML Language Reference Guide. (This document should now be always up-to-date with the website.)
- September 25, 2014 : Macro on several lines.
- September 16, 2014 : Fix 8005 bug that breaks Eclipse Plugin.
- September 15, 2014 : Minor bug fixes and improvements.
- September 4, 2014 : Tile as escape character for Creole.
- August 24, 2014 : Many new activity diagrams features.
- August 20, 2014 : Minor bug fixes and improvements.
- July 30, 2014 : PlantUML Gizmo allows you to create UML diagrams directly inside Google Docs!
- June 23, 2014 : Using several if/elseif in conditional branches .
- June 15, 2014 : 
	Hallvard TrÃ¦tteberg has added support for Ecore/Xcore .
	(Many thanks for his great work!)
- June 6, 2014 : Porting Graphviz/Dot to Java .
- May 14, 2014 : OpenIconic integration .
- April 13, 2014 : Beta export to LaTeX (Thanks to Ivan Enderlin for the suggestion).
- March 31, 2014 : New Zoom fit feature (Thanks to Zane Purvis for providing the code).
- March 24, 2014 : Integration with Gradle .
- March 18, 2014 : Finally, Creole available on all diagrams!
- March 6, 2014 : New options in tables for Salt diagram .
- March 5, 2014 : Beta version of the new online server .
- February 16, 2014 : Macro preprocessing with several args .
- January 28, 2014 : PlantUML Dependency 1.3.0 available on Maven Central Repository .
	(Thanks to Benjamin Croizet)
- January 24, 2014 : Nice slideshares: PlantUML introduction and Draw More, Work Less . (Thanks to theirs authors!)
- January 21, 2014 : Fix font-family from "SansSerif" to "sans-serif" in SVG output . (Thanks to Zane
	Purvis for pointing this out)
- January 16, 2014 : Warning : legacy syntax with end package and end namespace will be soon removed.
	Ensure that you are using the bracket notation .
- January 5, 2014 : Major update of Word Add-in with a new toolbar and EPS export for better printing .
	(Many thanks to Adriaan van den Brand)
- January 2, 2014 : Improved skinparams for component diagrams .
- December 11, 2013 : Visualize Xtext models with PlantUML .
	(Thanks to Boris Holzer)
- December 9, 2013 : Use sprites in Activity Diagram Beta.
- November 4, 2013 : New version of PlantUML Dependency (Thanks to Benjamin Croizet).
- October 28, 2013 : Use Creole for advanced text syntax in activity diagram beta .
- October 11, 2013 : Use PlantUML on Salesforce.com with Apex (Thanks to Robert SÃ¶semann for his work).
- September 30, 2013 : New rendering for condition .
	You can vote wether you want to keep this rendering or not .
- September 30, 2013 : New rendering for condition .
- August 30, 2013 : Use auto generating UML diagrams from SAP/ABAP code .
- July 24, 2013 : Use annotations in class diagrams (Thanks to Benjamin Croizet for the suggestion).
- July 17, 2013 : Add legend to sequence diagrams .
- July 15, 2013 : Use Puse editor .
- July 1, 2013 : Add legend to class/object/usecase/state/component diagrams .
- June 7, 2013 : Use database in sequence diagrams .
- May 28, 2013 : Integration with Python . (Thanks to Doug Napoleone)
- May 25, 2013 : Improved Word integration . (Thanks to Adriaan van den Brand for his great template!)
- April 29, 2013 : Splitting usecase diagrams .
- April 24, 2013 : Release version 7964 to avoid Java 7 update 21 issue .
- April 15, 2013 : Use notes in activity diagrams .
- April 14, 2013 : Available Apache Software License version of PlantUML .
- April 12, 2013 : Integration with Publet .
- April 5, 2013 : Use URL in img tag .
	(Thanks to Alain CorbiÃ¨re for his patch)
- March 28, 2013 : 
	Use PlantUML Viewer directly in Chrome .
- March 25, 2013 : 
	More labels in while loops .
- March 19, 2013 : Floating note in state diagrams .
- March 17, 2013 : 
	New web site design !
- February 28, 2013 : 
	Hide classes in class diagrams .
- February 18, 2013 : 
	Adding colors in beta activity diagrams .
- February 6, 2013 : 
	Proposal of a better syntax for activity diagrams .
- January 31, 2013 : 
	Use reference in sequence diagrams .
- January 29, 2013 : 
	Use bidirectional arrow in sequence diagrams .
- January 25, 2013 : 
	Generate PlantUML diagram for Lua with LDoc .
	(Thanks to Steve Donovan for his work)
- January 23, 2013 : 
	Hallvard TrÃ¦tteberg has made an Eclipse Juno compatible version of the Eclipse plugin .
	(Many thanks for his work)
- January 2, 2013 : 
	Change color arrows in sequence diagrams .
- December 5, 2012 : 
	Use long description for usecase .
- December 4, 2012 : 
	Online integration with Renderist on herokuapp.com . (Thanks to Julien Eluard for the job done)
- November 20, 2012 : 
	More option about automatic namespace creation .
- November 18, 2012 : 
	Integration with CKeditor .
- November 14, 2012 : 
	Integration with TiddlyWiki .
	(Thanks to AnÃ­bal CÃ¡ceres for the work done)
- November 12, 2012 : 
	Integration with TinyMCE Editor .
- November 10, 2012 : 
	Use new package styles in component and usecase diagrams .
- November 7, 2012 : 
	Integration with PmWiki .
- October 24, 2012 : 
	Use color gradient in diagrams .
- October 19, 2012 : 
	With JQuery, use PlantUML directly from HTML code .
- October 18, 2012 : PlantUML ã®ä½¿ãæ¹ .
- October 15, 2012 : Use macro in preprocessing .
- October 11, 2012 : Available LGPL version of PlantUML .
- October 2, 2012 : Adding entities, boundaries and controls in sequence diagrams .
- September 15, 2012 : Slight improvement of concurrent state drawing .
- September 10, 2012 : Rss flow about lastest PlantUML Version .
- September 9, 2012 : Minor bug fixes .
- August 28, 2012 : New PlantUML QEditor written in Qt4 (Thanks to Ioan Calin Borcoman for the job done)
- July 31, 2012 : Adding space in sequence diagrams .
- July 25, 2012 : Design your GUI using PlantUML .
- July 9, 2012 : Use transparent for background .
- June 20, 2012 : Use FTP to generate UML diagrams .
- June 6, 2012 : Use new package styles in class and component diagrams .
	(Thanks to Arno Petersen for the code)
- June 5, 2012 : Codeuml - design UML diagrams as fast as you can code .
	Very nice article here . (Congratulation to Omar Al Zabir for the job done)
- May 30, 2012 : What about porting Graphviz/Dot to Java ?
- May 22, 2012 : Integration with IDE Intellij idea (Thanks to Eugene Steinberg for the contribution).
- May 20, 2012 : Enhanced look and feel for sequence diagrams .
- May 10, 2012 : Enhanced look and feel for state diagrams .
- April 22, 2012 : Celebrate Earth Day .
- April 16, 2012 : Enhanced look and feel for activity diagrams .
- April 1, 2012 : Remember The Oregon Trail.
- March 30, 2012 : Using UML2 rendering in component diagrams. (Thanks to Arno Petersen for the patch)
- March 18, 2012 : Using sprites in diagrams.
- February 26, 2012 : Add an extra arrow on labels in class diagrams.
- February 14, 2012 : Specify class body as you like. (Thanks to Heiko Folkerts for the suggestion)
- January 30, 2012 : Use generics in class diagrams. (Thanks to Heiko Folkerts for the suggestion)
- January 17, 2012 : Use PlantUml filter plugin for AsciiDoc. (Thanks to Bartosz Wiklak)
- January 14, 2012 : Improved Doxygen support . (Thanks to Egbert Teeselink for the suggestion)
- January 8, 2012 : Declare abstract and static members in class diagrams .
- December 11, 2011 : Enhanced look and feel for usecase diagrams .
- October 31, 2011 : Enhanced look and feel for object diagrams .
- October 26, 2011 : Enhanced look and feel for class diagrams .
- October 12, 2011 : Some information about font change .
- October 11, 2011 : New return keyword and shortcut syntax in sequence diagram (Thanks to Adam Butcher for the idea and the code!)
- October 8, 2011 : New version of the Word Macro , with enhanced error mode
	(Thanks to Christopher Fuhrman for the VBA code)
- October 5, 2011 : Special command in memory of Steve Jobs. .
- October 3, 2011 : First version of the Sublime Text Editor plugin .
	(Thanks to Jayson Vantuyl for the job done).
- September 22, 2011 : Improved XMI support for StarUML .
- September 22, 2011 : Fixed broken link for downloading version 7255 .
	(Thanks to FranÃ§ois Deryck for reporting this).
- September 20, 2011 : Check if a newer version is available for download .
	(Thanks to Maxime Sinclair for the suggestion).
- September 19, 2011 : New version of the XWiki PlantUML Macro , with the new include parameter. (Thanks to Maxime Sinclair for his job).
- September 8, 2011 : Demo of new rendering for class diagrams .
- September 1, 2011 : Beta-testing of new rendering for class diagrams .
- August 23, 2011 : Integration of Java Chart Construction Kit to draw charts .
- August 8, 2011 : Better display of classes with several stereotypes (Thanks to Behrang Saeedzadeh for the suggestion).
- July 28, 2011 : New version of PlantUML Dependency .
- June 30, 2011 : Correction of a bug when drawing classes with members hidden .
- June 18, 2011 : Use DOT language to generate various diagrams.
- May 30, 2011 : Version 1.0.1 of plantuml-dependency available. (Thanks to Benjamin Croizet)
- May 25, 2011 : Warning about version 2.28 of Graphviz.
- May 23, 2011 : Correction of a performance issue on large sequence diagrams.
- May 14, 2011 : Correction of a bug when using multithread and !include (Thanks to Alexander Gusak for pointing this out).
- May 6, 2011 : New version of the MediaWiki plugin ,
	with SVG and imagemap. (Thanks to Pieter J. Kersten for the job done).
- May 5, 2011 : Wikipedia article started . You can contribute if you find it usefull.
- May 4, 2011 : Several new flags, including multithread in command line and ANT task .
- April 29, 2011 : Change text alignement in sequence diagrams.
- April 29, 2011 : Correction of a bug in MediaWiki extension . (Explanation here ).
- April 29, 2011 : Change text alignement in sequence diagrams.
- April 19, 2011 : Use DIagrams Through Ascii Art for many kind of diagrams.
	(Thanks to Stathis Sideris for this great project).
- April 17, 2011 : Integration with Confluence .
	(Thanks to Michael Griffel for his job).
- March 26, 2011 : Change the default shape for activities (Thanks to Oliver Vortex for the suggestion).
- March 24, 2011 : Generate PlantUML diagrams from SqlALchemy models.
	(Thanks to ÐÐ²Ð³ÐµÐ½Ð¸Ð¹ Ð¢Ð°ÑÐ°ÑÐºÐ¸Ð½ for the job done).
- March 20, 2011 : Put comments on several lines.
- March 11, 2011 : Official release of the PlantUML xwiki macro 1.0 (Thanks to Maxime Sinclair for the work done)
- March 9, 2011 : Use delay in sequence diagrams. (Thanks to Fabien Blanco for the suggestion)
- March 2, 2011 : Use PlantUML in your MediaWiki without installation thanks to Cloud computing .
- February 23, 2011 : Use (*top) to force starting point to be on top in activity diagrams .
- February 19, 2011 : Vote to eventually change the default shape for activities .
- February 17, 2011 : Generate diagrams with the Maven2 plugin . (Thanks to Julien Eluard for his job).
- February 16, 2011 : Hallvard TrÃ¦tteberg adds a scrollbar in the Diagram Source View and panning in the Image View of the Eclipse Plugin .
		(Thanks to Andree Junker for the suggestion).
- February 4, 2011 : New version of the Eclipse plugin with reverse engineering from
	Java code. (Thanks to Hallvard TrÃ¦tteberg for the great job
	done).
- February 1, 2011 : PlantUML available on Maven Central Repository repo1 on maven.org .
		(Thanks to Julien Eluard for his help).
- January 23, 2011 : Backcolor and wave for text formatting in sequence diagrams and notes .
- January 15, 2011 : Alpha support for xmi export .
- January 13, 2011 : Use different arrow styles in Sequence Diagram (thanks to Fabien Blanco for the suggestion).
- January 4, 2011 : Export to SVG with the Eclipse Plugin .
- January 2, 2011 : Happy new year! and updated
	version of the OpenOffice macro (Thanks to pbondo for this very complete documentation).
- December 22, 2010 : Feedback
	on proposal for new activity diagrams syntax .
- December 22, 2010 : Use PlantUML with XWiki (Thanks to Maxime Sinclair for the job done).
- December 19, 2010 : Use stereotype to modify colors & fonts in all diagrams (Thanks to Rainer Krug for suggestion).
- December 11, 2010 : Updated version of Language
	Reference Guide .
- December 7, 2010 : You can use the new forum for feedback/questions/suggestions/tips...
- December 6, 2010 : Correction of a major regression about font size and use non-letters in sequence diagrams .
- December 4, 2010 : First release of PlantUML Dependency (Thanks to Benjamin Croizet for the great job done).
- December 2, 2010 : Use images in activities description (Thanks to Benjamin Croizet for the suggestion).
- November 25, 2010 : Use non-letters in class diagrams (Thanks to Stefan Wallin for the suggestion).
- November 21, 2010 : Integration with DokuWiki (Thanks to Nicolas Fauvet for the implementation).
- November 14, 2010 : Use scale in generated images .
- October 29, 2010 : Change label for grouping in sequence diagrams (Thanks to
	Peter Antoniac for the suggestion).
- October 24, 2010 : Change arrow directions in usecase , component , state diagrams.
- October 19, 2010 : Change arrow directions in class diagrams (Thanks to flyisland for the suggestion).
- October 15, 2010 : Offer 250 to for PlantUML with Dropbox .
- October 9, 2010 : Use lollipop interface in class
	diagrams (Thanks to Roger Norling for the suggestion).
- September 26, 2010 : Put boxes arround participants in sequence
	diagrams (Thanks to Benjamin Croizet for the suggestion).
- September 8, 2010 : Hide methods
	and fields in class diagrams (Thanks to Roger Norling for the
	suggestion).
- August 18, 2010 : Integration with Emacs
	in Org-Mode (Thanks to Ian Yang).
- August 12, 2010 : Use ASCII
	art for Sequence Diagrams .
- August 10, 2010 : Short tags for text formatting .
	(Thanks to Roger Norling for the suggestion).
- July 18, 2010 : Important changes in
	activity diagram syntax .
- June 25, 2010 : Adding a
	black and white skin (Thanks to Bernd Viefhues for the suggestion).
- June 22, 2010 : Adding par/break/critical keywords
	for message grouping (Thanks to Bernd Viefhues for the suggestion).
- June 17, 2010 : Possibility to create new objects in sequence diagram .
- June 14, 2010 : Bug fix in doclet
	used for reverse engineering . (Thanks to vesterj for pointing this
	out!)
- June 6, 2010 : Use incoming
	or outgoing messages in sequence diagram.
- May 24, 2010 : Official release of object
	diagram . (Thanks to Hallvard TrÃ¦tteberg for the suggestion)
- May 20, 2010 : Zero installation UML through UML by E-Mail.
- May 19, 2010 : Integration with Docutils .
	(Greetings to Mauricio Cappella for the job done!)
- May 16, 2010 : Use asynchronous
	message in sequence diagrams . (Thanks to Omar Al Zabir for the
	suggestion)
- May 16, 2010 : Define a
	default font . (Thanks to naka_aki_spl for the suggestion)
- May 4, 2010 : Define visibility
	for fields and methods in class diagrams . (Thanks to Hallvard
	TrÃ¦tteberg for the suggestion)
- May 3, 2010 : Use brackets to define methods and fields in class
	diagram . (Thanks to Hallvard TrÃ¦tteberg for the suggestion)
- April 30, 2010 : Slight change in dot path for Linux/Mac OS-X . (Thanks to Zane
	Purvis for the suggestion)
- April 23, 2010 : Integration with Trac .
- April 7, 2010 : Support for APT
	files .
- April 3, 2010 : Use LaTeX to build
	the documentation . (Result is here )
- April 1, 2010 : Have a break and generate
	Sudoku with PlantUML .
- March 29, 2010 : Beta test the Open
	Office integration .
- March 25, 2010 : New version of the Eclipse
	plugin with newpage working in sequence diagrams and Graphviz path which can be set in
	preference page.
- March 19, 2010 : Correction of very annoying bug about the GRAPHVIZ_DOT variable which was
	sometimes not taken into account .
- March 17, 2010 : Colors in participants , notes and lifelines of
	sequence diagrams.
- March 9, 2010 : Test the new PlantUmlEditor created by Omar Al Zabir.
- March 5, 2010 : Export class diagrams to SVG format .
- February 28, 2010 : Export usecase, activity and
	component diagrams to SVG format .
- February 21, 2010 : Use namespaces
	in Class Diagram (Thanks to Jean-Francois Burdet for the suggestion)
- February 17, 2010 : Add divider
	in Sequence Diagram (Thanks to Torben Hoffmann for the suggestion)
- February 11, 2010 : Fix the Office
	2007 issue .
- February 10, 2010 : Export sequence diagrams to SVG format .
- January 27, 2010 : Very old news, but never mentioned
	here: Integration
	with Confluence thanks to Achim Abeling .
- January 27, 2010 : Integration
	with Redmine thanks to Alexander Tsvyashchenko .
- January 26, 2010 : Official release for State Diagram .
- January 13, 2010 : Links between packages in class diagrams .
- January 7, 2010 : Correction of a bug when including files .
- December 9, 2009 : Changing Usecase
	Diagram direction .
- November 29, 2009 : Adding footer
	and header .
- November 19, 2009 : Integration with MediaWiki .
- November 15, 2009 : Use standard input/output in command line .
- November 14, 2009 : Full Unicode support for internationalization .
- November 9, 2009 : Put some notes into Activity Diagram .
- November 7, 2009 : Information about Eclipse Plugin Upgrade .
- October 27, 2009 : Example of integration with Doxygen .
- October 23, 2009 : Change
	colors and font in drawing in Sequence
	Diagram , Usecase Diagram , Class Diagram , Activity Diagram , Component Diagram .
- October 20, 2009 : Official release for Component Diagram .
- October 12, 2009 : New syntax for Use
	Case Diagram . The old syntax is still working but will be removed in
	the future.
- October 2, 2009 : PlantUML
	on Twitter .
- September 29, 2009 : New version of the
	Eclipse Plugin , new button to disable automatic diagram generation.
- September 28, 2009 : Use wildcards in command line or ANT
	task . ( Version 3060 )
- September 23, 2009 : Be smart with the new preprocessor
- September 10, 2009 : New version of the
	Eclipse Plugin .
- September 7, 2009 : Recurse through directories with the command line or the ANT
	task .
- July 31, 2009 : Possibity
	to have titles when splitting diagrams
- July 27, 2009 : Use the doclet
	provided by Michael Welters
- July 10, 2009 : Example of Assocation classes
- July 9, 2009 : Using PlantUML
	with Javadoc tool
- July 6, 2009 : First version of the Eclipse
	Plugin
- July 2, 2009 : More information about titles in sequence diagrams , use case diagrams , classes diagrams , activity diagrams
- June 26, 2009 : Removing
	Footer in sequence diagrams
- June 23, 2009 : Stereotypes
	in sequence diagrams
- June 18, 2009 : New site design thanks to RaphaÃ«l !
- June 17, 2009 : Automatic
	message numbering
- June 15, 2009 : Language
	Reference Guide available on PDF.
- June 9, 2009 : Use the Online Server , (Explanation here)
- June 5, 2009 : Using
	packages .
- June 1, 2009 : Use PlantUML API .
- May 25, 2009 : Splitting
	large images .
- May 19, 2009 : Adding spots in classes diagrams .
- May 14, 2009 : Adding enum, interface and abstract
	classes in classes diagrams .
- May 12, 2009 : Demonstration online with Java Applet.
- May 7, 2009 : Adding images in notes and messages .
- May 6, 2009 : Change the command
	line to be able to run on single file, and to display Java & PlantUML version
- May 5, 2009 : Creation of the mailing list Plantuml-users for open discussion about PlantUML.
- May 4, 2009 : Adding C O L O R in notes and	messages .
- April 22, 2009 : First public release.
