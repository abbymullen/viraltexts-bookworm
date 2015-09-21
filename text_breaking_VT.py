import pandas as pd
import json
a = pd.read_csv("part-00001")

metadata_file = open('jsoncatalog.txt','w')
texts = open('input.txt',"w")

for row in a.iterrows():
    # This is a dictionary of the row attributes with the csv's names
    indexed = row[1]; # Pandas stores the dict as the second item.
    metadata = dict()
    for key in ["uid","cluster","size","date","id","series","title","url","ed","issue","corpus","text"]: # This can be longer
        metadata[key] = indexed[key]
    metadata["filename"] = str(indexed["uid"])
    metadata_file.write(json.dumps(metadata) + "\n")
    texts.write("%d\t%s\n" %(indexed["uid"],indexed["text"].replace("\n"," ")))