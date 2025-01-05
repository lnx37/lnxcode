package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"log"
	"net/http"
	"time"
)

func TimeTaken(started time.Time, action string) {
	var elapsed time.Duration
	elapsed = time.Since(started)
	log.Printf("%v took %v\n", action, elapsed)
}

func GetIP(request *http.Request) string {
	var ip string
	ip = request.Header.Get("X-Real-Ip")

	if ip == "" {
		ip = request.Header.Get("X-Forwarded-For")
	}
	if ip == "" {
		ip = request.RemoteAddr
	}

	return ip
}

func MakeHandler(next http.Handler) http.HandlerFunc {
	return func(response http.ResponseWriter, request *http.Request) {
		var err error

		var ip string
		ip = GetIP(request)

		var method string
		var path string
		var referer string
		var user_agent string

		method = request.Method
		path = request.URL.Path
		referer = request.Header.Get("Referer")
		user_agent = request.Header.Get("User-Agent")

		var msg map[string]interface{}
		msg = map[string]interface{}{
			"ip":         ip,
			"method":     method,
			"path":       path,
			"referer":    referer,
			"user_agent": user_agent,
		}

		var msg2 []byte
		msg2, err = json.Marshal(msg)
		if err != nil {
			log.Println(err)
			log.Println("skip error")
		}

		var msg3 string
		msg3 = string(msg2)

		defer TimeTaken(time.Now(), msg3)

		log.Println(msg3, "begin")

		next.ServeHTTP(response, request)

		log.Println(msg3, "end")
	}
}

func main() {
	var err error

	log.SetFlags(log.LstdFlags | log.Lshortfile)

	var host string
	var port int

	flag.StringVar(&host, "host", "0.0.0.0", "Host")
	flag.IntVar(&port, "port", 1234, "Port")

	flag.Parse()

	var address string
	address = fmt.Sprintf("%s:%d", host, port)

	var fileServerHandler http.Handler
	fileServerHandler = http.FileServer(http.Dir("."))
	// http.Handle("/", fileServerHandler)
	http.Handle("/", MakeHandler(fileServerHandler))

	log.Printf("ListenAndServe: http://%s/\n", address)

	err = http.ListenAndServe(address, nil)
	if err != nil {
		log.Fatal(err)
	}
}
