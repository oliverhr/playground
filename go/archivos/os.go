package archivos

import (
	"fmt"
	"log"
	"os"
)

func BasicsOsOperations() {
	fname := "fichero.txt"
	var fichero *os.File
	fmt.Printf("%T\n", fichero)

	create(fname)
	write(fname)
	read(fname)
	truncate(fname)
	info(fname)
	delete(fname)
}


func create(fname string) {
	fichero, err := os.Create(fname)
	if err != nil {
		log.Fatal(err)
	}
	fichero.Close()
}

func write(fname string) {
	fichero, err := os.OpenFile(fname, os.O_WRONLY, 0644)
	if err != nil {
		log.Fatal(err)
	}
	defer fichero.Close()

	byteSlice := []byte("What a luck man!")
	bytesWritten, err := fichero.Write(byteSlice)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("We write %d bytes to the file: %s\n", bytesWritten, fname)
}

func open(fname string) {
	fichero, err := os.OpenFile(fname, os.O_CREATE|os.O_APPEND, 0644)
	if err != nil {
		log.Fatal(err)
	}
	defer fichero.Close()
}

func read(fname string) {
	byteSlice, err := os.ReadFile(fname)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("File %s content:\n\t%v\n\t%s\n", fname, byteSlice, string(byteSlice))
}

func truncate(fname string) {
	if err := os.Truncate(fname, 0); err != nil {
		log.Fatal(err)
	}
}

func info(fname string) {
	var fInfo os.FileInfo
	fInfo, err := os.Stat(fname)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("File name:", fInfo.Name())
	fmt.Println("File size:", fInfo.Size())
	fmt.Println("File permissions:", fInfo.Mode())
}

func delete(fname string) {
	if err := os.Remove(fname); err != nil {
		log.Fatal(err)
	}
}
