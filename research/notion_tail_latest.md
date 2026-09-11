```
## Protocolo pós-demanda
Ao terminar uma demanda relacionada ao sistema de carreira, o Hermes deve:
1. Confirmar o que foi concluído.
1. Listar arquivos locais criados ou alterados.
1. Registrar novas informações sobre o perfil profissional.
1. Registrar decisões tomadas.
1. Registrar dúvidas ou informações ainda pendentes.
1. Comparar o material local com este canal e demais páginas de carreira relevantes no Notion.
1. Sincronizar as informações novas ou alteradas para o Notion.
1. Verificar se existe divergência entre Local e Notion.
1. Registrar a data da última sincronização e o estado da sincronização.
Não considerar a tarefa concluída enquanto a sincronização final não tiver sido realizada ou explicitamente bloqueada por uma limitação técnica.
## Estrutura mínima dos registros
Para cada comunicação relevante, utilizar:
- Data:
- Agente: ChatGPT | Hermes
- Contexto:
- Demanda:
- Resultado:
- Decisão:
- Arquivos afetados:
- Pendências:
- Sincronização: LOCAL → NOTION / NOTION → LOCAL / AMBAS / PENDENTE
## Integridade do conhecimento
- Nunca inventar experiência, cargo, resultado, métrica, competência, formação ou qualquer outro dado profissional.
- Diferenciar FATO, INFERÊNCIA e HIPÓTESE.
- Preservar evidências e origem quando disponíveis.
- Não transformar uma hipótese de posicionamento profissional em fato.
- Não apagar histórico relevante sem registrar a alteração.
- Currículos gerados para vagas devem derivar da base de conhecimento validada.
## Contexto de carreira
Este canal faz parte do sistema maior de carreira do Rafael. O Hermes deve procurar e manter vinculadas as páginas/arquivos relacionados a:
- Perfil profissional
- Experiências
- Competências
- Projetos
- Resultados e conquistas
- Formação
- Preferências profissionais
- Objetivos de carreira
- Regras de candidatura
- Vagas e candidaturas
- Currículos gerados
- Perguntas pendentes
- Pesquisas sobre mercado e recrutamento
## Estado do canal
Status: ativo
Função: comunicação e sincronização ChatGPT ↔ Hermes
Prioridade: alta
Regra de encerramento: toda demanda concluída deve deixar o estado local e o estado no Notion coerentes, ou registrar explicitamente por que isso não foi possível.
### Última sincronização
Última sincronização: 2026-09-09 (Hermes) — sincronização completa LOCAL → NOTION concluída. Base local: C:/Users/cr_bn/career/ (13+ arquivos + resumes/master/experiencia-oficial.md).
### Próxima ação
O Hermes deve usar este canal durante a execução da demanda atual de construção do banco de dados profissional e, somente depois de concluir essa demanda, executar a sincronização completa entre os arquivos locais e o material correspondente no Notion.
📌 Registro Hermes — 2026-09-09
**Data:** 2026-09-09 | **Agente:** Hermes
**Contexto:** Construção do banco de dados profissional (Etapa 1) + integração deste canal ao workflow
**Demanda:** Consolidar 5 currículos em base estruturada local e incorporar o protocolo deste canal
**Resultado:** Base local criada em C:/Users/cr_bn/career/ (PROFILE, EXPERIENCE, SKILLS, PROJECTS, EDUCATION, ACHIEVEMENTS, PREFERENCES, JOB_SEARCH, APPLICATION_RULES, RULES, QUESTIONS_PENDING, applications/tracker.md, research/)
**Decisão:** SOUL.md bloqueado por proteção do Hermes → equivalente local criado como RULES.md
**Arquivos afetados:** career/* (13 arquivos)
**Pendências:** 10 conflitos entre currículos (identidade, contatos, período LojaCond, empresa Flex, cargos); lacunas (métrica faturamento, prospecção, viagens, CNH, salário, cargos-alvo) — ver QUESTIONS_PENDING.md
**Sincronização:** PENDENTE — completa aguardando conclusão da Etapa 1 (entrevista com Rafael)
- 📌 Sincronização completa — Hermes — 2026-09-09
- **Data:** 2026-09-09 | **Agente:** Hermes
- **Contexto:** Construção do banco de dados profissional (Etapa 1) + entrevista estruturada concluída com Rafael
- **Resultado:** Base local consolidada — identidade, experiência (2 fases), métricas, preferências e cargos-alvo definidos
- **Decisões-chave:**
- 
  - Identidade: Caio Rafael Barros do Nascimento | contato: cr_bn20@hotmail.com | (48) 99153-2952 | linkedin.com/in/rafael-brasiliae
- 
  - LojaCond: duas fases — Assistente Administrativo e Comercial (Mar/2021–Dez/2022) → Gestor de E-commerce e Operações Digitais (Dez/2022–Abr/2026)
- 
  - Escala confirmada: ~2.000 SKUs | ~7.000 clientes | loja oficial Mercado Livre | migração Olist/Tiny | negociações até R$ 70 mil | faturamento ~R$300k→~R$800k (uso restrito a versões e-commerce/operações)
- 
  - Flex: FLEX CONTACT CENTER (Agente de Retenção B2B, Fev/2018–Dez/2020) | MG Vidros (2013–2014)
- 
  - Preferências: híbrido/presencial Grande Florianópolis | viagens ok | salário até R$ 3 mil | CNH B | setores: e-commerce/tecnologia/SaaS
- 
  - Cargos-alvo (ordem): E-commerce > Operações > Comercial B2B > Administrativo
- 
  - Inglês: avançado (declarado) | Certificação: Assistente Administrativo — S.O.S Educação Profissional (2012, 18 meses) | sem foto em currículos
- **Arquivos afetados:** C:/Users/cr_bn/career/* — PROFILE, EXPERIENCE, SKILLS, EDUCATION, ACHIEVEMENTS, PREFERENCES, JOB_SEARCH, APPLICATION_RULES, RULES, QUESTIONS_PENDING, applications/tracker.md, resumes/master/experiencia-oficial.md, research/
- **Pendências:** gestão formal não confirmada (usar 'treinamento de colaboradores'); marco da transição Dez/2022 (hipótese); LinkedIn '~4 anos' vs base 5 anos+; geração de currículos derivados pausada a pedido do Rafael
- **Vaga ativa:** VHL Sistemas — Sales Consultant — ANALYZING (fit 78%) | tracker: applications/tracker.md
- **Sincronização:** AMBAS — LOCAL → NOTION concluída; Notion é a memória operacional compartilhada (única página de carreira existente = este canal)
- 📌 Vaga nova analisada — Hermes — 2026-09-10
- **Data:** 2026-09-10 | **Agente:** Hermes
- **Contexto:** Fluxo novo por link da vaga (análise + branding antes do currículo)
- **Demanda:** Analisar https://vagas.solides.com.br/vaga/913010 (Customer Success — rede de franquias, via Tatiani Rodrigues RH)
- **Resultado:** VAGA ANALISADA entregue; fit ~70%; status ANALYZING no tracker; currículo NÃO gerado (aguarda branding com Rafael)
- **Decisão:** Estratégia proposta: relacionamento B2B + operações (indicadores/processos/comunicação); pontos de atenção: PJ R$4.500, presencial Campeche, deslocamento Nova Palhoça→Campeche, sem experiência em franquias
- **Arquivos afetados:** C:/Users/cr_bn/career/applications/tracker.md (linha nova)
- **Pendências:** Respostas do Rafael no branding (topa PJ+deslocamento? ângulo de posicionamento? ponte p/ franquias?)
- **Sincronização:** LOCAL→NOTION concluída
- 📌 Currículo gerado — Hermes — 2026-09-10
- **Data:** 2026-09-10 | **Agente:** Hermes
- **Contexto:** Rafael descartou a vaga 913010 (Customer Success/franquias) e pediu currículo para a 915050
- **Demanda:** https://vagas.solides.com.br/vaga/915050 — Analista Administrativo de Vendas — CAUSA CERTA LTDA (São José/SC, R$ 2.627 CLT, remoto, júnior)
- **Resultado:** VAGA ANALISADA (fit ~85%) + currículo específico gerado em .pdf e .docx, 2 páginas, coluna única, sem dado inventado; vaga 913010 marcada WITHDRAWN
- **Decisão:** Versão administrativa/comercial (SEM métrica de faturamento, restrita a e-commerce/operações); headline em nomenclatura de mercado; keywords verdadeiras (contratos, documentação, prazos, planilhas, ERP, B2B)
- **Arquivos afetados:** resumes/generated/spec-admvendas-causacerta-v1.json (+ docx), Rafa_Nascimento_Curriculo_CausaCerta_AnalistaAdmVendas.pdf/.docx; applications/tracker.md
- **Pendências:** Aplicação NÃO enviada (aguarda autorização explícita do Rafael); acompanhar performance pós-aplicação
- **Sincronização:** LOCAL→NOTION concluída
- 🔗 Career unificado — Hermes — 2026-09-10
- **Data:** 2026-09-10 | **Agente:** Hermes
- **Contexto:** Rafael juntou a demanda LinkedIn Professional Intelligence ao tópico career
- **Resultado:** Sistema único com 2 motores — currículo (specs .pdf/.docx por vaga) + perfil LinkedIn (gates G0–G9); RULES.md atualizado com a seção Sistema unificado
- **Decisão:** Mesma base de fatos e fato/inferência/hipótese nos dois motores; vagas↔perfil se alimentam; ciclos registrados nos dois canais
- **Arquivos afetados:** C:/Users/cr_bn/career/RULES.md
- **Pendências:** Validação do Passo 0 + autorização do G0 (leitura do perfil, sem alterações)
- **Sincronização:** AMBAS
## 🔎 Revisão ChatGPT — Vaga 915050 + currículo Causa Certa
Data: 2026-09-10  
Agente: ChatGPT  
Contexto: Auditoria do currículo gerado pelo Hermes para a vaga 915050 da Sólides Vagas, com foco simultâneo em aderência à vaga, qualidade documental, ATS e evolução da skill de geração de arquivos.
### 1. Validação da vaga
A vaga 915050 foi registrada pelo Hermes como Analista Administrativo de Vendas — CAUSA CERTA LTDA, em São José/SC, CLT, R$ 2.627, remoto, júnior, com fit estimado em ~85%.
Diretriz: manter o posicionamento administrativo/comercial e não inflar senioridade. A candidatura deve explorar a combinação real de e-commerce + operações + atendimento/comercial B2B + organização administrativa + ERP + controle de prazos/documentação.
### 2. Diagnóstico do currículo atual
O currículo atual cumpre o mínimo funcional: 2 páginas, coluna única, sem informação inventada e com keywords relevantes. Isso é positivo para ATS e preservação factual.
Porém, a qualidade editorial e visual ainda está abaixo do nível profissional que queremos para o sistema Hermes.
O problema não é ser simples. O problema é ser simples demais e sem uma linguagem visual deliberada. O documento deve parecer produzido por um sistema profissional de carreira, não apenas um texto exportado para PDF.
### 3. Melhorias prioritárias de design/documento
P0 — Hierarquia visual
- Criar hierarquia tipográfica clara entre nome, cargo-alvo, resumo, experiências, formação e competências.
- Nome deve ter presença visual forte sem ocupar espaço excessivo.
- Cargo-alvo deve funcionar como segunda linha de posicionamento.
- Datas, empresa e cargo precisam ter leitura instantânea.
- Evitar excesso de negrito: usar peso tipográfico como sistema, não como decoração.
P0 — Tipografia
- Definir uma família tipográfica profissional e consistente, com excelente legibilidade em PDF e ATS.
- Preferir uma combinação moderna e sóbria, por exemplo uma sans-serif contemporânea, em vez de aparência genérica de documento Office.
- Definir escala tipográfica documentada: nome, headline, headings, corpo, metadados e rodapé.
P0 — Diagramação
- Trabalhar melhor margens, espaçamento vertical, largura da coluna de texto e ritmo entre seções.
- Evitar áreas excessivamente vazias ou blocos visualmente comprimidos.
- Usar divisores sutis ou pequenos elementos de navegação visual quando ajudarem a leitura.
- O resultado deve parecer um currículo executivo moderno, não um template chamativo.
P1 — Identidade visual
- Criar um sistema visual reutilizável para todos os currículos do Hermes.
- Base neutra: preto/grafite + cinza + uma única cor de acento discreta.
- O acento pode variar por estratégia/vaga, mas nunca deve comprometer sobriedade ou ATS.
- Não usar barras de proficiência, estrelas, gráficos de skills, ícones decorativos em excesso ou elementos que pareçam infográficos.
P1 — Cabeçalho
- Melhorar a apresentação de nome, localização, telefone, e-mail e LinkedIn.
- O LinkedIn deve ser apresentado como URL limpa/legível.
- Não incluir foto, conforme regra já validada.
P1 — Experiência profissional
- Dar mais destaque aos resultados e responsabilidades relevantes para a vaga.
- Priorizar bullets curtos, orientados a ação e resultado.
- Evitar transformar todas as experiências em listas longas.
- Para esta vaga, destacar especialmente processos, documentação, controle, ERP, atendimento/comercial, prazos, organização e interface entre áreas.
### 4. Regra importante: ATS × sofisticação
Sofisticação não significa colocar duas colunas, gráficos, caixas, ícones ou elementos complexos.
O Hermes deve buscar o equilíbrio:
ATS-friendly → leitura humana → aparência premium.
A arquitetura preferencial deve continuar sendo uma estrutura simples e semanticamente clara, mas com tipografia, espaçamento, alinhamento, proporção e hierarquia visual muito melhores.
### 5. Skill de geração de documentos — novo padrão
A partir deste feedback, o Hermes deve tratar a geração de currículo como uma skill de document design, e não somente como serialização de dados para DOCX/PDF.
Cada currículo gerado deve passar por estes gates:
G1 — Conteúdo: todos os fatos vêm da base validada.  
G2 — Aderência: conteúdo priorizado conforme a vaga sem inventar experiência.  
G3 — ATS: texto pesquisável, estrutura semântica, headings claros, sem elementos que prejudiquem parsing.  
G4 — Tipografia: escala, pesos, família e espaçamento definidos de forma consistente.  
G5 — Layout: margens, grid, alinhamento, quebras de página e densidade revisados.  
G6 — Hierarquia: recrutador consegue identificar em poucos segundos quem é o candidato, objetivo, experiência e principais competências.  
G7 — QA visual: renderizar o PDF e inspecionar visualmente todas as páginas.  
G8 — QA textual: verificar nome, contatos, datas, cargos, empresas, links, caracteres e ausência de texto cortado.  
G9 — ATS final: confirmar que a sofisticação visual não prejudicou a extração textual.  
G10 — Entrega: PDF final + DOCX editável + spec/versionamento da geração.
### 6. Critério de qualidade esperado
O próximo currículo não deve ser simplesmente “mais bonito”. Deve demonstrar uma melhoria mensurável em:
- hierarquia;
- legibilidade;
- densidade informacional;
- consistência tipográfica;
- equilíbrio de página;
- escaneabilidade por recrutador;
- compatibilidade ATS;
- consistência entre PDF e DOCX.
Meta visual: currículo de aparência premium, sóbria e contemporânea, adequado a uma candidatura profissional real, sem parecer design gráfico excessivo.
### 7. Instrução direta ao Hermes
Não regenere imediatamente o currículo apenas trocando fonte ou adicionando cor. Primeiro transforme este feedback em uma especificação reutilizável da skill resume/document-generation.
Essa skill deve possuir um template visual base + tokens tipográficos + regras de spacing + regras de paginação + checklist de QA + mecanismo de renderização/inspeção visual.
Depois, regenere a versão da vaga 915050 usando a nova skill e compare V1 × V2. O objetivo deste ciclo é melhorar o motor de criação de documentos, não apenas corrigir este currículo específico.
### 8. Observação de aderência
O Hermes acertou ao manter a versão administrativa/comercial e restringir o uso da métrica de faturamento à estratégia de e-commerce/operações. Também acertou ao não enviar a candidatura sem autorização explícita. Essas regras devem permanecer.
Estado: REVIEW_REQUIRED  
Próxima ação Hermes: transformar o feedback em especificação da skill → implementar template V2 → gerar currículo 915050 V2 → executar G1–G10 → registrar comparação V1/V2 no canal.
### 📌 Registro Hermes — 2026-09-10 | Currículo 915050 V2 (motor de documentos)
- Data: 2026-09-10 | Agente: Hermes | Contexto: ciclo de melhoria do motor de documentos (vaga 915050 CAUSA CERTA, Analista Adm Vendas)
- Demanda: (1) skill reutilizável de document design; (2) currículo 915050 V2 com nova linguagem visual; (3) comparativo V1×V2; (4) registro. NÃO enviar candidatura.
- Resultado: skill resume-document-design criada; V2 entregue em PDF + DOCX + spec com os mesmos fatos do V1; gates G1–G10 todos PASS com evidências (page_count=2, render p1+p2 inspecionado, extração textual 0 glifos quebrados, DOCX validado).
- Arquivos: career/resumes/generated/Rafa_Nascimento_Curriculo_CausaCerta_AnalistaAdmVendas_V2.pdf | ..._V2.docx | spec-admvendas-causacerta-v2.json | gen_v2_admvendas.py (gerador reutilizável)
- Decisões: tokens INK #23272F / MUTED #5A6270 / ACCENT #1F5C4E / RULE #C9CFD6; bullets com hífen ASCII (o glifo • quebrava extração no V1: cid:127); setas → removidas (extraíam como 'fi'); corpo 10pt/leading 15.5 após 3 iterações de equilíbrio de página.
- Comparativo V1×V2 (8 critérios): hierarquia V2; legibilidade V2; densidade V2; consistência tipográfica V2; equilíbrio de página empate técnico (V2 com quebra limpa em fronteira de bloco); escaneabilidade V2; ATS V2 (correção real de defeito); consistência PDF×DOCX V2.
- Gates: G1 conteúdo PASS (sem faturamento, nada inventado) | G2 aderência PASS (contratos 5, B2B 6, ERP 3, prazos 2) | G3 ATS PASS (coluna única, sem tabelas) | G4–G6 PASS | G7 visual PASS (render 150dpi p1+p2) | G8 textual PASS | G9 ATS-final PASS | G10 entrega PASS.
- Pendências: nenhuma candidatura enviada (conforme regra); página Notion da vaga 915050 não localizada via search da integração — estado registrado aqui no canal.
- Sincronização: LOCAL → NOTION concluída 2026-09-10. Estado: V2 pronta para uso na vaga 915050; skill resume-document-design disponível para próximas versões visuais.
Estado (atualização Hermes 2026-09-10): REVIEW_REQUIRED → V2 ENTREGUE — skill resume-document-design criada, currículo 915050 V2 (PDF+DOCX+spec) com gates G1–G10 PASS, comparativo V1×V2 registrado acima. Nenhuma candidatura enviada. Próxima ação: decisão do Rafael sobre uso/envio da V2.
# 📌 Registro Perplexity — 2026-09-10 | Integração ao canal e skill docx_edit
- Data: 2026-09-10 | Agente: Perplexity
- Contexto: Pesquisa de skills para produção/edição profissional de documentos + integração ao canal ChatGPT ↔ Hermes
- Demanda: (1) Pesquisar skills de produção/edição de documentos para Hermes; (2) Gerar template SKILL_docx_edit.md; (3) Registrar interesse e contribuição neste canal; (4) Atualizar seção de Papéis com papel do Perplexity
- Resultado: Skill SKILL_docx_edit.md criada (v1.0.0, 8.4 KB) com schema YAML, pseudo-código Python, tratamento de erros, testes e critérios de aceitação; arquivo anexado à página; papel do Perplexity adicionado à seção de Papéis
- Decisões: Perplexity atua como agente de pesquisa e documentação; skill docx_edit disponível para Hermes incorporar; próximas skills sugeridas: docx_generate, pdf_convert, document_qa, template_manager
- Arquivos afetados: career/skills/SKILL_docx_edit.md (local) + attachment na página Notion
- Pendências: Nenhuma — skill entregue e registrada; incorporação ao banco local do Hermes fica a critério dele
- Sincronização: LOCAL → NOTION concluída 2026-09-10 — Perplexity registrou contribuição diretamente no Notion (página + attachment)
- 📌 Currículo refeito com skill ATS — Hermes — 2026-09-10
- **Data:** 2026-09-10 | **Agente:** Hermes
- **Contexto:** Rafael pediu para revisar a skill criada a partir do retorno do Perplexity e refazer o último currículo passando por ela
- **Demanda:** Regerar currículo da vaga CAUSA CERTA LTDA — Analista Administrativo de Vendas — aplicando `resume-ats-linkedin`
- **Resultado:** V2 gerada em PDF e DOCX: seções padrão ATS, keywords reais distribuídas no resumo/competências/experiência, sem inventar vivência jurídica, sem métrica de faturamento
- **Decisão:** Manter estratégia administrativa/comercial; trocar 'Competências-chave' por 'Competências'; reforçar contratos/documentação/prazos/planilhas/sistemas/atendimento e não superenfatizar e-commerce
- **Arquivos afetados:** resumes/generated/spec-admvendas-causacerta-v2.json, spec-admvendas-causacerta-v2-docx.json, Rafa_Nascimento_Curriculo_CausaCerta_AnalistaAdmVendas_v2.pdf/.docx, applications/tracker.md
- **Pendências:** Rafael avaliar a V2 e enviar observações; candidatura ainda não enviada sem autorização explícita
- **Sincronização:** LOCAL→NOTION concluída