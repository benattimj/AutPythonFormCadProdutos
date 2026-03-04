Automação de Cadastro de Produtos com Python 

📌 Sobre o Projeto

Este projeto foi desenvolvido durante minha Jornada Python, com foco em Automação de Tarefas e criação de Bots.

A proposta foi automatizar o processo de cadastro de produtos em um formulário, eliminando tarefas repetitivas e reduzindo erros manuais.

A automação realiza:

Leitura e tratamento de dados

Preenchimento automático de campos

Navegação entre telas

Sincronização de cliques e movimentos do mouse

🛠️ Tecnologias Utilizadas
🐍 Python

Linguagem principal utilizada para desenvolvimento da automação.

🖱️ PyAutoGUI

Biblioteca responsável por:

Movimentação do mouse

Cliques automáticos

Digitação automática

Interação com a interface gráfica

Permitiu simular a ação humana passo a passo no sistema.

📊 Pandas

Utilizado para:

Leitura de planilhas (CSV/Excel)

Tratamento e organização dos dados

Limpeza de informações antes do envio ao formulário

Foi essencial para garantir que os dados estivessem estruturados corretamente antes da automação executar o cadastro.

⏱️ Time

Biblioteca usada para:

Controlar o tempo entre ações

Sincronizar carregamentos de tela

Ajustar pausas estratégicas para evitar falhas

🚀 Como Funciona

O script lê uma base de dados contendo os produtos.

Os dados passam por um tratamento utilizando Pandas.

O PyAutoGUI executa:

Abertura do sistema

Navegação até a área de cadastro

Preenchimento automático dos campos

O Time garante que cada etapa aconteça no momento certo, evitando erros de sincronização.
