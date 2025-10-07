package interfaces

import "fmt"


type food interface {
	eat()
}


type veggie string
func (v veggie) eat() {
	fmt.Println("Eating", v)
}

type meat string
func (m meat) eat() {
	fmt.Println("Eating tasty", m)
}


func comer(f food) {
	veg, ok := f.(veggie)
	if ok {
		if veg == "okra" {
			fmt.Println("Yuk! not eating", veg)
		} else {
			veg.eat()
		}
		return
	}

	mt, ok := f.(meat)
	if ok {
		if mt == "chivo" {
			fmt.Println("Yuk! not eating", mt)
		} else {
			mt.eat()
		}
		return
	}

	fmt.Println("Not eating whatever that is:", f)
}

func eat(f food) {
	switch morfi := f.(type) {

	case veggie:
		if morfi == "okra" {
			fmt.Println("Yuk! not eating", morfi)
		} else {
			morfi.eat()
		}
	case meat:
		if morfi == "chivo" {
			fmt.Println("Yuk! not eating", morfi)
		} else {
			morfi.eat()
		}
	default:
		fmt.Println("Not eating whatever that is:", f)

	}
}


func Dinner() {
	var f meat = "beef"
	eat(f)
}
