CC=c99
CFLAGS=-Wextra -pedantic -c
LDFLAGS=

all: ephemeride edt clean
ephemeride: date.o ephemeride.o
	$(CC) date.o ephemeride.o -o $@
edt: cours.o salle.o date.o enseignant.o EDT.o
	$(CC) date.o salle.o enseignant.o cours.o EDT.o -o $@

depend:
	makedepend *.c -Y
# date.o: date.c date.h
# 	$(CC) $(CFLAGS) $<
# ephemeride.o: ephemeride.c
# 	$(CC) $(CFLAGS) $<
# EDT.o: EDT.c cours.h salle.h date.h enseignant.h
# 	$(CC) $(CFLAGS) $<
# cours.o: cours.c cours.h salle.h date.h enseignant.h
# 	$(CC) $(CFLAGS) $<
# enseignant.o: enseignant.c enseignant.h date.h
# 	$(CC) $(CFLAGS) $<
# salle.o: salle.c salle.h date.h
# 	$(CC) $(CFLAGS) $<

clean:
	rm *.o
.PHONY: clean all