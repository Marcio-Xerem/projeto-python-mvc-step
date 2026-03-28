# Projeto Python MVC - Step

Projeto educacional implementando o padrão **MVC (Model-View-Controller)** usando **FastAPI** com Python.

## Descrição do Projeto

Este projeto implementa uma API RESTful de gerenciamento de usuários utilizando o padrão arquitetural MVC:

- **Model (usuario_model.py)**: Camada de dados que gerencia a persistência de informações dos usuários
- **View (usuario_view.py)**: Camada de apresentação que formata as respostas da API
- **Controller (usuario_controller.py)**: Camada de lógica que orquestra a comunicação entre Model e View

## Estrutura do Projeto

```
projeto-python-mvc-step/
├── main.py                          # Aplicação FastAPI principal
├── app/
│   ├── models/
│   │   └── usuario_model.py        # Model - Gerencia dados de usuários
│   ├── controllers/
│   │   └── usuario_controller.py   # Controller - Lógica de negócio
│   └── views/
│       └── usuario_view.py         # View - Formatação de respostas
└── README.md                        # Este arquivo
```

## Dependências

- **Python**: 3.13.7+
- **FastAPI**: Framework web moderno para APIs Python
- **Uvicorn**: Servidor ASGI para executar a aplicação FastAPI

## Instalação

### 1. Ativar o Ambiente Virtual

Se usando Windows PowerShell:
```powershell
.\.venv\Scripts\Activate.ps1
```

Se usando Command Prompt:
```cmd
.\.venv\Scripts\activate.bat
```

Se usando Linux/Mac:
```bash
source .venv/bin/activate
```

### 2. Instalar Dependências (se necessário)

```bash
pip install fastapi uvicorn
```

## Como Executar

### Opção 1: Usar Uvicorn (Recomendado)

```bash
uvicorn main:app --reload
```

- `--reload`: Reinicia o servidor automaticamente ao detectar mudanças no código
- A API estará disponível em: **http://127.0.0.1:8000**
- Documentação interativa em: **http://127.0.0.1:8000/docs**

### Opção 2: Executar via Python Diretamente

```bash
python -m uvicorn main:app --reload
```

## Endpoints Disponíveis

### 1. Listar Todos os Usuários
```
GET /usuarios
```

**Resposta (exemplo):**
```json
["João Silva", "Maria Santos", "Pedro Oliveira"]
```

### 2. Criar Novo Usuário
```
POST /usuarios?nome=NomeDoUsuario
```

**Parâmetro:**
- `nome` (string): Nome do usuário a ser criado

**Resposta (sucesso):**
```json
{"msg": "Usuário criado"}
```

## Testando a API

### Usando a Documentação Interativa (Swagger)

Acesse **http://127.0.0.1:8000/docs** no navegador para testar os endpoints de forma visual.

### Usando cURL

```bash
# Listar usuários
curl http://127.0.0.1:8000/usuarios

# Criar novo usuário
curl -X POST "http://127.0.0.1:8000/usuarios?nome=Ana"
```

### Usando Python

```python
import requests

# Listar usuários
response = requests.get("http://127.0.0.1:8000/usuarios")
print(response.json())

# Criar usuário
response = requests.post("http://127.0.0.1:8000/usuarios?nome=Bruno")
print(response.json())
```

## Padrão MVC Aplicado

### Model - `app/models/usuario_model.py`
- Gerencia o armazenamento de dados (lista em memória)
- Funções: `listar()` e `criar(nome)`
- **Responsabilidade**: Persistência e manipulação de dados

### Controller - `app/controllers/usuario_controller.py`
- Orquestra a lógica de negócio
- Recebe requisições HTTP e coordena Model e View
- Funções: `listar_usuarios()` e `criar_usuario(nome)`
- **Responsabilidade**: Lógica de aplicação

### View - `app/views/usuario_view.py`
- Formata as respostas para o cliente
- Função: `resposta_sucesso(msg)`
- **Responsabilidade**: Apresentação dos dados

## Fluxo de Requisição

```
Cliente HTTP
    ↓
main.py (Rota FastAPI)
    ↓
usuario_controller.py (Controller)
    ↓
usuario_model.py (Model) ← → usuario_view.py (View)
    ↓
Resposta formatada ao Cliente
```

## Características Implementadas

✓ Padrão MVC bem definido  
✓ API RESTful com FastAPI  
✓ Separação de responsabilidades  
✓ Armazenamento de dados em memória  
✓ Documentação automática Swagger/OpenAPI  

## Melhorias Futuras

- [ ] Integrar banco de dados (SQLAlchemy, SQLite)
- [ ] Autenticação JWT
- [ ] Validação de dados com Pydantic
- [ ] Tratamento de erros melhorado
- [ ] Testes unitários
- [ ] Deploy em produção (Heroku, AWS, etc)

## Autor

Projeto realizado durante as aulas 5-6 do Módulo 14 - Python Backend da Step Computer Academy.

## Licença

Este projeto é fornecido para fins educacionais.