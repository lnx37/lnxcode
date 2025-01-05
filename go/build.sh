#!/bin/bash

set -e

cd $(dirname -- "$(readlink -f -- "")")

go build -ldflags "-s -w" -o build/http_download http_download.go
go build -ldflags "-s -w" -o build/http_dump     http_dump.go
go build -ldflags "-s -w" -o build/http_upload   http_upload.go
go build -ldflags "-s -w" -o build/tcp_socket    tcp_socket.go

GOOS=windows GOARCH=amd64 go build -ldflags "-s -w" -o build/http_download.exe http_download.go
GOOS=windows GOARCH=amd64 go build -ldflags "-s -w" -o build/http_dump.exe     http_dump.go
GOOS=windows GOARCH=amd64 go build -ldflags "-s -w" -o build/http_upload.exe   http_upload.go
GOOS=windows GOARCH=amd64 go build -ldflags "-s -w" -o build/tcp_socket.exe    tcp_socket.go
