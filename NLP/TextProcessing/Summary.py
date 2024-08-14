"""Contains methods for summarisation."""
import spacy
nlp = spacy.load("en_core_web_sm")

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np

def extractive_summary_sentences(text, n_sentences: int, processor):
    """Performs extractive summary for filtering sentences in the `text, processed by `processor()`. Returns a `list` of top `n_sentences` sentences."""
    
    processed_sentences = processor(text)

    if not processed_sentences: 
        return ""

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(processed_sentences)

    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    sentence_scores = similarity_matrix.sum(axis = 1)

    ranked_sentences = [processed_sentences[i] for i in np.argsort(sentence_scores, axis = 0)[-n_sentences:]]

    summarized_text = " ".join(ranked_sentences)
    sentences = list(nlp(summarized_text).sents)

    return sentences[::-1]

    
def keywords_extraction(text, n_words: int = 1, processor = None):
    """Extracts the keywords from the given `text` after processing it with `processor()`. Returns a `list` of top `n_words` keywords."""  

    if processor == None:
        processed_sentences = text
    else:
        processed_sentences = processor(text)  

    tokens = " ".join(processed_sentences)

    # TF IDF:
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([tokens])

    feature_names = tfidf_vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()[0]

    # Get the keywords:
    top_keyword_indices = np.argsort(tfidf_scores)[-n_words:]
    keywords = [feature_names[i] for i in top_keyword_indices][::-1]

    return keywords