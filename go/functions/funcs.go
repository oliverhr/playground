package functions

import (
	"fmt"
)

func Run() {
	fn()
	val := sum(1, 2)
	fmt.Println(val)

	x, y := values()
	fmt.Println(x, y)

	fmt.Println(suma(7, 9))

	n := 99
	fmt.Println("\n", n)
	replace(&n)
	fmt.Println(n)

	fmt.Println("\n", variadic(1, 2, 3, 4, 5, 6, 7, 8, 9))

	// defer
	var num int
	num++
	defer diferida(num)
	num = 9
	fmt.Println(num)
	num = 1
	fmt.Println(num)
}

func variadic(nums ...int) int {
	sum := 0
	for _, v := range nums {
		sum += v
	}
	for i := 0; i < len(nums); i++ {
		fmt.Println(i, nums[i])
	}
	return sum
}

func replace(x *int) {
	*x++
}

func fn() {
	x := 10

	fmt.Println("Value of x:", x)
	{
		x, y := 20, 30

		fmt.Println("Value of x:", x)
		fmt.Println("Value of y:", y)
	}
	fmt.Println("Value of x:", x)
}

func sum(x, y int) int {
	return x + y
}

func suma(x, y int) (res int) {
	res = x + y
	return
}

func values() (int, int) {
	return 1, 0
}

func diferida(num int) {
	fmt.Println(num)
}
