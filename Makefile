all: *.c *.cpp *.hs

	gcc problem_1.c -O2 -o problem_1
	gcc problem_2.c -O2 -o problem_2
	gcc problem_3.c -O2 -o problem_3 -lm
	gcc problem_4.c -O2 -o problem_4 -lm
	gcc problem_6.c -O2 -o problem_6

	g++ problem_5.cpp -O2 -o problem_35
	g++ problem_31.cpp -O2 -o problem_31

	ghc problem_1.hs -O2 -o problem_1
	ghc problem_2.hs -O2 -o problem_2
	ghc problem_3.hs -O2 -o problem_3
	ghc problem_4.hs -O2 -o problem_4
	ghc problem_5.hs -O2 -o problem_5
	ghc problem_6.hs -O2 -o problem_6
	ghc problem_7.hs -O2 -o problem_7
	ghc problem_8.hs -O2 -o problem_8
	ghc problem_9.hs -O2 -o problem_9
	ghc problem_10.hs -O2 -o problem_10
	ghc problem_11.hs -O2 -o problem_11
	ghc problem_12.hs -O2 -o problem_12
	ghc problem_13.hs -O2 -o problem_13
	ghc problem_14.hs -O2 -o problem_14
	ghc problem_15.hs -O2 -o problem_15
	ghc problem_16.hs -O2 -o problem_16
	ghc problem_17.hs -O2 -o problem_17
	ghc problem_18.hs -O2 -o problem_18
	ghc problem_19.hs -O2 -o problem_19
	ghc problem_20.hs -O2 -o problem_20
	ghc problem_21.hs -O2 -o problem_21
	ghc problem_22.hs -O2 -o problem_22
	ghc problem_23.hs -O2 -o problem_23
	ghc problem_24.hs -O2 -o problem_24
	ghc problem_25.hs -O2 -o problem_25
	ghc problem_26.hs -O2 -o problem_26
	ghc problem_27.hs -O2 -o problem_27
	ghc problem_28.hs -O2 -o problem_28
	ghc problem_29.hs -O2 -o problem_29
	ghc problem_30.hs -O2 -o problem_30
	ghc problem_31.hs -O2 -o problem_31
	ghc problem_32.hs -O2 -o problem_32
	ghc problem_33.hs -O2 -o problem_33
	ghc problem_34.hs -O2 -o problem_34
	ghc problem_35.hs -O2 -o problem_35
	ghc problem_36.hs -O2 -o problem_36
	ghc problem_37.hs -O2 -o problem_37
	ghc problem_38.hs -O2 -o problem_38
	ghc problem_39.hs -O2 -o problem_39
	ghc problem_40.hs -O2 -o problem_40
	ghc problem_41.hs -O2 -o problem_41
	ghc problem_42.hs -O2 -o problem_42
	ghc problem_43.hs -O2 -o problem_43
	ghc problem_44.hs -O2 -o problem_44
	ghc problem_45.hs -O2 -o problem_45


clean:

	rm -rf __pycache__
	rm -f Common.hi problem_?.hi problem_??.hi  # Haskell cache
	# Clean all executables and object files
	fish -c '\
	for FILE in (ls);                                                                             \
		if [ ! -d $$FILE ]; and [ (dd if=$$FILE bs=4 count=1 2>/dev/null) = (printf "\x7fELF") ];  \
			rm $$FILE;                                                                            \
		end;                                                                                      \
	end;                                                                                          \
	'
