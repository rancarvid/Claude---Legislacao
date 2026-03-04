# HANDOFF — Análise Comparativa da Legislação sobre Animais
## Documento de briefing para nova instância Claude

> Este documento descreve o estado atual do projeto, as convenções estabelecidas, a arquitetura técnica dos scripts, o que já foi feito e o que ficou por fazer. Lê-o na íntegra antes de qualquer intervenção.

---

## 1. O que é este projeto

Análise comparativa da legislação portuguesa e europeia sobre animais de companhia. O objetivo central é avaliar o **impacto do Regulamento Europeu 2023/0447** no quadro jurídico nacional, tendo em conta que já existem duas propostas de consolidação legislativa nacionais.

Os quatro diplomas principais em análise:

| Código interno | Diploma |
|---|---|
| `@legislacao` | Toda a legislação vigente (DL 276/2001, DL 82/2019, Lei 27/2016, Portarias) |
| `@codigo` | Código do Animal — DL n.º 214/2013 (proposta de consolidação 1) |
| `@rgbeac` | Regime Geral do Bem-Estar dos Animais de Companhia — jun. 2025 (proposta 2) |
| `@regulamento` | Regulamento Europeu 2023/0447 — cães e gatos (aplicação direta) |

O `@regulamento` é o **polo de referência** — toda a análise parte dele e avalia a conformidade/divergência dos restantes diplomas.

---

## 2. Ficheiros no repositório (branch de trabalho)

Branch: `claude/claude-md-mm6om6hd0ro2q4cd-HlaxD`

### 2.1 Documentos legislativos

| Ficheiro | Código |
|---|---|
| `Código do Animal DL214.2013_OCR.docx.docx` | `@codigo` |
| `RGBEAC_junh_2025 Original com Índice.docx` | `@rgbeac` |
| `11.12.2025 Regulamento cães e gatos-ocr - sem rasuras.docx` | `@regulamento` (EN original) |
| `11.12.2025 Regulamento cães e gatos - votação com tradução-ocr.docx` | Tradução PT do `@regulamento` (usada como fonte das `traducao` fields) |
| `Regulamento - Primeira Versão portuguesa.docx` | Primeira versão PT do `@regulamento` (fonte auxiliar de tradução) |
| `Parecer - European Economic and Social Committee - Opinion - PT-PT.docx` | Parecer EESC em PT — contexto complementar |
| `Decreto-Lei n.º 276-2001, de 17 de outubro v2.docx` | `@legislacao` |
| `DL n. 82_2019, de 27 de Junho_ocred.docx` | `@legislacao` |
| `Lei n.º 27_2016, de 23 de agosto - Aprova medidas...` | `@legislacao` |
| `Portaria 146-2017_ocred.docx` | `@legislacao` |
| `Portaria 148_2016 - Estabelece a obrigatoriedade...` | `@legislacao` |
| `Portaria n.º 264_2013 - Aprova as normas técnicas...` | `@legislacao` |
| `DECRET~1.DOC` | `@legislacao` |
| `oexcel.xlsx` | `@oexcel` — comparativo temático de referência |

### 2.2 Scripts (não são documentos legislativos)

| Ficheiro | Função |
|---|---|
| `gerar_comparativo_reuniao.py` | Script principal — gera HTML SPA, Excel e Word em simultâneo |
| `gerar_word.py` | Gerador Word standalone (formatação completa) |

### 2.3 Outputs gerados (não editar à mão)

| Ficheiro | Tipo |
|---|---|
| `comparativo_reuniao_exemplo.html` | SPA interativo — ferramenta de reunião |
| `comparativo_reuniao_exemplo.xlsx` | Excel artigo a artigo |
| `comparativo_reuniao_exemplo.docx` | Word formatado por artigo |
| `cobertura_regulamento.csv` | Rastreamento da cobertura do @regulamento |
| `reproducao_comparativo.csv` | CSV temático — reprodução |
| `reproducao_infografia.html` | HTML infográfico — reprodução |

---

## 3. Estado atual dos artigos — array ARTIGOS

O script `gerar_comparativo_reuniao.py` contém um array `ARTIGOS` com **6 entradas**, por esta ordem:

| ID | Tema |
|---|---|
| `ART-17` | Identificação e Registo |
| `ART-06` | Bem-Estar e Detenção |
| `ART-07` | Reprodução e Criação |
| `ART-05` | Princípios Gerais de Bem-Estar |
| `ART-06a` | Estratégias de Criação — Conformação e Consanguinidade |
| `ART-13` | Saúde e Monitorização Sanitária |

Estes seis artigos cobrem uma fração do `@regulamento`. O trabalho fica a meio — há mais artigos do Regulamento por mapear e analisar.

---

## 4. Estrutura de cada entrada do array ARTIGOS

```python
{
    "id": "ART-13",
    "tema": "Saúde e Monitorização Sanitária",
    "regulamento": {
        "ref": "Art.º 13.º do Regulamento 2023/0447 (PE/Conselho)",
        "titulo": "Health",           # Título inglês do artigo — aparece no cabeçalho da card EN
        "texto": "...",               # Verbatim EN — NUNCA tem [dim], NUNCA é truncado
        "traducao": "...",            # PT-PT — baseada nos ficheiros de tradução do repositório
    },
    "rgbeac":    { "ref": "...", "texto": "..." },
    "codigo":    { "ref": "...", "texto": "..." },
    "legislacao":{ "ref": "...", "texto": "..." },  # pode ter [dim] — ver secção 5
    "divergencia": {
        "legislacao": "Texto da divergência face ao @regulamento — legislação vigente",
        "codigo":     "Texto da divergência face ao @regulamento — @codigo",
        "rgbeac":     "Texto da divergência face ao @regulamento — @rgbeac",
        "sumario":    "Síntese e proposta de implementação",
    },
    "necessidade_alteracao": "Sim",   # ou "Não"
    "notas": "",                      # campo livre para notas de reunião
}
```

**Regras absolutas:**
- O campo `regulamento.texto` é sempre verbatim EN, sem cortes, sem `[dim]`
- O campo `regulamento.traducao` é sempre verbatim PT-PT, sem cortes, sem `[dim]`
- `[dim]` aplica-se **apenas** a `legislacao.texto`, `codigo.texto`, `rgbeac.texto`

---

## 5. Convenção [dim] — texto cinzento

Quando um n.º ou alínea de um artigo nacional não tem qualquer relação com o tema em análise, o bloco pode ser marcado com `[dim]`. O texto aparece a cinzento mas completamente legível — nunca é apagado.

**Como funciona nos dados:**
- O texto de cada coluna é uma string com blocos separados por `\n\n`
- Cada bloco começa com a primeira linha do parágrafo
- Para marcar um bloco como cinzento, coloca-se o prefixo `[dim]` **antes** do texto do bloco:

```python
"texto": """1 — Os detentores devem assegurar que:

a) O animal dispõe de alimentação adequada.

b) O animal tem acesso a água potável.

[dim]2 — O presente decreto-lei não se aplica a animais de produção."""
```

- O `[dim]` é prefixo do bloco inteiro (n.º com todas as suas alíneas)
- Nunca se usa `[dim]` a meio de um bloco
- Nunca se usa `[dim]` no `@regulamento`

**Quando usar:**
- Só em casos restritos em que o n.º está completamente desfasado do tema
- A regra geral é citar o artigo todo — o `[dim]` é a exceção

---

## 6. Convenção de formatação do texto nas colunas

### 6.1 Blocos e linhas

```
Bloco A\n\nBloco B\n\nBloco C
```

Cada bloco é um parágrafo separado (n.º do artigo). Dentro de um bloco, `\n` separa linhas (alíneas, sub-alíneas).

### 6.2 Múltiplos artigos numa coluna

Quando uma coluna cita mais do que um artigo, usa-se um cabeçalho de artigo como separador visual:

```python
"texto": """Artigo 13.º — Saúde

1 — Os animais devem receber cuidados veterinários.

a) Vacinação obrigatória.

Artigo 16.º — Identificação

1 — Todos os cães devem ser identificados.

a) Microchip obrigatório."""
```

A linha `Artigo X.º — Título` é detetada automaticamente por `formatarTexto()` (HTML) e `_classify_line()` (Word) e renderizada como separador visual em negrito.

### 6.3 Regra das alíneas

As alíneas **nunca aparecem sozinhas**. Antes de qualquer bloco de alíneas, tem de aparecer o n.º que as introduz:

```python
# ERRADO:
"texto": "a) Vacinação obrigatória.\nb) Desparasitação."

# CORRETO:
"texto": "1 — Os animais devem:\n\na) Vacinação obrigatória.\nb) Desparasitação."
```

### 6.4 Padrões reconhecidos (PT e EN)

| Padrão | Tipo |
|---|---|
| `1 —` ou `1.` | Parágrafo numerado (PT ou EN) |
| `a)` ou `(a)` | Alínea |
| `(i)` `(ii)` | Sub-alínea EN |
| `—` ou `–` no início da linha | Sub-alínea PT |
| `Artigo X.º` | Cabeçalho de artigo (separador visual) |

---

## 7. Ordem de apresentação no HTML e Word

### Na coluna `@regulamento`:
1. **Card EN** (primário, autoritativo) — com título inglês do artigo no cabeçalho
2. **Card PT-PT** (tradução, apoio de leitura) — a seguir

O inglês é sempre mostrado primeiro. A tradução é leitura complementar, não substitui o original.

### Nas colunas `@rgbeac`, `@codigo`, `@legislacao`:
- Texto verbatim PT, sem order especial

---

## 8. Como extrair texto dos ficheiros DOCX

Os ficheiros DOCX são por vezes mal formatados (OCR) — os parágrafos podem aparecer como strings vazias com o texto no XML. A forma mais robusta de extrair:

```python
import docx
from lxml import etree

doc = docx.Document("ficheiro.docx")
body = doc.element.body
text = etree.tostring(body, method='text', encoding='unicode')
```

Depois usa `re.finditer(r'Artigo (\d+)\.º', text)` para localizar os artigos por posição de caracter e extrair o texto entre eles.

---

## 9. Como correr os scripts

A partir da raiz do repositório:

```bash
python3 gerar_comparativo_reuniao.py
```

Isto gera os três outputs em simultâneo:
- `comparativo_reuniao_exemplo.html`
- `comparativo_reuniao_exemplo.xlsx`
- `comparativo_reuniao_exemplo.docx`

```bash
python3 gerar_word.py
```

Gera apenas o Word (standalone).

**Dependências Python necessá:**
```bash
pip install python-docx openpyxl
```

---

## 10. Workflow Git

Branch de trabalho: `claude/claude-md-mm6om6hd0ro2q4cd-HlaxD`

```bash
# Verificar sempre antes de commitar
git status

# Adicionar apenas ficheiros específicos
git add gerar_comparativo_reuniao.py comparativo_reuniao_exemplo.html ...

# Commitar com mensagem descritiva em PT-PT
git commit -m "Adiciona ART-XX — Tema do artigo"

# Push
git push -u origin claude/claude-md-mm6om6hd0ro2q4cd-HlaxD
```

**Nunca:**
- `git add -A` ou `git add .` sem verificar `git status` primeiro
- Push para `master` sem autorização explícita
- `--no-verify` ou `--force-push` para `master`

---

## 11. O que ficou por fazer

### 11.1 Atualizar traduções (em pausa — aguarda instrução)

Os campos `regulamento.traducao` dos 6 artigos existentes **não foram ainda revistos** com base nos três ficheiros de tradução que chegaram ao repositório:

- `11.12.2025 Regulamento cães e gatos - votação com tradução-ocr.docx` ← fonte principal
- `Regulamento - Primeira Versão portuguesa.docx` ← fonte auxiliar
- `Parecer - European Economic and Social Committee - Opinion - PT-PT.docx` ← contexto

O utilizador disse explicitamente **"não pretendo que alteres agora"** — este passo está em pausa. Quando for altura, o processo é:
1. Extrair o texto PT dos ficheiros de tradução usando `python-docx`
2. Localizar cada artigo pelo número (ex.: `Artigo 13.º`)
3. Copiar o texto verbatim para o campo `traducao` da entrada correspondente em ARTIGOS
4. Regenerar os outputs e commitar

### 11.2 Adicionar mais artigos do @regulamento

O Regulamento 2023/0447 tem muitos mais artigos para além dos 6 já mapeados. O trabalho analítico principal é continuar a popular o array ARTIGOS com os artigos restantes, seguindo exatamente a mesma estrutura.

Para cada novo artigo:
1. Extrair o texto EN verbatim do `@regulamento` (ficheiro `sem rasuras`)
2. Extrair a tradução PT do ficheiro `votação com tradução-ocr`
3. Identificar o `titulo` (título inglês do artigo)
4. Localizar as correspondências em `@legislacao`, `@codigo`, `@rgbeac`
5. Analisar as divergências e preencher os 4 campos do dict `divergencia`
6. Determinar `necessidade_alteracao` (Sim/Não)

### 11.3 Cobertura do @regulamento

O ficheiro `cobertura_regulamento.csv` rastreia quais artigos do Regulamento já foram cobertos. Consultar este ficheiro para saber o que falta.

---

## 12. Regras analíticas críticas (nunca esquecer)

| Regra | Detalhe |
|---|---|
| Idioma | Produção analítica sempre em PT-PT |
| Citações nacionais | Sempre verbatim — nunca parafrasear |
| Citações europeias | EN verbatim primeiro + tradução PT-PT a seguir |
| Formato de referência | `al. X), do n.º Y, do art.º Z.º do [Diploma]` |
| Opiniões | Só na coluna "Observações" / campo `notas` |
| `[dim]` | Nunca no `@regulamento`; com parcimónia no resto |
| `@regulamento` | Sempre citado na íntegra — sem cortes |

---

## 13. Como o HTML SPA funciona

O `comparativo_reuniao_exemplo.html` é um ficheiro HTML/JS autónomo (sem servidor):

- **Sidebar esquerda**: lista de artigos para navegação
- **Pesquisa**: campo de texto com highlight de palavras — pesquisa no texto, título, tema e campo `titulo` do regulamento
- **Cards por artigo**: EN primeiro, PT depois, depois `@rgbeac`, `@codigo`, `@legislacao`
- **Divergência**: 4 secções com bullet points (legislacao / codigo / rgbeac / sumario)
- **Campo de notas**: editável em reunião, exportável para CSV

O HTML é gerado pelo script — nunca editar o `.html` diretamente. Qualquer alteração ao layout/dados vai para o script Python.

---

## 14. Onde está a lógica de renderização

### No HTML (dentro do script Python como f-string):

- `formatarTexto(str)` — converte string com `\n\n` em HTML com classes CSS
- `render(art)` — renderiza um artigo completo (todas as cards)
- `artMatch(art, q)` — pesquisa por palavra-chave num artigo

Atenção: o HTML é gerado por uma f-string Python. As chaves JS têm de ser escapadas como `{{` e `}}`. Os template literals JS `${...}` ficam como `${{...}}` no código Python.

### No Word (`gerar_word.py`):

- `_classify_line(line)` — devolve `"art-header"`, `"sub"`, `"alinea"`, ou `"normal"`
- `cell_body(cell, text, ...)` — preenche uma célula de tabela com o texto formatado
- `add_article_section(doc, art)` — adiciona uma secção completa por artigo

---

## 15. Ficheiro CLAUDE.md

O `CLAUDE.md` é o documento metodológico oficial do projeto. Foi completamente revisto nesta sessão e está atualizado. Antes de qualquer trabalho analítico, lê o CLAUDE.md — define as convenções que este HANDOFF complementa com detalhe técnico.

Se detetares incoerências entre CLAUDE.md e HANDOFF.md, o CLAUDE.md prevalece — mas reporta ao utilizador para que ambos sejam alinhados.

---

*Documento produzido em 2026-03-01. Estado do repositório: 6 artigos completos, outputs gerados e commitados, branch actualizado.*
