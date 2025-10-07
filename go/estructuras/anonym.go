package estructuras

import "fmt"

type Persona struct {
	firstName, lastName string
	year, month, day    int
}

func anonimas() {
	cocoy := Persona{
		firstName: "Lilia",
		lastName:  "Helu",
		year:      2001,
		month:     1,
		day:       2,
	}
	fmt.Printf("%#v\n", cocoy)

	alguien := struct {
		firstName, lastName string
		year, month, day    int
	}{
		"Lilia",
		"Helu",
		2001,
		1,
		2,
	}
	fmt.Printf("%#v\n", alguien)

	// data comparison must return true only if
	// data and struct signature is the same
	// if the struct properties are different
	// it will return an error
	fmt.Println("Cocoy es alguien?", alguien == cocoy)

	/*
		This is another way to declare a struct with anonymus fields
		the constraint is that you can not use duplicated types
		since the fields does not have a name.

		A struct can have named properties or fields in cmbination
		of anonymus fields.
	*/
	type People struct {
		string
		int
	}
	sofi := People{"Sofia Helu", 2006}
	fmt.Printf("%#v\n", sofi)

	layla := struct {
		string
		int
	}{
		"Layla Helu",
		2011,
	}
	fmt.Printf("%#v\n", layla)
}
