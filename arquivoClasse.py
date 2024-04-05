import pandas as pd
import datetime
import os

class Questionario:
    def __init__(self,nome_arquivo='questionario.csv'):
        self.nome_arquivo = nome_arquivo
        self.perguntas = [
            "Pergunta 1? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Pergunta 2? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Pergunta 3? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Pergunta 4? (1 - Sim, 2 - Não, 3 - Não sei): "
        ]
        self.backup =  []
        
        if os.path.exists(nome_arquivo):
            self.respostas = pd.read_csv(nome_arquivo).to_dict('records')
            self.num_linhas = len(self.respostas)
        else:
            self.respostas = []
            self.num_linhas = 0
    
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

        respostas = {'ID': self.num_linhas+1,'Idade': idade, 'Gênero': genero}
        self.num_linhas += 1
        
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

    def escrever_csv(self):
        if os.path.exists(self.nome_arquivo):
            df = pd.read_csv(self.nome_arquivo)
            new_df = pd.DataFrame(self.respostas)
            
            # Verifica se há respostas duplicadas antes de adicionar
            df = pd.concat([df, new_df], ignore_index=True).drop_duplicates()
        else:
            df = pd.DataFrame(self.respostas)
        df.to_csv(self.nome_arquivo, index=False)

    def exibir_resultados(self):
        df = pd.DataFrame(self.respostas)
        print("\nResultados do Questionário: \n")
        print(df)
        print(f'Numero de linhas: {self.num_linhas}')

    def remove_linha(self):
        id = int(input('Digite o ID a ser deletado'))
        for i, resposta in enumerate(self.respostas):
            if resposta['ID'] == id:
                self.backup = self.respostas[i]
                del self.respostas[i]
                self.num_linhas -= 1
                df = pd.DataFrame(self.respostas)
                
                
                
                
                
                print(f'\nessa linha foi deletada {self.backup}')
                del self.respostas[i]
                self.num_linhas -= 1
                return True
        return False
