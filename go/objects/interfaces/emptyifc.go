package interfaces

import "fmt"

func Trick() {
	var anyType interface{}

	anyType = 77.55
	fmt.Println(anyType)

	anyType = "Im a string now!"
	fmt.Println(anyType)

	printAnyType("The car is slow")
	m := map[string] string{"ID": "1234", "name": "Peter"}
	printAnyType(m)
	printAnyType(12353443455)
}

func printAnyType(val interface{}) {
	fmt.Println(val)
}
