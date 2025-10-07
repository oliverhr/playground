package archivos

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func Delimited() {
	fname := "delimited.txt"
	file, err := os.Open(fname)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	// default behavior can be omited
	scanner.Split(bufio.ScanLines)
	// The default scanner is "bufio.ScanLines" and that means it will scan a
	// file line by line. There are also bufio.ScanWords and bufio.ScanRunes.

	if !scanner.Scan() {
		if err := scanner.Err(); err != nil {
			log.Fatal(err)
		}
		log.Println("Scan complete, reached EOF")
		os.Exit(0)
	}

	fmt.Println("First line found:\n", scanner.Text())

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
