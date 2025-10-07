package entrasale

import (
	"fmt"
)

func UserInput() {
	var name string
	fmt.Print("Please enter your first name: ")
	fmt.Scanln(&name)

	var lastName string
	fmt.Print("Please enter your last name: ")
	fmt.Scanln(&lastName)

	fmt.Println("Thank you for you visit:", name, lastName)
}
