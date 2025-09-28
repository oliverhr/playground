;; Sequences
;;
;; Clojure defines many algorithms in terms of sequences (seqs)
;; A sequence is a logical list. Clojure uses a ISeq interface to
;; allow data structures to access to their elements as sequences.
;;
;; (sequence coll) (sequence xform coll) (sequence xform coll & colls)
;; - sequences represent iteration as values
;; - consumers can partially iterate
(println "With a list:"
         (sequence '(1 2 3)))

(println "With a vector"
         (sequence [1 2 3]))

(println "With a map:"
         (sequence {:a 1 :b 2 :c 3}))

(println "Seq with a map:"
         (seq {:a 1 :b 2 :c 3}))

(println "Sequence called with multiple collections:"
 (sequence (map vector) [1 2 3] [:a :b :c]))

(println "With a string:"
         (sequence "abc"))

(println "SEQ for nil and empty collection returns nil:"
         (seq [])
         (seq nil))

(println "SEQUENCE for nil and empty collection returns an empty list:"
         (sequence [])
         (sequence nil))
