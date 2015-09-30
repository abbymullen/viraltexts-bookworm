all: part-00001 input.txt jsoncatalog.txt bookworm.cnf .bookworm bookwormdatabase

part-00001:
	scp mullen.ab@discovery2.neu.edu:/home/dasmith/work/corpora/ca/c19-o08.out/out.csv/part-00001 ~/Documents/ViralTexts/Bookworm_Test

input.txt jsoncatalog.txt: part-00001
	python text_breaking_VT.py 
	
bookworm.cnf:
	bookworm init

.bookworm:
	bookworm init

bookwormdatabase: bookworm.cnf input.txt jsoncatalog.txt
	bookworm build all
