(ns api.collections
  (:gen-class))

(defn -line
  ([] (-line "-"))
  ([ch] (println (apply str (repeat 60 ch))))
)

(defn -vectors []
  "Vectors is a stack data structure, sequential and indexed
  to create it use the square bracktes symbol `[]`
  or the function `vector`, you can observe that is the
  default collection type to define params/arguments/"
  (let [x [2 4 6 8]]
    (println "El vector construido localmente x:" x)
    (println "El numero de items es:" (count x))
    (println "El primer item es:" (first x))
    (println "El segundo item es:" (get x 1))
    (println "El ultimo item es:" (last x))
    (println "Constructor para vector:" (vector 1 3 5))
    ;; note: the items on a vector are appended (pushed)
    ;;       the original item is inmutable so a new
    ;;       collection is returned/created
    (println "Agregando items a x:" (conj x [1 3 5]))
    (println "Agregando x como items:" (conj [1 3 5] x))
  ))

(defn -lists []
  "List on clojure are implemented as a linked list therefore
  this collection has no index access, also on lists the new
  items items are added at the head (begginning) of the list
  instead of the tail (end) like in vectors"
  (let [x '(10 :ace :jack 9)]
    (println "Lista x:" x)
    (println "Contructor para lists:" (list 10 :spade :queen 9))
    (println "El numero de items en la lista:" (count x))
    (println "El primer item es:" (first x))
    (println "El resto de los items son:" (rest x))
    (println "El ultimo item es:" (last x))
    ;; note: the items on a list are inserted at the front of
    ;;       the collceiton like `unshift` in JS.
    (println "Agregando items a la lista x:" (conj x :king))
    ;; The collection can be used with functions like a stack
    ;; so we have functions to access the items:
    (println "Muestra el item al inicio de la lista:" (peek x))
    (println "Remueve el item inicial y regresa una lista nueva:\n" (pop x))
))

;; =============================================================================
((fn []
   (println "Running the app...")
   (-line "=")
   (-vectors)
   (-line)
   (-lists)
   (-line)
))

