package concurrency

import (
	"fmt"
	"runtime"
	"strings"
	"sync"
	"time"
)

/*
Concurrency != Paralelism

Concurrency in go is achieved mainly wih Goroutines (similar co coroutines in C++),
the keyword "go" is how you create/spawn a goroutine

A goroutine is a lightweight thread of execution.

- Typically only takes around 2kb from the stack space to initialize
  this is way less compared to a thread wich takes a fixed size from 1 to 2 Mb.
- Compared to an OS Thread Stack, a Goroutine stack size can grow or shrink as required.
- Scheduling a Goroutine is cheaper than scheduling a thread
- Goroutines are schedules by own GO scheduler using a technique called M:N Scheduling,
  because it multiplexes (or schedules) "M gouroutines on N OS threads"
- Goroutines has no idendity (there is no option of identify that is accessible to the programmer)
*/

func Concurrency() {
	// info()

	// fmt.Printf("\n%s\n", strings.Repeat("-", 30))
	// simple()

	// fmt.Printf("\n%s\n", strings.Repeat("-", 30))
	// goroutines()

	fmt.Printf("\n%s\n", strings.Repeat("-", 30))
	waitGroup()
}

func info() {
	fmt.Println("Concurrency submodule")
	fmt.Println(strings.Repeat("-", 30))

	fmt.Println("No. of CPUs:", runtime.NumCPU())
	fmt.Println("No. of Go goroutines:", runtime.NumGoroutine())
	fmt.Println("OS:", runtime.GOOS)
	fmt.Println("Arch:", runtime.GOARCH)
	fmt.Println("Max number of Go proccess:", runtime.GOMAXPROCS(0))
}

func simple() {
	// Normal function invocation
	doSomething("Go")

	// goroutine spawning
	go doSomething("Las GoRoutines")

	time.Sleep(time.Second * 2)
}
func doSomething(topic string) {
	fmt.Printf("Que onda con %s!\n", topic)
}

func goroutines() {
	fmt.Printf("\n%s\n", strings.Repeat("-", 30))
	go f1()
	fmt.Println("No. goroutines after go f1():", runtime.NumGoroutine())
	fmt.Printf("\n%s\n", strings.Repeat("-", 30))

	sycncronous()
	fmt.Println("No. goroutines after go func sycncronous():", runtime.NumGoroutine())
	fmt.Printf("\n%s\n", strings.Repeat("-", 30))

	// Artificial long duration task using sleep
	// uncomment next line to observer the 1f1 output
	// time.Sleep(time.Second * 2);
	fmt.Println("\nMain execution stopped")
}

func waitGroup() {
	var wg sync.WaitGroup

	wg.Add(1) // wait for 1 go routine

	go f3(&wg)
	fmt.Println("No. goroutines after go f1():", runtime.NumGoroutine())
	fmt.Printf("\n%s\n", strings.Repeat("-", 30))

	sycncronous()
	fmt.Println("No. goroutines after go func sycncronous():", runtime.NumGoroutine())
	fmt.Printf("\n%s\n", strings.Repeat("-", 30))

	/* The natural way we wait until the routines on
	   on the wait group are completed */
	wg.Wait()

	fmt.Println("\nMain execution stopped")
}

func f1() {
	fmt.Println("f1 - (GoRoutine) execution started")
	for i := 0; i < 3; i++ {
		fmt.Println("f1, i =", i)
	}
	fmt.Println("f1 - Execution finished")
}

func sycncronous() {
	fmt.Println("sycncronous func - (GoRoutine) execution started")
	for i := 5; i < 8; i++ {
		fmt.Println("sycncronous func, i =", i)
	}
	fmt.Println("sycncronous func - Execution finished")
}

func f3(wg *sync.WaitGroup) {
	fmt.Println("f3 - (GoRoutine) execution started")
	for i := 0; i < 3; i++ {
		fmt.Println("f3, i =", i)
		time.Sleep(time.Second)
	}
	fmt.Println("f3 - Execution finished")
	wg.Done()
	// (*wg).Done()
}
