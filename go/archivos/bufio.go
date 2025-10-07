package archivos

import (
	"bufio"
	"fmt"
	"io/fs"
	"log"
	"os"
)

/*
Package "bufio" implements buffered I/O

It wraps an io.Reader or io.Writer object, creating another
object (Reader or Writer) that also implements the interface
but provides buffering and some help for textual I/O

This package is useful if data manipulation is required in an
extensive way, since the data is buffered in memory.
*/

func Buffers() {
	var fname string = "fichero.txt"
	fmt.Println()

	var perms fs.FileMode = 0644
	file, err := os.OpenFile(fname, os.O_WRONLY|os.O_CREATE, perms)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var bufferedWriter *bufio.Writer
	bufferedWriter = bufio.NewWriter(file)
	fmt.Println("Unflushed buffer size:", bufferedWriter.Size())

	// the buffer needs to be flused to dump the data
	// from the memory to the file(s)
	defer bufferedWriter.Flush()

	// if for some reason we want to "clear" the buffer
	// method is available "bufferedWriter.Reset()"
	// this discards any unflushed data

	// data is being written to the memory buffer
	// not to the file
	dumpBytes(bufferedWriter)
	dumpByte(bufferedWriter)
	dumpString(bufferedWriter)
	dumpRunes(bufferedWriter)
	fmt.Println("Buffered data size (bytes):", bufferedWriter.Buffered())
}

func dumpBytes(bufferedWriter *bufio.Writer) {
	byteSlice := []byte{97, 98, 99}
	size, err := bufferedWriter.Write(byteSlice)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Available buffer space:", bufferedWriter.Available())
	fmt.Println("Bytes written:", size)
}

func dumpByte(bufferedWriter *bufio.Writer) {
	var char byte = 10 // var char byte = '\n'
	if err := bufferedWriter.WriteByte(char); err != nil {
		log.Fatal(err)
	}
	fmt.Println("Available buffer space:", bufferedWriter.Available())
	fmt.Println("Byte written:", char)
}

func dumpString(bufferedWriter *bufio.Writer) {
	text := "Esto es una cadena"
	size, err := bufferedWriter.WriteString(text)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Available buffer space:", bufferedWriter.Available())
	fmt.Println("Bytes written:", size)
}

func dumpRunes(bufferedWriter *bufio.Writer) {
	var char rune

	char = '\n'
	_, err := bufferedWriter.WriteRune(char)
	if err != nil {
		log.Fatal(err)
	}

	char = 'ñ'
	size, err := bufferedWriter.WriteRune(char)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Available buffer space:", bufferedWriter.Available())
	fmt.Println("Bytes written:", size)
}
