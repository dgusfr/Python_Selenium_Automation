# Teste de Carga com Flask, MySQL e JMeter

Este projeto é uma demonstração completa de um sistema para realizar cadastros em massa utilizando um backend em Flask, um banco de dados MySQL, e testes de carga realizados com o Apache JMeter. Ele permite avaliar o desempenho de aplicações submetidas a alto tráfego.

## Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Status](#status)
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Explicação](#explicação)
- [Como Usar](#como-usar)
- [Autor](#autor)

## Tecnologias Utilizadas

<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/python.png" alt="Python" width="100"/>
  </div>
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/flask.png" alt="Flask" width="100"/>
  </div>
</div>

## Status

![Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)

## Descrição

Este projeto consiste em uma aplicação web simples que permite:
- Realizar cadastros de clientes (nome, email, telefone) em um banco de dados MySQL.
- Testar o desempenho da aplicação utilizando o Apache JMeter para simulações de carga.
- Gerar relatórios detalhados de latência, throughput e taxa de erros.

## Funcionalidades

- Formulário web para cadastro de clientes.
- Backend desenvolvido em Flask.
- Banco de dados MySQL para armazenar os registros.
- Suporte a testes de carga em massa com dados gerados dinamicamente.
- Relatórios automatizados para análise de desempenho.

## Documentação

**Arquivos Principais:**

1. **`app.py`**: Backend desenvolvido em Flask que fornece as rotas para:
   - `/`: Renderização do formulário web.
   - `/register`: Endpoint para cadastro dos clientes.

2. **`create_table.sql`**: Script para criar o banco de dados e a tabela `clientes`.

3. **`templates/index.html`**: Formulário HTML simples para coleta de dados.

4. **`jmeter/dados_completos.csv`**: Arquivo CSV com 1000 registros fictícios para testes.

5. **Plano de Teste JMeter (`CadastroTeste.jmx`)**:
   - Configurado para enviar dados dinâmicos utilizando `dados_completos.csv`.
   - Inclui listeners para relatórios de resultados.

**Tecnologias de Suporte:**

- **Faker**: Utilizado para gerar dados fictícios realistas.
- **JMeter**: Ferramenta para simulação de carga e coleta de métricas.

## Explicação

O projeto utiliza o seguinte fluxo:
1. **Cadastro Manual:** O formulário web permite que um usuário insira dados manualmente.
2. **Teste Automatizado:** Utilizando o Apache JMeter, simulamos múltiplos usuários enviando requisições simultâneas ao backend.
3. **Relatórios:** As métricas coletadas pelo JMeter ajudam a analisar a latência, throughput, e o comportamento sob carga do sistema.

## Como Usar

1. **Configurar o Banco de Dados:**
   - Execute o script `create_table.sql` em seu servidor MySQL:
     ```bash
     mysql -u root -p < create_table.sql
     ```

2. **Instalar as Dependências:**
   - Configure um ambiente virtual e instale as dependências:
     ```bash
     python -m venv venv
     source venv/bin/activate  # Linux/Mac
     venv\Scripts\activate   # Windows
     pip install -r requirements.txt
     ```

3. **Iniciar o Servidor Flask:**
   - Execute o backend com:
     ```bash
     python app.py
     ```

4. **Acessar o Formulário Web:**
   - Abra o navegador e acesse: [http://127.0.0.1:5000](http://127.0.0.1:5000).

5. **Realizar Testes de Carga:**
   - Abra o Apache JMeter e carregue o plano `CadastroTeste.jmx`.
   - Configure o caminho do arquivo CSV (se necessário).
   - Clique no ícone de start para executar o teste.

6. **Analisar os Resultados:**
   - Verifique as métricas nos listeners configurados no JMeter.
   - Salve os relatórios em CSV para análise posterior.

## Autor

Desenvolvido por Diego Franco.

Se tiver dúvidas ou sugestões, fique à vontade para entrar em contato!

