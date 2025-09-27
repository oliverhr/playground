;; Reducers
;; - A "reducable"" collection is a collection which knows how to reduce itself.
;; - A reducer is a reucible collection with a reducing function
;; - (v1.5) represent iteration as function composition
;; - Alternative approach to using sequences
;; - clojure.core.reducers namespace (aliased here as r)
;;   provides an alternate r/reduce function
;; Note:
;;      - look up for the concept of "foldable" in clojure
;;      - r/fold
;;      - r/foldcat

(require '[clojure.core.reducers :as r])

;; using fold to sum with +
;; - iterate over the collection
;; - increase the current item
;; - filter if even  (added to the collection)
;; - apply + to the filtered items
(defn -suma [col]
  (r/fold + (r/filter even? (r/map inc col))))
(let [sum (-suma [1 1 1 5])]
  (println sum))

;; Get all even numbers
;; - create a collection from range (to the limit)
;; - map (inc) increment over every item of the range
;; - filter the current item if is even
;; - filtered items are deposited into []

;; idiomatic
(defn -evens [limit]
  (into [] (r/filter even? (r/map inc (range limit)))))

(println (-evens 42))

;; Deconstructed
(defn -evens-def [limit]
   (def rango (range limit))
   (def incre (r/map inc rango))
   (def filt (r/filter even? incre))
   (into [] filt))

(println (-evens-deco 28))

;; Deconstructed with let
(defn -evens-loc [limit]
   (let [_ (range limit)]
     (let [_ (r/map inc _)]
       (let [_ (r/filter even? _)]
         (into [] _)))))
(println (-evens-loc 14))

