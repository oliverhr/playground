#!/usr/bin/env bb

;; -----------------------------------------------------------------------------
;; https://www.braveclojure.com/quests/babooka/
;; https://github.com/braveclojure/babooka
;; -----------------------------------------------------------------------------
(require '[clojure.string :as str])
;; note the syntax for the require, here no namespace is declared
;; in clojure requiring in this way is considered bad practice

;; pr/prn :  produce output for the reader, output is quoted
(prn (str/join " " ["Hello," "inner" "world!"]))

;; print/println :  produce output for humans
(println (str/join " " ["Hello," "inner" "world!"]))

;; -----------------------------------------------------------------------------

(prn ["It's" "me," "your" "wacky" "subconscious!"])
(println ["It's" "me," "your" "wacky" "subconscious!"])

(println (str "Hello from -> " *ns* " <-, inner world!"))

