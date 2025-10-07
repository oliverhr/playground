package httpserial

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
	"sync"
)

func EntryPoint() {
	runner()
}

func runner() {
	var wg sync.WaitGroup
	urls := []string{
		"https://www.golang.org",
		"https://www.pedro.paramo.mx",
		"https://www.google.org",
		"https://www.medium.com",
	}

	wg.Add(len(urls))
	for _, url := range urls {
		go checkAndSaveBody(url, &wg)
	}
	wg.Wait()
}

func checkAndSaveBody(url string, wg *sync.WaitGroup) {
	defer wg.Done()

	res, err := http.Get(url)
	if err != nil {
		fmt.Println(err)
		fmt.Println("Site is Down!")
		return
	}
	defer res.Body.Close()

	fmt.Printf("%s -> Status Code: %d \n", url, res.StatusCode)
	if res.StatusCode == 200 {
		bodyBytes, _ := io.ReadAll(res.Body)
		file := strings.Split(url, "//")[1] + ".txt"

		fmt.Printf("Writing responde body to %s\n", file)

		err = os.WriteFile(file, bodyBytes, 0664)
		if err != nil {
			log.Fatal(err)
		}
	}
}
