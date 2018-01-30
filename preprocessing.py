import csv
import re

with open('E:\university\weetlid-test-tweets.tsv','r') as src:
    with open('E:\university\dest.tsv', 'w') as dest:
        with open('E:\university\dest2.tsv', 'w') as dest2:
            r = csv.reader(src,delimiter='\t')
            w = csv.writer(dest,delimiter='\t')
            w2 = csv.writer(dest2,delimiter='\t')
            i = 0
            for row in r:
                text = row[3]
                text = re.sub("(http://t.co/)\w+", '', text)
                text = re.sub("(https://t.co/)\w+", '', text)
                text = re.sub("(#)\w+", '', text)
                text = re.sub("(@)\w", '', text)
                text = re.sub("([#@!$?.,;:*-+/^])", '', text)
                text = re.sub(r"\d", '', text)
                text = text.lower()
                if i > 300:
                    w.writerow([row[0],row[1],row[2],text])
                else:
                    w2.writerow([row[0], row[1], row[2], text])
                i = i+1



