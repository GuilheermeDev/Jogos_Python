import random

def jogar():
    
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavras = ['python', 'java', 'csharp', 'javascript', 'php', 'ruby', 'swift', 'html', 'css']
    palavra_secreta = random.choice(palavras)
    
    vida = 6
    
    palavra_descoberta = list("_" * len(palavra_secreta)) # Função para gerar a palavra secreta divida por underline
    

    while True:
        print(' '.join(palavra_descoberta)) # Inserir as palavras numa string vazia
        chute = input("Qual letra você gostaria de colocar? ").lower() # converte o input para letras minusculas e printa vazia
        
        if chute in palavra_secreta.lower(): # compara as letras 
            for i in range(len(palavra_secreta)):
                if palavra_secreta[i].lower() == chute: # compara as letras 
                    palavra_descoberta[i] = chute
           
            if '_' not in palavra_descoberta:
                print('Parabéns! Você acertou a palavra: ' + palavra_secreta)
                break
        else:
            vida -= 1 # Se errou perde uma vida
            print("Você errou, ainda lhe restam ", vida)
            if vida == 0: # Caso suas tentativas chegue a 0 você perde e revela a palavra
                print('Você perdeu! A palavra era: ' + palavra_secreta)
                break
    print("Fim")

if (__name__=="__main__"):
    jogar()
