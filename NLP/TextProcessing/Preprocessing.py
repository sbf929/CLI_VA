"""Contains class and function for basic text analysis using `spacy` and related libraries. ="""
import spacy
from colorama import Fore
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

from textblob import TextBlob
from spellchecker import SpellChecker
#-------------------------------------------------------------------------------------------------------------------------
# Personal libraries:
from NLP.TextProcessing.Spelling_Checker import Autocorrect, get_closest_match
from NLP.TextProcessing.Summary import extractive_summary_sentences, keywords_extraction
from BaseClasses import User
#-------------------------------------------------------------------------------------------------------------------------

class TextPreprocessor():
    """Class for Preproccessing text data (User commands)."""
    def __init__(self, n_sentences = 1, n_words = 10, model = 'en_core_web_sm', processors = None) -> None:
        # Spacy
        self.nlp = spacy.load(model)
        self.current_loaded_text = ""
        self.doc = self.nlp(self.current_loaded_text)

        # NLTK:
        self.ps = PorterStemmer()

        self.n_sentences = n_sentences # Number of summarized sentences(Extraction)
        self.n_words = n_words  # Number of keywords(Extraction)

        # Other libraries:
        self.spell = SpellChecker()

        self.processing_stack = [] # Main preprocessing stack

        if processors != None:
            if type(processors) != list:
                processors = list(processors)

            self.processing_stack = processors

        # Create Processing stack:


    def update_text(self, updated_text):
        """Use when required to process a new text body. Update the `self.current_loaded_text`."""
        self.current_loaded_text = updated_text

    def create_processing_stack(self, methods):
        """For creating a processing stack with the methods from this class `self.processing_stack`."""
        self.processing_stack = [getattr(self, method) for method in methods if callable(getattr(self, method))]

    def execute_processing_stack(self, text):
        """Takes in a `text`, and processes it with the processing methods in `processors`"list."""

        if type(text) != str:
            text = " ".join(text)
        # -------------------------------
        # Stack:
        print(self.processing_stack)
        for method in self.processing_stack:
            text = method(text)
        return text
        
    # --------------------------------------------------------------------------
        
    def lower_case(self, text):
        """Converts the given `text` into lowercase."""     
        doc = self.nlp(text)
        return doc.text.lower()

    def extractive_summarize(self, text):
        """Summarises the given text."""
        extractive_summary_sentences(text, 5, self.sentence_segmentation)

        keywords_extraction(text, 10, self.normalize_text)

    def autocorrect(self, text):
        """Autocorrects the `text`.""" 
        blob = TextBlob(text)
        corrected_words = blob.correct()

        return str(corrected_words)
        
    def get_closest_match(self, text, matching_list):
        """"""

    def sentence_segmentation(self, text, is_list = True):
        """Returns a `list` of the sentences in `text`as a list if `is_list` = `True`"""
        doc = self.nlp(text)
        sentences = [sent.text.strip() for sent in doc.sents]

        if is_list:
            return list(sentences) # Returns as a list
        else:
            return sentences # Returns as a generator

    def tokenise(self, text):
        """Return the tokens in the given `text`"""
        doc = self.nlp(text)
        tokens = [token.text for token in doc]

    def remove_punctuation(self, text):
        """Removes puctuation from the given `text`."""
        doc = self.nlp(text)
        tokens = [token.text for token in doc if not token.is_punct]

        return " ".join(tokens)
    
    def remove_stopwords(self, text):
        """Removes stopwatch from the given `text`."""
        doc = self.nlp(text)
        tokens = [token.text for token in doc if not token.is_stop]

        return " ".join(tokens)
    
    def lemmatize(self, text):
        """Returns the lemmetized text."""
        doc = self.nlp(text)
        lemmas = [token.lemma_ for token in doc]

        return " ".join(lemmas) 

    def stemming(self, text):
        """Returns the stemmed text ( `NLTK` )."""
        tokens = word_tokenize(text)
        stems = [self.ps.stem(token) for token in tokens]

        return " ".join(stems)

    def remove_numeric(self, text):
        doc = self.nlp(text)
        tokens = [token.text for token in doc if token]

        return " ".join(tokens)
    
    def named_entity_recognition(self, text):
        """Returns the recognised entity and it type as a ``."""
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]

        print(entities)
        return entities

    def parts_of_speech_tagging(self, text):
        """Identify the parts of speech for each token."""
        doc = self.nlp(text)
        pos_tags = [(token.text, token.pos_) for token in doc]

        return pos_tags
    
    def remove_non_alphabetic(self, text):
        """Removes non - alphabetic tokens."""
        doc = self.nlp(text)

        tokens = [token for token in doc if token.is_alpha]

        return tokens
    
    def normalize_text(self, text):
        """Contains multiple preproccesing steps. Returns the nomalized `text`."""
        doc = self.nlp(text.lower())

        tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]

        return " ".join(tokens)
    
    def sentiment_analysis(self, text):
        """Returns the sentiment of the given `text`. ( `textblob` )"""
        blob = TextBlob(text)
        sentiment = blob.sentiment

        return sentiment
    
    def dependency_parse(self, text):
        doc = self.nlp(text)
        dependencies = [(token.text, token.dep_, token.head.text) for token in doc]

        return dependencies
    
    def vectorize_text(self, text):
        """Returns the `text` as a multidimensional array (Tensor)."""
        doc = self.nlp(text)

        return doc.vector
    
    def generate_ngram(self, text, n:int = 2, is_list = True):
        """Return an n-gram based on `n`. Returns it as a `list` if, `is_list` = `True`."""
        tokens = text.split() 

        n_grams = ngrams(tokens, n)

        if is_list:
            return list(ngrams)
        
        else:
            return ngrams

    #def encode_text(text, vocab, max_len):

class PreprocessingStack(TextPreprocessor):
    """Class for creating precessing stacks using functions from `TextPreprocessor`."""

    def __init__(self, n_sentences=1, n_words=10, model='en_core_web_sm', processors=None, processing_methods = []):
        super().__init__(n_sentences, n_words, model, processors)
        self.processing_methods = processing_methods
        self.stack = []

        # Create the stack on initialization:
        self.create_processing_stack(preprocessor_v1)

    def create_processing_stack(self, preprocessor_instance):
        """Creates a preprocessing stack based on given methods."""
        self.stack = [getattr(preprocessor_instance, method) for method in self.processing_methods if hasattr(preprocessor_instance, method)]
    
    def execute_processing_stack(self, text):

        for method in self.stack:

            text = method(text)

        return text
    
# Create different types of Text Processors:
#-------------------------------------------------------------------------------------------------------------------------
preprocessor_v1 = TextPreprocessor()
preprocessor_v1_ner = PreprocessingStack(processing_methods = ['lower_case', 'autocorrect', 'lemmatize', 'named_entity_recognition'])
preprocessor_v1_pos = PreprocessingStack(processing_methods = ['lower_case', 'autocorrect', 'parts_of_speech_tagging'])
#-------------------------------------------------------------------------------------------------------------------------

print(preprocessor_v1.parts_of_speech_tagging("Hello, would you like to play football?"))
#print(preprocessor_v1_ner.execute_processing_stack("The Axis powers included Germany, Japan and Italy?"), "\n")

print(preprocessor_v1_ner.processing_methods, "\n\n", preprocessor_v1_ner.stack, "\n\n")

text = "The Axis powers included Germany, Japan and Italy?"
print(preprocessor_v1_pos.execute_processing_stack(text))