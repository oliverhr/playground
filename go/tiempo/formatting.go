package tiempo

import (
	"fmt"
	"time"
)

func Formato() {
	date := dateParts()
	calcDate(date)
	losAngeles()

	fmt.Println("----------------------------------")
	customFormat()
}

func calcDate(date time.Time) {
	year := 1
	month := 2
	day := 3
	next := date.AddDate(year, month, day)
	fmt.Println(next)
}

func dateParts() time.Time {
	year := 2020
	month := time.Month(1)
	day := 10
	hour := 20
	minute := 20
	second := 20
	nano := 324359102
	location := time.UTC

	// Equivalent
	// date := time.Date(2019, 9, 27, 18, 50, 48, 324359102, time.UTC)
	date := time.Date(year, month, day, hour, minute, second, nano, location)
	fmt.Println(date)

	return date
}

func losAngeles() {
	current := time.Now()
	la, err := time.LoadLocation("America/Los_Angeles")
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("\nANSIC")
	fmt.Println("Local time:\t", current.Format(time.ANSIC))
	fmt.Println("LA time:\t", current.In(la).Format(time.ANSIC))

	fmt.Println("\nRFC3339")
	fmt.Println("Local time:\t", current.Format(time.RFC3339))
	fmt.Println("LA time:\t", current.In(la).Format(time.RFC3339))

	fmt.Println("\nUnixDate")
	fmt.Println("Local time:\t", current.Format(time.UnixDate))
	fmt.Println("LA time:\t", current.In(la).Format(time.UnixDate))
}

func customFormat() {
	// hh:mm:mm dd/mm/yyyy
	// 02:49:41 31/01/2023
	now := time.Now()

	day := now.Day()
	month := now.Month()
	year := now.Year()

	hour := now.Hour()
	minute := now.Minute()
	second := now.Second()

	fecha := fmt.Sprintf("%02d:%02d:%02d %02d/%02d/%02d\n", hour, minute, second, day, month, year)
	fmt.Println(fecha)
}
