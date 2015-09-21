all: input.txt jsoncatalog.txt
username=mullen.ab

csvs/%:
	rsync -razv $(username)@discovery2.neu.edu:/home/dasmith/work/corpora/ca/c19-o08.out/out.csv/$* csvs

csvs:
	rsync -rav $(username)@discovery2.neu.edu:/home/dasmith/work/corpora/ca/c19-o08.out/out.csv/ csvs

input.txt jsoncatalog.txt: csvs/part-00001
	python text_breaking_VT.py

#	mv input.txt BookwormDB/files/texts
#	mv jsoncatalog.txt BookwormDB/files/metadata



