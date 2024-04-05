import arquivoClasse as module

# Função principal
def main():
    questionario = module.Questionario()
    
    while True:
        opcao = input("\n1 - Fazer pesquisa // 2 - Mostrar tabela // 3 - Remover pesquisa // ou 00 para sair: \n")
        
        if opcao == '1':
            questionario.coletar_informacoes()
            questionario.escrever_csv()
            questionario.exibir_resultados()
        elif opcao == '2':
            questionario.exibir_resultados()
        
        elif opcao == '3':
            
            questionario.remove_linha()
        
        elif opcao == '00':
            break
        else:
            print("Opção inválida. Por favor, escolha '1', '2' ou '00'.")

main()