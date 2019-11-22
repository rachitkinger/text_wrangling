# remove simple stopwords + single character words
# tokenize words  
# lemmatize  
import nltk 

stop_words = nltk.corpus.stopwords.words('english')
wtk = nltk.tokenize.RegexpTokenizer(r'\w+')
wnl = nltk.stem.wordnet.WordNetLemmatizer()

def normalize_corpus(corpus): 
    norm_corpus = []
    for doc in corpus:
        doc = doc.lower()
        doc_tokens = [token.strip() for token in wtk.tokenize(doc)]
        doc_tokens = [wnl.lemmatize(token) for token in doc_tokens if not token.isnumeric()]
        doc_tokens = [token for token in doc_tokens if len(token) > 1]
        doc_tokens = [token for token in doc_tokens if token not in stop_words]
        doc_tokens = list(filter(None, doc_tokens))
        if doc_tokens:
            norm_corpus.append(doc_tokens)
    return norm_corpus