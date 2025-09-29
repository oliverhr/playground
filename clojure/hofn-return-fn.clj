;; -----------------------------------------------------------------------------
;; Higher Order Functions
;; -----------------------------------------------------------------------------

;; Functions returning functions

(defn adder [x]
  (fn [a] (+ x a))
)

;; note the value passed to adder is "retained"
;; this is because is a closure
(def add-five (adder 5))

(println (add-five 37))


