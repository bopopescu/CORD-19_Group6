# APPLY YAKE MODEL
import csv
import pandas as pd
import pandas as pd
import csv
import matplotlib
import wordcloud
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import yake
stopwords = set(STOPWORDS)

# open metadata file and cleaning
with open(r"E:\Helen\FinalProject_INFO5731\All_DS_CORD19\DS_CORD19_1st\all_sources_metadata_2020-03-13.csv", "r",  newline="", encoding='utf-8') as file:
    df= pd.read_csv(file)
file.close()

df['abstract']=df['abstract'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df['abstract']=df['abstract'].str.replace('[^\w\s,]','')
df['abstract']=df['abstract'].str.lower()

# convert type of data
text=''
for abstr in df['abstract'].dropna():
    text=text+str(abstr)

#print(text)
language = "en"
max_ngram_size = 3
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 1000

custom_kw_extractor = yake.KeywordExtractor(lan=language,  dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)
df_keywords = pd.DataFrame(keywords)

with open (r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Content_analysis\YAKEkeywords_DS1.csv", 'w',  newline="",
          encoding='utf-8') as file:
    df_keywords.to_csv(file)

# plot the wordcloud
'''
kw_str = ''
for kw in keywords:
    kw_str = kw_str + str(kw[0])
wordcloud = WordCloud(width=1600, height=1600,
                      background_color='white',
                      stopwords=stopwords,
                      min_font_size=23).generate(kw_str)

fig = plt.figure(figsize=(10, 10), facecolor=None)
plt.imshow(wordcloud)
title = "A WordCloud of Keywords"
plt.title(title, fontdict={'size': 20, 'color': 'black', 'verticalalignment': 'bottom'})
plt.axis("off")
plt.tight_layout(pad=0)
fig.savefig(r"E:\Helen\FinalProject_INFO5731\ALL_OUTPUTS\DS_1st\Content_analysis\all_keywords_Wordcloud.jpg", bbox_inches='tight', dpi=200)
plt.show()
'''