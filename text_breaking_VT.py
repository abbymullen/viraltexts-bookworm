import re
import json

def snippetyielder(filename):
	"""
	This function takes a text file with many small documents in it, and returns those documents broken out into 
	individual units. """
	text = open(filename, "r")
	a = text.readlines()
	p = "".join(a)

	docbreak = re.sub(r"(\"*-*\d{19}\"*)",r"DOCBREAK \1",p)
	docbreaks = docbreak.split("DOCBREAK") 	  #yielding one document at a time
	for doc in docbreaks:
		if re.search(r".+",doc): 	
			yield doc 	


class Document():
	def __init__(self, doc):
		self.doc = doc

	def test(self):
		return self.doc + 'BREAK\n'

	def id(self):
		id = re.search(r"\d{19}",self.doc)
		return id.group()

	def raw_text(self):
		raw_text = re.sub(r"(.+,){17}(.+)",r"\2",self.doc)
		raw_text = re.sub(r"\s",r" ",raw_text)
		raw_text = re.sub(r"\"",r"",raw_text)
		return raw_text

	def get_date(self):
		get_date = re.search(r"\d{4}-\d{2}-\d{2}",self.doc)
		if get_date:
			get_date = get_date.group()
			return get_date
		return "no_date"

	def page_no(self):
		page_no = re.search(r"seq-(\d+)",self.doc)
		if page_no:
			page_no = page_no.group(1)
			return page_no
		return "no_page"

	def sn(self):
		sn = re.search(r"(sn\d{8})/\d{4}-\d{2}-\d{2}",self.doc)
		sn2 = re.search(r"(\d{10})/\d{4}-\d{2}-\d{2}",self.doc)
		sn_trove = re.search(r"http://trove.nla.gov.au/ndp/del/article/(\d+),",self.doc)
		sn_moa = re.search(r"idno=([a-z]{4}\d{4}-\d+),",self.doc)
	
		if sn:
			sn = sn.group(1)
			return sn
		if sn2:
			sn2 = sn2.group(1)
			return sn2
		if sn_trove:
			sn_trove = sn_trove.group(1)
			return sn_trove
		if sn_moa:
			sn_moa = sn_moa.group(1)
			return sn_moa
		return "no_sn"


if __name__=="__main__":
	f = open("input.txt", "a")
	j = open("jsoncatalog.txt", "a")
	for snippet in snippetyielder("part-00001.txt"):
		doc = Document(snippet)
		# f.write(doc.sn() + '\n')
		f.write(doc.id() + '\t' + doc.raw_text() + '\n')
		data = {'searchstring': doc.get_date() + ' / ' + doc.raw_text()
		, 'date': doc.get_date()
		, 'filename': doc.id()
		, 'page_number': doc.page_no()
		, 'sn': doc.sn()
		, 'full_text': doc.raw_text()
		}
		data_string = json.dumps(data)
		j.write(data_string + '\n')

	j.close()
	f.close()