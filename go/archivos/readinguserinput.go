package archivos

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func InputScan() {
	scanUntilExit()
}

func scanUserInput() {
	scanner := bufio.NewScanner(os.Stdin)
	fmt.Printf("%T\n", scanner)

	fmt.Print("Enter you username: ")
	scanner.Scan()

	text := scanner.Text()
	fmt.Println("User input(text):", text)

	bytes := scanner.Bytes()
	fmt.Println("User input(bytes):", bytes)
}

func scanUntilExit() {
	scanner := bufio.NewScanner(os.Stdin)

	fmt.Print("Enter the data (exit to finish): ")
	for scanner.Scan() {
		text := scanner.Text()
		fmt.Println("You entered:", text)
		if text == "exit" {
			fmt.Println("\nScanning complete.")
			break
		}
		fmt.Print("Enter the data (exit to finish): ")
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
	fmt.Println("\nThank you!")
}
