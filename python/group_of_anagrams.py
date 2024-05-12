'''
Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the
letters of a different word or phrase, typically using all
the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
* 1 <= strs.length <= 10^4
* 0 <= strs[i].length <= 100
* strs[i] consists of lowercase English letters.
'''
from collections import defaultdict as hashmap	# con default dict nos ahorramos el dict.get o dict.default
from typing import List


def group_anagrams(words: List[str]) -> List[List[str]]:
	anagrams = hashmap(list)					# se crea un hashmap que cuyos valores por defectos son litas

	letters = ord('z') - ord('a') + 1			# cálculo con numero de letras en el alfabeto (26 de z...a)
	letter_a = ord('a')							# obtenemos el numero entero que le corresponde en ascii a la letra "a"

	for word in words:							# Se itera sobre la palabas del array
		count = [0] * letters					# Un array con 26 elementos inicializados a cero [0...0] == len(26)
		for letter in word:						# Por cada letra en la palabra en turno se aumenta el contador
			count[ord(letter) - letter_a] += 1	# se halla el indice que corresponde a la letra y se le suma + 1 al counter **
												# -- Las llaves de diccionarios solo pueden ser inmutables
		anagrams[tuple(count)].append(word)		# se pone una tupla como llave, con el array como key, sino existe se pone vacia
												# y se agrega la palabra a esa lista
	return anagrams.values()

# ** La parte que hace el truco es el array/lista del alfabeto, siempre tiene el mismo orden
# ** esto permite que sin importarla palabra no cambia el orden en la lista
# ** ya que es los indices se basan en el numero de la letra en el alfabeto.


if __name__ == '__main__':
	words = ["eat","tea","tan","ate","nat","bat"]

	print(group_anagrams(words))
