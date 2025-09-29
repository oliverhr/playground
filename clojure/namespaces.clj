;; -----------------------------------------------------------------------------
;; Namespaces
;; -----------------------------------------------------------------------------
;; https://clojure.org/guides/learn/namespaces
;;
;; Namespaces are similar to c++, c# namespaces and of course java packages
;; is a way to organize code and to avoid name collisions.

;; A ns is both a name context and a container for vars (def)

;; loading code in clojure is accomplished with `require`
;; require loads and reloads
;; can assign an alias using `:as` to a namespace
;; with refer works like python from ..import x tu use the unqualified name
;; think is similar to :as-alias but without loading the namespace

;; To use java packages/classes we need to use :import

(ns com.some-example.my-app
  "My app Example"
 (:require
   [clojure.set :as set]
   [clojure.string :as str]
   [clojure.set :refer [union intersection]])
 (:import
   [java.util Date UUID]
   [java.io File])
)
