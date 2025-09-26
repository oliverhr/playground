;; -----------------------------------------------------------------------------
;; Recursion
;; for, list comprehensions, loops
;; -----------------------------------------------------------------------------

(let [x 1]
  (println "Increased:" (inc x))  ;; +1
  (println "Decreased:" (dec x))  ;; -1
  (println "Original" x))        ;; original value

;; Clojure `for`
;; - Be aware that is a list comprehension, NOT a for-loop
;; - generator function for sequence permutation
;; - Bindings behave like doseq

(def coll (for [letter [:a :b]
                number (range 3)]
            [letter number]))
(println coll)

(let [digits [1 2 3]]
  (println "1...n:"
    (for [x1 digits
          x2 digits]
      (* x1 x2))))

(println "squares:"
  (for [x (range 6)]
    (* x x)))

;; Loop & Recur
;; - loop defines bindings and act as a `recur` target
;; - recur is "classic" recursion it re-executes loop with new bindings
;; - the docs recommends to prefer a higher-order functions library instead
(def i-final
  (loop [i 0]                       ;; start a loop with i equals to 0
    (if (< i 10) (recur (inc i)) i) ;; if i is less than N i+1 and recur
  )                                 ;; otherwise return the binding i
)
(println "Final value after the loop:" i-final)

;; recur must provide values for all bound symbols by position
(defn -inc [i]
  (if (< i 10) (recur (inc i)) i))  ;; when the condition is false
(println "From 0 to:" (-inc 0))     ;; the binding value is returned

