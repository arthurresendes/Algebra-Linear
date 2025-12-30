from sentence_transformers import SentenceTransformer

modelo_portugues = SentenceTransformer('serafim-100m-portuguese-pt-sentence-encoder')
frase = "Olá eu quero assitir TV"
embedding_portugues = modelo_portugues.encode(frase)

print(embedding_portugues)
print(embedding_portugues.shape)


modelo_multilingua = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
frase2 = "Olá eu quero assitir TV with drink water"
embedding_multilingua = modelo_multilingua.encode(frase2)

print(embedding_multilingua)
print(embedding_multilingua.shape)