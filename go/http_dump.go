package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"net/http/httputil"
)

func index(response http.ResponseWriter, request *http.Request) {
	var err error

	var dump []byte
	dump, err = httputil.DumpRequest(request, true)
	if err != nil {
		log.Fatal(err)
	}

	log.Println(string(dump))

	response.Write(dump)
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

	http.HandleFunc("/", index)

	log.Printf("ListenAndServe: http://%s/\n", address)

	err = http.ListenAndServe(address, nil)
	if err != nil {
		log.Fatal(err)
	}
}
