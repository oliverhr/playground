package interfaces

import (
	"fmt"
	"strings"
)

type emptyInterface interface{}

func empty(ei emptyInterface) {
	ei = "hello"
	fmt.Printf("%v\n", ei)

	ei = 34
	fmt.Printf("%v\n", ei)

	ei = []int{3, 6, 9}
	fmt.Println(ei)

	// type assertion
	fmt.Println(len(ei.([]int)))
}

func emptyOrAny() {
	var vacia interface{}
	empty(vacia)

	fmt.Println(strings.Repeat("-", 50))

	var cualquier any
	empty(cualquier)
}
