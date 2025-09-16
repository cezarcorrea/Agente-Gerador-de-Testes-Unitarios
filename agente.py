# -*- coding: utf-8 -*- # <<< Declaração de codificação UTF-8
import ast
from dotenv import load_dotenv
import google.generativeai as genai
import os
import inspect

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# --- Configuração do Google Gemini ---
def carregar_chave_api():
    """Carrega a chave da API do Google Generative AI a partir de variáveis de ambiente."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("A chave da API do Google Generative AI (GOOGLE_API_KEY) não está configurada.")
    genai.configure(api_key=api_key)

def gerar_prompt_teste(codigo_funcao: str, nome_funcao: str) -> str:
    """Gera o prompt para solicitar a geração de testes unitários."""
    prompt = f"""
    Gere testes unitários em Python para a seguinte função usando pytest.
    Inclua casos de sucesso e falha.
    O código da função é:

    ```python
    {codigo_funcao}
    ```

    A função a ser testada é '{nome_funcao}'.
    O output deve ser um arquivo Python puro, começando com 'import pytest\\n',
    e contendo funções de teste nomeadas como 'def test_*'.
    Por favor, certifique-se de que o código gerado inclua a linha de codificação '# -*- coding: utf-8 -*-' como a primeira linha do arquivo.
    """
    return prompt

def gerar_testes_unitarios(codigo_funcao: str, nome_funcao: str) -> str:
    """Gera testes unitários para uma dada função usando o modelo de IA."""
    try:
        carregar_chave_api() # Garante que a chave da API está configurada
        model = genai.GenerativeModel('gemini-1.5-flash') # Inicializa o modelo

        prompt = gerar_prompt_teste(codigo_funcao, nome_funcao)
        response = model.generate_content(prompt)

        # Limpa e formata a resposta para garantir que seja código Python puro
        test_code = response.text.strip()
        if test_code.startswith("```python"):
            test_code = test_code[len("```python"):].strip()
        if test_code.endswith("```"):
            test_code = test_code[:-len("```")].strip()

        # Adiciona a declaração de codificação como a primeira linha
        # e garante que 'import pytest' venha depois.
        # Se a resposta do modelo já inclui a declaração, isso garante que ela fique na primeira linha.
        # Se não inclui, ela é adicionada.
        codificacao = "# -*- coding: utf-8 -*-"
        if not test_code.startswith(codificacao):
            test_code = f"{codificacao}\n{test_code}"

        # Garante que 'import pytest' seja a segunda linha se a codificação for adicionada
        linhas_teste = test_code.splitlines()
        if linhas_teste[0] == codificacao and len(linhas_teste) > 1 and not linhas_teste[1].strip().startswith("import pytest"):
             # Encontra a linha 'import pytest' e a move para a segunda posição
            try:
                pytest_index = next(i for i, line in enumerate(linhas_teste) if line.strip().startswith("import pytest"))
                pytest_line = linhas_teste.pop(pytest_index)
                linhas_teste.insert(1, pytest_line)
                test_code = "\n".join(linhas_teste)
            except StopIteration:
                # Se 'import pytest' não for encontrado (improvável, mas seguro verificar),
                # apenas adiciona ao final da declaração de codificação.
                test_code = f"{codificacao}\nimport pytest\n" + "\n".join(linhas_teste[1:]) # Ajusta se import pytest não for achado


        return test_code

    except Exception as e:
        print(f"Ocorreu um erro ao gerar os testes: {e}")
        return None

def extrair_funcao_de_codigo(codigo_completo: str, nome_funcao: str) -> str:
    """Extrai o código de uma função específica de um código Python maior."""
    try:
        tree = ast.parse(codigo_completo)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == nome_funcao:
                return ast.get_source_segment(codigo_completo, node)
    except Exception as e:
        print(f"Erro ao extrair a função {nome_funcao}: {e}")
    return None

# --- Exemplos de Uso ---

def somar(a, b):
    """Soma dois números."""
    return a + b

def dividir(a, b):
    """Divide dois números. Lança erro se o divisor for zero."""
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

# Dicionário para mapear nomes de funções para os objetos de função
funcoes_para_testar = {
    "somar": somar,
    "dividir": dividir,
}

for nome_func, func_obj in funcoes_para_testar.items():
    print(f"--- Gerando testes para a função '{nome_func}' ---")
    codigo_funcao = inspect.getsource(func_obj)
    test_code = gerar_testes_unitarios(codigo_funcao, nome_func)

    if test_code:
        nome_arquivo_teste = f"test_{nome_func}.py"
        with open(nome_arquivo_teste, "w", encoding='utf-8') as f: # Garante que o arquivo seja aberto com UTF-8
            f.write(test_code)
        print(f"Testes gerados e salvos em '{nome_arquivo_teste}'.")
    else:
        print(f"Nenhum teste gerado para salvar.")

print("\nPara rodar os testes, navegue até o diretório deste script no terminal e execute:")
print("pytest")