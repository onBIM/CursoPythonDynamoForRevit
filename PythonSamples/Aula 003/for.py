# Dicionário de produtos
produtos = {
    "produto1": 100, 
    "produto2": 200, 
    "produto3": 300
}
    
for produto, preco in produtos.items():
    produtos[produto] = preco * 0.9
    print(f"O novo preço do {produto} é R$ {produtos[produto]}")