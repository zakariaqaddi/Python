from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt 

mytext=open('mytext.txt','r').read()

stopwords=set(STOPWORDS)
Text_cloud=WordCloud(background_color='white',max_words=2000,stopwords=stopwords)
Text_cloud.generate(mytext)

plt.imshow(Text_cloud)
plt.axis('Off')
plt.show()
