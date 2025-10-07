package mapsnstructs

import "fmt"

type estado struct {
	nombre  string
	capital string
}

func Mexico() {
	var texas estado
	fmt.Println(texas)

	ags := estado{nombre: "Yucatan", capital: "Merida"}
	zac := estado{"Zacatecas", "Fresnillo"}
	fmt.Println(ags, zac)

	var mexico = map[string]estado{}
	mexico["ags"] = ags
	mexico["zac"] = zac
	mexico["cdmx"] = estado{"Ciudad de México", "Zocalo"}
	for abrev, estado := range mexico {
		fmt.Println(abrev, estado)
	}

	parcial := estado{
		nombre: "Veracruz",
	}
	fmt.Println(parcial)
	fmt.Println("Nombre:", parcial.nombre)
	fmt.Println("Capital:", parcial.capital)

	apuntador(&zac)
}

func apuntador(entidad *estado) {
	fmt.Println("------------------------------------------")
	fmt.Println("Pointer:", entidad)
	fmt.Println("entidad.nombre:", entidad.nombre)
	entidad.capital = "Guadalupe"
	fmt.Println("*entidad.nombre:", (*entidad).capital)
}
