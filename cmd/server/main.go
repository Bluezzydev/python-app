package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"
)

const branch = "lang/go-cmd"

func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(map[string]string{"branch": branch, "lang": "go", "path": r.URL.Path})
	})
	log.Printf("%s listening on %s", branch, port)
	log.Fatal(http.ListenAndServe(":"+port, nil))
}
