---
title: Security — PlantUML Official Documentation
source: https://plantuml.com/security
description: Official documentation for PlantUML Security
---

# Deploy PlantUML safely

PlantUML News and information Security Â Â Â Â

## Choose your Security Profile

- Setting the OS environnement variable PLANTUML_SECURITY_PROFILE
- Setting the Java environnement variable PLANTUML_SECURITY_PROFILE
```
set PLANTUML_SECURITY_PROFILE=INTERNET
```
```
setenv PLANTUML_SECURITY_PROFILE INTERNET
```
```
java -DPLANTUML_SECURITY_PROFILE=INTERNET -jar /path/to/plantuml.jar ...
```
```
System.setProperty("PLANTUML_SECURITY_PROFILE", "INTERNET");
```

## List of Security Profiles

#### UNSECURE

#### LEGACY

#### INTERNET

#### ALLOWLIST

#### SANDBOX

## Allowlists

- plantuml.allowlist.path for local files
- plantuml.include.path for local files
- plantuml.allowlist.url for remote resources (URL)

#### plantuml.allowlist.path
```
java -DPLANTUML_SECURITY_PROFILE=INTERNET  -Dplantuml.allowlist.path=/usr/common/:/usr/plantuml/  ...
```

#### plantuml.include.path
```
java -DPLANTUML_SECURITY_PROFILE=INTERNET  -Dplantuml.include.path=c:/windows/plantuml/  ...
```

#### plantuml.allowlist.url
```
java -DPLANTUML_SECURITY_PROFILE=ALLOWLIST  -Dplantuml.allowlist.url=https://plantuml.com/;http://somelocalserver:8080/commons/  ...
```
