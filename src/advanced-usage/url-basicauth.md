---
title: Url Basicauth — PlantUML Official Documentation
source: https://plantuml.com/url-basicauth
description: Official documentation for PlantUML Url Basicauth
---

# BasicAuth configuration

PlantUML BasicAuth configuration BasicAuth configuration Â Â Â Â

- OAuth2 configuration
- Token Auth configuration
- General URL authentication documentation
```
{
  "name": "<name of the configuration>",
  "type": "basicauth",
  "identifier": "<client/user identifier>",
  "secret": "<client secret>",
  "proxy": {
    "type": "<proxy type>",
    "address": "<proxy server address>",
    "port": "<proxy server port>"
  }
}
```

- name : required
- type : basicauth
- identifier : required
- secret :

- proxy :
- proxy . type : required ( direct , socks , http )
- proxy . address : required
- proxy . port :
```
{
  "name": "jira",
  "identifier": "alice",
  "secret": "secret"
}
```
```
{
  "name": "stash-cloud",
  "type": "basicauth",
  "identifier": "repoadmin",
  "secret": "verySecret",
  "proxy": {
    "type": "socks",
    "address": "outboundcloud.int.example.com",
    "port": "8091"
  }
}
```
