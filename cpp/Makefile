.PHONY: all build clean run

all: clean build run

# Name for the executable to be generate
# output := a.exe
folder := .
file := main.cpp

build:
	@# This is a non echoed comment
	@echo $@ '...Compiling'
	g++ -std=c++20 -Wall ${folder}/${file}

#run:
	#@echo $@ '...Executing'; echo ''
	#./${output}

#clean:
	#@echo $@ '...Cleaning'
	#rm -f ${output}
