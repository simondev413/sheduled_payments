# Scheduled Payments API

Uma API REST construída com FastAPI para gerenciar pagamentos agendados. Permite criar, listar, atualizar e deletar pagamentos programados para execução futura.

## Funcionalidades

- **Criar Pagamento Agendado**: Adicione novos pagamentos com data de agendamento, valor, beneficiário e tipo.
- **Listar Pagamentos**: Visualize todos os pagamentos agendados ou um específico por ID.
- **Atualizar Pagamento**: Modifique detalhes de um pagamento existente.
- **Deletar Pagamento**: Remova um pagamento agendado.

## Tecnologias Utilizadas

- **Python 3.x**
- **FastAPI**: Framework para construção de APIs rápidas e modernas.
- **Uvicorn**: Servidor ASGI para execução da aplicação.
- **Pydantic**: Para validação de dados e modelos.

## Pré-requisitos

- Python 3.8 ou superior instalado.
- Pip para gerenciamento de pacotes.

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/sheduled_payments.git
   cd sheduled_payments
   ```

2. **Instale as dependências**:
   ```bash
   pip install fastapi uvicorn pydantic
   ```

## Como Executar

1. Execute o servidor de desenvolvimento:
   ```bash
   uvicorn main:app --reload
   ```

2. Acesse a documentação interativa da API em: `http://localhost:8000/docs`

3. Endpoint raiz: `http://localhost:8000/` - Retorna uma mensagem de boas-vindas.

## Estrutura do Projeto

```
sheduled_payments/
├── main.py                    # Ponto de entrada da aplicação
├── requests.http              # Arquivo para testes de requisições HTTP
├── src/
│   ├── controllers/
│   │   └── sheduled_payment_controllers.py  # Controladores da API
│   ├── models/
│   │   ├── sheduled_payment.py              # Modelo de dados do pagamento
│   │   └── enum/
│   │       └── sheduled_payment_enum.py     # Enums para status e tipo
│   ├── repositories/
│   │   └── sheduled_payment_repository.py   # Repositório para persistência
│   ├── routes/
│   │   └── sheduled_payments_routes.py      # Definição das rotas da API
│   ├── services/
│   │   └── sheduled_payments_service.py     # Lógica de negócio
│   └── utils/
│       └── __init__.py                      # Utilitários (se houver)
└── README.md                # Este arquivo
```

## API Endpoints

### Pagamentos Agendados

- **POST /sheduled_payments/**: Cria um novo pagamento agendado.
  - Corpo da requisição: Dados do pagamento (user_id, amount, beneficiary, etc.).

- **GET /sheduled_payments/**: Lista todos os pagamentos agendados.

- **GET /sheduled_payments/{sheduled_payment_id}**: Obtém detalhes de um pagamento específico por ID.

- **PUT /sheduled_payments/{sheduled_payment_id}**: Atualiza um pagamento agendado existente.

- **DELETE /sheduled_payments/{sheduled_payment_id}**: Deleta um pagamento agendado por ID.

### Modelo de Dados

O modelo `SheduledPayment` inclui:
- `id`: Identificador único (UUID).
- `user_id`: ID do usuário.
- `amount`: Valor do pagamento (float).
- `beneficiary`: Nome do beneficiário.
- `scheduled_date`: Data de agendamento.
- `scheduled_type`: Tipo de agendamento (ONE_TIME, RECURRING).
- `status`: Status do pagamento (PENDING, COMPLETED, FAILED).
- `next_execution_date`: Próxima data de execução.
- `description`: Descrição do pagamento.
- `createdAt` e `updatedAt`: Timestamps de criação e atualização.

## Testes

Use o arquivo `requests.http` para testar os endpoints via VS Code ou ferramentas como Postman.

Exemplo de requisição para criar um pagamento:
```
POST http://localhost:8000/sheduled_payments/
Content-Type: application/json

{
  "userId": "user123",
  "amount": 100.50,
  "beneficiary": "João Silva",
  "scheduled_date": "2023-12-01T10:00:00",
  "description": "Pagamento mensal"
}
```

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature: `git checkout -b feature/nova-funcionalidade`.
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`.
4. Push para a branch: `git push origin feature/nova-funcionalidade`.
5. Abra um Pull Request.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Contato

Para dúvidas ou sugestões, abra uma issue no GitHub ou entre em contato com o mantenedor.