package basics

import (
	"fmt"
)

func Cadenas() {
	fmt.Println("Résumé")
	cadenas()
	fmt.Println()
	runas()
}

func cadenas() {
	var myString = "résumé"
	var indexed = myString[0]

	fmt.Printf("%v, %T", indexed, indexed)
	fmt.Println()

	for i, v := range myString {
		fmt.Println(i, v)
	}
	fmt.Printf("\n The length of 'myString' is %v", len(myString))
}

func runas() {
	var myString = []rune("résumé")
	var indexed = myString[0]

	fmt.Printf("%v, %T", indexed, indexed)
	fmt.Println()

	for i, v := range myString {
		fmt.Println(i, v)
	}
	fmt.Printf("\n The length of 'myString' is %v", len(myString))
}

