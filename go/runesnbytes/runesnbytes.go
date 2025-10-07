package runesnslices

import "fmt"

func exampleOne() {
	var x int = 65
	y := string(x)
	fmt.Println(y)
}

func exampleTwo() {
	var s string = "Hello 🌞"
	fmt.Println(s)

	fmt.Println("----------- Length -----------")
	fmt.Println(len(s))
	r := []rune(s)
	fmt.Println(len(r))

	fmt.Println("--------- Bytes & Runes -------------")

	var bs []byte = []byte(s)
	var rs []rune = []rune(s)

	fmt.Println(bs)
	fmt.Println(rs)
}

func Example() {
	exampleOne()
	fmt.Println("----------------------")
	exampleTwo()
}
