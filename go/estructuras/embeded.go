package estructuras

import "fmt"

type Contact struct {
	email, address string
	phone          int
}

type Employee struct {
	name    string
	salary  int
	contact Contact
}

func embedded() {
	empleado := Employee{
		name:   "Pedro Paramo",
		salary: 80000,
		contact: Contact{
			email:   "pedro@paramon.mx",
			address: "El Llano en Llamas 101",
			phone:   5552723456,
		},
	}

	// initial data
	fmt.Printf("%+v\n", empleado)

	// updated data
	empleado.contact.address = "El Llano en Llamas #1, Comala, Colima"
	fmt.Printf("%+v\n", empleado)
}
