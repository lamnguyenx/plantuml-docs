---
title: Ftp — PlantUML Official Documentation
source: https://plantuml.com/ftp
description: Official documentation for PlantUML Ftp
---

# File Transfer Protocol

PlantUML Plugins FTP Â Â Â Â
```
java -jar plantuml.jar -ftp
```

By default, the server runs on the 4242 port, but you can specify another port:
```
java -jar plantuml.jar -ftp:12345
```

You can then connect to 127.0.0.1 on this port with any FTP client, using any user/password.

## Example of Transfer
```
Status:Connecting to 127.0.0.1:24242...
Status:Connection established, waiting for welcome message...
Response:220 PlantUML
Command:USER anonymous
Response:331 Password required
Command:PASS ***
Response:230 Logged in.
Command:SYST
Response:215 UNIX Type: L8.
Command:FEAT
Response:502 Command not implemented.
Status:Connected
Status:Retrieving directory listing...
Command:PWD
Response:257 "/" is current directory.
Command:TYPE I
Response:200 Command okay.
Command:PASV
Response:227 Entering Passive Mode (127,0,0,1,39,59).
Command:LIST
Response:150 Opening ASCII mode data
Response:226 Listing completed.
Status:Directory listing successful
Status:Connecting to 127.0.0.1:24242...
Status:Connection established, waiting for welcome message...
Response:220 PlantUML
Command:USER anonymous
Response:331 Password required
Command:PASS ***
Response:230 Logged in.
Status:Connected
Status:Starting upload of data1.txt
Command:CWD /
Response:250 "/" is new working directory..
Command:PWD
Response:257 "/" is current directory.
Command:TYPE A
Response:200 Command okay.
Command:PASV
Response:227 Entering Passive Mode (127,0,0,1,39,60).
Command:STOR data1.txt
Response:150 FILE: data1.txt
Response:226 Transfer complete.
Status:File transfer successful, transferred 339 bytes in 1 second
Status:Retrieving directory listing...
Command:TYPE I
Response:200 Command okay.
Command:PASV
Response:227 Entering Passive Mode (127,0,0,1,39,61).
Command:LIST
Response:150 Opening ASCII mode data
Response:226 Listing completed.
Status:Directory listing successful
Status:Retrieving directory listing...
Command:PASV
Response:227 Entering Passive Mode (127,0,0,1,39,62).
Command:LIST
Response:150 Opening ASCII mode data
Response:226 Listing completed.
Status:Directory listing successful
Status:Starting download of /data1.png
Command:PASV
Response:227 Entering Passive Mode (127,0,0,1,39,63).
Command:RETR data1.png
Response:150 Opening
Response:226 Transfer complete.
Status:File transfer successful, transferred 3705 bytes in 1 second
```
