package estructuras

import (
	"fmt"
)

type Book struct {
	title  string
	author string
	year   int
}

func printBook(libro *Book) {
	fmt.Printf("Book: %s, %s, %d\n", libro.title, libro.author, libro.year)
}

func basics() {

	libro1 := Book{"The divine comedy", "Dante Aligheri", 1320}

	libro2 := Book{
		title:  "Macbeth",
		author: "Shakespeare",
		year:   1606,
	}

	var libro Book
	libro.title = "El Llano en Llamas"
	libro.author = "Juan Rulfo"
	libro.year = 1953

	printBook(&libro1)
	printBook(&libro2)
	printBook(&libro)

	// partial item with zero values
	lastBook := Book{title: "Mil Risas"}
	fmt.Printf("%#v\n", lastBook)
}

func howCopyStruct() {
	oldBook := Book{"The divine comedy", "Dante Aligheri", 1320}
	newBook := oldBook

	fmt.Println(oldBook == newBook)

	newBook.year = 1999
	fmt.Println(oldBook == newBook)

	fmt.Printf("%+v\n", oldBook)
	fmt.Printf("%+v\n", newBook)
}
