package tiempo

import (
	"fmt"
	"time"
)

/**
Elapsing time calculation

- Wall clock vs Monotonic clock
Substract and Add (this later is not commonly used)
- time.Time.Sub
- time.Time.Add
*/

func Calculate() {
	// monotonic()
	__("_")
	manipulate()
}

func manipulate() {
	timeToManipulate := time.Now()
	toBeAdded := time.Duration(-10 * time.Second)

	fmt.Println("The original time:", timeToManipulate)
	fmt.Printf("%v duration later %v\n", toBeAdded, timeToManipulate.Add(toBeAdded))
}

func deadline() {
	deadlineSeconds := time.Duration((1600 * 10) * time.Millisecond)
	start := time.Now()

	fmt.Println("Deadline for the transcaction is:", deadlineSeconds)
	fmt.Println("The transaction has started at:", start)

	sum := 0
	for i := 1; i < 25_000_000_000; i++ {
		sum += 1
	}

	end := time.Now()
	duration := end.Sub(start)
	transactionTime := time.Duration(duration.Nanoseconds()) * time.Nanosecond

	fmt.Println("The transaction has completed at:", end, duration)

	if transactionTime <= deadlineSeconds {
		fmt.Println("Performance ok:", transactionTime)
	} else {
		fmt.Println("Performance problem:", transactionTime, "second(s)")
	}
}

func monotonic() {
	start := time.Now()
	fmt.Println("The script started at: ", start)

	sum := 0
	for i := 1; i < 10_000_000_000; i++ {
		sum += i
	}
	end := time.Now()
	duration := end.Sub(start)

	fmt.Println("The script completed at: ", end)
	put("hour", duration.Hours())
	put("minute", duration.Minutes())
	put("second", duration.Seconds())
	put("nanosecond", duration.Nanoseconds())
}

func put[Num int64 | float64](s string, t Num) {
	fmt.Printf("The task took: %v %s(s) to complete!\n", t, s)
}
