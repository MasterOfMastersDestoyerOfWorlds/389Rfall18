all: loop

loop: main.c fib.o
	gcc main.c fib.o -o loop

fib.o: fib.S
	yasm -f macho64 fib.S

clean:
	rm loop fib.o

