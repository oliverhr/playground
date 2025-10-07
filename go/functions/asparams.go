package functions

import (
	"fmt"
	"sort"
)

type Person struct {
	FirstName string
	LastName  string
	Age       int
}

func AsParams() {
	people := []Person{
		{"Pedro", "Paramo", 50},
		{"Dick", "Tracy", 33},
		{"Benito", "Bodoque", 12},
	}
	fmt.Println(people)

	// sort slice receives a function as param
	// we use an anonymus funtion declared in place
	sort.Slice(people, func(i, j int) bool {
		return people[i].LastName < people[j].LastName
	})
	fmt.Println(people)
}
