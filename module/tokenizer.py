from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
stemmer = StemmerFactory().create_stemmer()

from nltk.tag import CRFTagger
ct = CRFTagger()
ct.set_model_file('data/all_indo_man_tag_corpus_model.crf.tagger')
#ct.set_model_file('id_gsd-ud-train-morphind.crf.tagger')

def tokenize(sent_data):
    """SentenceData* -> None"""
    sent_data.set("tokens", sent_data.get("text").split())

def stem(sent_data):
    """SentenceData* -> None"""
    tokens = sent_data.get("tokens")
    stem_tokens = []
    for token in tokens:
        if not(token.startswith('(')):
            stem_word = stemmer.stem(token)
            stem_tokens.append(stem_word)
        else:
            stem_tokens.append(token)
    sent_data.set("stem", stem_tokens)
            
def pos(sent_data):
    """[str] -> [str]"""
    
    pos_tokens = []
    return pos_tokens