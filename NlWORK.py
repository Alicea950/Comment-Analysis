from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import mysql.connector
stop_words = set(stopwords.words('english'))



ucomment = """This is a sample sentence,
                  showing off the  stop words filtration."""

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(ucomment)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)


ps = PorterStemmer()

i=0;

for w in filtered_sentence:
    print(ps.stem(w))
    word = ps.stem(w)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='1Socialnetpy')
    cursor = conn.cursor()
    cursor.execute("SELECT *  FROM negtb WHERE words  like '%" + word + "%'  ")
    data2 = cursor.fetchone()
    if data2:
        i += 1
        uname = data2[1]

    else:
        print('no data')


print(i)

