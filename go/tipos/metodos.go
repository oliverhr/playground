package tipos

import (
	"fmt"
	"time"
)

func tiempo() {
	const day = 24 * time.Hour
	fmt.Printf("Day type: %T\n", day)

	seconds := day.Seconds()
	fmt.Printf("Seconds type: %T\n", seconds)
	fmt.Printf("Seconds in a day: %v\n", seconds)
}

// This is my custom type names
type names []string

// This is the method print() attached to the type names
func (n names) print() {
	for i, name := range n {
		fmt.Println(i, name)
	}
}

/*
The difference between a function and a method is:
- the method is binded to a type
- the function belongs to a package
*/
func metodos() {
	friends := names{"Roger", "Pastor"}
	friends.print() // type is implicit
	fmt.Println(". . . . . . . .")
	names.print(friends)
}
