#!/usr/bin/env bb

(require '[babashka.fs :as fs]
         '[clojure.edn :as edn])

(def ENTRIES-LOCATION "entries.edn")

(defn read-entries
  []
  (if (fs/exists? ENTRIES-LOCATION)
    (edn/read-string (slurp ENTRIES-LOCATION))
    [])
)

(defn add-entry
  [text]
  (let [entries (read-entries)]
    (spit ENTRIES-LOCATION
          (conj entries {:timestamp (System/currentTimeMillis)
                         :entry text}))))

(add-entry (first *command-line-args*))

