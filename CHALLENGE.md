# Desafio Técnico: Engenheiro(a) de Software - Rota Hunter

## Introdução

Bem-vindo(a) ao desafio técnico para a posição de Engenheiro(a) de Software! Este teste foi projetado para simular um problema real que enfrentamos no desenvolvimento do **Rota Hunter**, uma plataforma de CRM focada em prospecção e gestão de leads.

Aqui, você terá a oportunidade de demonstrar suas habilidades em resolução de problemas, design de software, e sua familiaridade com tecnologias de backend modernas.

## Contexto do Projeto

O **Rota Hunter** é uma aplicação web completa, construída com uma arquitetura desacoplada:

*   **Backend:** Uma API robusta desenvolvida em Python com o framework **FastAPI**.
*   **Frontend:** Uma interface interativa construída com **React** e **Vite**.
*   **Banco de Dados:** **PostgreSQL**, orquestrado via **Docker**.
*   **Orquestração:** O ambiente de desenvolvimento é totalmente containerizado com **Docker Compose**.

O objetivo principal da plataforma é ajudar equipes de vendas a encontrar e qualificar novos leads de forma inteligente.

## O Problema: A Rota de Prospecção (`/hunter/discover`)

Atualmente, uma das funcionalidades mais críticas da nossa plataforma, a rota de prospecção de empresas (conhecida como "rota hunter"), não está funcional. Ela foi desenvolvida inicialmente com uma **lógica de mock**, que apenas gera dados de empresas falsas e aleatórias.

Seu desafio é **substituir essa lógica de mock por uma solução real e funcional** que busque dados de empresas de verdade.

## Seu Desafio

Sua missão é refatorar o endpoint `POST /hunter/discover` para que ele, ao receber filtros como `setor` e `regiao`, busque empresas reais na internet e as cadastre como novos leads no banco de dados.

### Requisitos Funcionais

1.  **Fonte de Dados Real:** A rota deve deixar de usar dados falsos e passar a consumir dados de uma fonte externa e real.
    *   Você tem **total liberdade** para escolher a fonte: pode ser uma **API pública gratuita** (ex: Clearbit, ou qualquer outra que encontrar) ou uma solução de **web scraping** de um site público (ex: Google, DuckDuckGo, LinkedIn Sales Navigator, etc.). A criatividade e a justificativa da sua escolha serão avaliadas.

2.  **Filtragem:** A solução deve ser capaz de utilizar os parâmetros enviados no corpo da requisição (`setor`, `regiao`, `palavras_chave`) para filtrar a busca.

3.  **Cadastro no Banco:** As empresas encontradas devem ser cadastradas na tabela `leads` do banco de dados. A lógica para isso já existe parcialmente no `lead_service`.

4.  **Prevenção de Duplicatas:** A aplicação não deve cadastrar a mesma empresa (com o mesmo `site_url`) mais de uma vez.

### Requisitos Não Funcionais

*   **Manter a Arquitetura:** A solução deve se integrar à arquitetura existente (FastAPI, services, schemas).
*   **Código Limpo e Legível:** Escreva um código claro, bem-estruturado e que siga as boas práticas de desenvolvimento.
*   **Tratamento de Erros:** A aplicação deve ser resiliente e tratar possíveis falhas na comunicação com a fonte de dados externa (ex: timeouts, erros de rede, bloqueios).
*   **Ambiente Docker:** Todas as alterações devem funcionar dentro do ambiente Docker Compose fornecido. Se você adicionar novas dependências, elas devem ser incluídas nos arquivos de configuração correspondentes.

### O Que **NÃO** é Necessário

*   Você **não precisa** se preocupar em extrair informações de **contatos** (pessoas) dentro das empresas. O foco é apenas na descoberta e cadastro da **empresa** como um lead.
*   Você **não precisa** alterar o frontend. O foco deste desafio é 100% no backend.

## Como Configurar e Rodar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone <URL_DO_REPOSITÓRIO>
    cd Rota_Hunter
    ```

2.  **Inicie o ambiente:**
    ```bash
    docker compose up --build
    ```
    *   Este comando irá construir as imagens, instalar as dependências e iniciar os contêineres do backend, frontend e banco de dados.

3.  **Acesse os serviços:**
    *   **Backend (API):** `http://localhost:8000`
    *   **Documentação da API (Swagger):** `http://localhost:8000/docs`
    *   **Frontend:** `http://localhost:5173`

4.  **Teste a Rota Hunter (Opcional):** Você pode usar a documentação da API ou uma ferramenta como `curl` para testar o comportamento atual da rota `POST /hunter/discover` e entender o ponto de partida.

## Critérios de Avaliação

Nós avaliaremos sua solução com base nos seguintes critérios:

*   **Funcionalidade:** A solução atende a todos os requisitos funcionais? Ela realmente encontra e cadastra empresas?
*   **Qualidade do Código:** O código está limpo, organizado e fácil de entender?
*   **Escolha da Solução:** Qual foi a sua abordagem para obter os dados? Por que você a escolheu? A solução é robusta e escalável?
*   **Boas Práticas:** Você seguiu as boas práticas de desenvolvimento, como tratar erros, gerenciar dependências e escrever commits claros?
*   **Testes (Bônus):** Adicionar testes unitários ou de integração para a nova lógica será considerado um grande diferencial.

## Como Entregar

1.  Crie uma nova branch a partir da `main`.
2.  Desenvolva sua solução e faça quantos commits forem necessários.
3.  Ao finalizar, abra um **Pull Request** para a branch `main` e adicione uma descrição detalhada das suas alterações e das decisões que você tomou.

Boa sorte! Estamos ansiosos para ver sua solução.
