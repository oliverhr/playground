package errores

import (
	"errors"
	"fmt"
)

func Example() {
	var x int = 7
	var y int = 2

	res1, rest1 := intDiv(x, y)
	fmt.Println("El resultado es", res1)
	fmt.Println("El resto es", rest1)

	y = 0
	result, rest, err := intDivision(x, y)
	if err == nil {
		fmt.Println("El resultado es", result)
		fmt.Println("El resto es", rest)
	} else {
		fmt.Printf(err.Error())
	}
}

func intDiv(numerator int, denominator int) (int, int) {
	if denominator == 0 {
		fmt.Println("Error no se puede dividir por cero")
		return 0, 0
	}

	var result int = numerator / denominator
	var reminder int = numerator % denominator

	return result, reminder
}

func intDivision(numerator int, denominator int) (int, int, error) {
	var err error
	if denominator == 0 {
		err = errors.New("Divizion by Zero")
		return 0, 0, err
	}

	var result int = numerator / denominator
	var reminder int = numerator % denominator

	return result, reminder, err
}
