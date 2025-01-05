https://golang.google.cn/dl/

SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=amd64

go env CGO_ENABLED
go env GOOS
go env GOARCH

https://stackoverflow.com/questions/18207772/how-to-wait-for-all-goroutines-to-finish-without-using-time-sleep

go run tcp_socket.go --listen --host=127.0.0.1 --port=1-65536
go run tcp_socket.go --connect --host=127.0.0.1 --port=1-65536

---

http_dump

curl -X POST -d 'x=1' "http://127.0.0.1:1234/"
curl -X POST -H 'Content-Type: application/json' -d '{"x": 1}' "http://127.0.0.1:1234/"
