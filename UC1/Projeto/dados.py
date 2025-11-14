# dados.py

# Lista compartilhada entre cliente e garçom
# Mantém pedidos até o pagamento finalizar
pedidos_abertos = []

# Cardápio fixo dividido por categorias
# Cada item = (nome, preço, descrição)
cardapio = {
    "Sushis": [
        ("Atum (6 unidades)", 32, "Sushi de atum fresco, arroz e alga"),
        ("Camarão (6 unidades)", 34, "Sushi de camarão cozido"),
        ("Salmão (6 unidades)", 33, "Sushi de salmão selecionado")
    ],

    "Sashimis": [
        ("Atum (6 unidades)", 34, "Fatias de atum fresco"),
        ("Salmão (6 unidades)", 36, "Fatias de salmão"),
        ("Peixe Branco (6 unidades)", 30, "Fatias de peixe branco")
    ],

    "Temakis": [
        ("Philadelphia (1 unidade)", 25, "Salmão, cream cheese, arroz e alga"),
        ("Philadelphia Hot (1 unidade)", 27, "Versão empanada com cobertura"),
        ("Camarão (1 unidade)", 29, "Temaki de camarão com cream cheese")
    ],

    "Yakisobas": [
        ("Carne (400g)", 25, "Macarrão com carne e legumes"),
        ("Frango (400g)", 24, "Macarrão com frango e legumes"),
        ("Legumes (400g)", 23, "Macarrão com legumes frescos")
    ],

    "Sobremesas": [
        ("Harumaki Doce de Leite (1 unidade)", 12, "Rolinho crocante com doce de leite"),
        ("Harumaki Chocolate (1 unidade)", 12, "Rolinho crocante com chocolate"),
        ("Brownie (1 unidade)", 15, "Brownie de chocolate")
    ],

    "Bebidas": [
        ("Refrigerante Lata", 7, "350ml"),
        ("Água sem Gás", 2, "500ml"),
        ("Água com Gás", 3, "500ml")
    ]
}