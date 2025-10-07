package mutexes

import (
	"fmt"
	"sync"
	"time"
)

/**
Mutex [ Mutual Exclution ]

Un mutéx o bloqueo de exlusión mutua, es una especie de candado que
permite solo a un hilo el tener el acceso al recurso compartido entre
varios procesos, con el fin de evitar las condiciones de carrera.

Lost mutexes o exclusiones mutuas se utilizan para proteger los datos
u otros recursos en los que se tenga un acceso concurrente.

La especificación de un mutex se realiza a traves de atributos los
cuales definen sus caracteristicas.
*/

func EntryPoint() {
	fmt.Println("Ejemplo de MUTEX:")
	exclusionMutua()
}

func exclusionMutua() {
	const gr = 200
	var wg sync.WaitGroup
	var m sync.Mutex

	var n int = 0

	fn := func(v int) {
		time.Sleep(time.Second / 10)
		m.Lock()
		n += v
		m.Unlock()
		wg.Done()
	}

	wg.Add(gr * 2)
	for i := 0; i < gr; i++ {
		go fn(1)
		go fn(-1)
	}
	wg.Wait()

	fmt.Println("Final value of n:", n)
}
