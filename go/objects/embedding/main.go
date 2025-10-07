package embedding

import "fmt"

type shape interface {
	area() float64
}

type poligon interface {
	shape
	perimeter()
}

type curved interface {
	shape
	circunference()
}

func Run() {
	fmt.Println("An interface can ask to",
		"'implement' another interface",
		"this is a way of reutilization.")
}
