---
title: Changes — PlantUML Official Documentation
source: https://plantuml.com/changes
description: Official documentation for PlantUML Changes
---

# Recent changes

PlantUML News and information Recent changes Â Â Â Â

## V1.2026.6 (Jun 8, 2026)

- â¨ add Node/JS MCP server (plantuml-mcp-js) and MCP engine plumbing
- ðµ update standard library with JSON data and examples
- ðµ allow %load_json on TeaVM
- ðµ fix skinparam style strictuml for TeaVM
- ð· fix release downstream jobs being silently skipped after upload
- ðµ allow %get_all_theme on TeaVM
- ð§ preparation for hour/minute/second precision gantts
- ð fix gui regression
- ðµ enable TeaVM JS build for the MIT license flavor (#2741)
- ð· add MIT-flavored npm package assembly for @plantuml/core
- ð¾ add errorLine in MCP check_syntax
- ð fix NPE in SVG nested diagram

## V1.2026.5 (May 27, 2026)

- ð· improve Docker build
- â»ï¸ clean StringBounder code
- â»ï¸ simplify dictionary loading for GraalVM
- ð· add native image builds (windows + linux amd64/arm64)
- ðµ add npmPackage Gradle task to publish JS engine to npm (#2715)
- ð· rename native images
- ð add bitmap image support in PDF
- ð· add native image builds (macOS)
- ð§ add config file for GraalVM build
- ð¦ï¸ add examples in standard library
- ð fix HorizontalAlignment Right being ignored with MinimumWidth (#2717)
- ð accept decimal period, pulse and offset for timing clock (#2714)
- ð· Fix 32-bit build failure caused by hardcoded JVM heap size (#2721)
- ð¦ï¸ update standard library

## V1.2026.4 (May 20, 2026)

- â»ï¸ use UBrex in Gantt diagram parsing
- ðµ revert to TeaVM 0.13.1
- ð fix(svg-parser): support space-separated coordinates in polygon/polyline sprites (#2692)
- ð fix '!' separator not recognized in class relation identifiers
- ð improve CSS style for state diagrams
- ðµ add support of OpenIconic icons in TeaVM
- ð improve unique id for SVG group elements
- â fix Vega tests with class drawing
- ðµ fix SVG document background color
- ð color specific days on gantt diagram
- ðµ Add dark mode toggle and "Copy as bitmap" button to the Playground
- â¨ online style in state diagram
- â vega: add SVG test (for id , option , and move interaction ) (#2705)
- ð manage CSS for empty description states
- ð improve SVG arrow drawing
- ðµ playground: right-click menu to copy as bitmap or SVG
- ð¥ Replace Batik-based PDF backend with native OpenPDF backend
- â¨ add new INTERNET_WITH_DOTSVG security profile
- ð Improve dark mode (fontcolor) for activity spot or state history
- â¨ Allow CSS style on single line (#2713)

## V1.2026.3 (May 8, 2026)

- â»ï¸ improve unsupported diagrams
- ð¼ï¸ improve constraint arrowhead
- ð fix quoted URL misinterpreted in YAML
- ð fix incorrect Japanese translations in i18n properties (#2604)
- ð¾ Rename i18n property keys from ebnf.* to regex.* (#2605)
- â¨ Improvements to the JS editor (#2609)
- â¨ add Base64 sprites
- â¨ add MD5 sprites
- âï¸ Hotfix ubrex Creole implementation in TeaVM build by replacing unicode at build time with inline String.valueOf (#2616)
- ð¾ restore svg output for DOT diagram in UNSECURE mode
- ð detect misuse of @startuml for DOT or DITAA diagrams and print a helpful error
- ð¾ spelling corrections
- ðµ fix text rotation
- ð detect misuse of @startuml for network diagrams and print a helpful error
- ð¾ spelling corrections https://github.com/plantuml/plantuml/discussions/2614
- ð¾ fix sax parser issue with MD5 sprites
- ð fix NullPointerException in gantt diagram
- â¨ Two new features for WBS diagrams (#2627)
- â¨ [Chart] Improve chart diagram (allow x-axis and y-axis , space before keyword, space at the end) (#2634)
- â¨ change AutoWidth true to width auto in WBS diagrams
- ð Bar Charts: Added Min and Max functions to prevent bars from being drawn outside of the plot (#2639)
- ð disable access to external entities in XML parsing
- ð Add SonarQube Cloud badge to README
- â¨ [Packetdiag]add same_height param +center labels vertically (#2643)
- â add special crash diagram for testing
- ð component border color for ELK
- ð update UBrex documentation
- ð¾ slight change in UBrex syntax
- ðµ fix dash issue
- ðµ fix overlapping issue
- ð(gantt): fix working day calculation for milestone after start (#2657)
- â¨ read MaximumWidth style property for arrow message wrapping (#2660) (#2661)
- ðµ fix gantt i18n
- â»ï¸ refactoring about padding
- ð fix NPE
- ð use CSS instead of skinparam for margin and padding
- ð ignore !pragma and skinparam in listopeniconic and others
- ð make %date deterministic across time zones (#2674)
- ð¾ add --null flag for performance test
- ð add adding for Object thought CSS
- â¨ add --loop option for performance tests
- ð fix gantt today highlight using system timezone instead of UTC https://github.com/plantuml/plantuml/issues/688 (#2688)
- ð¼ï¸ migrate skinparam ParticipantPadding/Padding to CSS style in themes
- ð render {0,N} quantifier with the missing zero path
- ð¥ remove Pragma from SvgOption
- ð EBNF "0 *" generates a zero path
- ðµ standardize SVG output (group attributes)

## V1.2026.2 (Feb 27, 2026)

- â¨ Packetdiag (#2529)
- â¨ allow chart and packetdiag diagrams to be embedded (#2531)
- ð¼ï¸ allow cumulative textDecoration on SVG (#2542)
- â¨ Add role label to associations in class diagrams (#2537)
- ð¸ improve packetdiag and nwdiag (better def., deprecate @startuml, ...) (#2547)
- ð¥ [Chronology] temporary remove chronology diagrams
- ð¥ [Activity] Suppress old SDL end char management (#2489)
- ð¥ [Activity] Require stereotypes at end of line in activity diagrams
- ð add new gradle tasks and Jdepend-graph of plantuml on dev site (#2550)
- ð· publish Java 8 JAR built thanks to ant
- ð fix NPE
- â¨ [State] add groups for start and ending state (#2500)
- â¨ [State] group individual states in SVG (#2511)
- â¨ [Timing] allow Timing signals without full-label (similar to clock )(#2499)
- â¨ [Class] allow visibility on one-line class (#2519)

## V1.2026.1 (Jan 18, 2026)

- ð fix GUI - GUI flag generates error for release 1.2026.0
- ð¦ï¸ update C4-PlantUML to v2.13.0
- ð¾ remove from sub-diagram SVG processing instructions (#2478)
- ð loading local themes
- ð remove unmodifiable collection
- ð manage link for emoji in activity diagrams
- â¨ improvement on color for diamonds in activity diagrams

## V1.2026.0 (Jan 9, 2026)

- ð fix issue during negative comparison
- ð fix dot issue
- ð fix nested state attributes render outside parent composite
- ð Added repeat while labels to diamond Inside figure (#2422)
- â¨ clarify include path resolution rules
- ð Connectors from switch tile creates arrow to a different tile in a different swimlane (#2423)
- ð tikz: vertically center single AtomText and fix cuca height (#2055) (#2424)
- ð Connectors from switch tiles connect correctly (#2426)
- ð minor regression
- â¨ Text align for StripeSimple (#2408)
- âï¸ Add chart diagram support with comprehensive features (#2440)
- ð¦ï¸ adding awslab v20.0 and upgrade archimate to 3.2.2
- â¨ Add attributes to visibility modifiers in SVG (#2441)
- ð better handle CLI errors
- âï¸ 2436 style allow actor shape on activity diagram (#2444)
- â¨ add default value for !option
- â¨ add partition keyword for sequence diagram
- â¨ add default value for !pragma
- â¨ Add month (30 days) support in gantt diagram
- ð protection against memory error
- â¨ add stereotype and URL for CommandActivityLegacy1 on activity diagram (#2451)
- â¨ allow empty branch in mindmap (#2452)
- â¨ style allow actor shape on activity diagram
- ð remove SVG export for PSystemDot
- â¨ add link type attributes to SVG (#2453)
- â¨ allow minimal mindmap (#2454)
- ð©¹ fix lazy Regex on CommandActivityLegacy1 (#2456)
- â¨ add link type attributes to SVG (#2453)
- ð minor regression on mindmap diagram
- ð fix crash when using a bad reference in a state machine
- ð remove legacy !pragma SVGNEWDATA true
- ð¾ display warning when using legacy group syntax
- ð fix automatic font colors with table
- ð use "processing instruction" in SVG export
- ð improve !if management

## V1.2025.10 (Nov 4, 2025)

- â¨ Add support for rounded corners on orthogonal edges (#2389)
- âï¸ Add automatic vertical alignment for orthogonal edges at label nodes (#2395)
- ð fix substracting in preprocessor
- â¨ Allow access to internal SVG sprite (SVG by default with a PNG fallback) (#2397)
- â¨ allow unit (s, m, h, d, y, Y) on timing scale as pixel (#2398)
- ð improve help message
- ð Remove extra empty line after sub-diagram (#2404)
- ð restore 8080 as default port for picoweb
- ð fix dot issue
- â¡ï¸ speeding up generation sub-diagrams in SVG
- â¨ new rectangle shape in timing diagram

## V1.2025.9 (Oct 18, 2025)

- â¨ Add node-based transition labels for state diagrams
- â¨ Further improve edge routing for node-style transition labels in state diagrams
- â¨ allow * on ActivityLegacy1 (and adjust with spaceZeroOrOne )
- â¨ Center node-style transition labels on edge path in state diagrams
- â¨ Preserve original number format in timing diagram analog scale labels
- â»ï¸ refactor Regex on ActivityLegacy1, and spaceZeroOrOne
- ð Improve number format support in timing diagram analog scale
- âï¸ experimental support for !pragma sequenceMessageSpan true
- âï¸ Introduce new command-line interface (beta)
- ð¦ï¸ update standard library (archimate)

## V1.2025.8 (Oct 4, 2025)

- ð± [Archimate] Remove duplicate sprites and replace PNG sprites with SVG counterparts
- ð Improve error message for WBS diagram root validation (replace error 44)
- ð Language Descriptor Improvement [fix, update, add, suppress some keywords]
- ð Improve WBS declaration (with Direction , Code )
- â¨ WBS improve declaration (force order of parameters)

## V1.2025.7 (Sep 10, 2025)

- â»ï¸ improve font management
- ð fix regression with some o-- link
- ð Add inheritance to lifeline for delay (#2266)
- ð fix WBS direction
- ð fix scale regression in class diagrams
- ð¦ï¸ update standard library ( material7 and C4 )
- ð¥ remove obsolete skinparam setting
- â¨ add new activationBox style which works locally
- ð¾ adding trace for debug
- ð fix GraphvizDotHeader test to be more conform to the official DOT grammar (#2294)
- â¨ add svgTitle and svgDesc options for accessibility
- ð add documentation about CI
- ð· add compilation with ant on JDK8
- ð add documentation about CI and JDK8/ant
- â¡ï¸ improve perf by removing regex
- ð¥ remove dead code
- ð Support local style on Activity diagram elements
- ð include title with line breaks in SVG element
- â¡ï¸ optimize diagram type detection and start/end parsing
- â¡ï¸ refactor activity ftile snakes and worms
- ð fix regression
- â¡ï¸ optimized translation for Worm
- â¡ï¸ optimize color parsing
- â¡ï¸ optimize token parsing
- âï¸ optimize images by applying PNG quantization when feasible
- âï¸ slightly reduce PNG
- âï¸ using deflate level 7 for PNG
- ð§ add OKLab PNG quantization (currently unused, may be used later)
- ð Update Archimate sprites to assign correct colors; use new workpackage symbol (#2308)
- ð· fix missing archimate sprites
- â»ï¸ better handle alpha channel
- âï¸ improve transparency handling in image quantization
- [Style][Theme] Improve task margin management on all themes (for Gantt diagram) (#2312)
- ð§ prepare SVG sprites for Archimate
- ð Fix missing double dash un-escaping in SVG metadata (#2313)
- ð fix horizontal line in tips
- ð§ Archimate updates, including svg versions of the sprites (#2316)
- ð§ prioritize SVG sprites over PNG for Archimate diagrams
- ð fix include from !theme
- ð display SVG sprites in listsprites
- ð¦ï¸ update Archimte standard library
- ð Improve error reported when entity already exists (#2324)

## V1.2025.4 (Jun 28, 2025)

- See directly on GitHub: All GitHub Issues fixed or GitHub Pull Request accepted of the version
- Sequence - Lifeline border thickness is ignored when a delay is added in sequence diagram
- Sequence - CSS styling Beta - Sequence diagram - dots not colored with LineColor
- Sequence - Text of delay message in cerulean theme is invisible

## V1.2025.3 (Jun 1, 2025)

- See directly on GitHub: All GitHub Issues fixed or GitHub Pull Request accepted of the version
- Javadoc improvement
- Jacoco improvement (Add Java Code Coverage Report)
- Activity - How to change colour on new Activity Diagram goto
- Activity - How to draw send signal action and accept event action in activity diagram?
- DITAA has crashed
- DITAA - empty lines seem to be ignored; this may result in additionally rendered boxes
- Gantt - Adding a Note below a milestone in Gantt
- Gantt - Custom / financial weeks in Gantt chart
- Invalid message of obsolete version
- SVG sprites work in a node text, but not in an edge text
- SVG - Broken inline SVG support for Quadratic Curves
- State machine invalid generation for SVG

## V1.2025.2 (Mar 5, 2025)

- EBNF - Improve the curved line on the EBNF diagram
- SVG - Lost id-attribute (or group)
- SVG - Revert SVG fill to "none"; use UParam to indicate hit targets
- SVG - Interactive SVG with namespaced::nodes does not work properly
- SVG - Unable to Click Links in SVGs Due to Overlapping Transparent path Elements
- SVG - Interactive SVG with component ports is not working
- SVG - Add filtering to interactive sequence diagrams
- SURL - Follow HTTP redirection in !include directive
- Style - Allow old skinparam (stereotypeXBackgroundColor/BorderColor) for new spot style
- Style - Update handwritten themes in order to avoid warning
- Native - Naming of the snapshot native images
- Native - Support C4 on native image
- Native - Add Linux ARM64 native image on Native Image - Snapshot
- Newline - Possible regression bug (due to new newline management)
- Newline - Improve preproc output
- Gantt - Hide monthheader if the whole month is closed in gantt

## V1.2025.1 (Feb 16, 2025)

- Backslash future deprecation and introduction of new functions
- newline fix
- REGEX - Add method to map regex patterns to descriptive names
- SVG - Allow interactive SVG sequence diagram's header to float
- XMI - Add support for custom XMI generation
- SVG results with black box in Visio
- PDF export fails
- Problem with <style> and parameter Shadowing for rectangle
- YAML string quotes do not escape comment character
- Style boxless root on mindmap
- Allow colon character ( : ) on the value of a YAML field
- Unable to define variables on plantuml command line with -D
- Diagram sequence regression
- Improve internal YAML parser with a new parser
- YAML - Display key without label
- YAML - Fix Object attribute hierarchy in the yaml array
- YAML - Cannot render a list contain a key value pair
- YAML - Fix YAML processing if no spaces at start of list
- YAML - Last list entry used instead of showing top level YAML items
- EBNF - None-first style
- Entity names cannot start or end with separator character: fix error message

## V1.2025.0 (Jan 15, 2025)

- Gantt Chart with closed weekends does not render correctly depending on the theme
- Allow hide closed in the Gantt chart
- Ressources footer is messed when in monthly mode
- Gantt with weekly scale doesn't show named regions
- guillemotleft guillemotright
- Improve head of arrow position
- Smetana throws an ArrayIndexOutOfBoundsException
- test ExportOnUText
- Extend error message with diagram type
- Allow RoundCorner for object, map and json element
- Update DomainStory to version Delta 0.4.0
- Hiding/showing a specific stereotype hides/shows all of them
- Allow YAML frontmatter on beginning of theme files
- Allow to expand a element with the corresponding alternative element

## V1.2024.8 (Nov 15, 2024)

- Nwdiag: Allow line border for group
- Style: Allow all style for regex diagram
- Compact clocks in timing diagrams not rendered correctly
- Mindmap: node MaximumWidth: weird latex result
- Style: Improve HorizontalAlignment management
- Can I center the description text at the bottom the state box?
- Style: HorizontalAlignment management for diamond [Activity diagram]
- Text alignment for components in component diagram
- How to align text to the left in a container (for example a rectangle)?
- LaTeX labels not centered
- State: Exception on two transitions to the same deep history node
- Stereotype with plain circle: text should be elided
- Can't get bottom half arrow style to work when a macro is used
- Sometimes difficult to detect to which arrow a text in a Chen diagram belongs
- Allow MinimumWidth on all nested elements
- MinimumWidth doesnt work when there's a nested object
- Style: Improve map and json style in order to manage header style
- Improve edge cases for JSON diagram (manage null and empty Array/Object)
- JSON object: changing background color of Header line
- Gantt with monthly scale doesn't show named regions
- Add support for colors in Chen EER diagrams
- Dirpath built in preprocessor function returns empty in pipe mode
- Add overrideDirPath method
- Uniformisation of dirpath
- Regex: Allow to expand a [] element with the corresponding alternative | element
- Reintroduction of filedate and filename_no_extension builtin function
- Crash with IllegalStateException
- Allow Unicode ASCII Art for class, component, ...
- -tutxt switch does not produce unicode but simple ascii
- Request for adding a copy of the LGPLv3 as a COPYING.LESSER file along side the GPLv3 COPYING file?
- Style: Allow all style for Cardinality, Generic, Qualified associations on Class diagram
- Styling of qualified associations
- Style: Allow theme and style for files list diagram
- Fixing proprietary licenses in PlantUML software package of Replicant project
- Style: Allow stereotype on note for all diagram type
- State machine invalid generation for SVG [partial]
- State: Composite state error with namespace
- Allow stereotype for Clock on Timing diagram
- Allow stereotype on Timing diagram
- Can we have 2 or more colors for clocks in timing diagrams?
- Allow all JSON Values on JSON
- JSON-type component breaks
- Use latest graphviz version in docker image
- Allow (or skip) skin command on YAML diagram
- Fix: error in namespace management
- Allow stereotype for arrow, on sequence diagram
- Allow LineStyle for arrow, on sequence diagram
- Use latex to get string bounder
- tikz: make all fonts with the same baseline
- tikz: avoid latex manager crash for special characters
- tikz: use the same protectText when calc dimension and render
- tikz: optimize latex render
- Optimize tikz render
- Stdlib: Update Cloudogu to v1.0.2
- Stdlib: Update C4-PlantUML to v2.11.0
- Stdlib: Update DomainStory-PlantUML to v0.3.1

## V1.2024.7 (Sep 9, 2024)

- [Class][Deployment] Some issues about arrow between nested elements
- Crash happened on plantuml 1.2024.7beta5, related to "headless"
- hide does not work inside package
- After v1.2023.10, Remove command does not remove nested shapes
- When adding specific note at specific position, activity diagram not work
- Custom Theme loading
- [Creole] Fix color
- repeat starting point is in wrong swimlane
- Generate a svg:title tag when generating Svg
- fix: make native release as snapshot release
- feat: add builtin function %boolval
- feat: add builtin function %mod (modulo operator)
- Added background color to arrows and draw background for circles
- remove duplicate items in help message
- [Sprite][SVG] Manage more SVG functionalities for text
- pdf support broken with other gradle build file changes
- Allow style for backward element on repeat loop, on Activity diagram
- Allow >> and > on the same arrow
- Pause a task up to end of another task
- Rendering issue when nesting different elements
- Allow multiple style stereotypes for Mindmap, WBS
- Gantt: Weekscale with weeknumbers
- The utilization of resources does not color red correctly when week partly closed
- Remove and restore not working as expected

## V1.2024.6 (Jul 6, 2024)

- Improve Eclipse Layout Kernel support
- groups (e.g. alt) with else cannot be rendered in parallel
- alt/else block shown in parallel using teoz leads to wrong formatting
- Teoz: Shape of note changes only when "over" is used
- multiple activation of lifelines does not render properly in sequence diagrams
- 2024.5 breaks https includeurl
- Incorrect object reference in Gantt Chart
- Activity: Allow to style SDL on Repeat While loop
- inconsistent computation of group/alt/opt box size given left or right arrows
- !foreach $key from %get_json_keys() is not found by %json_key_exists(), but works for element access
- Allow scale max on JSON and YAML diagram
- [ELK][Smetana] Allow Fontcolor style on arrows
- [Style][WBS] Change (arrow) line color of a specific branch
- Elk: Allow full style on arrows (except fontcolor)
- feat: math: add newline command for formatting
- feat: add support for [one-line] title to JSON diagram
- Performance issue with JRE21
- Fix parallel group active levels
- Extend @@@format to support more formats
- [teoz] [bug] [sequence] Group becomes too wide when containing activations
- [Theme] sunlust theme does not work for JSON or YAML diagram/data

## V1.2024.5 (May 26, 2024)

- BUG: Activation is offset (Sequence diagram, Teoz)
- teoz: activation breaks parallell lines
- sequence lifeline height badly depends on message height
- Sequence diagram: Wrong start/end of activation boxes in activation boxes while using teoz
- The display of text, line, and arrow on the left side of the Lifeline is incorrect
- the location of the Comment is INCORRECT
- teoz arrow alignment
- activate/deactivate issues
- Inline multicast activate only activates the first target
- Activation is offset (Using Teoz)
- Small rendering difference between default and Teoz
- Side effect of variable management when using %json_add
- timing diagram initial concise state
- Java OutOfMemoryError with some Sequence diagrams
- Smetana is not supporting colors in UML
- Timing: Set background color of concise
- (timing diagram) message labels ignore default style
- "off by one errors" in text output
- hyperlinkUnderline causes NumberFormatException
- Wrong component is highlighted on hover for svginteractive
- [Theme] sunlust theme does not work for JSON or YAML diagram/data
- Stereotype won't be hidden with "hide stereotype"
- [Chen ERD] Allow horizontal layout or left to right direction
- add %splitstrregex builtin function
- ASCIIMathTeXImg.java with a lot of corrections/enhancements
- add new JSON builtin functions (%str2json, %json_add and %json_remove)
- add new JSON builtin function (%json_set)
- add new JSON builtin function (%json_merge)
- Fix on osa2 and Classy

## V1.2024.4 (April 6, 2024)

- Implement Chen Notation for ER-diagrams
- Add a tool-independent XMI format
- feat: add %get_all_stdlib builtin function
- fix: suppress @[start|end]uml on sunlust theme
- How to extends a generic class
- Negative values causing syntax error in robust "has" list
- Activity Diagram: Style of multiline Box
- Allow style for multi-line elements on Activity diagram
- EIP standard library

## V1.2024.2 (February 14, 2024)

- Update standard library
- feat: add %get_all_theme builtin function
- fix: update graphviz version check pattern
- Add theme Sunlust
- feat: Improve new Random function
- Improve Chronology diagram management
- add: Language Descriptor Improvement (adding action and process)

## V1.2024.0 (February 1, 2024)

- EDGY: An Open Source tool for collaborative Enterprise Design
- Gantt Layout issue when Print between is used with Printscale weekly
- teoz produces odd legend for sequence diagrams
- Note invalid position in Directory tree listing
- shape "activity" ist hardly missing
- Allow full local style (for while, repeat) on Activity diagram
- Allow full local style (for if diamonds) on Activity diagram
- Color individual conditional in activity diagram
- Bug with activity diagram arrows fork
- change the milestone icon from a diamond

## V1.2023.13 (December 11, 2023)

- Javadoc improvement , thanks to The-Lum
- Bug with activity diagram arrows fork
- Is is possible to change the milestone icon from a diamond?
- Gantt crashes with specific Project start dates
- Add support to style timeline fonts for gantt charts
- Directory tree listing
- Unable to set MaximumWidth style for legend
- Wrong note shape in sequence diagram when arrow has only one participant
- GANTT: How to handle if a resource starts or terminates at a specific date
- Is it possible to set gantt tasks to be incomplete by default
- [Style] Allow LineThickness style for awesome Actor on Component/UC/Deployment diagram
- [Style] Allow multiple style stereotypes for backward element on Activity diagram
- Syntax error on two and more array items in macros

## V1.2023.12 (October 20, 2023)

- Crash on sample DITAA diagram
- Only one transition permitted to State[H] in state diagram
- Rendering issue when nesting different elements (partially)
- force notes to use inner namespaces not global namespace only (partially)
- ASL distribution no longer includes graphiz.dat
- ASL distribution no longer includes OpenIconic SVGs

## V1.2023.11 (September 13, 2023)

- [Style] Allow style for backward element on Activity diagram
- Sequence diagram: Multi-level nested boxes overlaying each other
- Using -cypher does not always recognize restricted words
- Verticals separators in gantt chart don't appear under certain conditions
- namespace/package consolidation broke existing remove/restore behaviour when using namespace separators
- Last label on last elseif branch does not get rendered
- no colored border on state start/end
- Qualifier labels and associations' lines not correctly drawn for qualified associations
- Notes on conditionnal elements
- Update C4-PlantUML to v2.8.0
- Handle @start/@end syntax error better
- Adds copy task for graphviz.dat to epl build

## V1.2023.10 (July 12, 2023)

- Exception error when adding note to timing diagram
- Skinparam inconsistencies on class diagram grouping elements
- Batik SVG rendering: The attribute "width" of the element 'rect' is required
- skinParam fixCircleLabelOverlapping doesn't work anymore
- Using an external style file by pointing to a URL or by using a relative file path doesn't work
- Add regex, files on Embedded Diagram

## V1.2023.9 (June 13, 2023)

- nwdiag possible misbehavior
- Replace old ALLOW_PLANTUML_INCLUDE flag by security profile
- sprite transparent issue
- Alpha feature: Directory tree listing
- Smetana and ELK: Improve nested elements with last {} declaration
- [Font][Skinparam or Style] Issues on fall back font (partly)
- Decimal time values not accepted in parameters or procedures

## V1.2023.8 (May 21, 2023)

- First support for regular expression
- !theme supports no calculated from path and no stdlib from path
- Grammar error occurs when specifying full-width digits with the "as" keyword in timing diagrams

## V1.2023.7 (May 12, 2023)

- Activity: Allow to style SDL stereotype
- Activity: Allow post-positioned stereotype style
- specifying full-width digits with the "as" keyword in timing diagrams
- force notes to use inner namespaces not global namespace only
- teoz: Support notes on references
- Activity diagram, Case statement, arrow label missing
- When connecting attributes between object graphs, the connection error

## V1.2023.6 (April 18, 2023)

- Gantt Milestone with Multiline Text Placement
- Start and end nodes can only be styled globally in CSS style
- Gantt diagram - Can't close day in the period of opened days
- Support notes on references
- [gantt] make it possible to color last day
- Is it possible to color the days in the default Gantt Diagram?
- Automatic font color with gradient participant background creates UnsupportedOperationException
- ConditionStyle InsideDiamond not working for elseif
- StateBackgroundColor transparent is not effective
- Multible breaks in one repeat

## V1.2023.5 (March 24, 2023)

- Error in generating State Diagram
- Bug - Crowfoot notation on ERD rendering buggy
- Regarding the February update with intermediate namespaces
- Malformed layout and missing arrows on large amount of edges
- Smetana and ELK: Improve arrow position and suppress empty space
- [Class] Note on field is considered unlinked
- How to change direction of arrow in beta syntax in "Activity Diagram"?
- Rollback new style
- 'help preprocessors' command is not working
- JSON diagram SVG has misplaced arrows when containing newlines
- [Smetana] Allow notes (or comments) on lines or links
- ClassAttributeFont(Style|Size|...) overrides ClassFontStyle(Style|Size|...)
- The command help themes to list all the themes of PlantUML seems broken
- Note and position not rendering correctly on CheerpJ
- Ports with similar names
- Notes linked to messages in Sequence Diagrams
- !global $variable ?= "default variable" produces error "a001"
- Allow only one underscore when escaping
- Using end if as an alias for endif in Activity diagrams
- Drastic Behavior Change of "as" Parsing with "." (period)
- nwdiag bug: group causes element to incorrectly connect to network

## V1.2023.4 (March 9, 2023)

- Improve backward compatibility about package and namespace simplification
- Allow only one underscore when escaping
- Using end if as an alias for endif in Activity diagrams
- Ability to hide empty fields for object diagrams
- Namespace association class connection point outside namespace
- Dotted arrow --> is also the close of comment blocks

## V1.2023.2 (February 26, 2023)

- package and namespace simplification
- .repx file generation
- Cannot set long name arrow label in repeat statement with break
- together behaves different starting from 1.2023.0
- Possible regression with class alias declaration
- The footer is not displayed at the footer
- latex and package: no perpendicular corners
- Allow full style on label of Port, Point, Pin
- Structs do not function properly within a namespace
- Nwdiag problem with address label position on peer network
- Update tupadr3 in the stdlib

## V1.2023.1 (January 29, 2023)

- The footer is not displayed at the footer
- latex and package: no perpendicular corners
- Allow full style on label of Port, Point, Pin
- What is the best practice for font name definition on skinparam or style
- Nwdiag problem with address label position on peer network
- Support for JSONC (JSON with Comments)
- added sprites keycloak and apache superset
- Poll/Discussion to confirm current SDL stereotype naming
- Composite state functionality with allow_mixing
- Style management (error on carbon-gray theme)
- Elements inside together block in namespace belong to root namespace
- User defined style only works for empty elements
- smetana breaks entity arrows

## V1.2023.0 (January 9, 2023)

- namespace with slashes in the name
- 'skinparam lifelineStrategy solid' is not working as expected
- Box title is not displayed within some themes
- !Include wbs fails generating Syntax Error on line continuations
- Appling different Style to component ignores skinparams for component
- Cannot open URL
- Verticals separators in gantt chart don't appear under certain conditions
- Max size for notes
- Smetana: Allow full style on label of arrows
- Activity diagram: Using if(...) is (...) syntax in ELSEIF
- Allow 'MaximumWidth' and 'MinimumWidth' on all styles for all diagrams
- package and together closes the parent namespace in class diagram
- smetana breaks hover tooltip
- YAML Multiple highlight defs
- Can we use different backgroundcolor for highlight is jsonDiagram ?
- Decreasing visibility of links
- HyperlinkUnderline skinparam is broken
- Yaml diagram highlight wildcard
- Ability to add a background color to a component of a network in nwdiag
- nwdiag: can't change nodes background color
- Parsing issue with new style syntax on stereotype class
- Problem with parallel execution of plantuml in Windows

## V1.2022.14 (December 6, 2022)

- Link between objet in WBS
- hnote fails to render in txt (ASCII Art)
- Checkmetadata combined with newpage not skipping file creation
- EBNF Special border enhancement
- StrictUML arrowheads in Activity diagrams
- Inline SVG for sprites
- SVG Sprite shows up in PNG output, but SVG Image doesn't
- Transparent background colours on Alt/Else elements
- [Sequence] Improve background color of group with RoundCorner
- Boolean builtin functions
- prevent wrap for comma, dot, etc...

## V1.2022.13 (November 19, 2022)

- substr does not work if strings are added in the same line
- Center-aligned text not in the middle of a node
- skinparam ArrowHeadColor none doesn't work as expected on note node
- awslib/Mobile/Mobile.puml is black
- Arrow position and size in timing diagram
- Internal Server Error: !if -1 == -1yyyyyy
- Timing diagram: invalid display with only on state in concise
- Unicode inside sub diagram is not shown ok
- EBNF - Allow special sequence management with special-sequence-symbol "?"
- Adding support nested sub-diagrams
- Why can't is set "open" and "colored" on the same line ?
- How can I define note with stereotype?
- Style for note on Component and Deployement diagram, Class,...
- how to hide the vertical grid-lines in timming diagram?
- How can I apply a style or background color to a note on a class method?

## V1.2022.12 (October 23, 2022)

- Important change on Gantt Diagram : you *do* have to use @startgantt and @endgantt now.
- EBNF - Allow empty definition
- EBNF add notes
- EBNF - Allow full repetition management with repetition-symbol "*"
- colors on concise timeline in timing diagram don't respect line color
- Need to allow dashes in entity names
- [Style] Allow [all] style for mainframe
- [Style] Allow [all] style for JSON object
- [Style] Allow [all] style for stereotype on Activity diagram
- hide @unlinked fails in case of component {} notation
- Spaces in Markdown syntax in MindMap
- WBS Diagram: HyperlinkUnderline false
- Gantt: diff between days and working days
- cannot follow extends by string in class diagram
- multiline in mindmap: latex/math formula can only stay in oneline
- Add support for MetaClass and Stereotype in class diagram
- bullet list bug
- C4-PlantUML: AddComponentTag uses default component font color

## V1.2022.8 (September 25, 2022)

- Alpha support for EBNF
- multiline in mindmap: latex/math formula can only stay in oneline
- usecase: business usecase with multiline description
- How to style partition (group, package or card) like rectangle on Activity diagram?
- Packages loose skinparameters with nested elements
- Frame header font style
- "remove @unlinked" doesn't remove nodes if links were removed by "remove $tag"
- Hide empty descriptions removes inline style in State Diagram
- State diagram causes UnsupportedOperationException with smetana
- [Smetana] Frame title missing and links to the frame missing
- SCXML files generated from state diagrams don't preserve state hierarchies
- How to color note on link
- Static classes
- & a -> b crashes teoz
- Add qualified associations to class diagrams
- Attribute visibility on association names do not show with classAttributeIconSize 0
- "on the same row" breaks when used on self
- Max size for notes
- How to use textcolor for rectangle?
- BUG: rendering state with local transition and using StateBackgroundColor style
- Gantt Chart Vertical Separators

## V1.2022.7 (August 22, 2022)

- Could you improve port management?
- Error when mixed use of class,card and portin portout
- Coloring single ports
- Error when using map and portin/portout in a component
- Inline SVG for sprites
- Why does plus change from name of Map key to comment?
- improve descendant pseudo selector on Mindmap
- Declare Participants similar to Components
- How to left align when the AWS lib is also used?
- Gantt diagram - how to start a project a number of days before today?
- SVG generate embedded image
- Is it possible to add line color and thickness to analog variables?
- Timing Diagram: Adding double arrows to analog signal type
- Bug in class diagram member to member connection if naming is similar and contains underscores
- NPE observed during local theme testing
- Characters Â« and Â» not allowed in participant titles (sequence diagrams)
- Map can not set color of line
- The horizontal alignment style does not work correctly.
- Scenario in Ditaa that "hangs" PlantUML
- YAML Diagram - Unable to render elements where key has a space
- Plantuml draw odd line
- rocket emoji causes UnsupportedOperationException
- The mindmap's root node could never be centered now
- replace printStackTrace by java.util.logging.Logger

## V1.2022.6 (June 21, 2022)

- SVG images using creole img don't support scaling
- Regression in skinparam participant stereo behavior losing styling
- Is it possible to link elements from two jsons, with both jsons embeded ?
- Element line style not applied in usecase diagram
- Creole trees do not respect indent levels in a Class diagram
- error when using indented elements as ports
- Business usecase or "usecase/" does not work when "allow_mixing"
- Display year in timing diagrams using time and date
- Element line style not applied in usecase diagram
- Plantuml draw odd line
- How do I mark a binary as indeterminate in a timing diagram?
- For timing diagram binary data, allow data to be indetermine
- Latex generation fails with \t in front of html tag
- [Timing][Style] Allow all Style for timeline, on timing diagram
- overlapped groups in nwdiag throws exception
- Missing state fork/join in plain theme
- No way to add a note text next to a switch case branch in activity diagrams beta
- Is the skinparam ArrowHeadColor no longer available?

## V1.2022.5 (April 30, 2022)

- White-space management on stereotype
- Stereotype/skinparam with spaces in the name are not working anymore
- BetaStyle for timingDiagram
- Allow stereotype on Timing diagram
- Allow handwritten on file, stack and note
- Fix several visual regression
- Skinparam Shadowing true not working anymore
- Standard Library update

## V1.2022.4 (April 9, 2022)

- V1.2022.1: legitimate error message lost in a lot of logs
- map do not show members and fluffy arrows
- Bug with ArchiMate shapes
- Restore ability to change background color of class/entity header
- Have more than one Hyperlink text color
- 1.2022.2 regression: SVG does not include connections if notes are used
- 1.2022.3 regression: NPE @ TikzGraphics.getColorName
- Annotate binary waveforms
- [Activity][Style] Allow full style on diamond (e.g. internal label and external label)

## V1.2022.3 (March 29, 2022)

- Annotate binary waveforms
- Bold arrows via skinparam are not working anymore
- Composite state diagram causes UnsupportedOperationException with smetana
- Wrong colors in generated EPS file
- AmazonS3_LARGE seems to be an error in 1.2022.2
- [Style][Sequence] Allow stereotype for arrow, on sequence diagram
- 1.2022.2 regression - black backgrounds
- Crash when note on object member

## V1.2022.2 (March 5, 2022)

- New default style
- Use of CSS styles
- Stereotypes cannot be overwritten anymore
- BorderStyle dashed not working anymore
- Mostly Getting Cannot decode Image Error
- Gantt with Weekly Scale bugs
- New json entity
- Skinparam ArrowColor cannot be combined via multiple stereotypes
- stereotype priorities changed compared to older implementations
- skinparam DefaultFontColor overwrittes all existing font color definitions
- How to generate a legend with colors in PlantUML
- Error when using "-" as double arrow for styles
- BorderColor and BackgroundColor set to "None" returns a java.lang.NullPointerException from Graphviz
- "Normal" rectangles corners, "package" rectangles text colors are not supported anymore
- Line styles are not supported anymore
- "Default" line colors are not supported anymore
- "Fork" line not appearing in many built-in themes for Activity Diagrams
- New %json_key_exists() function
- New %splitstr() function
- Allow new styling for nested package

## V1.2022.1 (February 1, 2022)

- Added start Stereotype
- fix: nwdiag server or element name with special char
- Xmi export for Sequence Diagrams
- New styling not working for nesting elements
- ideas for 2 new json builtins
- Activity: Strange glitch repeat loop
- private/public indicators are not always present in state diagramm
- Add capability to nest state diagrams in package or frame
- skinparam Dpi causes exception
- groupInheritance cause NullPointerException
- backward in repeat loop in the wrong swimlane
- Some diagram description contains errors
- How to set color of the Gantt unstarted task
- Multiline backward statements in Activity Diagram
- Dark mode

## V1.2022.0 (January 11, 2022)

- Use of Emoji
- Declare Participants similar to Components
- Xmi export for Sequence Diagrams
- Why not to support nested boxes in sequence diagrams?
- Class Diagram can't extends inner class
- Preprocessor function %lighten
- Question related to 'Working with Resources' feature in Gantt charts
- Potential infinite loop on timing diagram
- Crash when try to use named as reference
- WBS: missing link and missing box

## V1.2021.16 (December 8, 2021)

- Broadcast, multicast in sequence diagrams crashes with theme
- Beta support for Emoji

## V1.2021.15 (November 30, 2021)

- change default JSON/YAML theme
- Support for URL authentication (Thanks to Aljoscha Rittner )
- Hide footbox breaks network diagram
- add: hide as NOP on style for JSON or YAML diagram
- Changing the color of both fork and join states
- Multiroot Mindmap (Thanks to chapterjason ) for the idea
- Style tag breaks rendering in deployment diagram
- Sequence: Lifeline color missing on in/out messages with teoz
- theme in search path
- Improve hyperlink support for dark theme
- New %size() function
- New %chr() function
- Suppress delay for more than a minute before exiting

## V1.2021.14 (November 12, 2021)

- Typo in error message
- Sequence: Lifeline color missing on in/out messages with teoz
- Custom Themes: Don't require "from folder" if theme is in search path
- Improve theme support
- Improve chinese text supports word wraps
- Description on an returning arrow of repeat is not rendered
- The combination of while, if, note, and break statements does not draw the figure.
- Issues with switch in the activity diagram
- Using AWSPuml and code causes Java error
- Use style with map
- Add new chr(), size() and loadJSON() functions in preprocessor
- Fix folder width growing with length of alias
- Improve transparent support
- Better themes support

## V1.2021.13 (November 1, 2021)

- Update Smetana arrow colors
- Fix folder width growing with length of alias
- Fix Braille text descent calculation
- Update C4-PlantUML to v2.4.0
- Update awslib to iconset 10.0.0 2021.04.30
- Is something planed that chinese text supports word wraps too
- Description on an returning arrow of repeat is not rendered
- The combination of while, if, note, and break statements does not draw the figure.
- Additional text for elseif missing when using "useVerticalIf"
- Issues with switch in the activity diagram
- Using AWSPuml and code causes Java error
- Can we apply style to map?

## V1.2021.12 (October 5, 2021)

- Add ability to contol placement of a constraint in a timing diagram
- [Activity][Style] Allow full style on diamond (e.g. internal label and external label)

## V1.2021.11 (October 2, 2021)

- timing diagrams: can we get an "offset" for clocks
- Optional signal name for clock signals
- Possible bug in nwdiag
- [Style][State] Allow FontColor style on State
- [Style][Object] Allow style on Object diagram
- Crash in ganttDiagram with style and progress > 100%
- [Style] Allow style on nwdiag Diagram
- Is it possible to color the days in the default Gantt Diagram
- Activity [beta] broken switch/case arrows when using kill/detach
- skinparam shadowing in nwdiag
- Cannot easily customize note on class members
- [Sequence] Improve background color of group with RoundCorner

## V1.2021.10 (August 30, 2021)

- Nwdiag Issue (on other internal networks) with the new layout engine
- nwdiag group description can intersect with ip address
- Allow Shadowing with RoundCorner on sequence reference
- Improve background color of group with RoundCorner
- Broken diagram with nested rectangles and remove @unlinked
- Locale DE showing Month Number not Name
- Task is paused, but this did not subtract allocation
- Differences between PNG and SVG outputs, for circles on JSON or YAML diagram
- "!pragma teoz true" ignores border color of participant activation box
- color of arrow in timing diagram
- Using parenthesis in object diagram field values
- Hyphen in node id causes syntax error
- Allow RoundCorner on sequence reference
- Styling descendents error in WBS diagrams
- Regular expression denial of service using very long and never ending arrow
- Ensure that PlantUML does not crash when EmbeddedDiagram meets wrap_width.
- Switch arrow doesn't get drawn with end in activity diagram
- Plant UML Gantt Diagram: persentage completed determines color of task-bar

## V1.2021.9 (July 25, 2021)

- Encoding error with nested diagrams
- Sequence diagram incoming/outgoing some arrows are inverted
- Udpate of some stdlib (archimate, azure, C4, cloudinsight, kubernetes, logos)
- Management on CLI of -P option
- Adding new Preprocessing Builtin functions (%dec2hex, %hex2dec, %hsl_color)
- On switch-case, horizontal line missing 'case-diamond'

## V1.2021.8 (June 26, 2021)

- Removed JavaScript engine from Math : there might be some regressions. Please tell us if you find any.
- Add an eval function on Preprocessing Builtin functions
- [Activity] Switch/Case - Notes are not working
- Calendar locale (German) for PlantUML gantt diagrams
- Note text has no text alignment skinparam & default alignment is not applied
- using exitPoint stereotype in parallelized state causes plantuml to render a NullPointerException
- Encoding error with nested diagrams
- Expose as a builtin functions a color reverse function
- License output broken
- Feature: Gantt progress
- How prevent PlantUML from creating error images?

## V1.2021.7 (May 23, 2021)

- Plantuml generating invalid link example:
- Bug Report: automatic text color will crash if participant body includes icon
- Crash when using @startnwdiag
- Missing arrowheads in sequence diagram
- An error has occured : java.lang.UnsupportedOperationException
- message to itself on left side?
- [Activity] Layout issue or java error, on end merge, with more than 2 fork
- Getting UnsupportedOperation when adding stop and/or end to case

## V1.2021.6 (May 14, 2021)

- Upgrading C4 library to 2.2.0
- Choose a different theme for rendering your diagrams
- Support SVG Opacity Correctly
- [UseCase] Problem to apply syle class on use case
- [Gantt] Add zoom for daily scale
- [Gantt] Force today's color even if this day is colored after
- Spaces in Markdown syntax in MindMap
- Hide empty descriptions removes inline style in State Diagram

## V1.2021.5 (April 25, 2021)

- [Style] Allow BackgroundColor for all closed days on Gantt diagram
- [Style] Allow FontColor transparent or #00000000 on SVG
- YAML chart parsing issue
- [Style] Regression on document background-color style
- Is it possible to display milestones on same row as tasks that have notes?
- Add in GANTT
- Can you style the days and months of a gantt chart
- [Gantt] Issue with yearly print when project does not begin at beginning of year

## V1.2021.4 (April 4, 2021)

- Adding new "person" keyword
- Color inheritance in wbs
- Add quarterly and yearly print scale to gantt diagram (Thanks to LoÃ¯c PÃ©ron)

## V1.2021.3 (March 22, 2021)

- Matthew Leather has started several very interesting code refactorings. Many thanks for his help!
- Gantt: Minor issues of coloring current week during printscale weekly and closed days
- Gantt milestone bug
- UnsupportedOperationException in while loops
- Simple default value for undefined variables
- UnsupportedOperationException: class net.sourceforge.plantuml.ugraphic.UPixel
- teoz, deactivate not working
- Cannot use symbols at the beginning of keys in YAML
- [WBS] Allow boxless node on all level and not only on leafnode
- Lollipop overlaps with arrows label
- [Inline style] Manage 'line style' (bold, dashed or dotted) and 'text color' for nested element (Deployment)
- The ability to customise the highlight for json/yaml
- C4 and Archimate StdLib update
- Could you allow MaximumWidth on style for note [test on activity]
- Unsupported background colour for YAML parser
- Crash when there is a missing label on timing diagram
- Fix style for simple nested package

## V1.2021.2 (March 7, 2021)

- Add interactive functionality for Usecase diagrams exported to SVG
- Skinparam ArrowColor cannot be combined via multiple stereotypes
- [Inline style] Manage 'line style' (dashed or dotted) and 'text color' for package and usecase (Deployment/Usecase)
- The ability to customise the highlight for json/yaml
- WBS OrgMode notation should support removing the box
- Allow style on WBS boxless node
- 'hide members' break when a note is attached to a member
- Is there a way to style JSON and/or YAML input (i.e. startjson, startyaml)?
- Differences between PNG and SVG outputs, for ArrowLollipopColor on component diagram
- Timing diagram scale fails with certain sequence of times
- Newline in state diagrams is inconsistent
- Broadcast or a Multicast message in a sequence diagram
- YAML Sequence of Mappings doesn't work at top level
- Activation shorthand for sequence diagrams
- Support annotations with members
- style: HorizontalAlignment management also for usecase [Deployment diagram]
- beta-style: is style management local or global? [Deployment diagram vs Mindmap]
- Regression: Line break in state actions ignored

## V1.2021.1 (February 2, 2021)

- SVG in img do not render
- Destroy not displayed with teoz
- Component Regression with version 1.2021.01beta7
- beta-style: HorizontalAlignment management for Component or Deployment diagram
- Indented creole tree treated as seperate trees
- Allow style for collections or database [Deployment-diagram]
- Accept bracket long description form for circle [Deployment-diagram]
- Bug in new YAML parser?
- How to convert {curly brackets} to tikz?
- Object diagram: crash when map refers to object inside a group
- Please allow #transparent to be a synonym of #00000000 [on arrow color of activity-diagram]
- Change Activity Diagram "Stop" and "End" symbols to fill using the diagram background color instead of always using white
- Change link decorators to fill with diagram background color instead of white
- [gantt] thursday are colored in #AAF
- [Bug] Sequence diagram: ascii art output includes html-style tags for messages to self
- YAML Diagrams: accept YAML diagram as sub-diagram or embedded diagram
- Please provide a hexagon shape

## V1.2021.0 (January 10, 2021)

- Color attribute is not working in arithmetic mindmap
- [GANTT] Implement "[day] are colored in #AAAAFF"
- [GANTT] Implement arrow style color
- Add YAML data diagram, same concept as JSON data
- Letters 'i' and 'I' in the comments rendering like 'l'
- Better support for %filename()
- second keyword argument with comma not working
- Using 0% workload on gantt diagram produces an infinite loop
- Smetana doesn't allow [hide] in connections?

## V1.2020.26 (December 21, 2020)

- For some reasons, there is no 1.2020.25 version.
- We fixed a regression about GraphViz diagrams under Windows. Sorry about that!

## V1.2020.24 (December 18, 2020)

- We slightly change the way we generate PNG Metadata .
Contact us if it's not working anymore for you.
- Incubation of hardware block diagram
- Incubation of board diagram
- Scaling of SVG sprites does not work
- variable increased 2 times in diagram (maybe function is called twice during preprocessing)
- Ability to manage several groups on same network in nwdiag
- Ability to add a label to a group in nwdiag
- [nwdiag] grouping does not work properly
- Drawing issue multinetwork diag
- Nwdiag overlapp problem with 3 networks

## V1.2020.23 (December 13, 2020)

- Image with data URI containing SVG does not render
- Sequence diagram: ascii art output includes html-style tags for messages to self
- JSON Diagrams: accept JSON diagram as sub-diagram or embedded diagram
- Table Syntax on Entity Class for ERM

## V1.2020.22 (December 6, 2020)

- Differences between PNG and SVG outputs, for unicode char with size
- Color alpha channel ignored for text in SVG
- Missing Connection in multilane if structure
- Arrow not correct with Json Big Data
- InsideDiamond condition style not showing one of the branch label for activity diagram

## V1.2020.21 (November 30, 2020)

- Easily display your JSON data
- Repeat over multiple swimlanes bugged
- New line in table built with variables broken [from 1.2020.20]
- Allow not significant space or indentation (on the beginning of the lines) on mindmap diagram
- Black package background when transparent used for package and default background (ubuntu)
- wrapWidth wraps punctuation when a font size is set?
- Is there a way to indent text inside a shape?
- styles (css method ) are not applied correctly in usecase diagram

## V1.2020.20 (November 20, 2020)

- user defined style targets in activity diagram (beta)
- Strange stereotypes grouping
- Add support of node colors to WBS for single nodes
- Cypher not working properly
- activity diagram (beta) on error when adding fork or split under a if statement that contains a break
- LifeLineBorderColor stereotype not working
- Allow not significant space or indentation (on the beginning of the lines) on mindmap diagram
- Observations on preprocessing test of boolean expression [V1.2020.19]
- Improve, on activity-diagram, last label position when break on loop [1.2020.19]
- Transparence management with monochrome reverse
- conditionStyle InsideDiamond not work
- New actor style - Hollow
- Gantt, printscale weekly, coloring current week
- "o" sets wrong arrow direction
- How to define background color to sprite in legend?
- How can I hide parts of a robust state in timing-diagram?

## V1.2020.19 (October 12, 2020)

- Official release of PlantUML PicoWebServer
- Arrow description for while loop
- Differences between PNG and SVG outputs, of BackgroundColor with salt on activity diagram
- Uncorrect drawing with Weekly printscale
- Unable to add arrow text description after backward keyword
- Quotes in digraph name causes Syntax Error
- Jdot/Smetana random associations in class diagram
- Add support to Business Use Case
- change color of salt button to represent disabled status
- Association classes does not work with quotes inside the parentheses
- Lollipop notation direction does not change when parties are re-positioned

## V1.2020.18 (September 30, 2020)

- Gantt chart bug: weird interaction with notes, tasks and separators
- 'note right' doesn't always work on Activity (beta) when using swimlanes
- An html-tag for code
- Gantt chart: allow closed days to be coloured
- Embed sub diagrams (of all type, especially Mindmap or WBS) in (all type of) diagram
- You can no longer nest partitions from Version 2.13.11
- scale not honoured in Gantt chart
- beta-style: LineStyle and LineThickness management for all elements of Deployment diagram
- misintepretation of tooltip as operation
- Allow Creole list on Component, Deployment, Use-Case and Creole sub-item on Class or Object [V1.2020.16]
- Order mismatch with embedded diagram and Creole line [on deployment-diagram]
- Allow Creole horizontal lines on Object and strong horizontal lines on Activity, MindMap, Title or Legend
- Arrow should point along diagonal line as well
- Can't use repeat with swimlanes
- Missing tokens from -language option

## V1.2020.17 (September 19, 2020)

- Rendering errors when nesting multiple repeat-while blocks
- Order mismatch between Note and rectangle with embedded salt
- Could we have an Error report on one line (report any syntax error on one line)?
- Line numbers of error messages in the sequence diagram are different.
- Invalid activity diagram failing with internal exception
- Observations on Common commands (title, header, footer, caption or legend) on all diagrams
- Package with only legend shows up empty

## V1.2020.16 (August 23, 2020)

- Nwdiag: issue with multi-connected networks
- ids generated by plantuml are not xml compliant
- Path id in generated SVG
- Dotted arrow is also the close of comment blocks (HTML, XML, Markdown)
- Change task default color (You can use styles to retrieve old colors)
- Gantt diagram: tasks on the same line
- Gantt diagram: pause tasks
- Gantt Diagram: add memos or explanations to tasks
- Add style in GANTT
- How to change color (or thickness, or style) of arrows, in gantt diagram?
- Could be possible to define simply Task between two Milestones?

## V1.2020.15 (June 28, 2020)

- Shape issue on stack element (Deployement diagram)
- Using hide stereotype overrides database stereotype customisation
- Quote is visible in class name when using hide circle

## V1.2020.14 (June 20, 2020)

- Does V1.2020.13 work with the PDF dependencies zip file?
- Bug Fix: When port with added node in the cluster crashes PlantUML
- Cluster Empty node is not properly located when thereALinkFromOrToGroup2 is enabled
- beta-style: Backgroundcolor doesn't work with mix of group components and sub-diagram
- packageStyle doesn't seem to always work
- Automatic underlined name in Object Diagrams
- Timing diagram crash with constraint in binary
- New CSS styling is not recognized in class diagrams

## V1.2020.13 (June 13, 2020)

- beta-style: LineStyle and LineThickness management for Component or Deployment diagram
- Bibliotekon.getNodeUid throws IllegalStateException
- mind map diagrams BackGroundColor transparent is failing with NullPointerException
- Is it possible to hide the component icon ?
- Shadowing issues with (rounded) empty group with transparent BackgroundColor
- beta-style: How to disable shadowing?
- Sequence Diagrams: Anchros and Durations with Incoming/Outgoing Messages
- beta-style: Cropped output images when we use beta-style functionality

## V1.2020.12 (June 6, 2020)

- Some improvement in transparent support for beta style
- Gantt: Dependency arrows are drawn incorrectly when using weekscale
- Remove whitespace
- Math/LaTex resolution/dpi
- Full opacity (alpha compositing) support (for SVG and PNG)
- Multi-line message: comment handling changed

## V1.2020.11 (May 30, 2020)

- How to deploy PlantUML safely.
- Backgroundcolor transparent doesn't work for empty group
- mind map diagrams BackGroundColor transparent is failing with NullPointerException
- Timing diagram using time & scale cuts off times
- Group components can't be set transparent
- PNG export to 300 dpi no longer works correctly?
- Sate deep history first implementation

## V1.2020.10 (May 17, 2020)

- Print between remove resources on Gantt chart
- Could you add Unicode and/or entities management on link's tooltip?
- Preprocessor line merging break ditaa diagrams with sloped edge at line end
- Ball-and-socket connection does not orient correctly for .eps output
- Introduce padding setting

## V1.2020.9 (May 10, 2020)

- Do not statically initialize ImportedFiles
- Backgroundcolor transparent doesn't work for only some element
- Few improvements on padding
- mixed signal timing diagram
- No text spacing with fork - Activity Diagram
- Creole trees do not respect indent levels in a component diagram
- Applying style to multiline node in mindmap diagram
- Please allow to set notes skimparams by stereotypes in all notes
- latex command requires space
- Lines without arrows

## V1.2020.8 (April 26, 2020)

- Backgroundcolor transparent doesn't work anymore
- Background color partial transparency/opacity support
- Lines without arrows
- backward for while: confusing arrow layout on continuation
- nwdiag ignores on "title" keyword in plantuml.1.2020.7
- Gantt: Add support for #color
- is there a "compact" timing diagram?
- backward for while: confusing arrow layout on continuation

## V1.2020.7 (April 19, 2020)

- ifelse and swimlanes seems to break logic
- json structures inside a function
- Multiple Function calls in Text: only one processed
- Deployment Diagram: Creole does not work on 'card'
- Class HeaderBackgroundColor doesn't work when RoundCorner is defined
- "Ghost links" between diagrams
- Add Elastic Icon Set
- Update awslib to release 6.0
- Full support for Creole in legend
- backward for while / endwhile

## V1.2020.6 (April 5, 2020)

- Support for map-like objects (still in progress)
- Cannot change separator on backward items
- Javascript hyperlinks in SVG
- IllegalArgumentException: height=0.0
- Remove unlinked components
- How to make it render less "scrambled"

## V1.2020.5 (March 19, 2020)

- Anchors and Duration with groups: Do not work (sequence diagram)

## V1.2020.4 (March 19, 2020)

- Rollback to regular license.

## V1.2020.3 (March 17, 2020)

- Updated software license to Coronavirus license. Please apply social distancing
- Deployment Diagram Regression: If name ends with "."
- [Sequence] QueueBorderColor not respected
- Please provide macros to insert the current page number and total number of pages
- GANTT printscale weekly
- How to create a Creole table without a bolded first row?
- Issues with diagrams within diagrams
- State labels overlap with participants' names
- Enable "RoundCorner" and "DiagonalCorner" for Participant Stereotypes on Sequence Diagrams

## V1.2020.2 (March 1, 2020)

- Highlighted periods in timing diagrams
- Gantt: Hyperlinks
- Minor fix for Gantt language
- While loop in preprocessor
- Bug fix for missing anchor
- Includesub regression fix
- Sequence diagram incoming/outgoing half headed arrows are inverted

## V1.2020.1 (February 16, 2020)

- GANTT Year incorrect for December
- Change gantt scale for long projects
- interface does not work when allow_mixing
- Font Style not working on title
- https://forum.plantuml.net/10761/latex-export-limitations
- Repeat: Plus Colour
- Encountering java.lang.IllegalArgumentException

## V1.2020.0 (January 12, 2020)

- PreprocessorV2: multiline function invocation
- Sequence diagram: shortcut act/deact does not work with incoming/outgoing messages
- Simple text element
- Creole in sequence diagram participants
- Sequence diagram bug, missing polygon (outer box of object) with handwritten, create and SVG
- Exception when using !includesub
- Cannot add preprocessing variables from commandline any more
- Vertical IF composition bug
- Please allow adding edges to class members and methods with complex names

## V1.2019.13 (December 10, 2019)

- Class diagrams: Method to method arrow sometimes points to the wrong method
- How can I customize the actor icon in SVG output
- Is there a supported way to specify fall back fonts
- Can an img be supported as a thumbnail, linked to the original?
- Formatting when forking over colored swimlanes
- link does not get parsed in plantuml.1.2019.12
- Can I reference a png from the include path

## V1.2019.12 (November 3, 2019)

- Fix coloring regression
- Style rendering in mindmaps broken
- Kubernetes-icons included in PlantUML Standard Library
- plantuml_version no longer working, starting with version 1.2019.6
- Tilde character cannot be escaped
- cannot remove shadow in sequence diagrams for all kind of participants
- Part time workers in gantt diagrams (individual holidays)
- preserveAspectRatio is not configurable
- CSS over two lines
- Error if not at least a newline in class, namespace, package

## V1.2019.11 (September 22, 2019)

- Is it possible to combine the icons with text formats
- Don't require dot for shapeless diagrams and svg output
- Extend mindmap syntax to allow multiline nodes
- Cannot combine "skinparam wrapWidth" with icons
- Sequence Diagrams with Diagrams In Note And Functions
- text of relations between "container rectangles" are not correct formatted
- UnsupportedOperationException: plantuml.creole.AtomImg
- Preprocessor: function %substr 2nd parameter only takes the first value of the formula as parameter

## V1.2019.10 (September 14, 2019)

- New preprocessor: returning elements from functions
- Teoz: note issue
- Assigning color to connectors
- New activity diagram syntax error when using openicon
- UnsupportedOperationException: AtomWithMargin
- Activity-beta: Background color is ignored in case of more than one note
- split fork if swimlane Bug
- Text before and after functions is discarded by the v2 preprocessor
- Namespace label formating
- Style-BETA: user defined style not working for mindmaps

## V1.2019.9 (August 26, 2019)

- Macros in macro parameters does not work
- Skinparam not working on Activity embedded into partition
- Bug + fix: white spaces in preprocessor macros
- Component Diagrams: please add link direction/type token into the id of the corresponding SVG path
- Max size for notes
- Splicing Up Notes
- include file in tooltip
- Exception occurred rendering
- Teoz renderer does not support "mainframe" keyword
- Template parameter boxes rendered with no lines in eps
- More compact specification of nested namespaces
- Background color is ignored in case of more than one note
- Pipemap for diagrams containing no links give non-zero exit code

## V1.2019.8 (July 13, 2019)

- Alpha testing of new Style feature
- backgroundColor of swimlane title
- Split/While Bug - with a couple of workarounds
- skinparam monochrome does not get inherited within the embedded diagram
- No text alignment skinparam for labels in state diagram
- Is it possible to add an hyperlink to an image
- "hide empty description" in state diagram breaks sequence diagram
- Changed behaviour from Vers. 2019.5 to Vers. 2019.6
- Teoz group header overlaps note
- Adding [dashed] style fails diagram generation
- New Activity diagrams don't support function calls in else branch
- Include PlantUML version numer in testdot output
- Java error occurs when sequence diagram message has both note and duration

## V1.2019.7 (June 24, 2019)

- Sequence diagram: Note over all
- Is it possible to add an hyperlink to an image
- Bad arrow routing in sequence diagram with swimlanes
- skinparam monochrome does not get inherited within the embedded diagram
- Split/While Bug - with a couple of workarounds
- backgroundColor of swimlane title
- Legend comes on top of title when having large header
- Arrow inversion with skinparam linetype ortho and missing arrow part
- "hide empty description" in state diagram breaks sequence diagram
- No text alignment skinparam for labels in state diagram

## V1.2019.6 (May 24, 2019)

- Syntax error with includesub with comments since 2018.11
- Arrow inversion with skinparam linetype ortho and missing arrow part
- Style Chopped-off Corners for Archimate
- Archimate - using a Node for Technology: Device
- How can I style Archimate elements individually using skinparams
- Stereotype note over multiple participants is crashing
- Decision node in loop
- Crash when processing activity diagram
- sequenceArrowThickness does not work with teoz
- Activity diagram: ELSE arrow for a "switch-like" breaks sometimes

## V1.2019.5 (April 20, 2019)

- Lifeline starts above created object; should not be visible
- why queue "a" notation fails?
- color of activations/lifelines are same when they are on same row
- teoz + create + note issue
- Embedding in interface note fails
- Please allow to hide clases by stereotype using the "hide" keyword
- activity diagram - swim lane -> whitespace issue
- Syntax error with includesub with comments since 2018.11
- Interface consumption socket
- namespaceSeparator = none breaks class association

## V1.2019.4 (March 31, 2019)

- Two or more break statement does not work correctly
- Customize Stereotype display
- Improved legend support

## V1.2019.3 (March 10, 2019)

- Please provide skinparam shadowing false for all elements individually
- UnsupportedOperationException at latex output and interfaces
- teoz crash with arrow to self
- Is combination of break and detach statement supported

## V1.2019.2 (March 1, 2019)

- Not able to use partition inside repeat
- skinparam handwritten true is not inherited within embedded diagram
- Teoz wrong note position after array
- Why no gradient support for sequence diagram boxes
- Colored return lines in Sequence Diagrams
- Dependency between packages containing classes
- Scaling of the sprites or images
- Notes on fields when some fields have visibility modifiers causes an exception
- Links not working

## V1.2019.1 (February 9, 2019)

- Box title syntax error
- defaultTextAlignment too mighty
- the autonumber variable is displayed incorrectly if the note is assigned between two participants
- Improved legend support
- Inconsistent placements of legend and title across diagram types
- Elseif SkinParam doesn't seem to use the ActivityDiamond

## V1.2019.0 (January 13, 2019)

- Footer text on sequence diagrams appears over sequences
- WrapWidth causes bullet and number lists to behave inconsistently
- note right breaks split in Activity-beta
- Color of sprite not working with archimate and sprite from zip file
- Change color of sprite
- Max size for long state names
- gui not working on Windows
- Class diagram skinparam not applied for enum, interface, or abstract

## V1.2018.14 (December 21, 2018)

- Use scrollbar in Salt
- Gantt chart - Add "open day" feature
- New -stdrpt flag
- skinparam ResponseMessageBelowArrow interacts badly with participant lifetimes
- Artificat in activity diagram
- Activity: Hidding arrow entering a split does not work
- Activity: Arrow color before a start is assigned to the wrong arrow
- Use of ## in !define macro stops macro replacement
- Cutting off component diagram interfaces
- Interaction frame
- Align text on arrows of sequence digrams
- note right breaks split in Activity-beta
- skinparam defaultTextAlignment center does not work on elseif boxes
- Hide the Activities in Activity diagram
- Bug on class diagram relations with an "Header" class

## V1.2018.13 (November 26, 2018)

- Support for Network Diagrams
- UnsupportedOperationException in gantt
- Add option to hide alias on folder top part
- report when no diagram found in source
- svgLinkTarget not working
- FontColor for Timing diagrams
- Skinparam RoundCorners breaks when setting individual background on elements with stereotype
- Skinparam from command line breaks salt diagrams
- How to conditionally connect components
- Skinparam rectangle not working in Activity beta
- Max size for long state names
- Detach in split drawing wrong lines
- autonumber problem with note right of
- Teoz wrong note position after array
- hide footbox not recognized in timing diagrams
- Align text on arrows of sequence digrams
- interaction frame
- Option to throw ErrorUml

## V1.2018.12 (October 21, 2018)

- Regression in component diagram layout
- Gradient background colors respond to scale twice
- Sprites are not interpreted in hyperlink display text
- Encoding seems to be lost after export to PNG and extract back
- Version 1.2018.11 doesn't work with comments in config file
- Version 1.2018.11 cannot !include with pipe
- Adding diamond keyword in class diagram
- Use !include from within a Macro
- Why don't sprites scale properly
- Use long description with archimate elements
- Issue when changing skinparam defaultTextAlignment from center to right
- Support visibility on compositions and aggregations
- Text alignment skinparam for rnote and hnote
- Relative !include path resolution in Eclipse preview broken

## V1.2018.11 (September 22, 2018)

- Set Background Color of Latex Math Entries
- skinparam packageShadowing not working for class-diagrams
- Allow turn on/off shadowing for elements with stereotypes
- class Method cannot be hidden
- Max size for notes
- Labels overlapping in component diagrams
- svglinktarget param set by FileFormatOption is overridden
- Tabulation character doesn't work in legend
- Teoz: Nesting a group causes parent group to expand all the way left
- Teoz: Autonumbering is not applied for messages to left or right of flow
- Includes from Classpath or local Zip-file
- It is still would be useful to style partitions in activity-beta diagrams with skinparam
- Elseif SkinParam doesn't seem to use the ActivityDiamond
- Improve text on arrows in activity diagram
- partition are not compacted if distributed over multiple swinlane
- Formatting state actions sometimes doesn't work

## V1.2018.10 (August 26, 2018)

- Weird stereotype sprite alignment in rectangle and database containers
- Elseif SkinParam doesn't seem to use the ActivityDiamond
- Style partitions in activity-beta diagrams with skinparam
- Includes from Classpath or local Zip-file
- Autonumbering is not applied for messages to left or right of flow
- Nesting a group causes parent group to expand all the way left
- PlantUML stdlib upgrade
- Tabulation character doesn't work in legend
- Labels overlapping in component diagrams

## V1.2018.9 (July 27, 2018)

- SVG in mathexpressions without style information
- Weird stereotype sprite alignment in rectangle and database containers
- just a note over an activated lifeline does not work
- How do you add a link to multiline component
- Is it possible to run only the preprocessor
- Is it possible to wrap swimlane headings automatically
- Is it possibly to automatically wrap text in swimlane boxes
- Documentation skinparameters
- Version 1.2018.07 DPI handling
- Milestones at fixed events
- tasks ends on a date
- Missing title in the ASCII art of a sequence diagram
- sequenceMessageAlign direction does not center for arrow in two directions
- Note text has no text alignment skinparam and default alignment is not applied

## V1.2018.8 (June 24, 2018)

- Crash with teoz
- Devicons and Font Awesome library
- How to use BoxPadding with Teoz
- DPI handling
- Please provide skinparam shadowing false for all elements individually
- Stereotyped multi-line notes on messages
- Gantt chart colorize time sections
- Problem with txt / utxt (ASCII-art) output for standard commands

## V1.2018.7 (June 11, 2018)

- New release of PlantUML Standard Library
- Null pointer exception, possible erroneous output from newpage
- Usage of Clipboard as hidden I/O pipe
- directory selection is broken preventing new target directory from being specified
- Support Allman brace style
- Backgroundcolor in math block
- text rendered in math is not scaled by scale command
- Formatting options inside startmath
- Skinparam and hidden Stereotypes
- Table vertical character can't be escaped
- Timing Diagram: allow negative time values
- Don't take focus away from current window if ui is not needed
- Teoz doesn't work in a "group" or "alt".
- teoz box around participants
- teoz and parallel within groups is not working
- Office Icons for PlantUML
- Cloudinsight PlantUML sprites

## V1.2018.6 (May 21, 2018)

- Improved support for GraphViz on MacOS
- Fix newpage crash
- Improve jar start up time

## V1.2018.5 (May 5, 2018)

- Order of states in timing diagram
- Activity beta: arrow is longer in partition

## V1.2018.4 (May 1, 2018)

- EntityFont skinparams don't appear to work in sequence diagram
- Rendering error on component diagram require/provide interface connection
- With ParticipantPadding, Create Message arrow is on wrong position.
- How do you color a partition in new Activity syntax
- Component diagram crashes when changing from component to interface
- Note breaks the component diagram if 0-dashed-0 arrow is used
- miss an actual skinparameter from the -language list

## V1.2018.3 (April 5, 2018)

- Diagonal Corner
- Cards and rectangles have the same formatting
- EPS output does not support dashed states
- Support for multiple label arrows in use case diagram
- Tool tip doesn't work on down arrow
- An error has occurred: java.lang.NullPointerException
- Fix Timing diagram case when introducing constraint that lies before
- New flag -checkmetadata in the command line
- New Gantt diagram features.

## V1.2018.2 (March 9, 2018)

- Max size for notes
- Hide/Remove feature
- How do I change the spot letter by stereotype
- In State diagrams, Concurrent color customization not honored
- single detach circle after ELSE as STOP symbol
- A way to disable style, width and heigth attributes in SVG
- Break in while loop renders incorrectly
- Empty title results in java.lang.illegalArgumentException
- How can I hide members in ASCII art class diagram
- Set LegendBorderThickness to 0
- componentBorderColor does not work for all notations
- autonumber variable in sequence diagram
- Defining two folder entities with the same name generate a java.lang.IllegalArgumentException

## V1.2018.1 (January 28, 2018)

- Prefix inlined dependencies
- can i do round corners of elements in component diagrams
- change participant order in sequence diagram
- Simplier way to deactivate lifeline without return message
- Shadowing false doesn't work with all elements
- Sequence Diagram Skinparam for Collections BorderColor is wrongly using ParticipantBorderColor setting.

## V1.2018.0 (January 4, 2018)

- Fix image rendering in Gitlab
- Improved Sphinx integration
- The -D option of command line does't work when -pipe option is used
- Dashed Border on Single Rectangle
- definelong requires extra { charater
- Comments are interpreted as code in macro
- Adding componentBorderThickness
- Timing Diagram: Feature request for adding notes

## V1.2017.20 (December 11, 2017)

- Integration of Google Material Icons (Thanks to Anthony Gaudino)
- Block comment before code gives syntax error
- Image transparency
- how to best use the new icon features
- syntax breaking in component diagram
- Dashed Border on Single Rectangle
- How do I change the border style of a rectangle
- Bugs of generating image map with pipe
- OpenIconic icons dont work inside labeled hyperlinks in sequence diagrams
- access to filename
- skinparam PartitionBorderColor does not work

## V1.2017.19 (November 12, 2017)

- Integration of Icon-Font Sprites icons
- Add "Zoom width" option
- Performance problem
- Add special char in LaTex-Export
- Page numbers
- Add support for "multiple instances" display in all diagram
- Alias of interfaces in component diagrams
- Ability to include blocks from other file without using startuml
- File encoding of LaTeX export
- Cannot recognize included file in config file
- How do I change the border style of a rectangle
- Whether is it possible to set SequenceBoxBackgroundColor = transparent
- Config file doesn't include another config file using command line
- abstract and static not handled in class diagram for latex output
- Special characters not handled in latex output
- Dashed line is not generated for latex output

## V1.2017.18 (October 7, 2017)

- title, note and legend are not supported in timing diagrams
- Wrong class widths after LaTeX export
- Acivity diagramm - loop without closing decider
- Exceptions during export with color gradients
- Missing background color of databases after LaTeX export
- Create PDF generates Error
- Beautiful C in classes after LaTeX export
- Multiple stereotypes on one component
- allow_mixing not working for rectangle inside rectangle
- How to style the lollipop color
- Issue in OpenJDK
- txt, tutxt does not handle multi-byte string
- Integrate AWS-PlantUML into PlantUML

## V1.2017.16 (September 3, 2017)

- Older way to show generics in a class
- Colored lines change order when returned from swimlane A to swimlane B

## V1.2017.15 (July 3, 2017)

- Timing Diagram bugs
- specifying default values in macro result in failure
- Support for generics/templates
- hide empty members bug
- Class attribute font size issue with SVG output
- Archimate 3 Specifications
- Hide sterotype on sequence diagram

## V1.2017.14 (June 5, 2017)

- computeurl does not work with pipe
- Unbalanced Padding on SVG with out shadowing
- preprocessor condition, based on the current plantuml.jar version
- Are collections supported in teoz
- Different -right- interface generation
- Can multiline links be properly supported
- Line number in Error message not correct
- Component diagram invalid text positions
- hide unlinked results in error for the following code
- Border thickness
- Incorrect error line number when config file used

## V1.2017.13 (May 10, 2017)

- Styling failing on conditional blocks
- entity description fails in deployment beta
- where is the rest text of the note
- Queue display bug
- note goes out the partition
- floating notes on their own in swimlanes
- Bug in drawing interface connection to left or right
- Center text in activity diagram
- Layout problems in TEOZ engine: DIVIDER and NOTE OVER

## V1.2017.12 (April 26, 2017)

- output file naming bug if more than 1 diagram in a single input file
- class Diagram : hide private
- would like to represent queues and topics
- timing diagram enhancements
- Can a defined constant be parsed correctly after backslash n
- id in svg output

## V2017.11 (April 19, 2017)

- Skinparam for the background color of the actionDiamond
- timing diagram with -tsvg output
- plantuml.jar 2017.10 appears to be broken

## V2017.10 (April 6, 2017)

- Splitted diagrams are not correctly named

## V2017.09 (April 5, 2017)

- Support for sprites salt
- how to refer to methods with parameters / return values
- Activity: Add action on the return arrow of a repeat
- How to start generating picture with pipe mode
- Groupbox in salt
- Repeat loop starting with action instead of condition
- page (hpages)x(vpages) and multiple diagrams in source file
- Include block from current file
- Is it possible to add metadata to SVG file like it is done for PNG files
- Does PlantUML expose Graphviz ratio setting
- Timing diagram problems with very large values
- Change of text alignment during recent updates
- Initial stat and 1st time state
- make as work consistent
- error message if same name is used for different objects
- latex rendering fails when escaped characters are used
- Latex formulas don't scale
- How to draw the lollipop socket symbol in a class diagram
- box color gets hidden by the goup definition

## V2017.08 (March 21, 2017)

- latex rendering - transparent background instead of white background
- How to start generating picture with pipe mode
- Scaling of the sprites or images
- How to draw the lollipop socket symbol in a class diagram
- Hyperlink and tooltip for namespace and package
- Split and Lanes not working together
- Note for Java developers: in SourceStringReader class, methods generateDiagramDescription have been renamed to generateImage

## V8059 (March 15, 2017)

- Why UML Frame are now in blank and don't have the color under
- Notes can not be added beside a grouping message
- Include file(s) or path via command line
- Pop-Up box with FileNotFoundException when including directory

## V8058 (March 12, 2017)

- how to get the nth generated image at server
- Ability to define hyperlink on diagram elements
- Adding +/- button on GUI
- Proposal for fixing some layout deficiences
- Connector unexpectedly changes diagram type
- Unnamed state in timing diagram
- Lifeline is not drawn on the new page, but only the shadow with SVG output
- Grouping messages should be on top level
- Notes can not be added beside a grouping message

## V8057 (March 9, 2017)

- Automatic line breaks for long lines
- Two colors for an arrow line color (class diagram) crashes PlantUML
- How to get some space beween participants
- Dates in Gantt diagrams
- storage object parsed with tikz as rectangle

## V8056 (February 24, 2017)

- Timing Diagram enhancement (beta)
- SVG hover style to tell apart arrows in a large component diagram
- file extension when using @startuml filename
- Empty while condition doesn't work
- Activity diag not generated
- Connection between fields in classes without descriptions not working

## V8055 (February 15, 2017)

- SVG monospace output has wrong font-family
- As for actor do not work in class diagram
- Note in XMI output becomes a class
- Extends do not work with non empty rectangle
- Timing Diagram (beta)

## V8054 (February 1, 2017)

- How do I style Use Cases
- skinparam shadowing false for all
- Sequence Participant Color Missing
- Language definition
- joinspec for join nodes
- Border thickness
- Information Engineering (IE) data modelling notation support

## V8053 (January 20, 2017)

- Better XMI support
- Border thickness
- Reverse colors

## V8052 (December 21, 2016)

- Generate code from plant UML
- Round corners in component diagram
- Is the latex equation supported
- add possibility to show not navigable
- How to use the PHP namespace separator with an association
- Attaching links to class members and methods with complex names
- How can I unbold part of class name
- Miss formed arrows in class diagram

## V8051 (December 14, 2016)

- Place notes next to the boundary of partition in Activity Diagram
- Any support for math/equation rendering in Activity-Beta
- Equal width swimlanes in activity diagram
- Preprocessor enhancement
- separator in element delaration
- ifdef A or B

## V8050 (November 30, 2016)

- Activity beta: default arrow direction with one-branch if
- Activity diagrams - Bug on arrow position with note
- Can the hotspot areas of tooltips be controlled
- ASCII ART / Unicode Art : Delay not supported
- Activity-Beta: Stack Overflow when Lane + Partition + Repeat
- Scaling does not work for latex output
- Hyperlink interferes with visibility

## V8049 (November 16, 2016)

- Page splitting with overlap
- Expand environnement variable in constants
- Border thickness
- Hide fields of objects
- Problem with making two links
- IS there a possiblity to align the text over the arrow for example to be aligned centered
- Skinparam for boundary, control, database, and entity in sequence diagram
- Sprite as internal (in-jar resource) images

## V8048 (November 3, 2016)

- Different colors on if and elseif
- Activity beta --- Any way to put a text on arrow going to elseif node
- An error has occured while creating diagram with ports and separators
- Lifelines broken for txt seq diagrams when create is used
- Skinparam LegendBorderThickness is missing
- Skinparam NoteBorderThickness seems not to work
- Link with association class and note ignores the note
- setting ad hoc gradient backgrounds in activity
- StereotypeABackgroundColor vs. Stereotype@BackgroundColor
- Skinparam minClassWidth not part of java -jar plantuml.jar -language
- Empty package ignores its stereotype
- Skinparam svgLinkTarget not working for API
- vector output formats: openiconic icons leak onto adjacent pages
- Rendering of several stereotypes is different for classes and objects
- Classes with individual spot hide their stereotypes
- add possibility to show not navigable

## V8047 (September 28, 2016)

- Translate Class Diagram to Braille
- 0 byte PNG generated when a while is nested in a repeat inside a swimlane
- Nodes name in svg file or more verbose debug
- Activity beta: text of condition optionally outside the symbol
- Label on upward edge in while loop

## V8046 (September 23, 2016)

- Salt fails when there is an empty line between @startuml and salt keywords
- Marking class diagram if is public, private, or protected
- Problem with a while inside a fork
- Apply skinparam defaultTextAlignment to other items
- Need a way to color and number different routes on an activity diagram

## V8045

- Set background color for one note
- Database modeling
- Does PlantUML support references between class/component members
- Ability to hide packages
- Tooltip issue on sequence diagram
- Param to center text in activity
- Why do strange symbols appear on an eps printout, but not on the screen
- Package style erase Partition style
- Notes on conditionnal elements

## V8043

- Arrow's thickness in sequence diagrams and skins
- Arrow marker`s background color is incorrect in v. 8042
- Leak in TranscoderUtil

## V8042

- newpage makes the actors go vertical
- Need a way to color and number different routes on an activity diagram
- Set colour of font to hide text in Sequence Diagram
- StackOverflowError
- Syntax error causes 10x slower syntax checking and generation of image
- JDK 1.6.0.45 java.lang.IllegalArgumentException: Illegal pattern character u
- Restore the method OptionFlags.setDotExecutable

## V8041

- How to move a node to left

## V8040

- detach after if statement in activity diagram
- Alias for links in sequence diagrams
- Add custom label for bracket syntax
- Formatting of repeat loops spread trough several swimlanes
- select !include block based on a "identifier" instead of its number

## V8039

- How to move a node to left

## V8038

- Scaling does not work correctly when non-default fonts are used
- Sometimes Missing Response-Headers for broken PNG Images
- From Plant Uml to a structured object
- Would it be possible to provide more information in the error stream
- Error java.lang.StackOverflowError
- New shapes for entrypoints and exitpoints

## V8037

- How do I hide all classes having a given stereotype
- Repeat followed by detach
- Is there a "plain" style
- stereotype is not displayed when component has nested one
- Stereotype Fontcolor
- Graphviz strict mode not supported
- request on sequence participant individual border color
- Swimlanes not showing in SVG
- Crash of the PlantUML
- Multiple stereotypes on one component

## V8036

- If you comment out swimlane lines the drawing is correct.
- How can I limit the column width of ascii-art sequence drawings.
- Please support PHP namespace separator
- Is the PNG output size limited to 4096 pixels only
- Error generating uml when same file included in two different uml diagram
- Image link not working anymore
- Is it possible to only use straight lines in a class diagram
- Can I not put the title at the bottom in a diagram
- how to change background color in a table
- Double quote in a event

## V8035

- Package composition regression
- Double quote in a event
- how to change background color in a table
- Is it possible to only use straight lines in a class diagram

## V8034

- Keep same pan position after rerendering
- Vertical blocks can't be right aligned (e.g. for stereotype and title of a component)
- No stereotype on empty components
- Is it possible to draw if/elseif/else structure vertically
- java.lang.ClassCastException bug
- Note on grouping component
- It is still would be useful to style partitions in activity-diagram-beta diagrams with skinparam
- Association Node breaks link direction
- Multi-line tooltip on note/hnote of sequence diagram
- newpage don't keep params
- How to style package titles

## V8033

- Clipping in Activity Diagram
- skinparam for swimlanes
- How do I add link notes in sub states
- How to set font color inside controling elements in activity2 diagrams
- json content tooltip on sequence diagram
- An error has occured java.lang.NullPointerException

## V8032

- Sequence: note right rendering issue after activate
- stereotypes for notes to be used when defining note's skinparam
- The deprecated BlueModern skin cannot be replicated exactly using skinparam directives
- Concurrent state nesting limit
- Overlapping into Activity Diagram between a big note and an arrow
- Make multi-line comment delimiters work on a single line
- Compilation Network Issue
- Can a block quote begin and end on the same line
- multi-line tooltip

## V8031

- Embedding images (bitmap or svg) in diagrams
- Stereotype not show with uml2 component style
- Change tab spacing to 2
- Adding Pages between Objects
- alias of folder is drawn in top part
- How to acces to different blocks in a included file

## V8030

- How do you change the font used for monospaced-style text
- Arrow Color, "While" inside partition and if
- Macro expansion goes wrong depending on argument content
- HTML code for use cases to show that sub-use-cases are available
- Class diagram: Crash when specifying visibility on a method/attribute and attaching a note to it
- auto scaling based on declared max-size

## V8029

- startUML capitalization causes crash
- Is the number of nesting levels in activity diagrams limitated

## V8027

- How to change font color of a composite state
- hide empty members no longer working
- Implement shortcuts for Previous, Copy, Next and Zoom fit
- java.lang.IllegalStateException for @startdot without installed Graphiz
- activity-diagram-beta : Condition of RepeatWhile multi-lines
- How can I escape the HTML img tag

## V8026

- Flow final activity
- Bug on API for included files
- Distribute jars with allowed debugging
- supporting comments inside a skinparam section
- URLs are not shown when mixed with text in component captions
- SVG background is not set according to SkinParam
- Decreasing visibility of links
- Error generating uml when same file included in two different uml diagram

## V8023

- Detach not working with nested splits
- Swimlines disappear in multi-page diagrams with ellipsis
- Stereotyping does not work for composite states
- inconsistent units pt and px in generated SVG image
- IllegalArgumentException when note's name is already known in a package diagram
- Can PlantUML produce diagram in 'hand drawn' style?

## V8021

- SyntaxChecker produces IndexOutOfBoundsException
- Placement of sprites wrong with "newpage" for vector formats
- Grouping inheritance arrow ends
- Sequence diagram: "cross arrow style" ignored for message to itself
- Dashed arrows to Sequence Diagram edges cannot be colored
- Add norank option on links
- Component diagram arrow color bug

## V8020

- activity-diagram-beta Diagram: long text on arrow after elseif
- Activity : while within fork doesn't work
- Is there a way to disaply summary table (right side) in Sequence diagram
- Activity Beta - labelling an arrow that enters a partition, label is never shown
- Activity Beta - labelling an arrow before an end split - label is shown on the recombined arrow
- support \l and \r in additon to \n
- Bug : Arrow with "elseif" in activity-diagram-beta diagram
- Incorrect rnote layout

## V8019

- Note for while
- Left-aligning transition text in state diagrams
- Class diagram / Package border thickness
- Activity : while within fork doesn't work
- First release of Teoz layout engine

## V8018

- sequence delays break double-activated lifelines
- Represent if/then or while loop over swimlanes to show a document review process
- loop bottom border encloses trailing deactivate
- Activity Beta: Arraw text and color problems
- Represent if/then or while loop over swimlanes to show a document review process
- Activity Beta: drawing improvements

## V8016

- Decreasing visibility of links
- Activity Diagram: More then one stop states
- Stereotyping does not work for activityShape
- Sequence Chart: diagram doesn't scale with long text in 'else' of a group message

## V8015

- Web links in generated images

## V8013

- New !includeurl feature in preprocessing.
- Sub package / namespace conflicts
- Detach not working with nested splits in sequence diagrams

## V8011

- Activity: fork within repeat and while loop doesn't work

## V8010

- Solid Life Line in Sequence Diagrams
- Activity Beta: how to set default font color?

## V8009

- Name of Class does not fit in the box
- URL in name of link not working in class diagram

## V8008

- Rendering bug solved
- Define a multi line macro

## V8007

- Fix the broken eclipse plugin

## V8005

- Substituting variable using !define
- EPS output format with Salt
- Incorrect propagation of defined variables
- How-to get visible double double quotes

## V8004

- PlantUML jars in Maven repositories don't contain OpenIconic SVGs
- Increasing visibility of links
- Partitions (group of actions) in Activity Diagram Beta
- Unexpected Error when using Stereotype with Activity (Beta)
- Pre-alpha goto implementation.

## V8003

- Line separator for generic types
- Is multiple inheritance or implementation possible?
- alt does not work -tlatex, with IllegalArgumentException
- Names of nested nodes with stereotype
- why there's an error when using both 'extends' and 'implements' statements in the same class

## V7998

- OpenIconic integration
- Border thickness

## V7997

- New <space:30> feature, still undocumented
- Beta Latex support

## V7996

- associating class in two different naemspace
- Left-hand tab exceeds boundaries
- New Zoom fit feature

## V7995

- How to specify incomplete specification
- Tree Table in Salt
- hide stereotype in component diagrams
- Creole support
- ## macro
- pause/unpause
- Allowing hide footbox in class diagram

## V7994

- New options in table for Salt .
