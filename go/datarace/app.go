package datarace

import (
	"fmt"
	"sync"
	"time"
)

func EntryPoint() {
	const gr = 100 // number of goroutines
	var wg sync.WaitGroup
	wg.Add(gr * 2)

	var n int = 0
	for i := 0; i < gr; i++ {
		go func() {
			time.Sleep(time.Second / 10)
			n++
			wg.Done()
		}()

		go func() {
			time.Sleep(time.Second / 10)
			n--
			wg.Done()
		}()
	}
	wg.Wait()

	// Since the value of N is being updated separately
	// in two different places (200 [100 and 100]) the
	// value depends on what goroutine "go func" are
	// completed first.

	// This type of bugs are called a Data Race, and iss
	// a common error on Concurrent/Asynchronous applications.
	fmt.Println("Final value of n:", n)
}
