package interfaces

import (
	"fmt"
	"strings"
)

/*
In go variables has types known at compilation and never change
Interfaces has dynamic types who may change during runtime
*/

func vacias() {
	separator := strings.Repeat("-", 30)

	fmt.Println("Interfaces vacias aka {}")

	// The declaration with var seems is important,
	// since we are declaring a var which is an
	// "interface type" that will work as undelying type
	var s shape
	fmt.Printf("%T\n", s)

	ball := circle{radius: 1.2}
	s = ball              // now the concrete type
	fmt.Printf("%T\n", s) // of s is circle

	// printShape ask to a type shape
	fmt.Println(separator, "shape:")
	printShape(s) // implicit acceptance since type is shape
	fmt.Println("The area", s.area())

	fmt.Println(separator, "ball:")
	printShape(ball) // circle implements shape methods
	fmt.Println("The area", ball.area())

	fmt.Println(separator, "room:")
	room := rectangle{width: 2, height: 3}
	s = room
	fmt.Printf("Type of s: %T\n", s)
}
