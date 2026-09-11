# DIAGNÓSTICO LinkedIn — G2B → G4 (2026-09-10)

> Versão: DIAGNOSTICO-2026-09-10 | Sessão somente leitura, **zero alterações no LinkedIn**. Para em G4; **G5 aguarda aprovação humana**.
> Fontes: `LI-BASELINE-2026-09-10.md` (G0/G1/G2A) + base local `C:/Users/cr_bn/career/` (PROFILE, EXPERIENCE, SKILLS, EDUCATION, ACHIEVEMENTS, PREFERENCES, JOB_SEARCH, PROJECTS, QUESTIONS_PENDING; fonte mestra `resumes/master/experiencia-oficial.md`) + observação nova desta rodada (analytics, search appearances, busca de benchmark, 3 vagas do tracker).
> Convenção: **FATO** = observado | **INFERÊNCIA** = interpretação marcada | **HIPÓTESE** = a validar | **NÃO OBSERVÁVEL** = LinkedIn não renderizou / sem acesso.

## Correção ao baseline (FATO novo desta rodada)

- A página `analytics/profile-views` exibe **"19 — Quem viu seu perfil nos últimos 90 dias"**. O baseline registrou "19 visualizações / 7 dias" — **corrigir para 90 dias**.
- Search appearances (página `analytics/search-appearances`, FATO): **42 exibições do perfil (1–7 set)**; **4 ocorrências em resultados de pesquisa (+300% / 7d)**; engajamento **>10 impressões**; LinkedIn sugere "adicionar competências" e "atualizar o perfil". **Termos de busca que levaram ao perfil: NÃO OBSERVÁVEL** (requer Premium / não renderizou).
- Visitantes visíveis sem Premium (FATO, nomes públicos): **Clara Martins** (RH, Digital Growth, há 3h — **1 recrutador**), **Allan Alves** (CEO/Fundador, há 4h), **Dani Amorim** (Psicóloga Organizacional, 1 conexão em comum). Segmentos anonimizados: Telecom (Floripa), imóveis comerciais, contabilidade (fundador), **Insular Auto Peças**, **especialista em e-commerce (Angeloni)**, vendedor atacadista, empresário (esportes). Sinais: "6 encontrou você por meio de um perfil do LinkedIn"; "1 tem uma conexão que pode estar contratando para cargos na sua função".
- Skills detail (`/details/skills/`) e corpo do perfil renderizaram só o shell nesta sessão: **lista completa de skills, detalhe de Formação, certificações, recomendações, Featured: NÃO OBSERVÁVEL** (mantido do baseline). Conhecido (FATO do baseline): top-5 do About + 3 skills vinculadas à Exp1 (Análise de dados, Atendimento ao cliente + 1 não identificada).

---

## G2B — Searchability (Gate G2B)

Cargos-alvo (FATO de PREFERENCES/JOB_SEARCH, ordem do Rafael): **1) E-commerce · 2) Operações · 3) Comercial B2B · 4) Administrativo**.

### Matriz cargo-alvo × keywords

| Cargo-alvo | Keywords PRESENTES no perfil (evidência) | Keywords AUSENTES / fracas | Evidência existente | Gap |
|---|---|---|---|---|
| Gestor/Analista de E-commerce | e-commerce, marketplace, Mercado Livre (loja oficial), SEO de anúncios, ERP (Olist/Tiny), catálogo (2k SKUs), logística/frete, KPIs (FATO: About + Exp1, baseline) | "Gestão de e-commerce" no headline; TikTok Shop/Shopee; Google Ads/Analytics nominais; CRO; "marketplace manager" em inglês | Exp1 + About ricos em termos; visitante "especialista em e-commerce (Angeloni)" sugere match parcial | Headline sem cargo-alvo = peso de busca perdido (skill resume-ats-linkedin: headline+título atual têm MAIOR peso) |
| Operações / Ops Digital | operações digitais, processos, melhoria contínua, integração de sistemas, fluxo do pedido, expansão nacional (FATO: About + Exp1) | "operations", "business operations", ownership/decisões explícitas, SLA, automação nominal no perfil | Exp1 descreve operação fim-a-fim; base confirma fluxo venda→pós-venda | Senioridade operacional diluída entre 6 famílias citadas no About |
| Comercial B2B / Vendas consultivas | B2B, prospecção, negociação (até R$70 mil), CRM, WhatsApp Business (FATO: About + Exp2 + base) | "vendas consultivas", "prospecção ativa/cold calling", "pipeline", HubSpot/Salesforce nominais, SaaS | Exp2 (orçamentos→vendas B2B, Olist/Tiny); Flex (retenção B2B) **fora do LinkedIn** | Sem Flex/MG Vidros no perfil: 5 anos de comercial B2B (2013–14, 2018–20) invisíveis p/ busca |
| Administrativo | rotinas administrativas, atendimento, planilhas/sistemas, organização (FATO: Exp2 + base) | "assistente/analista administrativo" como título atual; Excel nominal; setor jurídico (vaga Causa Certa não exige) | Exp2 cobre rotinas admin/comercial/atendimento | Título atual ("Gestão de E-commerce — Autônomo") não sinaliza admin; vaga-alvo é Júnior (compatível) |

### Search Appearances (FATO)

- 4 ocorrências/7d (+300%), 42 exibições (1–7 set), >10 impressões, 19 views/90d, 1 recrutador visitante. **INFERÊNCIA (média confiança):** descoberta existe mas é baixa e difusa — visitantes vêm de setores variados (imóveis, contabilidade, telecom), não concentrados no núcleo e-commerce/operações. **Termos de busca: NÃO OBSERVÁVEL.**
- **Gate G2B: SATISFEITO** (keywords e cargos sustentados por evidência; lacunas de observabilidade registradas).

---

## G2C — Skill Graph (Gate G2C)

- **Explícitas (FATO):** top-5 do About (Operações de e-commerce, Gestão logística, Melhoria de processos, Automação de processos, Comércio eletrônico) + vinculadas à Exp1 (Análise de dados, Atendimento ao cliente + 1 não identificada). Lista completa: **NÃO OBSERVÁVEL**.
- **Inferidas do texto (INFERÊNCIA forte, com fonte):** SEO de anúncios, gestão de marketplace (ML), ERP Olist/Tiny, gestão de catálogo, negociação logística, CRM/WhatsApp Business, análise de dados/KPIs, treinamento de equipes.
- **Comprovadas (evidência na base):** todas as inferidas acima + prospecção B2B ativa, contratos com transportadoras, fluxo pedido→entrega→pós-venda, evolução orçamentos→e-commerce completo.
- **Fracas (aparecem sem contexto suficiente):** "Automação de processos" (sem exemplo nominal no perfil; Condstore fora do perfil), "Customer Success / Produto" (citados no About como busca, sem experiência titulada), "IA aplicada" (só na base/projetos).
- **Ausentes mas sustentadas pelo histórico (recomendação futura):** Prospecção B2B, Negociação, CRM, Logística e frete, Gestão de marketplaces, ERP, E-mail marketing/Google Ads (se confirmados — **HIPÓTESE: verificar uso real antes de adicionar**), Condstore/automação com link.
- **Gate G2C: SATISFEITO.**

---

## G2D — Senioridade (Gate G2D)

- **FATO:** títulos "Gestão de E-commerce" (Autônomo, 1a6m) + "Assistente administrativo" (3a5m); sem menção a liderança formal, orçamento, time, ou decisões; sem métricas no perfil (2k SKUs/7k clientes estão na descrição mas sem resultado associado; R$300k→800k e R$70 mil **fora do perfil**).
- **Teste de controle** ("sem os títulos, o conteúdo demonstra o nível?"): parcialmente — INFERÊNCIA: Exp1 demonstra **ownership operacional** (gestão multicanal, integrações, expansão nacional) compatível com **pleno / gestor operacional**, mas faltam escala quantificada, decisões e impacto. "Autônomo" rebaixa a leitura para freelancer (INFERÊNCIA média).
- **Verbos/estrutura:** descrições ricas em escopo, pobres em resultado (responsabilidades sem resultados — achado G2D clássico).
- Percebida hoje: **pleno operacional com viés executor**; desejada: **gestor de e-commerce/operações com impacto mensurável**. **Gate G2D: SATISFEITO.**

---

## G2E — Valor oculto (Gate G2E)

| Competência | Evidência (base) | Contexto | Resultado | Keyword de mercado | Cargo relacionado |
|---|---|---|---|---|---|
| Migração/implantação de ERP | Olist/Tiny, site orçamentos→e-commerce | LojaCond Fase 1 | Digitalização completa da operação | Implantação de sistemas, ERP | Operações / Implantação |
| Negociação B2B alto ticket | Até R$70 mil (fabricantes, transportadoras, institucionais) | LojaCond | Contratos + tabelas nacionais | Negociação B2B, vendas consultivas | Comercial B2B |
| Retenção/negociação por metas | Agente Retenção B2B, Claro NET | Flex 2018–20 | **Sem número (lacuna)** | Retenção, contorno de objeções | Comercial B2B / CS |
| SEO de marketplace | Títulos/atributos/categorização, loja oficial ML | LojaCond Fase 2 | Reputação/anúncios (sem métrica) | SEO, Marketplace Manager | E-commerce |
| Logística nacional | Contratos transportadoras, cálculo frete/rastreio | LojaCond | Cobertura nacional | Logística, frete | Operações |
| Automação/IA aplicada | Condstore OS (GitHub), fluxos WhatsApp→pedido→logística | Projeto autoral | **Sem lançamento/métrica (FATO)** | Automação, CRM, IA | Operações/Produto |
| Treinamento de equipes | Treinou colaboradores, interface gerência/diretoria | LojaCond | Liderança informal (sem título formal) | Treinamento, liderança | Operações |
| Escala operacional | 2k SKUs, 7k clientes, R$300k→800k/mês (uso restrito) | LojaCond Fase 2 | Crescimento receita (só p/ e-comm/ops) | E-commerce Manager, growth | E-commerce |

Nada acima está no LinkedIn com esse enquadramento (FATO: About genérico, sem métricas, sem Flex/MG Vidros, sem Condstore). **Gate G2E: SATISFEITO.**

---

## G2F — Evidências / claims (Gate G2F)

| Claim no perfil/base | Classificação | Rastreabilidade |
|---|---|---|
| "Atuo com e-commerce e operações desde 2021" | Comprovada | About + Exp1/Exp2 + base Mar/2021–Abr/2026 |
| Gestão multicanal, 2k SKUs, 7k clientes, ML, ERP | Plausível, evidência parcial | Descrição Exp1; números vêm da base (sem fonte externa no perfil) |
| R$300k→800k/mês | Comprovada p/ uso restrito (fora do perfil hoje) | ACHIEVEMENTS; regra: só e-commerce/operações |
| Negociações até R$70 mil | Plausível, sem evidência no perfil | Base Fase 1; ausente no LinkedIn |
| "Autônomo" (Exp1) | **Contraditória** | Base diz CLT até Abr/2026 — corrigir ou confirmar com Rafael |
| Períodos out/2024–mar/2026 e jun/2021–out/2024 | **Contraditória** | Base: Dez/2022–Abr/2026 e Mar/2021–Dez/2022 |
| "~4 anos" (texto Fase 1) | **Contraditória** | Base: 5 anos+ (QUESTIONS_PENDING) |
| Projetos próprios automação/IA | Genérica (sem link/nome) | PROJECTS (Condstore, sem lançamento) — adicionar link ou remover |
| "Busco posições em E-commerce, Marketplace, Operações, Implantação, CS ou Produto" | Genérica/difusa | 6 famílias diluem sinal — focar (G3) |

**Gate G2F: SATISFEITO.**

---

## G2G — Trajetória (Gate G2G)

- **FATO (base):** MG Vidros (2013–14, jovem aprendiz/venda técnica) → Flex Retenção B2B (2018–20) → LojaCond Assistente (2021–22, estágio→CLT) → LojaCond Gestor E-commerce (2022–26). Formação: Administração (3 anos, trancada) + ADS (cursando, conclusão 2027).
- **FATO (LinkedIn):** só o bloco LojaCond (2021–26). **INFERÊNCIA:** narrativa atual = "profissional de empresa única regional" (progressão visível, mas sem raiz comercial anterior nem transição explicada).
- Narrativa causal permitida pelos fatos: **venda técnica → retenção/negociação B2B por metas → estruturação comercial e digitalização → gestão de e-commerce em escala** — progressão coerente rumo ao núcleo, com Administração→ADS como ponte operação→tecnologia. Hiato 2014–18 e 2020–21: **não explicados (não inventar)**.
- **Gate G2G: SATISFEITO.**

---

## G2H — Benchmark (Gate G2H)

Observados via busca "Gestor de E-commerce" + 2 perfis visitados (somente leitura; **nada copiado**):
- Padrão de headline: **cargo + pipe + 2–5 especialidades** (ex.: "Gestor de E-commerce & Marketplaces | Estratégia Digital | Mercado Livre | … | Performance | Growth"). Contraste: headline do Rafael é frase institucional sem cargo buscável (FATO).
- Padrões: 180–230+ conexões/seguidores vs 6 do Rafael (FATO); atividade pública frequente (posts de mudança, playbook ML); especialidades recorrentes: **Marketplaces, Performance/Ads, SEO, ERP/CRM, Growth**.
- **Padrão de mercado ≠ requisito:** atividade intensa e "growth" são padrão, não obrigação; diferencial do Rafael (operação fim-a-fim + B2B + automação/ADS) é raro nesse recorte (INFERÊNCIA média).
- **Gate G2H: SATISFEITO.**

---

## G2I — Auditoria de vagas (Gate G2I)

Vagas do tracker (descrições reais extraídas hoje):

| Vaga | Aderência | Evidências fortes | Gaps (tipo) | Keywords | Ação |
|---|---|---|---|---|---|
| VHL Sistemas — Sales Consultant Pleno (home office+viagens) | 78% (tracker) | Prospecção B2B ativa, negociação, viagens+CNH B, formação em andamento, CRM/WhatsApp | **Experiência:** vender SaaS (parcial); cartório (diferencial); **keyword:** pipeline, cold calling, HubSpot/Salesforce nominais | Prospecção ativa, CRM, pipeline, metas, B2B consultivo | Currículo B2B; perfil: nominalizar CRM/pipeline |
| Causa Certa — Analista Adm. Vendas Jr (R$2.627 CLT remoto) | ~85% | Organização, comunicação, rotinas admin, planilhas/sistemas, admin/comercial/atendimento | **Evidência de impacto:** sem SLA/métricas (não exigido); jurídico (não exigido) | Contratos, documentação, prazos, planilhas, apoio a vendas | Aplicar (currículo pronto); perfil: keywords "contratos/prazos" |
| Rede franquias — Customer Success (R$4,5k PJ presencial, WITHDRAWN) | ~70% | B2B, indicadores, processos, comunicação | **Experiência:** franquias; título CS; **senioridade/logística:** deslocamento + PJ presencial | Relacionamento, indicadores, retenção, comunicação | Mantida como referência de keywords CS/relacionamento |

Padrão entre vagas (INFERÊNCIA média): **CRM/pipeline + prospecção ativa + indicadores + comunicação** repetem-se; nenhum gap é bloqueador exceto SaaS/cartório (diferenciais). Gaps são majoritariamente **de keyword/evidência**, não de competência real. **Gate G2I: SATISFEITO.**

---

## G2J — Adversarial (Gate G2J)

1. **Recrutador (30s):** "Para qual vaga serve?" — Resposta: e-commerce operacional de empresa pequena; **não sei o nível nem se é CLT** ("Autônomo" + headline sem cargo). Risco: descarte por ambiguidade.
2. **Hiring manager:** "Que problema resolve?" — Digitaliza e opera vendas (orçamento→e-commerce, ERP, logística), mas **sem número de impacto** não diferencio de qualquer assistente com 5 anos de casa.
3. **Sistema de busca:** termos que conectam ≈ {e-commerce, marketplace, operações, logística, B2B, atendimento} — presentes no About; mas **headline e título atual não repetem o cargo-alvo** (peso máximo desperdiçado) e skills explícitas são poucas.
- **Contradições:** (a) About mira 6 famílias × base define núcleo único; (b) "Gestão" no título × conteúdo sem decisões/métricas; (c) Open-to-work amplo (presencial+híbrido+remoto, 4 praças) × headline de empresa única (sinal local, não móvel); (d) visitantes reais incluem RH e e-commerce (Angeloni) mas também setores aleatórios — descoberta sem direção.
- **Gate G2J: SATISFEITO.**

---

## G3 — Estratégia de posicionamento (Gate G3 — proposta, sem aplicar)

1. **Identidade principal:** Gestor de E-commerce e Operações Digitais (B2B + marketplaces + processos).
2. **Cargos-alvo (ordem):** Analista/Gestor de E-commerce · Operações/Processos · Comercial B2B/Vendas consultivas · Administrativo (ponte, não identidade).
3. **Setores:** e-commerce/tecnologia/SaaS; adjacente: operações e comercial B2B (Grande Florianópolis + remoto).
4. **Competências centrais:** gestão multicanal/marketplace, ERP e integrações, logística/frete, SEO de anúncios, CRM e prospecção B2B, análise de dados/KPIs.
5. **Diferenciais comprováveis:** escala (2k SKUs/7k clientes), digitalização completa (orçamento→e-commerce+ERP), negociação (R$70 mil), automação/ADS+Condstore.
6. **Evidências prioritárias:** métricas no About/Exp1, Flex+MG Vidros, link Condstore/GitHub.
7. **Keywords prioritárias:** e-commerce, marketplace, Mercado Livre, ERP, logística, SEO, CRM, prospecção B2B, pipeline, processos, indicadores.
8. **Remover/reduzir:** "Autônomo", 6 famílias no About, "~4 anos", projetos próprios sem link.
9. **Tom:** primeira pessoa, executor com ownership, parágrafos curtos, keywords nos primeiros ~300 caracteres.
10. **Limites (não afirmar):** liderança formal, inglês além do declarado, métricas fora das autorizadas, SaaS/cartório como experiência, resultados do Condstore.
- **Frase interna:** "Gestor de e-commerce e operações digitais que transformou orçamentos em e-commerce nacional (2k SKUs, 7k clientes) e negocia B2B de alto ticket — com base técnica em ADS e automação."
- **Gate G3: ESTRATÉGIA PROPOSTA — requer validação do Rafael antes de G5.**

---

## Plano P0–P3

- **P0 (crítico):** LI-CHANGE-001 (headline), 002 (vínculo Autônomo + datas).
- **P1 (alto impacto):** 003 (título Exp1), 004 (Exp2), 005/006/007 (About), 008 (Flex+MG Vidros), 009 (skills).
- **P2 (clareza/conversão):** 010 (Featured/Condstore), 011 (formação), 012 (recomendações), 013 (network).
- **P3 (experimental):** 014 (open-to-work), 015 (conteúdo/modo criador).
- Ordem: identidade → headline → About → experiências → skills → Featured → formação → prova social → network → configurações → conteúdo.

## G4 — Propostas Before/After (Gate G4 — propostas, NADA aplicado)

- **LI-CHANGE-001 [P0] Headline.** Antes (FATO): "Gestão de projetos de e-commerce da empresa Lojacond Equipamentos para Condomínios". Depois (proposta): "Gestor de E-commerce e Operações Digitais | Marketplace, ERP, Logística e Vendas B2B". Motivo: cargo-alvo + 2–4 competências; headline tem o maior peso em busca. Evidência: About/base + padrão benchmark. HIPÓTESE: ↑ ocorrências em busca p/ "e-commerce/marketplace". Risco: baixo; rever se Rafael preferir título + empresa.
- **LI-CHANGE-002 [P0] Exp1 vínculo + datas.** Antes: "Autônomo · out/2024–mar/2026". Depois: "Tempo integral · Dez/2022–Abr/2026" (ou o que o Rafael confirmar). Motivo: contradição com base CLT; "Autônomo" induz leitura freelancer. Evidência: EXPERIENCE.md. HIPÓTESE: ↑ credibilidade/senioridade. Risco: **médio — exige confirmação do Rafael (divergência registrada)**.
- **LI-CHANGE-003 [P1] Exp1 título.** Antes: "Gestão de E-commerce — Lojacond Store". Depois: "Gestor de E-commerce e Operações Digitais — Lojacond (Store + Equipamentos, bloco único)". Motivo: nomenclatura de mercado + progressão contínua. Evidência: base duas fases. HIPÓTESE: ↑ match recrutador. Risco: baixo.
- **LI-CHANGE-004 [P1] Exp2 datas/título.** Antes: "Assistente administrativo · jun/2021–out/2024". Depois: "Assistente Administrativo e Comercial · Mar/2021–Dez/2022" (a confirmar). Motivo: coerência com base + comercial explícito. Evidência: EXPERIENCE.md. HIPÓTESE: ↑ sinal B2B. Risco: médio (datas — confirmar).
- **LI-CHANGE-005 [P1] About — abertura.** Antes: abertura atual sem cargo/métrica nos ~300 primeiros caracteres. Depois: abrir com frase de posicionamento G3 + keywords (e-commerce, marketplace, ERP, logística, B2B). Motivo: AI-search e recrutador leem o topo. Evidência: skill LinkedIn (keywords nos primeiros ~300). HIPÓTESE: ↑ descoberta + clareza 30s. Risco: baixo.
- **LI-CHANGE-006 [P1] About — métricas.** Antes: zero números. Depois: 2k SKUs, 7k clientes, R$300k→800k (só e-comm/ops), R$70 mil negociações. Motivo: evidência de impacto (G2F). Evidência: ACHIEVEMENTS + regra de uso. HIPÓTESE: ↑ conversão visita→contato. Risco: baixo (dentro do autorizado).
- **LI-CHANGE-007 [P1] About — foco.** Antes: 6 famílias (E-commerce, Marketplace, Operações, Implantação, CS, Produto). Depois: núcleo + 1 frase-ponte p/ adjacentes. Motivo: sinal difuso (G2J). Evidência: PREFERENCES (ordem de cargos). HIPÓTESE: ↑ precisão do matching. Risco: baixo.
- **LI-CHANGE-008 [P1] Adicionar Flex + MG Vidros.** Antes: ausentes (trajetória começa 2021). Depois: 2 entradas com descrições da base, sem métricas inventadas. Motivo: 5 anos de B2B invisíveis; raiz comercial. Evidência: EXPERIENCE.md. HIPÓTESE: ↑ match B2B/comercial + trajetória completa. Risco: baixo.
- **LI-CHANGE-009 [P1] Skills 20–40 + top-3.** Antes: top-5 genérico + 3 vinculadas (lista completa não observável). Depois: fixar (ex.) E-commerce, Gestão de marketplace, ERP; completar com SEO, CRM, logística, negociação B2B, análise de dados etc. — só as verdadeiras. Motivo: 5+ skills ≈ 17–33x views (pesquisa 2026); AI-search usa skills. Evidência: SKILLS.md. HIPÓTESE: ↑↑ descoberta. Risco: baixo-médio (exige auditoria item a item — nada popular por ser popular).
- **LI-CHANGE-010 [P2] Featured + Condstore.** Antes: sem Featured/projetos (não observável/ausente). Depois: Featured com GitHub Condstore + descrição honesta (laboratório, sem lançamento). Motivo: prova técnica/automação (diferencial raro). Evidência: PROJECTS.md. HIPÓTESE: ↑ diferenciação p/ operações/produto. Risco: baixo (desde que sem overclaim).
- **LI-CHANGE-011 [P2] Formação detalhada.** Antes: só "UNISUL" no cabeçalho. Depois: ADS (cursando, 2027) + Administração (3 anos, trancada) + certificados (Jovem Aprendiz, Assistente Administrativo 2012). Motivo: title-weight + palavras de curso (SQL, banco de dados, gestão). Evidência: EDUCATION.md. HIPÓTESE: ↑ match júnior/ops + credibilidade. Risco: baixo.
- **LI-CHANGE-012 [P2] Recomendações (1–2).** Antes: nenhuma observável. Depois: solicitar a ex-gerência/diretoria LojaCond. Motivo: prova social (evidência moderada). Evidência: base (interface direta). HIPÓTESE: ↑ conversão. Risco: baixo (depende de terceiros).
- **LI-CHANGE-013 [P2] Network 6 → 200+.** Antes: 6 conexões, 6 seguidores. Depois: rotina de conexões (ex-colegas, fornecedores, pares e-commerce/SC). Motivo: rede mínima limita alcance e sinal social. Evidência: benchmark (180–230+). HIPÓTESE: ↑ visitas e "encontrado via perfil". Risco: baixo (sem spam).
- **LI-CHANGE-014 [P3] Open-to-work.** Antes: 4 praças, presencial+híbrido+remoto (amplo). Depois: manter amplo (coerente c/ PREFERENCES) + revisar títulos-alvo das preferências de vaga. Motivo: alinhar sinal ao G3. Evidência: PREFERENCES. HIPÓTESE: melhor recomendação de vagas. Risco: mínimo.
- **LI-CHANGE-015 [P3] Conteúdo.** Antes: 0 impressões publicação, 1 comentário. Depois: 1 post/mês (playbook real: ex. SEO de anúncios ML) — experimental. Motivo: branding; SEM evidência de impacto em ranking (skill). HIPÓTESE: ↑ visitas de pares/recrutadores. Risco: baixo (custo de tempo).

**Gate G4: 15 propostas documentadas — SATISFEITO. Gate G5: AGUARDANDO APROVAÇÃO HUMANA (nada aplicado).**

## Scorecard interno (0–5, comparação temporal, não oficial)

Clareza 2 · Discoverability 2 · Alinhamento cargos 2 · Evidências 1 · Senioridade 2 · Coerência 3 · Skills 2 · Prova social 1 · Conversão 2 · Autenticidade 4. Justificativas: perfil honesto e coerente, mas sem cargo buscável, sem métricas, sem prova social e com rede mínima.

## Backlog (p/ loop XVIII)

Confirmar vínculo/datas LojaCond; números Flex (retenção, volume); volume pedidos/dia LojaCond; SLA/entrega; cursos livres reais; status Administração; termos reais de busca (Premium); monitorar 42 exibições/4 buscas como linha de comparação pós-mudança.
