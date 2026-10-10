package main

import "fmt"

// If this one is built instead of cmd/server, the pod exits at once.
func main() {
	fmt.Println("worker: wrong main package was picked")
}
