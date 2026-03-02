# CLAUDE.md — Análise Comparativa da Legislação sobre Animais

Documento metodológico estruturante do projeto. Referência para produção analítica consistente por assistentes de IA e colaboradores humanos.

**Última atualização**: 2026-03-02

---

## 1. Contexto e Objetivo

Este repositório suporta uma **análise comparativa da legislação portuguesa e europeia sobre animais**, com foco em animais de companhia. A análise abrange:

- Legislação portuguesa e europeia vigente
- Duas propostas de nova legislação que compilam e alteram a vigente
- Um novo Regulamento Europeu de aplicação direta (2023/0447)

**Objetivo central**: avaliar o impacto da aplicação do Regulamento europeu na legislação nacional, considerando que já existem duas propostas de consolidação e revisão do regime jurídico.

---

## 2. Mapeamento de Ficheiros do Repositório

### 2.1 Documentos e Códigos Internos

Cada ficheiro tem um **código interno** para referência rápida em prompts e análises:

| Código Interno | Ficheiro | Descrição |
|---|---|---|
| `@codigo` | `Código do Animal DL214.2013_OCR.docx.docx` | Código do Animal — DL n.º 214/2013 |
| `@rgbeac` | `RGBEAC_junh_2025 Original com Índice.docx` | Regime Geral do Bem-Estar dos Animais de Companhia (proposta, jun. 2025) |
| `@regulamento` | `11.12.2025 Regulamento cães e gatos-ocr - sem rasuras.docx` | Regulamento Europeu 2023/0447 — versão de trabalho sem rasuras |
| `@regulamento_trad` | `11.12.2025 Regulamento cães e gatos - votação com tradução-ocr.docx` | Regulamento Europeu 2023/0447 — versão de votação com tradução PT |
| `@regulamento_pt` | `Regulamento - Primeira Versão portuguesa.docx` | Regulamento Europeu 2023/0447 — primeira versão em português |
| `@parecer_eesc` | `Parecer - European Economic and Social Committee - Opinion - PT-PT.docx` | Parecer do Comité Económico e Social Europeu (PT-PT) |
| `@oexcel` | `oexcel.xlsx` | Ficheiro Excel comparativo por temas |
| `@legislacao` | `Decreto-Lei n.º 276-2001, de 17 de outubro v2.docx` | DL 276/2001 — Proteção dos animais de companhia |
| `@legislacao` | `DL n. 82_2019, de 27 de Junho_ocred.docx` | DL n.º 82/2019 — Bem-estar de animais de companhia |
| `@legislacao` | `Lei n.º 27_2016, de 23 de agosto - (...).docx` | Lei 27/2016 — Rede de centros de recolha; proibição do abate |
| `@legislacao` | `Portaria 146-2017_ocred.docx` | Portaria n.º 146/2017 |
| `@legislacao` | `Portaria 148_2016 - (...).docx` | Portaria n.º 148/2016 — Matilhas de caça maior |
| `@legislacao` | `Portaria n.º 264_2013 - (...).docx` | Portaria n.º 264/2013 — PNLVERAZ (raiva e zoonoses) |
| `@legislacao` | `DECRET~1.DOC` | DL n.º 74/2007 — Direito de acesso de pessoas com deficiência acompanhadas de cães de assistência |
| `@legislacao` | `Lei n.º 8_2017, de 03 de Março - Estatuto jurídico dos animais-ocr.pdf` | Lei n.º 8/2017 — Estatuto jurídico dos animais |
| `@legislacao` | `Lei n.º 92_95, de 12 de Setembro - Lei de proteção aos animais-ocr.pdf` | Lei n.º 92/95 — Lei de proteção aos animais |
| `@legislacao` | `Lei n.º 20_2019, de 22 de Fevereiro - REFORÇA A PROTEÇÃO DOS ANIMAIS UTILIZADOS EM CIRCOS-ocr.pdf` | Lei n.º 20/2019 — Proteção de animais em circos |
| `@legislacao` | `Decreto-Lei n.º 315_2009, de 29 de Outubro - Animais perigosos e potencialmente perigosos-ocr.pdf` | DL n.º 315/2009 — Animais perigosos e potencialmente perigosos |
| `@legislacao` | `Portaria n.º 422_2004, de 24 de Abril - Raças potencialmente perigosas-ocr.pdf` | Portaria n.º 422/2004 — Raças potencialmente perigosas |
| `@legislacao` | `Decreto-Lei n.º 265_2007, de 24 de Julho - Transporte de animais-ocr.pdf` | DL n.º 265/2007 — Transporte de animais |
| `@legislacao` | `Decreto-Lei n.º 314_2003 - Aprova o PNLVERAZ - consolidado-ocr.pdf` | DL n.º 314/2003 — PNLVERAZ (consolidado) |
| `@legislacao` | `Decreto-Lei n.º 121_2017, de 20 de Setembro - EXECUÇÃO DA CONVENÇÃO SOBRE O COMÉRCIO INTERNACIONAL DAS ESPÉCIES DE FAUNA E FLORA SELVAGENS-CITES-ocr.pdf` | DL n.º 121/2017 — Execução da Convenção CITES |
| `@legislacao` | `Decreto-Lei n.º 92_2019, de 10 de Julho - CONTROLO, DETENÇÃO, INTRODUÇÃO NA NATUREZA E REPOVOAMENTO DE ESPÉCIES EXÓTICAS DA FLORA E FAUNA-ocr.pdf` | DL n.º 92/2019 — Espécies exóticas |
| `@legislacao` | `Decreto-Lei n.º 38_2021, de 31 de Maio - Proteção e Conservação da Fauna e Flora Selvagens e dos habitats naturais  Convenções de Berna e de Bona-ocr.pdf` | DL n.º 38/2021 — Proteção e conservação da fauna e flora selvagens |

> **Regra de classificação**: Tudo o que não for `@codigo`, `@rgbeac`, `@regulamento`, `@regulamento_trad`, `@regulamento_pt` ou `@parecer_eesc` integra o grupo `@legislacao`.

### 2.2 Ficheiros de Análise Produzidos

| Ficheiro | Descrição | Estado |
|---|---|---|
| `oexcel.xlsx` | Ficheiro Excel comparativo principal por temas | Em curso |
| `cobertura_regulamento.csv` | Mapeamento artigo a artigo do Regulamento 2023/0447 | Completo |
| `reproducao_comparativo.csv` | Tabela comparativa do tema Reprodução (4 diplomas) | Completo |
| `reproducao_infografia.html` | Infografia HTML interativa do tema Reprodução | Completo |

### 2.3 Legislação Ainda Não No Repositório

A legislação relevante que não conste do repositório deve ser consultada online na sua versão mais atual (e.g., via [dre.pt](https://dre.pt) ou [EUR-Lex](https://eur-lex.europa.eu)).

---

## 3. Estrutura das Categorias Documentais

### a) Legislação portuguesa e europeia atual — `@legislacao`
Toda a legislação vigente relevante que não seja `@codigo`, `@rgbeac`, `@regulamento`, `@regulamento_trad` ou `@regulamento_pt`.

### b) Propostas compiladoras da legislação nacional

- **`@codigo`** — Código do Animal (DL 214/2013): proposta de consolidação do regime jurídico nacional.
- **`@rgbeac`** — Regime Geral do Bem-Estar dos Animais de Companhia: segunda proposta de consolidação, versão de junho de 2025.

### c) Novo Regulamento Europeu — `@regulamento` / `@regulamento_trad` / `@regulamento_pt`

Regulamento 2023/0447, de aplicação direta nos Estados-Membros. Ponto de referência central para a análise de impacto. Existem três versões no repositório:
- `@regulamento` — versão de trabalho sem rasuras (base para citações verbatim em inglês)
- `@regulamento_trad` — versão de votação com tradução PT integrada
- `@regulamento_pt` — primeira versão em português

Para **citações verbatim** usar preferencialmente `@regulamento` (versão em inglês). Para **tradução** confrontar com `@regulamento_trad`.

### d) Parecer do CESE — `@parecer_eesc`
Parecer do Comité Económico e Social Europeu sobre o Regulamento. Relevante para contextualização política e técnica da proposta europeia.

### e) Ficheiro Excel comparativo — `@oexcel`
Contém colunas comparativas por temas entre: DL 276/2001, `@codigo`, `@rgbeac` e `@regulamento`. O modelo será replicado para os restantes diplomas vigentes.

---

## 4. Estado Atual da Análise

### 4.1 Trabalho Concluído

| Produto | Descrição |
|---|---|
| `cobertura_regulamento.csv` | Mapeamento completo dos artigos do Regulamento 2023/0447, com estado de cobertura no `@oexcel`, diplomas nacionais relevantes, prioridade e notas analíticas |
| `reproducao_comparativo.csv` | Comparativo detalhado do tema **Reprodução** entre DL 276/2001, `@codigo`, `@rgbeac` e `@regulamento`, com citações verbatim, tipo de norma, divergências e observações |
| `reproducao_infografia.html` | Infografia HTML interativa com visualização comparativa do tema Reprodução |

### 4.2 Lacunas Críticas Identificadas no `@oexcel`

Com base no `cobertura_regulamento.csv`, os seguintes temas estão **ausentes** do Excel e são **prioritários**:

| Artigo do Regulamento | Tema | Prioridade |
|---|---|---|
| Art. 6a | Estratégias de reprodução; traços conformacionais; consanguinidade | Alta |
| Art. 10 | Visitas de bem-estar veterinárias obrigatórias | Alta |
| Art. 11 + Anexo I(1) | Alimentação e abeberamento | Alta |
| Art. 14 + Anexo I(4) | Necessidades comportamentais | Alta |
| Art. 15a | Exposições e competições estéticas | Média |
| Art. 19 | Bases de dados nacionais e interoperabilidade europeia | Alta |
| Art. 20 | Recolha de dados e relatórios aos Estados-Membros | Média |
| Art. 20a | Proteção de dados pessoais | Baixa |
| Art. 21 | Entrada de cães e gatos na União (importação) | Alta |
| Art. 25 | Medidas nacionais mais estritas — janela de harmonização | Alta |

---

## 5. Objetivos da Análise

A análise deve:

- Salientar diferenças entre regimes jurídicos
- Identificar incompatibilidades ou lacunas normativas
- Procurar harmonização entre o direito nacional e o Regulamento europeu

### 5.1 Eixos Materiais de Harmonização

| Eixo | Descrição |
|---|---|
| Detenção responsável | Reforço dos deveres e responsabilidades dos detentores |
| Reprodução | Limitação da reprodução não planeada |
| Rastreabilidade | Promoção da identificação e registo de animais |
| Animais errantes | Inversão do panorama descontrolado de animais errantes |

---

## 6. Regras Metodológicas

### 6.1 Idioma

- Toda a produção analítica deve ser em **PT-PT**.
- Exceção: citações de legislação europeia (manter em inglês, com tradução incluída).

### 6.2 Citações de Legislação Nacional

- Sempre **verbatim** — proibido alterar palavras, estrutura ou ideia.
- Referenciação obrigatória no formato:

  ```
  al. X), do n.º Y, art.º Zº do [Diploma]
  ```

### 6.3 Citações de Legislação do Parlamento Europeu

1. Citação verbatim em **inglês** (usar `@regulamento` — versão sem rasuras).
2. Tradução imediatamente a seguir, respeitando a terminologia histórica consolidada (confrontar com `@regulamento_trad`).
3. Resultado final: **duas citações** (original + tradução).

### 6.4 Observações

- Qualquer **dedução, inferência ou opinião** deve constar exclusivamente na coluna "Observações".
- A análise principal deve ser descritiva e comparativa — nunca valorativa.

---

## 7. Estrutura das Tabelas (Excel / CSV)

Cada linha deve conter os seguintes campos:

| Campo | Descrição |
|---|---|
| Tema | Eixo temático (ex.: detenção, reprodução, rastreabilidade) |
| Subtema | Subdivisão específica do tema |
| Diploma | Diploma de origem (ex.: DL 276/2001, `@regulamento`) |
| Artigo | Referência articulada no formato normalizado |
| Texto citado | Transcrição verbatim do dispositivo legal |
| Tipo de norma | obrigação / proibição / definição / sanção / competência / etc. |
| Divergência face ao Regulamento | Descrição objetiva da diferença normativa |
| Necessidade de alteração | Sim / Não / Parcialmente |
| Observações | Deduções, inferências ou recomendações |

### Requisitos dos Ficheiros

- Compatíveis com tratamento posterior em **Python** e **HTML**.
- Permitir filtragem por tema, diploma e tipo de norma.
- Manter estrutura uniforme entre diplomas.
- Não fundir células; manter compatibilidade com pandas/Python.

---

## 8. Requisitos Analíticos

É essencial:

- Análise aprofundada de todos os documentos do repositório.
- Pesquisa de legislação conexa quando necessário (consulta online).
- Identificação de remissões e referências normativas internas e cruzadas.
- Comparação artigo a artigo, organizada por tema.

---

## 9. Estratégia de Apresentação Gráfica

Além da análise tabular, devem ser previstas formas de apresentação sintética:

- **Poster temático** por eixo (detenção, reprodução, rastreabilidade, errantes)
- **Infografia comparativa** por diploma
- **Matriz artigo-a-artigo**
- **Diagrama de impacto** do Regulamento
- **Sistema de cores** por tipo de alteração

Organização obrigatoriamente **temática** para garantir legibilidade.

O ficheiro `reproducao_infografia.html` é o modelo de referência para os restantes temas.

---

## 10. Workflow de Desenvolvimento (Git)

### Ramo de trabalho

O desenvolvimento decorre no ramo:

```
claude/claude-md-mm8hc9nys5hzcgpx-20QXc
```

Nunca fazer push para `master` sem autorização explícita.

### Fluxo de commits

```bash
git checkout claude/claude-md-mm8hc9nys5hzcgpx-20QXc
# ... editar ficheiros ...
git status
git add <ficheiros específicos>
git commit -m "Descrição clara da alteração"
git push -u origin claude/claude-md-mm8hc9nys5hzcgpx-20QXc
```

### Convenções de commit

- Mensagens em **PT-PT** ou inglês técnico, descritivas e concisas.
- Nunca usar `git add -A` ou `git add .` sem verificar o estado com `git status` primeiro.
- Não usar `--no-verify` nem `--force-push` para `master`.

---

## 11. Instruções para Assistentes de IA

### 11.1 Antes de qualquer análise

1. Verificar quais ficheiros estão presentes no repositório (`ls -la`).
2. Identificar o código interno correto (`@codigo`, `@rgbeac`, `@regulamento`, `@regulamento_trad`, `@regulamento_pt`, `@parecer_eesc`, `@legislacao`, `@oexcel`).
3. Consultar `cobertura_regulamento.csv` para saber o estado de cobertura de cada artigo do Regulamento.
4. Para legislação em falta, consultar online na versão mais atual.

### 11.2 Ao produzir análises

- **Nunca parafrasear** dispositivos legais — citar sempre verbatim.
- **Nunca misturar** descrição analítica com opiniões — opiniões vão em "Observações".
- **Sempre referenciar** no formato `al. X), do n.º Y, art.º Zº`.
- **Sempre produzir em PT-PT**, exceto citações europeias (com tradução imediata).
- Para lacunas: registar explicitamente "Sem disposição equivalente." na coluna `Texto_citado_verbatim`.

### 11.3 Ao trabalhar com o Excel (`@oexcel`)

- Manter a estrutura de colunas definida na secção 7.
- Garantir que cada linha corresponde a um único dispositivo legal.
- Não fundir células; manter compatibilidade com pandas/Python.
- Consultar `reproducao_comparativo.csv` como modelo de referência para a estrutura correta.

### 11.4 Ao produzir CSVs

- Usar `reproducao_comparativo.csv` como modelo de referência.
- Colunas obrigatórias: `Tema`, `Subtema`, `Diploma`, `Artigo`, `Texto_citado_verbatim`, `Tipo_de_norma`, `Divergencia_face_ao_Regulamento`, `Necessidade_de_alteracao`, `Observacoes`.
- Usar ponto e vírgula (`;`) como separador não é necessário se os campos com vírgulas estiverem entre aspas — garantir escaping correto para compatibilidade com pandas.

### 11.5 Ao produzir HTMLs de infografia

- Usar `reproducao_infografia.html` como modelo de referência.
- Manter interatividade (filtros, ordenação).
- Incluir sistema de cores por tipo de alteração.

### 11.6 Pesquisa online

Quando a legislação não estiver no repositório:
- Usar [dre.pt](https://dre.pt) para legislação portuguesa.
- Usar [EUR-Lex](https://eur-lex.europa.eu) para legislação europeia.
- Citar sempre a versão consolidada mais recente.

---

## 12. Finalidade deste Documento

Este ficheiro constitui:

- Documento metodológico estruturante do projeto.
- Referência para produção analítica consistente por humanos e assistentes de IA.
- Base para integração futura em interfaces gráficos e sistemas automatizados.
- Guia para manutenção e expansão do repositório.
