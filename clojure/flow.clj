;; -----------------------------------------------------------------------------
;; Flow control
;; -----------------------------------------------------------------------------
;; Expressions vs Statements
;; in programming languages like Java expressions returns values
;; whereas statements not
(comment
"
```javascript
const n = 99
let x = 'less or equal'

// statement
if (n > 10) {
  s = 'greater'
}
// expression
s = n > 10 ? 'greater' : 'less or equal'
```
"
; - IN CLOJURE EVERYTHING RETURNS A VALUE
; - In clojure everything is an expression
; - and a block of multiple expressions returns the last value
; - Expressions that exclusively permorm side-effects returns nil
; - Accordingly Flow Control operators are expressions too
)

;; -----------------------------------------------------------------------------

(println (str "2 is " (if (even? 2) "even" "odd")))

; else is optiona; else is optionall
(println (if (true? true) "impossible!"))
(println (if (true? false) "impossible!"))

;; Truth
;; In clojure all values are logically true or false.
;; all other values are logically true.
(println "if true:" (if true :truthy :falsy))
(println "if (Object.) objects are true:" (if (Object.) :truthy :falsy))
(println "if 0 zero is true:" (if (Object.) :truthy :falsy))
;; The only "false" values inclojure are `false` and `nil`
(println "false is" (if false :truthy :falsy))
(println "nil is:" (if nil :truthy :falsy))

;; -----------------------------------------------------------------------------
;; if and do

(print "the number is: ")
(if (even? 5)
  (do (println "even")
      true)
  (do (println "odd")
      false))

;;`when` is an `if` with only a then branch.
;; - it checks a condition and then evaluates any number of statements
;; - No `do` is required
;; - The value of the last expression is returned.
;; - IF the condition is FALSE `nil` is returned.
(let [x -1]
  (when (neg? x)
    ; (throw (RuntimeException. (str "Exception: x must be positive: " x)))
    (println "x is negative")
  )
)

;; `cond` is a series of tests and expressions
;; - each test is evaluated in order
;; - the first expression evaluated to `true` is returned
(let [y 5]
  (println (cond
             (< y 2) "y is less than 2"
             (< y 10) "y is less than 10")))

;; `cond` and `else`
;; - if no test is satisfied, nil is returned
;; - a common idiom is to use a final test of :else keywordd this
;;   always evaluate to `true` this becasue remember that all the
;;   values are logically true, except for `false` and `nil`
(let [z 11]
  (println (cond
             (< z 2) "z is less than 2"
             (< z 10) "z is less than 10"
             :else "z is greater than or equal to 10")))

;; `case` compares an argument to a series of values to find a match
;; - this is done in constant time (like matching a dictionary item by key)
;; - The value who acts as "key" must be a compile-time literal:
;;   [number, string, keyword, etc]
(defn -foo [x]
  (case x
    5 "x is 5"
    10 "x is 10"))
(-foo 10)

(defn -foo-else [x]
  (case x
    0 "x is 0"
    1 "x is 1"
    "x is neither 0 nor 1"))
(-foo-else 11)

;; Iteration
;; `dotimes` evaluate expression n times; it reetun nil
(dotimes [i 3]
  (println "i:" i))

;; `doseq`
;; - iterates over a sequence
;; - if a lazy sequence, forces evaluation
;; - returns nil
(doseq [n (range 3)]
  (println "n:" n))

;; doseq with multiple bindings
;; - similar to nested foreach loops
;; - processes all permutations of sequence content
;; - returns nil
(doseq [letter [:a :b]
        number (range 3)] ; this evaluates a list from 0 to 2
  (prn [letter number]))

;; Clojure `for`
;; - is a list comprehension, not a for-loop
;; - generator function for sequence permutation
;; - Bindings behave like doseq

(for [letter [:a :b]
      number (range 3)]
  [letter number])


