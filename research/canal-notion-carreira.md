Este é o canal operacional compartilhado entre **ChatGPT** e **Hermes** para o projeto de inteligência de carreira e candidaturas de Rafael.
## Objetivo
Servir como **ponte persistente de contexto, validação e sincronização** entre o trabalho realizado pelo ChatGPT no ambiente Notion e o trabalho local executado pelo Hermes.
O canal deve concentrar decisões, descobertas, pendências, validações e referências necessárias para que os dois agentes trabalhem sobre a mesma base sem duplicar ou contradizer informações.
## Papéis
### ChatGPT
- Analisar criticamente a estrutura e a qualidade do sistema de carreira.
- Ajudar a interpretar experiências, competências e posicionamento profissional.
- Validar estratégias de currículo e candidatura quando solicitado.
- Identificar inconsistências, lacunas e informações que precisam de confirmação.
- Propor melhorias estruturais no banco de conhecimento e no workflow.
### Hermes
- Manter a execução local e os arquivos locais do sistema de carreira.
- Processar currículos, documentos e demais fontes disponíveis localmente.
- Manter `SOUL.md`, perfil profissional, experiências, competências, projetos e demais arquivos de carreira.
- Gerar currículos específicos para vagas e manter o acompanhamento das candidaturas.
- Registrar neste canal resultados importantes da execução local.
- Sincronizar o estado local com o material mantido no Notion ao concluir cada ciclo relevante.
## Regra fundamental de sincronização
Existem duas representações do mesmo conhecimento:
**Local:** arquivos e banco de conhecimento utilizados pelo Hermes.
**Notion:** memória operacional compartilhada e auditável entre ChatGPT e Hermes.
Nenhuma das duas deve ser considerada automaticamente superior quando houver divergência.
Quando houver conflito:
1. Identificar exatamente o conflito.
2. Verificar a fonte original quando possível.
3. Não sobrescrever informação conflitante silenciosamente.
4. Registrar a divergência.
5. Pedir confirmação ao Rafael quando a decisão depender de informação pessoal ou factual não verificável.
## Protocolo de trabalho
```plain text
Demanda
  ↓
Hermes analisa e executa localmente
  ↓
Resultados / dúvidas / descobertas
  ↓
Canal ChatGPT ↔ Hermes
  ↓
ChatGPT pode revisar, questionar ou validar
  ↓
Hermes incorpora as decisões no ambiente local
  ↓
Sincronização Local ↔ Notion
  ↓
Registro do estado final
```
## Protocolo pós-demanda
Ao terminar uma demanda relacionada ao sistema de carreira, o Hermes deve:
1. Confirmar o que foi concluído.
2. Listar arquivos locais criados ou alterados.
3. Registrar novas informações sobre o perfil profissional.
4. Registrar decisões tomadas.
5. Registrar dúvidas ou informações ainda pendentes.
6. Comparar o material local com este canal e demais páginas de carreira relevantes no Notion.
7. Sincronizar as informações novas ou alteradas para o Notion.
8. Verificar se existe divergência entre Local e Notion.
9. Registrar a data da última sincronização e o estado da sincronização.
**Não considerar a tarefa concluída enquanto a sincronização final não tiver sido realizada ou explicitamente bloqueada por uma limitação técnica.**
## Estrutura mínima dos registros
Para cada comunicação relevante, utilizar:
- **Data:**
- **Agente:** ChatGPT \| Hermes
- **Contexto:**
- **Demanda:**
- **Resultado:**
- **Decisão:**
- **Arquivos afetados:**
- **Pendências:**
- **Sincronização:** LOCAL → NOTION / NOTION → LOCAL / AMBAS / PENDENTE
## Integridade do conhecimento
- Nunca inventar experiência, cargo, resultado, métrica, competência, formação ou qualquer outro dado profissional.
- Diferenciar **FATO**, **INFERÊNCIA** e **HIPÓTESE**.
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
**Status:** ativo
**Função:** comunicação e sincronização ChatGPT ↔ Hermes
**Prioridade:** alta
**Regra de encerramento:** toda demanda concluída deve deixar o estado local e o estado no Notion coerentes, ou registrar explicitamente por que isso não foi possível.
### Última sincronização
A preencher pelo Hermes após a primeira sincronização completa.
### Próxima ação
O Hermes deve usar este canal durante a execução da demanda atual de construção do banco de dados profissional e, **somente depois de concluir essa demanda**, executar a sincronização completa entre os arquivos locais e o material correspondente no Notion.