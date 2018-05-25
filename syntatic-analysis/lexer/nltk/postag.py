from nltk.tag import CRFTagger

# Melakukan POS tag dengan menggunakan CRF Tagger NLTK dan model tagger Indonesia
ct = CRFTagger()
ct.set_model_file('E:/Transformers/My Book/Python/project-nlu/syntatic-analysis/lexer/nltk/all_indo_man_tag_corpus_model.crf.tagger')

kalimat = 'Budi membeli dua buah pisang'
hasil = ct.tag_sents([kalimat.split()])

print(hasil)
print(type(hasil[0][0]))

# Hasil: tiap token dapat menampilkan POS