---
title: Url Tokenauth — PlantUML Official Documentation
source: https://plantuml.com/url-tokenauth
description: Official documentation for PlantUML Url Tokenauth
---

# Token Auth configuration

PlantUML Token Auth configuration Token Auth configuration Â Â Â Â

- see also

## Token auth configuration
```
{
  "name": "<name of the configuration>",
  "type": "tokenauth",
  "properties": {
    "headers": {
      "key1": "value1",
      "key2": "value2",
      ...
    }
  },
  "proxy": {
    "type": "<proxy type>",
    "address": "<proxy server address>",
    "port": "<proxy server port>"
  }
}
```

- name : required
- type : tokenauth required
- properties . headers :
- proxy :
- proxy . type : required ( direct , socks , http )
- proxy . address : required
- proxy . port :
```
{
  "name": "public-api",
  "type": "tokenauth",
  "properties": {
    "headers": {
      "Authorization": "ApiKey a4db08b7-5729-4ba9-8c08-f2df493465a1"
    }
  }
}
```
