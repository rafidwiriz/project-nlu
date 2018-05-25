import spacy

# Melakukan POS tagging dengan menggunakan model fasttext Indonesia yang telah dikonversi
nlp = spacy.load('E:/Transformers/My Book/Python/svara_voice/model/id_model')
doc = nlp(u'Budi membeli dua buah pisang')

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

# Hasil: token hanya berisi informasi teks, lemma, shape, isAlpha dan isStop.
#        Sedangkan bagian POS dan tag tidak memiliki informasi sama sekali.
# Masalah: model yang digunakan tidak menyertakan tagger untuk tiap token.