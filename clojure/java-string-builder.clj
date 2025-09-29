;; -----------------------------------------------------------------------------
;; Working with scripts
;; -----------------------------------------------------------------------------

;; Clojure is not pure or better sayed purist
;; regarding inmutability for this the interop
;; with java is a nice feature

;; StringBuilder: a mutable sequence of characters

(def cadena
  (let [builder (StringBuilder.)]
    (.append builder "This is")
    (.append builder " aa more")
    (.append builder " efficient way!")
    (.toString builder)))
(println cadena)

