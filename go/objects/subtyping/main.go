package subtyping

import (
	"fmt"
	"math"
)

// ####################### Interface #######################
type shape interface {
	area() float64
	perimeter() float64
}

// Funcion cliente o helper para los tipos "shape"
func showShapeInfo(s shape) {
	fmt.Println("Area:", s.area())
	fmt.Println("Perimeter:", s.perimeter())
}

// ########## Definición de shapes ##########

// ---------- Rectangle ----------
type rectangle struct {
	width, height float64
}

// Cumplimiento del contrato al imlementar
// las funciones area y perimeter
func (r *rectangle) area() float64 {
	return r.width * r.height
}
func (r *rectangle) perimeter() float64 {
	return 2 * (r.width + r.height)
}

// ---------- Triangle ----------
type triangle struct {
	sideA, sideB, sizeC float64
}

// Cumplimiento del contrato al imlementar
// las funciones area y perimeter
func (t *triangle) area() float64 {
	return 0.5 * (t.sideA * t.sideB) / 2
}
func (t *triangle) perimeter() float64 {
	sqroot := (t.sideA * t.sideA) + (t.sideB * t.sideB)
	return t.sideA + t.sideB + math.Sqrt(sqroot)
}

// ####################### Public #######################
// uso de implementaciones especificas y funciones cliente
func Run() {
	fmt.Print("This is how interfaces work in Golang\n")

	fmt.Println("Rectangle:")
	rect := rectangle{width: 3, height: 4}
	showShapeInfo(&rect)

	fmt.Println("Triangle:")
	tri := triangle{2, 3, 4}
	showShapeInfo(&tri)
}
