package arraysnslices

import (
	"fmt"
	"sort"
)

/*
- slices are a sequence of values, meaning the allocation is consecutive
- Slices has "capacity" this means the number of consecutive locations reserved in memory
	- capacity es the ammount of items that a slice can have
	- lenght is the number of items added to the slice
	- when an item is added the length increase by 1
- sliced can grow as required since the length is not part of its type
- if we use [...], or [n] we are declaring an array
- if we use a set of empty brackets [] makes a slice
- slices are not comparable we can't use "==" or "!="
- sliced can only be compared using == nil
- to compare the elements of slices the type must be comparable
- to compare these elements we use the function:
	- "slices.Equal(sliceX, sliceB)"
	- "slices.EqualFun(fn)"

- The add elements to the slice the function "append" is used
- Append is a variadic function, meaning that can accept multiple parameters
- append does not affect the slice instead return a new slice
- since append return a slice the value (slice) returned must be assigned
	- x = append(x, 1, 2, 3)
	- y = append(x, y, ...) // chech the ... operator

*/

func slices() {
	// first thing to notice is that slices does not require the size to be specified
	ndf := []string{"", "Oliver", "Marcela", "Cocoy", "Sofia", "Layla"}

	fmt.Println(ndf[1:3])      // oliver, marcela
	fmt.Println(ndf[3:6])      // cocoy, sofia, layla
	fmt.Println(ndf[3:], "\n") // cocoy, sofia, layla

	a := [8]string{"Shanghai", "Hiroshima", "Jaipur", "Gorakhpur", "Nagpur", "Mumbai", "Nashik", "Lucknow"}
	ind_cities := a[2:] // 2:8 from jaipur to the las element
	maha_cities := ind_cities[2:5]

	fmt.Println("Cities =", a)
	fmt.Println("2:7", a[2:7])
	fmt.Println("2:5", maha_cities)

	fmt.Println("\n------------")
	var slc = make([]int, 4, 8)
	fmt.Printf("Length = %d", len(slc))
	fmt.Printf("\nCapacity = %d \n", cap(slc))
	slc[2] = 1
	fmt.Println(slc)

	fmt.Println("\n------------")
	var nilslc []string
	fmt.Println("Is the slice nil?:", nilslc == nil)
	fmt.Printf("Length of a NIL Slice = %d\n", len(nilslc))
	fmt.Printf("Capacity of NIL Slice = %d ", cap(nilslc))

	fmt.Println("\n------------")
	// Creating multi-dimensional slice
	multi := [][]string{
		[]string{"Rajasthan", "Jaipur"}, // this is redundant
		{"Maharashtra", "Mumbai"},       // so we simply can ommit
		{"Karnataka", "Bengaluru"},      // the []string part
	}
	fmt.Println("Slice multidimensional:\n", multi, "\n")

	sorting()
}

func sorting() {
	// Creating Slice
	slice1 := []string{"India", "Japan", "China", "Russia", "Singapore"}
	slice2 := []int{200, 500, 700, 400, 800, 300, 600, 900}

	fmt.Println("***** Before sorting *****")
	fmt.Println("Slice 1:", slice1)
	fmt.Println("Slice 2:", slice2)

	// Performing sort operation on slice
	sort.Strings(slice1)
	sort.Ints(slice2)
	fmt.Println("\n***** After sorting *****")
	fmt.Println("Slice 1:", slice1)
	fmt.Println("Slice 2:", slice2)
}

func tamanio() {
	var arr = [3]int{1, 2, 3}
	var slc = []int{1, 2, 3}

	xlice := make([]int, 3, 5)

	fmt.Println(arr, len(arr), cap(arr))
	fmt.Println(slc, len(slc), cap(slc))
	fmt.Println(xlice, len(xlice), cap(xlice))

	// declaring a nil slice
	var data []int
	fmt.Println(data, len(data), cap(data))
}

func Rabanadas() {
	tamanio()
}
