
;; Sequences
;; (sequence coll) (sequence xform coll) (sequence xform coll & colls)
;; - sequences represent iteration as values
;; - consumers can partially iterate
(println "With a list:"
         (sequence '(1 2 3)))

(println "With a vector"
         (sequence [1 2 3]))

(println "With a map:"
         (sequence {:a 1 :b 2 :c 3}))

(println "Sequence called with multiple collections:"
 (sequence (map vector) [1 2 3] [:a :b :c]))

(println "With a string:"
         (sequence "abc"))

;; Reducers
;; - (v1.5) represent iteration as function composition
;; - Alternative approach to using sequences



