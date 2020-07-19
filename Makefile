all: *.c *.cpp *.hs

	gcc problem_1.c -O2 -o problem_1
	gcc problem_2.c -O2 -o problem_2
	gcc problem_3.c -O2 -o problem_3 -lm
	gcc problem_4.c -O2 -o problem_4 -lm
	gcc problem_6.c -O2 -o problem_6

	g++ problem_5.cpp -O2 -o problem_35
	g++ problem_31.cpp -O2 -o problem_31

	ghc problem_27.hs -O2 -o problem_27
	ghc problem_28.hs -O2 -o problem_28
	ghc problem_29.hs -O2 -o problem_29
	ghc problem_30.hs -O2 -o problem_30
	ghc problem_32.hs -O2 -o problem_32
	ghc problem_34.hs -O2 -o problem_34
	ghc problem_35.hs -O2 -o problem_35
	ghc problem_36.hs -O2 -o problem_36
	ghc problem_39.hs -O2 -o problem_39
	ghc problem_40.hs -O2 -o problem_40
	ghc problem_43.hs -O2 -o problem_43
	ghc problem_44.hs -O2 -o problem_44


clean:

	rm -rf __pycache__
	rm -f problem_??.hi  # Haskell cache
	# Clean all executables and object files
	fish -c '\
	for FILE in (ls);                                                                             \
		if [ ! -d $$FILE ]; and [ (dd if=$$FILE bs=4 count=1 2>/dev/null) = (printf "\x7fELF") ];  \
			rm $$FILE;                                                                            \
		end;                                                                                      \
	end;                                                                                          \
	'
