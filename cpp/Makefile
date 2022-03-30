all: *.cpp

	g++ problem_5.cpp -O2 -o problem_35
	g++ problem_31.cpp -O2 -o problem_31


clean:

	# Clean all executables and object files
	fish -c '\
	for FILE in (ls);                                                                             \
		if [ ! -d $$FILE ]; and [ (dd if=$$FILE bs=4 count=1 2>/dev/null) = (printf "\x7fELF") ];  \
			rm $$FILE;                                                                            \
		end;                                                                                      \
	end;                                                                                          \
	'
