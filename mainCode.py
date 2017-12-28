import ngram
import csv
from collections import Counter
import re


#---------------// the first port that create model of English Language //-----------------#

index = ngram.NGram(N=1)
Ngram_list_en = []
Ngram_list_other = []
main_list = []

with open('C:\Users\user\Documents\university\dest.tsv','r') as data:
    reader = csv.reader(data,delimiter='\t')
    for row in reader:
        if row[3] != None:
            if row[2]=='en':
                #create English language model
                Ngram_list_en = Ngram_list_en+list(index.ngrams(index.pad(row[3])))
            else:
                Ngram_list_other = Ngram_list_other+list(index.ngrams(index.pad(row[3])))

cnt = Counter(Ngram_list_en)

#sort and select 80 first N-grams
commonList = cnt.most_common(80)

# -------------- // the second port that create N-grams of a tweet and compare with English language model // ---------- #
# -------------- // then pridict the language of tweet // -------------------------------------------------------------- #

FP = 0
TP = 0
TN = 0
FN = 0

text = "this is a sample for evaluation method"
with open('C:\Users\user\Documents\university\dest2.tsv','r') as testData:
    reader = csv.reader(testData, delimiter='\t')

    for row in reader:
        tweet = row[3]
        tweet = re.sub("(http://t.co/)\w+", '', tweet)
        tweet = re.sub("(https://t.co/)\w+", '', tweet)
        tweet = re.sub("(#)\w+", '', tweet)
        tweet = re.sub("(@)\w", '', tweet)
        Ngram_list_test = list(index.ngrams(index.pad(tweet)))
        i = 0
        cnt2 = Counter(Ngram_list_test)
        diff = 0
        commonNewList = cnt2.most_common(50)

        for item in commonNewList:
            if item in commonList:
                diff = diff+commonList.index(item)-i
                i= i+1
                print "index: "+commonList.index(item)+"\n"
            else:
                i = i+1
                diff = diff + 80

        if diff/130 < 9:
            if row[2] == 'en':
                TP = TP+1
            else:
                FP = FP+1
        else:
            if row[2] == 'en':
                FN = FN+1
            else:
                TN = TN+1

# -------------------------- // evaluation // ---------------------------- #

recall = float(TP)/float(TP+FN)
precision = float(TP)/float(TP+FP)
F_measure = 2*recall*precision/(precision+recall)
print recall
print precision
print F_measure

