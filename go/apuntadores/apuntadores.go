package apuntadores

import "fmt"

func Punteros() {
	basics()

	fmt.Println("-- -- --")
	withNew()

	fmt.Println("-- -- --")
	pointerAsParam()
}

func basics() {
	var x string = "hola"
	pointerToX := &x

	fmt.Println(x)
	fmt.Println(&x)
	fmt.Println(pointerToX)
	fmt.Println(*pointerToX)
}

func withNew() {
	// Built in function "new" can be used
	// to create a pointer variable
	var p = new(int)
	// default value is the reserved address space
	fmt.Println("initialized then not nil: p == nil?", p == nil)
	fmt.Println("Is a pointer so the value is:", p)
	// The type is zero value initialized
	fmt.Println("If we use the * operator we get the value (zero value):", *p)
}

// If something is declared as a pointer in Golang is a declaration
// for the intentionallity of mutability.

// Go is a call-by-value language, meaning that all the values passed
// to functions are copies therefore the original data inmutability
// is granted.

// ----------------------------------------------------------------------------
// pointer as parameters/arguments: if a pointer is passed to a function,
// the function gets a copy of the pointer. This still points to the
// original data, which means that the original data can be modified by
// the called function. When you pass a nil pointer to a function,
// you cannot make the value non-nil. Since the memory location was passed
// to the function via call-by-value, you can’t change the memory address.
func pointerAsParam() {
	x := 40
	fmt.Println("Original value:", x)

	failedUpdate(&x)
	fmt.Println("Unachanged:", x) // still nil istead of 10

	fmt.Println("--------")
	// this will do the work
	update(&x)
	fmt.Println("Value updated:", x)
}

/*
failedUpdate
Esta function es sobre ejemplificar el como todos los parametros en golang
son pasados "ByVal" o mejor dicho se crea una copia del valor.

En este caso el parametro es un "aputador a un entero", esto es el parametro
es una dirección de memoria cuyo contenido debe ser un int

Si se accede al valor de pToInt este es una dirección "0x00...", para poder acceder
al valor se debe de hacer una desreferencia utilizando el operador * asterisk

En la linea: `pToInt = &x` no es cambiar el valor del entero sino la dirección
hacia la que apunta, por la de la variable "x"
*/
func failedUpdate(pToInt *int) {
	fmt.Printf("--- pToInt address: %v, content: %d\n", pToInt, *pToInt)
	var x int = 10                      // x is type int, pToInt is a pointer
	pToInt = &x                         // this change the copy of "f" (meaning "g") to 10
	fmt.Println("--- pToInt:", *pToInt) // but at the end the original value remains unchanged
}

func update(px *int) {
	*px = 20
}

// The only time you should use pointer parameters to modify
// a variable is when the function expects an interface.
