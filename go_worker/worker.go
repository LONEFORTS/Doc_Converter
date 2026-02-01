package main

import "fmt"

// Go receives task from Python
func process(fileType string) string {
	fmt.Println("Go: Received", fileType)
	return "Go processed " + fileType
}

func main() {
	fmt.Println("Go worker active")
}