package interfaces

import "fmt"

type animal interface {
	breathe()
	walk()
}

type human interface {
	animal
	speak()
}

// Note there is not a special reserved word like
// "implements", just a normal type declaration
type student struct {
	name string
}

// Next the methods implementation:
// - breathe and walk to comply with animal
// - and speak to comply with human

func (s student) breathe() {
	fmt.Println("ahhha ahhhha ahhhaa")
}

func (s student) walk() {
	fmt.Println("Walking")
}

func (s student) speak() {
	fmt.Println("blah blah blah")
}

// We can also add methods that only belong to the concrete type student
func (s student) study() {
	fmt.Println("Studying")
}

func composicion() {
	animalito()
	humano()
}

func animalito() {
	var a animal = student{name: "Pedro"}
	a.breathe()
	a.walk()

	// type assertion either to human or student
	// where the method speak exist
	a.(human).speak()
	a.(student).speak()

	// since the declaration is type "human"
	// in order to invoke student->study method
	// we need to make a type assertion
	a.(student).study()
}

func humano() {
	var h human = student{name: "Pedro"}
	h.breathe()
	h.walk()
	h.speak()

	h.(student).study()
}
