package main


import (
    "fmt"
    "log"
    "io/ioutil"
    "net/http"
)

func main() {
    r, err := http.Get("http://ifconfig.io/ip")
    if err != nil{
        log.Fatal(err)
    }
    defer r.Body.Close()
    ip, err := ioutil.ReadAll(r.Body)
    if err != nil{
        log.Fatal(err)
    }
    fmt.Println(string(ip))
}
