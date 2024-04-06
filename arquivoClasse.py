import pandas as pd
import datetime
import os

class Questionario:
    def __init__(self, nome_arquivo='questionario.csv', nome_arquivo_backup = 'backup.csv'):
        self.nome_arquivo = nome_arquivo
        self.nome_arquivo_backup = nome_arquivo_backup
        self.backup = []
        self.perguntas = [
            "Pergunta 1? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Pergunta 2? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Pergunta 3? (1 - Sim, 2 - Não, 3 - Não sei): ",
            "Pergunta 4? (1 - Sim, 2 - Não, 3 - Não sei): "
        ]
        self.linha_backup = []
        if os.path.exists(nome_arquivo):
            self.respostas = pd.read_csv(nome_arquivo)
            self.num_linhas = len(self.respostas)
        else:
            self.respostas = pd.DataFrame(columns=['ID', 'Idade', 'Gênero', 'Resposta 1', 'Resposta 2', 'Resposta 3', 'Resposta 4', 'Data/Hora'])
            self.num_linhas = 0

    
    def salva_backup(self):
        if os.path.exists(self.nome_arquivo_backup):
            self.backup = pd.read_csv(self.nome_arquivo_backup)
            new_df_backup = pd.DataFrame(self.linha_backup)
            self.backup = pd.concat([self.backup, new_df_backup], ignore_index=True).drop_duplicates()
            
        else:
            
            self.backup = pd.DataFrame(self.linha_backup)
            
        self.backup.to_csv(self.nome_arquivo_backup, index=False) 
            
        print(self.backup)

    
    def maior_id(self):
        if os.path.exists(self.nome_arquivo):
            maior_id = max(self.respostas['ID'].tolist())+1
        else:
            maior_id=1
        return maior_id
    
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

        respostas = {'ID': self.maior_id(),'Idade': idade, 'Gênero': genero}
        
        
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
        self.respostas = pd.concat([self.respostas, pd.DataFrame([respostas])], ignore_index=True)
        self.num_linhas +=1
        return True
    
    
    def remove_linha(self):
        id = int(input('Digite o ID a ser deletado: '))
        if id in self.respostas['ID'].tolist():
            self.backup = self.respostas[self.respostas['ID'] == id]
            self.respostas = self.respostas[self.respostas['ID'] != id]
            self.respostas.to_csv(self.nome_arquivo, index=False)
            self.num_linhas -= 1
            print(f'Linha com ID {id} removida do arquivo CSV.')
            print(self.linha_backup)
            self.salva_backup()
            print(self.respostas)
            return True
        else:
            print("ID não encontrado.")
            return False

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

    