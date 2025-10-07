package archivos

/**
 * Writing to files using the package: io/ioutil
 */
import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

// IOUtil was deprecated since Go 1.16
// documentation ask to use "io" or "os" packages
// For the sake of this example we still to ioutil

func IOWriteFileOperations() {
	var fname string = "archivo.txt"
	fmt.Println()

	escribir(fname)
	leer(fname)
}

func escribir(fname string) {
	bs := []byte("Que onda con Golang, es super cool!")
	err := ioutil.WriteFile(fname, bs, 0644)
	if err != nil {
		log.Fatal(err)
	}
}

func leer(fname string) {
	bs, err := os.ReadFile(fname) // ioutil.ReadFile(fname) <- Deprecated
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("Contenido del archivo:", fname)
	fmt.Println(bs)
	fmt.Println(string(bs))
}
