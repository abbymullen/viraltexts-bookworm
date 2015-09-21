all: part-00001 input.txt jsoncatalog.txt 

part-00001.txt:
	scp mullen.ab@discovery2.neu.edu:/home/dasmith/work/corpora/ca/c19-o08.out/out.csv/part-00001 ~/Documents/ViralTexts/Bookworm_Test

input.txt jsoncatalog.txt: part-00001.txt
	python text_breaking_VT.py 
	mv input.txt BookwormDB/files/texts
	mv jsoncatalog.txt BookwormDB/files/metadata

