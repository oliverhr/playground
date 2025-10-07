package functions

import "fmt"

func makeMult(base int) func(int) int {
	return func(factor int) int {
		return base * factor
	}
}

func currying() {
	twoBase := makeMult(2)
	threeBase := makeMult(3)

	for i := 0; i < 3; i++ {
		fmt.Println(twoBase(i), threeBase(i))
	}
}

func decorator(base int, fn func(int) int) (result int) {
	base += 2
	result = fn(base)
	return
}

func firstClass() {
	callback := func(n int) int {
		return n * n
	}

	x := decorator(4, callback)
	fmt.Println(x)
}

func HighOrder() {
	currying()
	firstClass()
}
