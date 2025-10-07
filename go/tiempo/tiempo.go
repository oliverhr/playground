package tiempo

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func __(s string) {
	fmt.Println(strings.Repeat(s, 30))
}

func EntryPoint() {
	__("_")
	fn1()
	__("_")
	fn2()
	__("_")
	fmt.Println(whatsTheClock())
	__("_")
	fn3()
	__("_")
	fn4()
}

func fn4() {
	now := time.Now()
	nowToo := now

	time.Sleep(1 * time.Second)
	later := time.Now()

	comp := func(t time.Time) {
		if now.Equal(t) {
			fmt.Println("The two time vars are equal!")
		} else {
			fmt.Println("The two time vars are different!")
		}
	}
	comp(nowToo)
	comp(later)
}

func fn3() {
	year := "2023"
	now := time.Now()
	onlyAfter, err := time.Parse(time.RFC3339, year+"-11-01T22:08:41+00:00")
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(now, onlyAfter, "\n---")
	fmt.Println(now.After(onlyAfter), "\n---")

	if now.After(onlyAfter) {
		fmt.Println("Executing actions!")
	} else {
		fmt.Println("Now is not the time yet!!")
	}
}

func fn2() {
	date := time.Now()
	appName := "HTTPCHECKER"
	action := "BASIC"

	logFileName := strings.Join([]string{
		appName,
		action,
		strconv.Itoa(date.Year()),
		date.Month().String(),
		strconv.Itoa(date.Day())},
		"_",
	)
	fmt.Println("The name of the logfile is:", logFileName)
}

func whatsTheClock() string {
	return time.Now().Format(time.ANSIC)
}

func fn1() {
	start := time.Now()

	fmt.Println("The script has started at:", start)
	fmt.Println("Saving the World...")

	// This creates a pause on the execution
	s := 2 * time.Second
	time.Sleep(s)

	end := time.Now()
	fmt.Println("The script has completed at: ", end)

	now := time.Now()
	day := now.Weekday()
	hour := now.Hour()

	fmt.Printf("Day: %v, Hour: %v\n", day, hour)
	if day.String() == "Saturday" {
		switch h := hour; { // No h after the semicolon ";"
		case h >= 12 && h <= 16:
			fmt.Println("Afternoon")
		case h >= 17 && h <= 18:
			fmt.Println("Evening")
		case h >= 19 && h <= 24:
			fmt.Println("Night")
		default:
			fmt.Println("Morninig")
		}
	}
}
