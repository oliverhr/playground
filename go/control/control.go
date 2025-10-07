package control

import (
	"fmt"
)

func Run() {
	testIfElse()
	testSwitchCase(1)
	loops()
}

func loops() {
	for i := 0; i < 10; i++ {
		fmt.Print(i)
	}
}

// in Golang the break is implied
func testSwitchCase(day int) {
	switch day := 0; day {
	case 1:
		fmt.Println("Lunes")
	case 2:
		fmt.Println("Martes")
	case 3:
		fmt.Println("Miercoles")
	case 4:
		fmt.Println("Jueves")
	case 5:
		fmt.Println("Viernes")
	case 6:
		fmt.Println("Sabado")
	case 7:
		fmt.Println("Domingo")
	default:
		fmt.Println("A cabrón!")
	}
}

func testIfElse() {
	fmt.Println("")

	if true {
		fmt.Println("always")
	} else {
		fmt.Println("never")
	}
}
