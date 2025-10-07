package channels

import (
	"fmt"
)

/*
*
Channels [ Mutual Exclution ]

Add an explanation about channels, the concept
and how they work in golang
*/
func EntryPoint() {
	fmt.Println("Ejemplo de Canales:")
	channels()
}

func channels() {
	c := make(chan int)
	r := make(<-chan string) // receive
	s := make(chan<- string) // send

	fmt.Printf("%T, %T, %T\n", c, r, s)

	go fn(10, c)

	n := <-c
	fmt.Println("Valued received:", n)

	fmt.Println("Exit function channel")
}

func fn(n int, ch chan int) {
	ch <- n
}
