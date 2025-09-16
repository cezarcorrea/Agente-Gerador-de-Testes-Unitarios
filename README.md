# Agente Gerador de Testes Unitários com Pytest e Google Generative AI

Este projeto demonstra a criação de um agente de Inteligência Artificial em Python que, utilizando a biblioteca ```google.generativeai``` (substituindo o Azure OpenAI conforme a necessidade do desafio), gera automaticamente testes unitários em Python para funções fornecidas. O agente é capaz de criar testes para casos de sucesso e falha, formatados para serem executados com a biblioteca ```pytest```.


### Funcionalidades

- **Geração de Testes Unitários:** Cria testes para funções Python, incluindo cenários de sucesso e de erro.

- **Integração com Google Generative AI:** Utiliza o modelo ```gemini-1.5-flash``` para gerar o código dos testes.

- **Extração de Código:** Utiliza ```ast``` para extrair o código fonte de funções específicas.

- **Formato Pytest:** Os testes gerados seguem a convenção do ```pytest```, com funções ```def test_*``` e importação ```import pytest```.

- **Tratamento de Codificação:** Garante que os arquivos de teste sejam salvos com codificação UTF-8 para evitar erros de caracteres.


### Estrutura do Projeto

- ```agente.py```: O script principal que contém a lógica do agente.

- ```.env.example```: Um arquivo de exemplo para configurar as variáveis de ambiente, incluindo a chave da API.

- ```test_somar.py``` (gerado): Arquivo de teste para a função ```somar```.

- ```test_dividir.py``` (gerado): Arquivo de teste para a função ```dividir```.

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes softwares instalados:

- Python 3.11.4 ou superior

- ```pip``` (gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório:**

```Bash
git clone <URL_DO_SEU_REPOSITORIO>
cd <NOME_DO_DIRETORIO_DO_REPOSITORIO>
```

2. **Crie e ative um ambiente virtual (recomendado):**

```Bash
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No macOS/Linux:
source venv/bin/activate
```

3. **Instale as dependências:**

```Bash
pip install google-generativeai python-dotenv pytest
```

### Configuração

1. **Obtenha uma chave de API:**

  - Acesse o [Google AI Studio](https://aistudio.google.com/) para obter sua chave de API do Google Generative AI.

2. **Configure as variáveis de ambiente:**

  - Copie o arquivo ```.env.example``` para ```.env```:

```Bash
cp .env.example .env
```
  - Abra o arquivo .env em um editor de texto e substitua <SUA_CHAVE_API_AQUI> pela sua chave de API real:

```Snippet de código
GOOGLE_API_KEY=<SUA_CHAVE_API_AQUI>
```

### Como Rodar o Agente

1. **Navegue até o diretório do projeto** no seu terminal (onde o arquivo ```agente.py``` está localizado).

2. **Execute o script do agente:**

```Bash
python agente.py
```
O agente irá:

- Identificar as funções de exemplo (```somar```, ```dividir```).

- Solicitar ao modelo ```gemini-1.5-flash``` que gere testes unitários para cada função.

- Salvar os testes gerados em arquivos ```test_somar.py``` e ```test_dividir.py``` no mesmo diretório.

### Como Rodar os Testes Gerados

Certifique-se de que você está no diretório onde os arquivos de teste foram gerados.

Execute o ```pytest``` no terminal:

```Bash
pytest
```
O ```pytest``` irá descobrir e executar os testes gerados automaticamente. Você deverá ver um relatório indicando se os testes passaram ou falharam.

### Contribuições

Este projeto é um exemplo prático dos conceitos de IA para geração de código. Sinta-se à vontade para expandir as funcionalidades, adicionar mais exemplos de funções ou explorar outros modelos de linguagem.

### Exemplos de Uso

O agente foi testado com as seguintes funções simples:

1. ```somar(a, b)```:

- Descrição: Soma dois números.

- Testes Gerados: Cobrem casos de sucesso com números positivos, negativos e zero.

2. ```dividir(a, b)```:

- Descrição: Divide dois números e lança um ```ValueError``` se o divisor for zero.

- Testes Gerados: Incluem um caso de sucesso para a divisão e um teste específico para verificar se o ```ValueError``` é lançado corretamente quando o divisor é zero.

O código fonte dessas funções está incluído no arquivo ```agente.py``` para fins de demonstração.

### Licença
Este projeto está licenciado sob a Licença MIT.

### Contato

Fique à vontade para visitar meu perfil no GitHub: [@cezarcorrea](https://github.com/cezarcorrea)

---

  
