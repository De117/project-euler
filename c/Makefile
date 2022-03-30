all: *.c

	gcc problem_1.c -O2 -o problem_1
	gcc problem_2.c -O2 -o problem_2
	gcc problem_3.c -O2 -o problem_3 -lm
	gcc problem_4.c -O2 -o problem_4 -lm
	gcc problem_6.c -O2 -o problem_6


clean:

	# Clean all executables and object files
	fish -c '\
	for FILE in (ls);                                                                             \
		if [ ! -d $$FILE ]; and [ (dd if=$$FILE bs=4 count=1 2>/dev/null) = (printf "\x7fELF") ];  \
			rm $$FILE;                                                                            \
		end;                                                                                      \
	end;                                                                                          \
	'
