package conventions

import (
	"fmt"
)

// - in go variables can contain any UTF-8 character
// - Go style does not use snake case instead use camel case but ...
// - if a function or property name starts with a
//   capital letter this is module exported
// - "_" the underscore is a "special" character in Go

const Pi = 3.1416 // this constant is exported as part of the module


func Naming() {
	var x float64
	fmt.Println(x == 0)

	var π = 355 / 113.0
	fmt.Println(π)

	if π < 3.14 {
		fmt.Println("mmm something is wrong")
	} else {
		fmt.Println("yeih!!! looks good")
	}
}

