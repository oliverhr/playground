(ns api.hashes
  (:gen-class))

(defn -line
  ([] (-line "-"))
  ([ch] (println (apply str (repeat 60 ch))))
)

;; -----------------------------------------------------------------------------
;; Sets

(defn -sets []
  "Sets are like hash maps but their items are
  unique, also the order is not guaranteed"
  (println "sets")
  (let [players #{"Alice", "Bob", "Kelly"}]
    (println "Items en el set:" players)
    (println "Agregando al set:" (conj players "Fred"))
    ;; Note: if we try to remove an item which does not exists
    ;;       on the set, does not affect at all.
    (println "Removiendo del set:" (disj players "Bob" "Patrick"))
    ;; contains?
    (println "Revisando pertenencia:" (contains? players "Bob" ))
    (println "Revisando pertenencia:" (contains? players "Patrick" ))
    ;; The sort can be customized with a "comparator" using `sorted-set-by`
    (println "Ordenando sets:" (conj (sorted-set) "Zeta" "Bravo" "Charlie" "Sigma" "Alpha"))
    ;; Merging sets
    (let [players #{"Rambo" "Commando" "Aliens"}
          bench #{"Lethal-Weapon" "Die-Hard" "Terminator"}]
      (println "Combinando sets:" (into players bench)))
  )
)

;; -----------------------------------------------------------------------------
;; Maps

(defn -maps []
  (println "maps")
  (println {"Fred" 1400, "Bob" 1240, "Angela" 1024})
  (let [scores {"Fred" 1400 "Bob" 1240 "Angela" 1024}] (println scores))
  (let [scores {"Fred"    1400
                "Bob"     1240
                "Angela"  1024}]
    (println scores)
    (println "Agregando pares:" (assoc scores "Sally" 0))
    (println "Agregando mas pares:\n" (assoc scores "Adam" 128 "Sally" 0))
    ;; if the key already exists the value is replaced
    (println "'Actualizando' pares:" (assoc scores "Fred" 2048))
    ;; Removing elements
    (println "Quitando items:" (dissoc scores "Fred"))
    ;; Access items
    (println "Marca de Angela:" (get scores "Angela"))
    ;; Acces by key
    (println "Marca de Bob:" (scores "Bob"))
  )
  (-line)
  (let [directions {:north 0
                   :east  1
                   :south 2
                   :west  4}]
    (println "Norte:" (directions :north))
    (println "Sur" (directions :south))
    ;; This return nil but if the map is nil it will throw and error
    (println "Esto no existe (worth):" (directions :worth))
    ;; (let [bad-lookup-map nil] (bad-lookup-map :foo))
    ;; Looking up with a default value
    (println "Esto no existe (worth) pero:" (directions :worth -1))
    ;; checking just if a key exist
    (println "Existe 'north'?:" (contains? directions :north))
    (println "Existe 'worth'?:" (contains? directions :worth))
    ;; Finding and getting the item
    (println "Buscar 'north'?:" (find directions :north))
    (println "Buscar 'worth'?:" (find directions :worth))
    ;; Get the keys of the map
    (println "Llaves:" (keys directions))
    ;; Get the values of the map
    (println "Llaves:" (vals directions))
  )
  (-line)
  (let [players #{"Messi" "Cristiano" "Ronadinho"}]
    (println (zipmap players (repeat 0)))
    (println(into {} (map (fn [player] [player 10]) players)))
    (println (reduce (fn [m player]
                       (assoc m player 1))
                     {} ;; initial value
                     players))
  )
  (-line)
  (let [lineup {"Messi" 10
                 "Cristiano" 7}]
    (let [bench  {"Pele" 10
                   "Hugo" 9
                   "Maradona" 10}]
      (println lineup "\n" bench)
      (println (merge lineup bench)))
  )
  (-line)
  ;; Sorted maps
  (let [mapa (sorted-map
               "Zeta" 435
               "Bravo" 204
               "Alfa" 35
               "Sigma" 99
               "Charly" 100)]
    (println mapa)
    (println (keys mapa))
    (println (vals mapa)))
)

;; -----------------------------------------------------------------------------
;; Records

(defn -records []
  (println "Recods")
  (defrecord Person [first-name last-name age occupation])
  (def oliver (->Person "Oliver" "Rangel" 50 "Site Reliability Engineer"))
  (def marcela (map->Person
                 {:first-name "Marcela"
                  :last-name "Lucero"
                  :age 45
                  :occupation "Todologa"}))
  (println oliver)
  (println marcela)
  (:occupation marcela)
)

;; =============================================================================
((fn []
   (println "Running the app...")
   (-line "=")
   (-sets)
   (-line "=")
   (-maps)
   (-line)
   (-records)
))

