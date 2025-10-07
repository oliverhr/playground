package concurrency

import "fmt"

func Canales() {
	ch := make(chan int)
	defer close(ch)

	go factorial(5, ch)

	f := <-ch
	fmt.Println(f)

	for i := 1; i <= 20; i++ {
		go factorial(i, ch)
		f := <-ch
		fmt.Println(f)
	}

	for i := 5; i <= 20; i++ {
		go func(n int, c chan int) {
			f := 1
			for i := 2; i <= n; i++ {
				f *= i
			}
			c <- f
		}(i, ch)

		fmt.Printf("Factorial of %d is %d\n", i, <-ch)
	}

}

func factorial(n int, c chan int) {
	f := 1
	for i := 2; i <= n; i++ {
		f *= i
	}
	c <- f
}
