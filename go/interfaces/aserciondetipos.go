package interfaces

import (
	"fmt"
	"math"
)

func aserciones() {
	// the declaration is type shape
	// but the assigment is for a type circle
	var s shape = circle{radius: 2.5}

	// So the concrete type is circle,
	// still the underlying type is shape
	fmt.Printf("%T\n", s) // [package].circle

	// Now we declare a var for a concrete type
	var c circle = circle{radius: 2.5}
	fmt.Printf("%T\n", c)

	// this works since volume is binded to circle
	var v float64

	v = c.volume()
	fmt.Println("Circle:", v)

	// but this will fail since shape does not specify a volume method
	// v= s.volume()

	// To "cast" (there is no type cast in go) or extract the interface
	// we use type assertions:
	// [obj].(type) return two items:
	v = s.(circle).volume()
	fmt.Println("type asserted:", v)
	// - the object (s in this case) casted to the type passed
	// - a bool value true if the type was asserted or false if not
	if circulo, ok := s.(circle); ok {
		fmt.Println("Circle volume:", circulo.volume())
	}

	// --------------------------------------------------------------
	// Type assetions with switch...case
	r := rectangle{width: 2, height: 5}

	bifurcation(c)
	bifurcation(r)
	bifurcation(s)
}

func bifurcation(s shape) {
	// Type Switch
	switch t := s.(type) {
	case circle:
		fmt.Println("---- Es un circulo ----", t)
	case rectangle:
		fmt.Println("---- Es un rectangulo ----", t)
	default:
		fmt.Println("---- Is a shape but none specified ----")
	}
}

// We declared a method "volume" which is not
// declared on the interface, still we bind this
// to the circle type
func (c circle) volume() float64 {
	return 4 / 3 * math.Pi * math.Pow(c.radius, 3)
}
