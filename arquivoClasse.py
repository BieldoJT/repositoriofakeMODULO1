import pandas as pd
import datetime
import os

class Questionario:
    def __init__(self,nome_arquivo='questionario.csv'):
        self.respostas = []
        self.perguntas = [
            "Pergunta 1? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Pergunta 2? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Pergunta 3? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Pergunta 4? (1 - Sim, 2 - Não, 3 - Não sei): "
        ]
        
        if os.path.exists(nome_arquivo):
            self.respostas = pd.read_csv(nome_arquivo).to_dict('records')
        else:
            self.respostas = []

    def coletar_informacoes(self):
        while True:
            try:
                idade = int(input("\nDigite sua idade (00 para não inserir dados):\n"))
                if idade == 0:
                    return False
                elif idade < 0 or idade > 150:
                    raise ValueError("Idade inválida. Por favor, insira uma idade válida.")
                break
            except ValueError as e:
                print(e)

        while True:
            genero = input("\nDigite seu gênero (M/F):\n ").upper()
            if genero in ['M', 'F']:
                break
            else:
                print("Gênero inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")
                
        ##botar o codigo pra verificar o numero de linhas e adicionar o id como chave

        respostas = {'Idade': idade, 'Gênero': genero}
    
        
        for i, pergunta in enumerate(self.perguntas, start=1):
            while True:
                resposta = input(pergunta)
                if resposta in ['1', '2', '3']:
                    break
                else:
                    print("Resposta inválida. Por favor, insira '1', '2' ou '3'.")

            #colocando a resposta em texto na tabela
            if resposta == '1':
                respostas[f'Resposta {i}'] = 'sim'
            elif resposta == '2':
                respostas[f'Resposta {i}'] =  'não'
            else:
                respostas[f'Resposta {i}'] = 'não sabe'
            
        respostas['Data/Hora'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.respostas.append(respostas)
        return True

    def escrever_csv(self, nome_arquivo='questionario.csv'):
        if os.path.exists(nome_arquivo):
            df = pd.read_csv(nome_arquivo)
            new_df = pd.DataFrame(self.respostas)
            df = pd.concat([df, new_df], ignore_index=True)
            
        else:
            df = pd.DataFrame(self.respostas)
        df.to_csv(nome_arquivo, index=False)


    def exibir_resultados(self):
        df = pd.DataFrame(self.respostas)
        print("\nResultados do Questionário: \n")
        print(df)
        