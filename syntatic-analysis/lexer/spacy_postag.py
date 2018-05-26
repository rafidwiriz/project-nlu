import spacy

# Melakukan POS tagging dengan menggunakan model fasttext Indonesia yang telah dikonversi
nlp = spacy.load('E:/Transformers/My Book/Python/svara_voice/model/model-final')
nlp2 = spacy.load('en_core_web_sm')
doc = nlp(u'Budi membeli dua buah pisang')
doc2 = nlp2(u'John buys two bananas')

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

for token in doc2:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)

# Hasil: token hanya berisi informasi teks, lemma, shape, isAlpha dan isStop.
#        Sedangkan bagian POS dan tag tidak memiliki informasi sama sekali.
# Masalah: model yang digunakan tidak menyertakan tagger untuk tiap token.