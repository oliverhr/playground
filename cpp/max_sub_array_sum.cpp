#include <iostream>
#include <type_traits>

#define _n "\n"

int solution1(int n, int arr[]) {
	int best = 0;
	for (int i = 0; i < n; i++) {
		int sum = 0;
		for (int j = i; j < n; j++) {
			// cout  << arr[j] << ", ";
			sum += arr[j];
			best = std::max(best, sum);
		}
		// cout << _n;
	}
	return best;
}

int solution2(int n, int arr[]) {
    int best = 0;
    int sum = 0;
    int counter = 0;
    for (int i = 0; i < n; i++) {
        counter++;
        // esta parte es la importante en este algoritmo
        // sum detecta si en algun momento el valor
        // del item corriente es mayor que lo que se
        // lleva acumuado en la suma
        // best solo hace la comparativa y va conservando
        // el valor mayor que se haya visto.
        //
        // El valor de suma puede cambiar y bajar eso
        // nos indica que se romperia una racha de
        // un sub-array pero no afecta a la respuesta
        // ya que el valor mayorse conserva en best.
        sum = std::max(arr[i], sum + arr[i]);
        best = std::max(best, sum);
    }
    std::cout << "Steps: " << counter << _n;
    return best;
}

int main() {
   	const int n = 8;
	int arr[n] = {-1, 2, 4, -3, 5, 2, -5, 2};

	std::cout << "Solution 1: " << solution1(n, arr) << _n;
	std::cout << "Solution 2: \n" << solution2(n, arr) << _n;
}
