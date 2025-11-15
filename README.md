# Rota Hunter 1.0

Plataforma gratuita e local de Prospeccao B2B + CRM + IA Comercial. Todo o codigo esta em PT-BR e segue clean architecture com camadas claras (API, Services, Models, Frontend Vite).

## Principais Recursos
- Autenticacao JWT com cadastro, login e rota `/auth/me`
- Hunter automatizado com scraping local, captura de decisores e automacao Playwright
- CRM completo com pipeline Kanban, contatos, interacoes e formularios
- Engajamento por e-mail personalizado (limite seguro 300/dia) e atalhos WhatsApp
- Modelo IA (scikit-learn) para probabilidade de fechamento (`p_win`)
- Dashboards com KPIs e graficos (pizza, barras, linha) alimentados pela API
- Docker Compose com backend FastAPI, frontend Vite e PostgreSQL opcional

## Estrutura Obrigatoria
```
/backend
  app.py
  requirements.txt
  /src (auth, hunter, crm, engagement, ia, scraping, forms, whatsapp, common)
  /database, /models, /schemas, /services
/frontend (Vite + React)
/docs (arquitetura, rotas, modelo IA)
.env.example
run_app.py | seed_db.py | train_ia.py
docker-compose.yml
```

## Pre-requisitos
- Python 3.11+
- Node 20+
- npm ou yarn
- (Opcional) Docker + Docker Compose

## Configuracao do Ambiente
1. Copie `.env.example` para `.env` e ajuste:
   - `DATABASE_URL` (SQLite local por padrao ou PostgreSQL do Docker)
   - `JWT_SECRET`
   - `SMTP_*` caso use Gmail com app password
   - `MODO_ENVIO_EMAIL=simulado` para ambiente seguro
2. (Opcional) Execute `python seed_db.py` para criar usuario demo e dados iniciais.

## Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```
API padrao: `http://localhost:8000`. Documentacao automatica disponivel em `/docs` (Swagger) e `/redoc`.

Scripts auxiliares (raiz):
- `python run_app.py` - sobe FastAPI em modo dev
- `python seed_db.py` - popula usuario demo + lead
- `python train_ia.py` - treina e salva `database/modelo_ia.pkl`

## Frontend
```bash
cd frontend
npm install
npm run dev
```
Acesse `http://localhost:5173`. Faca login com o usuario demo (`demo@rotahunter.com / senha-demo`) ou cadastre um novo. Configure `VITE_API_URL` em `frontend/.env` caso o backend execute em outro endereco.

### Uso Rapido
1. **Hunter**: defina setor, regiao e palavras chave, clique em "Descobrir Empresas". Novos leads e decisores serao exibidos no CRM.
2. **CRM**: acompanhe o pipeline, crie leads manuais e acompanhe contatos/interacoes. Use `/leads/{id}/status` para mover etapas.
3. **E-mails**: envie lotes via `/engagement/email-batch` com personalizacao `{{nome_contato}}` e `{{nome_empresa}}`.
4. **WhatsApp**: gere links com `/whatsapp/link` ou botao "Enviar WhatsApp".
5. **IA**: treine com `/ia/train`, depois consulte `/ia/predict` para obter `p_win` e motivos.
6. **Dashboards**: cards e graficos atualizam automaticamente a partir de `/crm/dashboard`.

## Docker Compose
```bash
docker compose up --build
```
Servicos: `backend (8000)`, `frontend (5173)` e `database Postgres (5432)`. Ajuste `DATABASE_URL` para apontar ao Postgres interno.

## Seguranca e Boas Praticas
- Todas as entradas validadas via Pydantic.
- Hash de senha com bcrypt e tokens JWT com expiracao configuravel.
- Controle de pipeline impede pular estagios.
- Limite diario de e-mails checado antes e apos cada lote.
- Zero dependencias pagas ou chamadas externas obrigatorias.

## Como Contribuir
1. Crie branch e mantenha PT-BR nos textos.
2. Execute lint/testes conforme necessidade.
3. Abra PR descrevendo novos modulos, rotas ou melhorias de IA/CRM.

Rota Hunter 1.0 e 100% open-source e local. Aproveite!
