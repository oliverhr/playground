;; -----------------------------------------------------------------------------
;; Higher Order Functions
;; -----------------------------------------------------------------------------

(def mascots [
  {:name "Michi" :type :cat}
  {:name "Sparky" :type :dog}
  {:name "Solovino" :type :dog}
  {:name "Bicho" :type :cat}
])

(defn loop-dogs [coll]
  (loop [pets coll
         dogs []]
    (if (first pets)
      (recur (rest pets)
             (if (= :dog (:type (first pets)))
               (conj dogs (first pets))
               dogs))
      dogs)))

(println (loop-dogs mascots))

;; Instead filter can be used to simplify
;; the code, filter is a higher order function
;; because it receives a function as argument
;; function can be named or anonymous
(defn filter-dogs [pets]
  (filter #(= :dog (:type %)) pets))

(println (filter-dogs mascots))

;; Breaking down
(defn dog? [pet] (= :dog (:type pet)))
(defn filter-puppies [pets] (filter dog? pets))
(println (filter-puppies mascots))

