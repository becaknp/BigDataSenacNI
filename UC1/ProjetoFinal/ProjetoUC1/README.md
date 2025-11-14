<h1>Projeto: Sistema de Pedidos - Restaurante Tanoshimi

Descrição
--------
Sistema completo em Python que simula o fluxo de atendimento de um restaurante japonês: cliente faz pedido via cardápio digital, garçom gerencia entregas, e sistema processa pagamentos com emissão de nota fiscal.

Arquivos
--------
- main.py → Menu principal integrando todos os sistemas
- dados.py → Cardápio e lista compartilhada de pedidos
- cliente.py → Fluxo completo do cliente: pedido, confirmação, pagamento e nota fiscal
- garcom.py → Sistema do garçom: visualizar e gerenciar status dos pedidos

Requisitos
----------
- Python 3.x
- Não requer bibliotecas externas

Como rodar
---------
1. Coloque os quatro arquivos no mesmo diretório.
2. No terminal, rode:
   - `python main.py`  -> para testar o sistema
3. Siga as opções no menu.

Fluxo de Sistema

Cliente entra → Digita nome → Acessa cardápio → Monta pedido → Confirma → Volta ao menu

Garçom entra → Visualiza pedidos → Marca como "Entregue" → Volta ao menu

Cliente entra novamente → Sistema detecta pedido pronto → Vai direto para pagamento

Funcionalidades implementadas
-----------------------------
Sistema Cliente

- Cardápio digital organizado em 6 categorias com descrições
- Montagem de pedido com adição/remoção de itens
- Resumo interativo e confirmação antes do envio
- Cálculo automático de totais e subtotais em tempo real
- ID único para cada pedido (5 dígitos aleatórios)
- Sistema de pagamento com Pix, Cartão (1-3x) e Dinheiro
- Nota fiscal completa com CNPJ e dados fiscais
- Validação de mesa e confirmação dupla antes do pagamento

Sistema Garçom

- Visualização unificada de todos os pedidos ativos
- Controle de status (Na Cozinha / Entregue)
- Dar baixa em pedidos entregues
- Interface simplificada com numeração automática

Processo de Pagamento

- Busca por mesa para localizar pedidos
- Confirmação dupla com nome, mesa, itens e total
- Múltiplos métodos com parcelamento opcional
- Nota fiscal profissional com todos os dados exigidos

Estruturas de Dados Utilizadas

- Dicionários → Cardápio por categorias
- Listas → Pedidos abertos, itens do pedido
- Tuplas → Itens do cardápio (nome, preço, descrição)
- Set → Métodos de pagamento válidos
- Constantes → MESA_FIXA para todos os clientes

Conceitos Python Aplicados

- Controle de fluxo: While/For loops, If/Elif/Else
- Tratamento de erros: Try/Except com mensagens específicas
- Funções: Modularização e reutilização de código
- Importação: Compartilhamento de dados entre módulos
- Validação: Entradas numéricas e opções de menu
- Formatação: Preços (R$X ou R$X.XX) e layout visual

Observações
-----------
- O sistema é didático e usa apenas estruturas e comandos do módulo.
- O projeto foi pensado para ser simples de rodar e explicar na apresentação.

Créditos
--------
Desenvolvido por: Rebeca Knupp da Silva
Curso/Módulo: Analista de dados big data science 
Módulo: DESENVOLVER ALGORITMOS, VERSIONAMENTOS E LINGUAGEM DE CONSULTA ESTRUTURADA

