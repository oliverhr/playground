;; -----------------------------------------------------------------------------
;; Higher Order Functions
;; -----------------------------------------------------------------------------

(defn double-+
  [a b]
  (* 2 (+ a b)))
(println (double-+ 2 4))

(defn double-*
  [a b]
  (* 2 (* a b)))
(println (double-* 2 4))

;; the patter is clear `double-d` so can be writen
;; as a more composable functions receiving a function
;; as argument
(defn double-op
  [f a b]
  (* 2 (f a b)))

(println (double-op + 2 4))
(println (double-op * 2 4))

;; Anonymous functions (lambdas)
;; using fn
;; using function literal: #(...)
;; The function literal supports multiple arguments via %, %n, and %&.

(def bands [
            {:name "Rush" :genre :rock}
            {:name "Kiss" :genre :rock}
            {:name "Limon" :genre :regionalmx}
            {:name "Recodo" :genre :regionalmx}
])

(def rock-bands (filter #(= :rock (:genre %)) bands))
(println rock-bands)
