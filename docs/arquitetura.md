# Arquitetura Oficial - Rota Hunter 1.0

## Visao Geral

Plataforma modular PT-BR com backend FastAPI, banco relacional e frontend React/Vite. Componentes principais:

- **Auth**: usuarios, JWT, seguranca basica.
- **Hunter**: scraping simulado, captura de decisores e preenchimento inicial.
- **CRM**: pipeline completo, contatos, interacoes e formularios.
- **Engagement**: envio de emails personalizados e registro automatico de historico.
- **IA**: modelo scikit-learn para p_win, treinado com dados locais.
- **Dashboards**: KPIs e graficos demandando API `/crm/dashboard`.

## Pastas

```
/backend
  app.py
  /src (rotas + utilitarios)
  /models (SQLAlchemy)
  /schemas (Pydantic)
  /services (regras de negocio)
  /database (engine e session)
/frontend
  Vite + React + Recharts
/docs
  arquitetura, rotas e modelo de IA
```

## Fluxo de Dados

1. Usuario autentica -> recebe JWT.
2. Hunter descobre empresas -> cria leads e contatos -> CRM.
3. CRM atualiza pipeline, registra interacoes e formularios automacao Playwright.
4. Engagement dispara emails em lote com controle de limite.
5. IA coleta features de leads e calcula `p_win` exibido no front.
6. Dashboards consomem dados agregados.

## Camadas

- **API Layer** (`src/*/routes.py`): valida entradas.
- **Services**: orquestram regras, integracoes locais e IA.
- **Models**: persistencia.
- **Frontend**: componentes reutilizaveis para cards, graficos e pipeline Kanban.
