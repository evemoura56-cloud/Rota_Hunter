# Rotas da API

## Autenticacao
- `POST /auth/register` - cadastro de usuario
- `POST /auth/login` - login + JWT
- `GET /auth/me` - dados do usuario logado

## Hunter
- `POST /hunter/discover` - scraping simulado, cria leads e contatos

## CRM
- `POST /leads`
- `GET /leads`
- `GET /leads/{id}`
- `PUT /leads/{id}`
- `PUT /leads/{id}/status`
- `GET /leads/{id}/contacts`
- `POST /leads/{id}/contacts`
- `GET /leads/{id}/interactions`
- `POST /leads/{id}/interactions`
- `GET /leads/{id}/forms`
- `GET /crm/dashboard` - KPIs + graficos

## Forms
- `POST /forms/auto-fill` - automacao Playwright simulada e registro

## Engagement
- `POST /engagement/email-batch` - ate 300 envios/dia

## IA
- `POST /ia/train`
- `POST /ia/predict`

## WhatsApp
- `POST /whatsapp/link` - gera link `wa.me`
