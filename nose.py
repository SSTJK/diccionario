meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "Es una exprecion de risa que proviene de un emoji"
            "CREEPY":"Es una exprecion qeu se usa cuando algo da miedo o es siniestro"
            }
for i in range(5)
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    
    else:
        print("¡Problemas con el internet!,")
