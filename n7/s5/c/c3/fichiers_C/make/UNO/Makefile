CC=c99
CFLAGS=-Wextra -pedantic -c
LDFLAGS=

all: test_uno jouer_uno clean
test_uno: uno.o carte.o main.o jeu.o test_uno.o
	$(CC) uno.o carte.o main.o jeu.o test_uno.o -o $@
jouer_uno: uno.o carte.o main.o jeu.o jouer_uno.o
	$(CC) uno.o carte.o main.o jeu.o jouer_uno.o -o $@
# jouer_uno.o: jouer_uno.c
# 	$(CC) $(CFLAGS) $<
# uno.o: uno.c
# 	$(CC) $(CFLAGS) $<
# carte.o: carte.c
# 	$(CC) $(CFLAGS) $<
# main.o: main.c 
# 	$(CC) $(CFLAGS) $<
# jeu.o: jeu.c
# 	$(CC) $(CFLAGS) $<
depend:
	makedepend *.c -Y

clean:
	rm *.o
.PHONY: clean all depend
