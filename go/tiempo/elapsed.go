package tiempo

import (
	"fmt"
	"strconv"
	"time"
)

func Elapsed() {
	start := time.Now()

	time.Sleep(2 * time.Second)

	end := time.Now()

	fmt.Println(elapsedTime(start, end))
}

func elapsedTime(start time.Time, end time.Time) string {
	elapsed := end.Sub(start)
	hours := strconv.Itoa(int(elapsed.Hours()))
	minutes := strconv.Itoa(int(elapsed.Minutes()))
	seconds := strconv.Itoa(int(elapsed.Seconds()))

	return "The total execution time elapsed is: " +
		hours + " hour(s) and " +
		minutes + " minute(s) and " +
		seconds + " second(s)!"
}
