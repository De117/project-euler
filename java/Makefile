build: */*.java

	javac */*.java -d classfiles/

run: build

	java --class-path classfiles/ problems.Main

clean:
	rm -rf classfiles/
