package main

import (
	"fmt"
	"os"
)

func main() {
	var input string
	baseMessage := "hello"

	if len(os.Args) == 2 {
		input = os.Args[1]
	} else {
        input = "world!"
    }

	fmt.Printf("%s %s\n", baseMessage, input)

}
