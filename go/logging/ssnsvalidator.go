package logging

import (
	"errors"
	"fmt"
	"log"
	"strconv"
	"strings"
)

var (
	ErrInvalidSSNLength  = errors.New("Invalid SSN Length")
	ErrInvalidSSNNumbers = errors.New("Invalid SSN Numbers")
	ErrInvalidSSNPrefix  = errors.New("Invalid SSN Prefix")
	ErrInvalidDigitPlace = errors.New("Invalid SSN Digit Place")
)

func ValidateSSN() {
	ssns := []string{
		"123-45-6789",
		"013-8-678",
		"000-12-0962",
		"999-33- 3333",
		"087-65-4321",
		"123-45-zzzz",
	}

	for _, ssn := range ssns {
		fmt.Printf("\nValidating: '%s'\n", ssn)
		ssn = strings.Replace(ssn, "-", "", -1)

		var err error

		err = validateLength(ssn)
		if err != nil {
			log.Println(err)
		}

		err = validateOnlyNums(ssn)
		if err != nil {
			log.Println(err)
		}

		err = validatePrefix(ssn)
		if err != nil {
			log.Println(err)
		}

		err = validateDigitPlace(ssn)
		if err != nil {
			log.Println(err)
		}
	}
}

func validateLength(ssn string) error {
	ssn = strings.TrimSpace(ssn)
	if len(ssn) != 9 {
		return ErrInvalidSSNLength
	}
	return nil
}

func validateOnlyNums(ssn string) error {
	_, err := strconv.Atoi(ssn)
	if err != nil {
		return ErrInvalidSSNNumbers
	}
	return nil
}

func validatePrefix(ssn string) error {
	if !strings.HasPrefix(ssn, "000") {
		return ErrInvalidSSNPrefix
	}
	return nil
}

func validateDigitPlace(ssn string) error {
	firstDigit := string(ssn[0])
	keyDigit := string(ssn[3])
	if firstDigit == "9" && !strings.ContainsAny(keyDigit, "79") {
		return ErrInvalidDigitPlace
	}
	return nil
}
