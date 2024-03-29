import pandas as pd
#import openpyxl
tabela = pd.read_excel("Produtos.xlsx")
#print(tabela)

# Modify the service tax
tabela.loc[tabela["Tipo"]=="Serviço","Multiplicador Imposto"] =1.5
    
# Calculate the updated price for the new service tax
tabela["Preço Base Reais"] = tabela["Preço Base Original"]*tabela["Multiplicador Imposto"]

print(tabela)

# Create an updated sheet without pandas indexes
tabela.to_excel("ProdutosUpdated.xlsx",index=False)



