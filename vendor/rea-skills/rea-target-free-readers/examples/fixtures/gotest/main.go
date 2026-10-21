package main

import (
	"fmt"
	"strings"
)

func Greet(n string) string { return "Hello, " + strings.ToUpper(n) }

func main() { fmt.Println(Greet("world")) }
