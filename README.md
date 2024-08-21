# PRD - IA Generativa (Modelagem de banco de dados)


# *Introdução & objetivo*

### **Introdução**

A modelagem de dados é crucial para a estruturação eficaz de sistemas de informação, mas pode ser um processo manual e demorado. Com o avanço da IA, é possível automatizar essa tarefa, aumentando a eficiência e precisão. Este projeto propõe o uso de IA generativa para criar modelos de dados de forma automatizada, otimizando o processo e descobrindo padrões complexos.

### **Objetivo**

Desenvolver uma ferramenta baseada em IA generativa que:

1. **Gere Modelos de Dados** automaticamente a partir de dados fornecidos.
2. **Otimize Estruturas de Dados**, identificando redundâncias e sugerindo melhorias.
3. **Adapte-se a Mudanças**, ajustando modelos conforme novos requisitos surgem.

# *Por que* implementar isto?

A implementação deste projeto é crucial porque:

1. **Eficiência Operacional**: A modelagem manual de dados é demorada e propensa a erros. Automatizar esse processo com IA generativa reduzirá significativamente o tempo e o esforço, aumentando a produtividade das equipes de desenvolvimento.
2. **Qualidade e Precisão**: A IA generativa pode identificar padrões e otimizações que seriam difíceis de perceber manualmente, resultando em modelos de dados mais robustos e eficientes.
3. **Adaptação Rápida**: Com as constantes mudanças nos requisitos de negócios, uma solução que pode ajustar automaticamente os modelos de dados garante que as organizações mantenham sua competitividade e flexibilidade.
4. **Redução de Custos**: Automatizando a modelagem e otimizando os dados, o projeto pode reduzir custos operacionais, minimizando a necessidade de intervenção manual e evitando retrabalho.
5. **Inovação e Vantagem Competitiva**: Implementar uma solução de modelagem de dados baseada em IA coloca a organização na vanguarda da inovação tecnológica, criando uma vantagem competitiva no mercado.

---

# ***Público alvo***

Este projeto é voltado para empresas e equipes que lidam com grandes volumes de dados e que necessitam de soluções eficientes para modelagem e gerenciamento de bancos de dados. A solução proposta será útil tanto para profissionais técnicos quanto para gestores que precisam garantir que os dados da organização sejam estruturados de maneira eficiente e escalável.

### **Prioridade de Usuários:**

1. **Alta Prioridade:**
    - Engenheiros de Dados
    - Engenheiro de Banco de Dados (DBA)
    - Arquitetos de Sistemas
2. **Média Prioridade:**
    - Desenvolvedores de Software
    - Cientistas de Dados
3. **Baixa Prioridade:**
    - Gestores de TI
    - Executivos e Tomadores de Decisão

### **Tabela de Perfis de Usuários**

| **Perfil de Usuário** | **Descrição** |
| --- | --- |
| **Engenheiros de Dados** | Profissionais responsáveis pela construção e manutenção da arquitetura de dados, incluindo o design de modelos de dados. Precisam de ferramentas que automatizem tarefas e garantam a qualidade dos modelos gerados. |
| **Engenheiros de Banco de Dados (DBA)** | Especialistas focados na administração, otimização e manutenção de bancos de dados. Buscam soluções que simplifiquem a gestão e permitam ajustes rápidos e precisos nos modelos de dados. |
| **Arquitetos de Sistemas** | Profissionais que desenham a estrutura geral dos sistemas, incluindo a integração e interação dos dados. Precisam garantir que os modelos de dados estejam alinhados com as necessidades do sistema e sejam facilmente integráveis. |
| **Desenvolvedores de Software** | Desenvolvedores que criam aplicativos que interagem com bancos de dados. Eles se beneficiam de modelos de dados claros e bem estruturados que facilitem a implementação de funcionalidades de software. |
| **Cientistas de Dados** | Profissionais que analisam e interpretam dados para extrair insights. Precisam de acesso a modelos de dados bem organizados para garantir a precisão e a eficiência nas análises. |
| **Gestores de TI** | Responsáveis pela supervisão geral da infraestrutura de TI, incluindo a gestão de dados. Eles precisam de visibilidade sobre a eficiência e segurança dos modelos de dados implementados. |
| **Executivos e Tomadores de Decisão** | Líderes que definem estratégias de negócios baseadas em dados. Eles buscam garantias de que os modelos de dados suportam as metas estratégicas da organização e permitem uma rápida adaptação às mudanças do mercado. |

# *Personas*

**Persona 1: João, o Engenheiro de Dados**

- **Idade:** 32 anos
- **Cargo:** Engenheiro de Dados
- **Objetivos:**
    - Automatizar a criação de esquemas de banco de dados.
    - Garantir que os modelos de dados estejam otimizados e sejam escaláveis.
    - Integrar novos fluxos de dados de maneira ágil.
- **Desafios:**
    - Manter a consistência e a qualidade dos dados em ambientes complexos.
    - Reduzir o tempo gasto em tarefas manuais de modelagem.
    - Adaptar-se rapidamente às mudanças nos requisitos de negócios.
- **Como o projeto ajuda:**
    - A ferramenta permite a geração automática de modelos de dados, economizando tempo e evitando erros manuais.

### **Persona 2: Maria, a Cientista de Dados**

- **Idade:** 28 anos
- **Cargo:** Cientista de Dados
- **Objetivos:**
    - Facilitar a criação de modelos que possam ser usados em análises preditivas.
    - Garantir que os dados sejam estruturados de forma que maximizem o valor das análises.
    - Minimizar o tempo necessário para preparar dados para projetos de machine learning.
- **Desafios:**
    - Encontrar padrões ocultos nos dados que possam melhorar os modelos preditivos.
    - Ajustar modelos de dados para diferentes cenários de análise.
- **Como o projeto ajuda:**
    - A ferramenta identifica automaticamente padrões nos dados, ajudando Maria a focar mais nas análises e menos na preparação dos dados.

### **Persona 3: Pedro, o Arquiteto de Sistemas**

- **Idade:** 40 anos
- **Cargo:** Arquiteto de Sistemas
- **Objetivos:**
    - Assegurar que a estrutura dos dados atenda às necessidades dos sistemas corporativos.
    - Garantir que os modelos de dados sejam robustos e possam escalar com o crescimento da empresa.
    - Minimizar a complexidade na integração de novos sistemas.
- **Desafios:**
    - Manter a coerência entre diferentes sistemas e bancos de dados.
    - Equilibrar performance com flexibilidade na modelagem de dados.
- **Como o projeto ajuda:**
    - A ferramenta automatiza a otimização dos modelos de dados, o que facilita o trabalho de Pedro ao integrar novos sistemas e manter a performance.

### **Persona 4: Ana, a Gestora de TI**

- **Idade:** 45 anos
- **Cargo:** Gestora de TI
- **Objetivos:**
    - Garantir que as operações de TI sejam eficientes e alinhadas com os objetivos estratégicos da empresa.
    - Minimizar os custos de operação, sem comprometer a qualidade dos serviços.
    - Facilitar a tomada de decisões estratégicas baseadas em dados confiáveis.
- **Desafios:**
    - Justificar os custos e benefícios de novas ferramentas e tecnologias.
    - Gerenciar equipes de TI diversas, garantindo a eficiência e alinhamento entre elas.
- **Como o projeto ajuda:**
    - A ferramenta melhora a eficiência operacional, reduzindo a necessidade de intervenção manual e cortando custos, o que ajuda Ana a justificar o investimento.

---

## Resumo do Projeto

Estamos desenvolvendo um agente de IA que será integrado a uma ampla gama de dados. A interação será semelhante ao ChatGPT, permitindo que o usuário insira um prompt e receba uma saída automatizada. O agente realizará uma espécie de pré-processamento de ETL, facilitando a análise dos dados ao realizar queries específicas automaticamente. Isso reduzirá o tempo necessário para que os especialistas em dados encontrem insights, evitando, por exemplo, a recuperação de dados nulos em determinadas consultas, como dados de vendas de itens específicos.

---

## Requisitos Funcionais

1. **F1:** O sistema deve permitir que o usuário insira um prompt solicitando dados específicos. O agente deve processar a solicitação e retornar os dados com base nos critérios definidos.
    - **Critérios de Aceitação:** O usuário insere um prompt válido, e o sistema retorna os dados corretos por meio do terminal ou em um arquivo CSV tratado.
    - **Prioridade:** P1 (Crítico).
2. **F2:** O agente deve realizar pré-processamento de dados (pré-ETL) automaticamente, eliminando dados inválidos ou nulos com base nas instruções fornecidas pelo usuário.
    - **Critérios de Aceitação:** O sistema filtra e limpa os dados conforme especificado no prompt, retornando os resultados no terminal ou em um arquivo CSV.
    - **Prioridade:** P1 (Crítico).
3. **F3:** O sistema deve gerar e fornecer saídas em formatos adequados, como exibição de dados processados no terminal ou exportação para arquivos CSV tratados.
    - **Critérios de Aceitação:** O sistema gera o arquivo CSV corretamente ou exibe os resultados no terminal sem falhas.
    - **Prioridade:** P2 (Importante).

### Casos de Uso

- **Caso de Uso 1:** O usuário digita um prompt no terminal solicitando a análise de vendas de um determinado produto, e o sistema retorna os dados relevantes no terminal ou como um CSV, excluindo colunas com valores nulos.
- **Caso de Uso 2:** O usuário solicita que o sistema retorne informações financeiras e o agente processa e exporta os resultados filtrados em um arquivo CSV.
- **Caso de Uso 3:** O especialista em dados usa o terminal para otimizar o tempo em consultas complexas, delegando as queries ao agente, que devolve os dados processados no formato escolhido.

---

## Requisitos Não Funcionais

1. **NF1:** O sistema deve ser escalável, suportando grandes volumes de dados e múltiplas requisições simultâneas sem perda de performance.
    - **Prioridade:** P1 (Crítico).
2. **NF2:** O sistema deve garantir a segurança dos dados, evitando vazamento de informações sensíveis durante o processamento e armazenamento.
    - **Prioridade:** P1 (Crítico).
3. **NF3:** O sistema deve ser eficiente e rápido, retornando as saídas no terminal ou gerando arquivos CSV dentro de tempos aceitáveis para o usuário.
    - **Prioridade:** P2 (Importante).

