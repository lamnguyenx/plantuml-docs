---
title: Url Oauth — PlantUML Official Documentation
source: https://plantuml.com/url-oauth
description: Official documentation for PlantUML Url Oauth
---

# OAuth2 configuration

PlantUML OAuth2 configuration OAuth2 configuration Â Â Â Â

- see also

## OAuth2 client credentials flow
```
{
  "name": "<name of the configuration>",
  "type": "oauth",
  "identifier": "<principal identifier>",
  "secret": "<principal secret>",
  "properties": {
    "grantType": "client_credentials",
    "accessTokenUri": "<URL to token access controler>",
    "scope": "<access scopes>"
  },
  "proxy": {
    "type": "<proxy type>",
    "address": "<proxy server address>",
    "port": "<proxy server port>"
  }
}
```

- name : required
- type : oauth required
- identifier : required
- secret :
- properties . grantType : client_credentials required
- properties . accessTokenUri : required
- properties . scope :
- proxy :
- proxy . type : required ( direct , socks , http )
- proxy . address : required
- proxy . port :
```
{
  "name": "curity-demo",
  "type": "oauth",
  "identifier": "demo-backend-client",
  "secret": "MJlO3binatD9jk1",
  "properties": {
    "grantType": "client_credentials",
    "scope": "read write",
    "accessTokenUri": "https://login-demo.curity.io/oauth/v2/oauth-token"
  }
}
```

## OAuth2 resource owner password credentials flow
```
{
  "name": "<name of the configuration>",
  "type": "oauth",
  "identifier": "<principal identifier>",
  "secret": "<principal secret>",
  "properties": {
    "grantType": "password",
    "accessTokenUri": "<URL to token access controler>",
    "scope": "<access scopes>",
    "resourceOwner": {
      "identifier": "<resource owner name>",
      "secret": "<resource owner secret>"
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
- type : oauth required
- identifier : required
- secret :
- properties . grantType : password required
- properties . accessTokenUri : required
- properties . scope :
- properties . resourceOwner . identifier :
- properties . resourceOwner . secret :
- proxy :
- proxy . type : required ( direct , socks , http )
- proxy . address : required
- proxy . port :
```
{
	"name": "oauth-example",
	"type": "oauth",
	"identifier": "demo-backend-client",
	"secret": "MJlO3binatD9jk1",
	"properties": {
		"grantType": "password",
		"scope": "read write",
		"accessTokenUri": "https://login-demo.curity.io/oauth/v2/oauth-token",
		"resourceOwner": {
			"identifier": "alice",
			"secret": "secret"
		}
	}
}
```
