from nltk import word_tokenize
from nltk.tag import CRFTagger

# Melakukan POS tag dengan menggunakan CRF Tagger NLTK dan model tagger Indonesia
ct = CRFTagger()
#ct.set_model_file('E:/Transformers/My Book/Python/project-nlu/syntatic-analysis/lexer/all_indo_man_tag_corpus_model.crf.tagger')
ct.set_model_file('E:/Transformers/My Book/Python/project-nlu/syntatic-analysis/lexer/id_gsd-ud-train-morphind.crf.tagger')

kalimat = 'Budi membeli dua buah pisang.'
token = word_tokenize(kalimat)
hasil = ct.tag_sents([token])[0]

print(hasil)
#print(type(hasil))

# Hasil: tiap token dapat menampilkan POS