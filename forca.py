def jogar():
    
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "maça"
    enforcou = False
    acertou = False
    
    while not enforcou and not acertou:
        chute = str(input("Qual letra você gostaria de colocar? "))
        
        index = 0
        for letra in palavra_secreta:
            if chute.upper().strip() == letra.upper().strip():
                print(f"Encontrei a palavra {chute} na posição {index} ")
            index += 1
        

    
















print("Fim do jogo")

if (__name__=="__main__"):
    jogar()