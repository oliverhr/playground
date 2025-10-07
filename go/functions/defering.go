package functions

import (
	"fmt"
	"io"
	"log"
	"os"
)


func Diferido() {
	fileExample()
	deferExample()
}

func deferExample() {
	a := 10
	defer func(val int) {
		fmt.Println("First:", val)
	}(a)

	a = 20
	defer func (val int) {
		fmt.Println("Second:", val)
	}(a)

	a = 30
	fmt.Println("exiting:", a)
}

func fileExample() {
	if len(os.Args) < 2 {
		log.Fatal("File not specified")
	}

	f, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

	data := make([]byte, 2048)
	for {
		count, err := f.Read(data)
		os.Stdout.Write(data[:count])
		if err != nil {
			if err != io.EOF {
				log.Fatal(err)
			}
			break
		}
	}
}
