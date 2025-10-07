package basics

import (
	"fmt"
)

func Basicos() {
	x := "Hello, World!\nbye."
	fmt.Println(x)

	var y string
	y = `Apple\nOrange.`
	fmt.Println(y)

	var z string = "Hi, everyone!"
	fmt.Println(z)

	var i int
	fmt.Println(i)
	var b bool
	fmt.Println(b)

	var cadena = "Esto es una cadena"
	fmt.Println(cadena)

	texto := "Esto es una cadena tambien"
	fmt.Println(texto)

	const pi = 3.1416
	fmt.Println(pi)

	fmt.Println(11/2, 11%2)
}
