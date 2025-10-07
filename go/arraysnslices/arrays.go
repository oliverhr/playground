package arraysnslices

import "fmt"

// Arrays are rarely used directly in go
// is more commonly used the slices


// Arrays are a single type with static number
// of predeclared items

// Arrays are 0 indexed

// To get and element from an array the brackets notation
// is used array[3]


func Arreglos() {
	var nums [10]int
	fmt.Println(nums)

	vec := [2][2]string{
		{"Oliver", "Rangel"},
		{"Jose", "Hernandez"},
	}
	fmt.Println(vec)

	fmt.Println("")
	arr := [5]int{4, 8, 16, 32, 64}
	fmt.Println(arr)

	fmt.Println(arr[3:])
	fmt.Println(&arr[3], ":", arr[3])
	fmt.Println(&arr[4], ":", arr[4])
	fmt.Println("")

	// Elipsis ... the numbers of items is upon  inmediate assigment
	ndf := [...]int{1, 2, 4, 8, 16, 32, 64, 128}

	for index := 0; index < len(ndf); index++ {
		fmt.Print(index, ":", ndf[index], ", ")
	}

	fmt.Println("\n")
	forloop(arr)
}

func forloop(array [5]int) {
	for _, value := range array {
		fmt.Println(value)
	}
}


func sparcedArrays() {
	// with this syntax we are creating an array with twelve positions
	// and telling that the index 5 value is 4 the index 10 value is 100
	// the rest of the elements respect, the  next position and the value
	// the non filled (sparced) items are zero value filled,
	// index six value is 6 and the index eleven value is 15
	var sparced = [12]int{1, 5: 4, 6, 10:100, 15}
	fmt.Println(sparced)

	// the length of the array can be know with the function len
	fmt.Println(len(sparced))
}


