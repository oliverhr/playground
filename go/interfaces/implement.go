package interfaces

import (
	"fmt"
	"math"
	"strings"
)

/*
In Go is not required the use of any special reserved word
like in java ("public class MyClass implements MyInterface")
or a special operator like in C# ("public class MyClass : IMyInterface")

In Golang interfaces are more like a contract than a type, this
because does not require a hierarchical structure, in go cares more
about how a type behaves "what can do" more than like "what is".

A very important thing to notice is that intefaces follow the pattern
"Duck Typing" any "type" that implements the methods specified in the
interface signature are considered that fullfill the interface.
*/

// Shape interface
type shape interface {
	area() float64
	perimeter() float64
}

// Rectangle
type rectangle struct {
	width, height float64
}

func (r rectangle) area() float64 {
	return r.height * r.width
}

func (r rectangle) perimeter() float64 {
	return 2 * (r.height + r.height)
}

// Circle
type circle struct {
	radius float64
}

func (c circle) area() float64 {
	return math.Pi * math.Pow(c.radius, 2)
}

func (c circle) perimeter() float64 {
	return 2 * math.Pi * c.radius
}

// Next a normal function (not a method)
// this function accepts any type that
// implements the methods declared on
// by the shape interface
func printShape(s shape) {
	fmt.Printf("Shape: %+v\n", s)
	fmt.Println("Area:", s.area())
	fmt.Println("Perimeter:", s.perimeter())
}

// ----------------------------------------------------------------------------

func implementacion() {
	c := circle{radius: 2.3}
	printShape(c)

	fmt.Println(strings.Repeat("-", 30))

	r := rectangle{width: 2.3, height: 3.4}
	printShape(r)
}
