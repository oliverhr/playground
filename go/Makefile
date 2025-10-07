.PHONY: all build clean run exe

all: clean build exe

# Name for the executable to be generate
output := application
folder := .

build:
	@# This is a non echoed comment
	@echo $@ '...Compiling'
	go build -o ${output}

run:
	@echo $@ '...Running'; echo ''
	go run .

exe:
	@echo $@ '...Executing'; echo ''
	./${output}

clean:
	@echo $@ '...Cleaning'
	rm -f ${output}
