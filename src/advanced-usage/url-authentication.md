---
title: Url Authentication — PlantUML Official Documentation
source: https://plantuml.com/url-authentication
description: Official documentation for PlantUML Url Authentication
---

# URL authentication

PlantUML Advanced usage URL Authentication Â Â Â Â
```
@startuml

!include https://access@raw.example.com/stash/repository/architecture/master/modelbase.puml

!$DATA = %load_json('https://service-cred@localhost/api/rest/endpoint?format=json)

' Embedded rendering of JSON structure

 rectangle Test #tan as "
    {{json
    $DATA
    }}
    Example JSON data
    "
' ...
@enduml
```

## Credentials configuration
```
{
  "name": "<name of the configuration>",
  "type": "<type of the authentication method>",
  "identifier": "<client identifier>",
  "secret": "<client secret>",
  "properties": {
    "<key1>": "<value1>",
    "<key2>": "<value2>"
  },
  "proxy": {
    "type": "<proxy type>",
    "address": "<proxy server address>",
    "port": "<proxy server port>"
  }
}
```

- name : required
- type : ( basicauth , oauth , tokenauth ), default: basicauth
- identifier : required
- secret :
- properties :
- proxy :
- proxy . type : required ( direct , socks , http )
- proxy . address : required
- proxy . port :

- The name of a configuration may only contain characters from the following set: [ a-z ], [ A-Z ], [ 0-9 ], and " - ". Not more than 64 characters are allowed.

- Basic Auth configuration
- OAuth2 configuration
- Token Auth configuration

## Proxy configuration
```
{
  "type": "<proxy type>",
  "address": "<proxy server address>",
  "port": "<proxy server port>"
}
```

- direct
- socks
- http

- address
- port
```
"proxy": {
  "type": "socks",
  "address": "192.168.1.251",
  "port": "80"
}
```
```
"proxy": {
  "type": "direct"
}
```
```
"proxy": {
  "type": "http",
  "address": "proxy.example.com",
  "port": "8081"
}
```

## Property configuration

- plantuml.security.credentials.path

- The internal function %getenv will not expose the configuration value.
- Any content in the configured path (and in all subfolders) are invisible for DSL model scripts. It is required that the configured folder is a separate location for the credentials files.
- Multiple paths will be ignored. PlantUML reads the credentials files only from the first configured folder.

- plantuml.security.allowNonSSLAuth
