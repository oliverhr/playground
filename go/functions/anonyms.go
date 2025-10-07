package functions


import "fmt"

func Anonima() {
	a := 20
	f := func() {
		fmt.Println(a)
		// shadows upper lever a
		a := 30
		fmt.Println(a)
	}
	f()
	fmt.Println(a)
}
