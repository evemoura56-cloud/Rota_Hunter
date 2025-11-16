# Rota Hunter 1.0

Plataforma gratuita e 100% local para prospecção B2B, CRM e automação comercial com IA. O projeto segue clean architecture, foi escrito em Português e permanece totalmente independente de serviços pagos.

## Sumário

1. [Visão Geral e Recursos](#visão-geral-e-recursos)
2. [Arquitetura do Repositório](#arquitetura-do-repositório)
3. [Tecnologias Principais](#tecnologias-principais)
4. [Pré-requisitos](#pré-requisitos)
5. [Configuração do Ambiente](#configuração-do-ambiente)
6. [Execução Local](#execução-local)
7. [Scripts e Tarefas](#scripts-e-tarefas)
8. [Segurança e Boas Práticas](#segurança-e-boas-práticas)
9. [Contribuição e Roadmap](#contribuição-e-roadmap)

---

## Visão Geral e Recursos

- **Autenticação JWT** com cadastro, login e rota de auto-inspeção (`/auth/me`).
- **Hunter automatizado** combinando scraping local, captura de decisores e automação Playwright.
- **CRM completo** com pipeline Kanban, leads manuais, contatos, interações e formulários customizados.
- **Engajamento multicanal**: e-mail em lote (com limite seguro de 300/dia) e atalhos WhatsApp.
- **IA Comercial** baseada em scikit-learn para estimar `p_win` e justificar previsões.
- **Dashboards operacionais** alimentados pela API com indicadores, gráficos e KPIs em tempo real.
- **Docker Compose** opcional com backend FastAPI, frontend Vite e PostgreSQL pronto para produção.

### Fluxo esperado
1. Hunter encontra empresas e decisores.
2. Leads chegam ao CRM com contatos e histórico.
3. Engajamento dispara mensagens personalizadas.
4. IA calcula probabilidade de fechamento e motiva o time.
5. Dashboards exibem funil, atividades e alertas.

## Arquitetura do Repositório

```
/backend
  app.py
  requirements.txt
  /src            # domínios (auth, hunter, crm, engagement, ia, scraping, forms, whatsapp, common)
  /services       # regras de negócio
  /schemas        # validação Pydantic
  /models         # ORM SQLAlchemy
  /database       # engine, sessões, arquivos SQLite/modelos
/frontend         # Vite + React + TypeScript
/docs             # arquitetura, rotas, IA e materiais auxiliares
.env.example
run_app.py | seed_db.py | train_ia.py
docker-compose.yml
```

## Tecnologias Principais

| Camada     | Tecnologias                                           |
| ---------- | ----------------------------------------------------- |
| Backend    | FastAPI, SQLAlchemy, Pydantic, Playwright, Passlib    |
| Frontend   | Vite, React, TypeScript, Zustand, Tailwind (ou CSS)   |
| IA         | scikit-learn, joblib                                  |
| Banco      | SQLite (dev) ou PostgreSQL (Docker/produção)          |
| Autenticação | JWT + bcrypt                                        |
| Infra      | Docker Compose, dotenv, scripts utilitários           |

## Pré-requisitos

- **Python 3.11+**
- **Node.js 20+** e npm (ou pnpm/yarn, caso prefira)
- **Playwright** (instalado via `python -m playwright install`)
- **Docker + Docker Compose** (opcional, para stack completo com Postgres)

## Configuração do Ambiente

1. Copie `.env.example` para `.env` e ajuste os valores essenciais:
   - `DATABASE_URL`: SQLite local (padrão) ou string do Postgres do Docker.
   - `JWT_SECRET` / `JWT_EXP_HORAS`: defina um segredo seguro e validade adequada.
   - `SMTP_*`: configure host, porta e credenciais (use app password no Gmail).
   - `MODO_ENVIO_EMAIL=simulado` recomenda-se em dev para evitar disparos reais.
   - `FRONTEND_URL`: endereço do cliente (padrão `http://localhost:5173`).
2. Execute (opcional) `python seed_db.py` para criar usuário demo e dados iniciais.
3. Execute (opcional) `python train_ia.py` para gerar/atualizar `database/modelo_ia.pkl`.

> **Usuário demo padrão**: `demo@rotahunter.com / senha-demo`. Ajuste em `seed_db.py` conforme necessário.

## Execução Local

### Backend (FastAPI)

> Todos os comandos abaixo devem ser executados **a partir da raiz do repositório** para que o pacote `backend` seja encontrado corretamente.

```bash
# 1) Ambientes isolados evitam conflitos entre projetos
python -m venv .venv
.\.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # macOS/Linux

# 2) Dependências e Playwright (robôs do Hunter)
pip install -r backend/requirements.txt
python -m playwright install

# 3) Suba o servidor apontando direto para backend.app
python -m uvicorn backend.app:app --reload
# ou simplesmente
python run_app.py
```

- API: `http://localhost:8000`
- Documentação: `http://localhost:8000/docs` (Swagger) e `http://localhost:8000/redoc`
- Se preferir Postgres/Docker, ajuste `DATABASE_URL` ou use `docker compose up --build`

### Frontend (Vite + React)

```bash
cd frontend
npm install
npm run dev
```

- Interface disponível em `http://localhost:5173`
- Crie `frontend/.env` caso precise sobrescrever `VITE_API_URL`

> Dica: o script `npm run dev` executa `kill-port 5173 5174 5175` antes de subir o Vite, garantindo que nenhuma instância antiga do Node fique segurando essas portas. Caso prefira limpar manualmente, use `Get-NetTCPConnection -LocalPort 5173` seguido de `Stop-Process -Id <PID>` no PowerShell antes de iniciar.

### Docker Compose

```bash
docker compose up --build
```

Serviços provisionados:

| Serviço   | Porta | Observações                     |
| --------- | ----- | --------------------------------|
| backend   | 8000  | FastAPI + docs + WebSocket      |
| frontend  | 5173  | Vite/React em modo dev          |
| database  | 5432  | PostgreSQL com volume persistido |

Ajuste `DATABASE_URL` para apontar para o Postgres do Compose (`postgresql+psycopg2://...`).

## Scripts e Tarefas

| Script                | Descrição                                                                 |
| --------------------- | ------------------------------------------------------------------------- |
| `python run_app.py`   | Inicializa o backend com Uvicorn em modo desenvolvimento.                 |
| `python seed_db.py`   | Cria usuário demo, lead de exemplo e contato associado.                   |
| `python train_ia.py`  | Treina modelo scikit-learn e salva `database/modelo_ia.pkl`.              |
| `pytest` (quando disponível) | Executa a suíte de testes (configurar conforme necessidade).      |
| `npm run build`       | Empacota o frontend para produção (gera `frontend/dist`).                 |

## Segurança e Boas Práticas

- Entradas validadas via Pydantic e respostas padronizadas.
- Hash de senha com `bcrypt` e tokens JWT com revogação por expiração.
- Limites de envio de e-mail são checados antes e depois de cada lote.
- Pipeline do CRM impede saltos de estágio não permitidos.
- Recomenda-se manter `.env` fora de commits e rotacionar segredos com frequência.
- Ative logs estruturados (FastAPI/Uvicorn) para auditoria em produção.

## Contribuição e Roadmap

1. Abra uma branch com nome descritivo (ex.: `feature/hunter-inteligente`).
2. Mantenha textos/PT-BR e escreva commits claros.
3. Execute lint/testes antes de enviar PR.
4. Documente novas rotas, modelos IA ou integrações no diretório `docs/`.

**Ideias futuras**:
- Playbooks de outbound/ABM prontos.
- Integração com ferramentas externas via MCP.
- Benchmark automatizado para modelos IA customizados.

Rota Hunter 1.0 é open-source e continuará evoluindo com a comunidade. Boas vendas!
