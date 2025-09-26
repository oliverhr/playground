(ns chapter.one)

;;##############################################################################
;; Iniciando con clojure
;;##############################################################################
(do (print "This is ") (println "My awesome clojure script\n"))

(comment
  ; La siguiente forma ejemplifica dos cosas:
  ; - funciones anonymas
  ; Son utilizada para ser enviadas como parametros a otras functiones

  ; - inmediatelly invoked expression como en Javascript las IIFE
  ; No son comunmente utilizadas pero pueden ser utiles pero
  ; como se puede ver en la funcion `-main` de este archivo resultan
  ; muy utiles
)
((fn [msg] (println msg)) "----------------------------------")

(defn -if-do [& args]
  "--------------------------------------------------------"
  " This is practice on how to use `if` statement and `do` "
  "--------------------------------------------------------"
  (if (first args)
    (do (println "Hello, World!")
        (println "Clojure is Cool"))
    (println "Clojure is weird.")))

(defn -when [bool]
  "
  ----------------------------------------------------------
  This is how we can use when instead of if-do
  ----------------------------------------------------------
  "
  (when bool
    (print "Param was truthy" "")
    (println "That's why this is displayed")
    )
  (println "This is always being diplayed.")
)

(defn -multi-arity
  ([] (-multi-arity "Hello"))
  ([msg] (println msg)))

(defn -variadic [msg nation & targets]
  "
  Variadic signatures the rest must be the last
  element on the params preceded with an ampersand
  "
  (println msg targets "I love" nation))

;; -----------------------------------------------------------------------------
;; Truthiness, nil and Equality
;;
;; in clojure nil is a falsy value in clojure when is evaluated
;; in a bolean expression
(defn -truthy-falsy []
  ; Nil
  (println (if nil "Truth" "False"))
  (println (if false "Truthy" "Falsy"))
  (println (if true "Verdadero" "Falso"))
  ; interrogation mark
  (println (if (true? "true") "Yes" "No"))
  (println (if (true? 1) "Yep" "Nop"))

  (println (if (false? nil) "Es falso" "Es cierto"))
  (println (if (false? false) "Si, es falso" "No, no es cierto"))

  (println (if (nil? nil) "Cierto esta vacio" "Tiene algo"))
  (println (if (nil? true) "??" "Nil no equivale a true"))
  (println (if (nil? false) "??" "Y tampoco Nil es identico a false"))

  (println (= [1 2 3] [1 2 3])) ; true
  (println (= '(1 2 3) [1 2 3])) ; true
  (println (= "hello" "hello" (clojure.string/reverse "olleh")))

  (println "not true =" (not true)) ; false
  (println "not nil =" (not nil)) ; true
  (println "not false =" (not false)) ; true
  (println "not 1==1" (not (= 1 1))) ; false
)


(comment
  let x = 50
  if (x >= 1 && <= 100 || x % 100 == 0) {
    console.log("Valid")
  } else {
    console.log("Invalid")
  }
)
(let [x 50]
  ; First approach
  (if (or (<= 1 x 100) (= 0 (mod x 100)))
    (println "Valido")
    (println "Invalido"))
  ; Second approach
  (println (if (or (<= 1 x 100) (= 0 (mod x 100)))
             "Es valido"
             "No es valido"))
)

;; =============================================================================

((defn -main []
  "---------------------------------------------------------
  This is the documentation for my clojure script
  ---------------------------------------------------------"
  (-if-do true)
  (-when false)
  (-multi-arity "Qué tal!")
  (-variadic "Foo" "Mexico" "Bar" "Baz")
  (-truthy-falsy)
))

; vim ft=clojure
