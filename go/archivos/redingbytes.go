package archivos

import (
	"fmt"
	"io"
	"log"
	"os"
)

func IORead() {
	fname := "fichero.txt"
	file, err := os.Open(fname)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	readBytes(file)
	readAllBytes(file)
}

func readBytes(file *os.File) {
	byteSlice := make([]byte, 2)

	numberBytesReaded, err := io.ReadFull(file, byteSlice)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Bytes readed: %d\n", numberBytesReaded)
	fmt.Printf("Data readed: %s\n", byteSlice)
}

func readAllBytes(file *os.File) {
	data, err := io.ReadAll(file)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Data as string:\n\t%s\n", data)
	fmt.Printf("Numbers of bytes readed: %d\n", len(data))
}
