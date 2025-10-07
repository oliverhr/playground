package basics

import "fmt"

func variableShadow() {
	shadowing()
	fmt.Println(example())
}

func example() map[string]bool {
	x := map[string]bool{
		"name": true,
	}
	return x
}

func shadowing() {
	x := 1
	fmt.Println(x)

	if true {
		fmt.Println(x)

		x := 2

		fmt.Println(x)
	}
	fmt.Println(x)
}
