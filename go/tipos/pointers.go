package tipos

import "fmt"

type car struct {
	brand string
	price int
}

func changeCar(c *car, newBrand string, newPrice int) {
	c.price = newPrice
	c.brand = newBrand
}

func (c *car) updateCar(brand string, price int) {
	c.brand = brand
	c.price = price
}

func pointers() {
	vocho := car{brand: "Vocho", price: 35_000}
	vocho.print()

	changeCar(&vocho, "Ferrari", 126_000)
	vocho.print()

	vocho.updateCar("VolksWagen", 215_000)
	vocho.print()
}

func (c car) print() {
	fmt.Printf("Brand: %s, Price: %d\n", c.brand, c.price)
}
