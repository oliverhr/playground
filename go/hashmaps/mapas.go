package mapsnstructs

import (
	"fmt"
)

func keyint() {
	var mapa = map[int]string{
		33: "Texas",
		1:  "Aguascalientes",
		7:  "Distrito Federal",
		32: "Zacatecas",
	}

	mexico := mapa
	fmt.Println(mexico)

	delete(mexico, 33)
	capital := mapa[7]
	fmt.Println(capital)

	mapa[7] = "CDMX"
	fmt.Println(mapa[7])
	fmt.Println(capital)

	for i, state := range mapa {
		fmt.Println(i, "\t", state)
	}

	if _, exists := mapa[31]; !exists {
		mapa[31] = "Yucatan"
	}
	fmt.Println(mapa)
}

func iterate() {
	var mapa = map[string]string{
		"first": "Oliver",
		"last":  "Rangel",
	}
	mapa["middle"] = "JG"

	for key, value := range mapa {
		fmt.Println(key, value)
	}

}

func emptyliteral() {
	var mapa = map[string]int{}
	mapa["cero"] = 0
	fmt.Println(mapa)
}

func literalmap() {
	var mapa = map[string]int{
		"uno": 11,
		"dos": 22,
	}
	mapa["tres"] = 33
	fmt.Println(mapa)
}

func makemap() {
	var mapa = make(map[string]int)
	if mapa == nil {
		fmt.Println("Mapa esta vacio")
	}
	fmt.Println(mapa, mapa == nil)

	mapa["cuatro"] = 99
	mapa["cinco"] = 55
	if mapa != nil {
		fmt.Println(mapa)
	}
}

func nilmap() {
	var nilMap map[string]int

	if nilMap == nil {
		fmt.Println("Map is NIL (also empty)")
		fmt.Println(nilMap)
	}
	fmt.Println()
	anotherNilMap := map[string]int{}
	if anotherNilMap != nil {
		fmt.Println("Not NIL, just empty")
		fmt.Println(anotherNilMap)
	}
}

func Mapas() {
	fmt.Println("---------------------\n", "Nil map")
	nilmap()

	// fmt.Println("---------------------\n", "Empty literal")
	// emptyliteral()

	// fmt.Println("---------------------\n", "Literal map")
	// literalmap()

	// fmt.Println("---------------------\n", "Make map")
	// makemap()

	// fmt.Println("---------------------\n", "Iterate")
	// iterate()

	// fmt.Println("---------------------\n", "Key int")
	// keyint()
}
