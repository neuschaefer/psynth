psynth: psynth.c
	gcc -std=c99 -O1 -o $@ -ljack $<

notes.h: notes.py
	./notes.py 48000 > notes.h
