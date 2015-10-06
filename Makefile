all: part-00001 input.txt jsoncatalog.txt bookworm.cnf .bookworm bookwormdatabase

username=mullen.ab

part-00001:
	scp $(username)@discovery2.neu.edu:/home/dasmith/work/corpora/ca/c19-o08.out/out.csv/part-00001 $@

input.txt jsoncatalog.txt: part-00001
	python text_breaking_VT.py 

bookworm.cnf:
	bookworm init

.bookworm:
	bookworm init

bookwormdatabase: bookworm.cnf input.txt jsoncatalog.txt
	bookworm build all
