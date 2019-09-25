# 

IDIR =../include
CC=gcc
CFLAGS=-I$(IDIR)

ODIR=obj
LDIR =../lib

LIBS=-lm

_DEPS = hellomake.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))   # $(patsubst pattern,replacement,text)
                                          # Finds whitespace-separated words in text that match pattern and replaces them with replacement.
                                          # Here pattern may contain a ‘%’ which acts as a wildcard
                                          # What this line does: replace dependency files with their full paths

_OBJ = hellomake.o hellofunc.o 
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))  # Here, replace obj files with their full paths


$(ODIR)/%.o: %.c $(DEPS)   # Put .o files in the obj directory
	$(CC) -c -o $@ $< $(CFLAGS)

hellomake: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean  # The .PHONY rule keeps make from doing something with a file named clean

clean:  # clean rule here cleans all files under obj and include dirs that end with .o or ~, or named core or hellomake
	rm -f $(ODIR)/*.o *~ core $(IDIR)/*~  hellomake




