package logging

import (
	"errors"
	"log"
)

func Logging() {
	base()
	settingGlobalFlags()
	logFatalErrors()
}

func base() {
	name := "The App"
	log.Println("Demo Software")
	log.Printf("%s is here", name)
	log.Print("Run.\n")
}

func settingGlobalFlags() {
	// Set the configuration for the calls to log.Functions from here
	// Does not matter if they are on a different context
	log.SetFlags(log.Ldate | log.Lmicroseconds | log.Llongfile)
	appName := "Golinator"
	log.Println("Some text")
	log.Printf("%s Application name", appName)
	log.Print("executing.\n")
}

func logFatalErrors() {
	log.Println("Starting application")
	err := errors.New("Application aborted.")
	if err != nil {
		log.Fatalln(err) // print the error and terminate de app with exit status 1
	}
	log.Println("----- This is never reached! -----")
}
