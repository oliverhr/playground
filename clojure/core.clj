(ns api.core
  (:gen-class))

;; -----------------------------------------------------------------------------
;; function signature
;; name     "doccmt"     params        body

(defn -greet [name]
  "Single parameter `name`"
  (str "Hello, " name))

;; multi arity functions define the params in the forms
(defn -messenger                                          ; No params here
  "Multy arity functions - mimic overloading"
  ([] (-messenger "Hello, Welcome Buddy!"))               ; Zero params
  ([msg] (println msg)))                                  ; One param

; Variadic functions
(defn -variadic
  [greeting & _who]
  (comment
    "The `&`` ampersand symbol is used as the rest operator this means all
    the params sent to the function are collected into a single varible,
    in this case named as `_who`.
    note: the `*` asterisk symbol can be used for the same purpose there is
    no clear difference.
    ref: https://clojure.org/reference/special_forms#_fn_name_params_expr
    "
  )
  (println greeting _who))

; def vs defn
(def -hell-o (fn [name] (str "Hello, " name)))
(defn -hello [name] (str "Hello, " name))

; Apply
(defn f [& args] (println "f args:" args))
(apply f '(1 2 3 4))
(apply f 1 '(2 3 4))
(apply f 1 2 '(3 4))
(apply f 1 2 3 '(4))

;; -----------------------------------------------------------------------------
;; Locals and Closures
;; (let [name value] (code that uses name))
(let [x 4
      y 5]
  (println "x + y =" (+ x y)))

(defn -local-scope-example [txt]
  (let [a 7
        b 5
        c (clojure.string/capitalize txt)]
    (println a b c)
  ) ;; this is where the `let` scope ends
)   ;; and here is the end of the function

(defn -messenger-builder [greeting]
  (fn [who] (println greeting who))) ; Closes over greeting

;; Greeting provider
(def hello-er (-messenger-builder "Que pedo"))

;; The greeting value `hello` is still available because it was "encapsulated"
(hello-er "Myfren!!")

;; =============================================================================
((fn []
   "IIFE Inmediatelly Invoked Function Expression"
   (println "Running the app...")
   (println (-greet "Oliver") "Welcome to ;:Clojure:;")
   (-messenger)
   (-variadic "Hi! nice to meet you" "foo" "bar" "baz")
   (println (-hell-o "Foo") "and" (-hello "Bar"))
   (-local-scope-example "this text must be CAPITALIZED")
))

;; -----------------------------------------------------------------------------

; Anonymous functions
(println "8^2 =" ( (fn [x] (* 2 x)) 8))
(println "4^2 =" ( #(* 2 %) 4))
(#(println %1 %2 %3 %&) "uno" "dos" "tres" "cuatro" "cinco")

