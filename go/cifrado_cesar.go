package main

import (
	"fmt"
)

func main() {
	text := "attackatonce"
	shift := 4

	encoded := rotate(text, shift)
	decoded := rotate(encoded, -shift)

	fmt.Println(text)
	fmt.Println(encoded)
	fmt.Println(decoded)
}

/**
 * Sustituye los caracteres del parametro "texto" alfabeto Latino/Inglés
 * el desplazamiento lo realiza de acuerdo al valor del parametro "shift"
 *
 * El alfabeto utilizado es en código ASCII
 * La secuencua de mayúsculas es del código 65 al 90
 * La secuencia de minúsculas es del código 97 al 122
 * Ambas secuencias no incluyen la ñ/Ñ ni vocales con acento
 */
func rotate(text string, shift int) string {
	shift = (shift % 26 + 26) % 26 // [0, 25] = 26 items

	slice := make([]byte, len(text))

	for i := 0; i < len(text); i++ {
		var ascii int
		char := text[i]

		switch {
			case 'a' <= char && char <= 'z': // mayúsculas
				ascii = 'a'
			case 'A' <= char && char <= 'Z': // minúsculas
				ascii = 'A'
			default:
				slice[i] = char
				continue
		}
		slice[i] = byte(ascii + ((int(char) - ascii) + shift) % 26)
	}

	return string(slice)
}

