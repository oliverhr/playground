;; -----------------------------------------------------------------------------
;; Dealing with errors
;; -----------------------------------------------------------------------------
;; try/catchh/finally

;; exception handling
(try
  (/ 2 1)
  (catch ArithmeticException e "divide by zero")
  (finally (println "cleanup"))
)

;; throwing errors
(try
  (throw (Exception. "something went wrong"))
  (catch Exception e (.getMessage e))
)

(try
  (throw (ex-info "There was a problem" {:detail 42}))
  (catch Exception e
    (prn (:detail (ex-data e))))
)

;; -----------------------------------------------------------------------------
;; File name
(def file-sufix "-new.txt")

;; Writing to a file using try/catch
(let [f (clojure.java.io/writer (str "some" file-sufix))]
  (try
    (.write f "some text")
    (finally (.close f))
  )
)

;; idiomatic with: with-open
(with-open [f (clojure.java.io/writer (str "other" file-sufix))]
  (.write f "other text")
)

