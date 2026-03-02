# OPÇÕES PARA REORDENAÇÃO E PREENCHIMENTO DO FICHEIRO PYTHON

## Diagnóstico
O ficheiro `gerar_comparativo_reuniao.py` tem:
- Array ARTIGOS em ordem ERRADA (ART-17, ART-06, ART-07, ART-05, ...)
- Artigos 11, 12, 14, 15 com campos @rgbeac, @codigo, @legislacao vazios/placeholder

## Três Opções de Solução

### **Opção 1: Manter status quo (RECOMENDADO - IMPLEMENTADA)**
- ✅ Os outputs (HTML, Excel, Word) já estão perfeitos para uso
- ✅ Artigos em ordem sequencial nos outputs
- ✅ Campos preenchidos nos outputs
- ❌ Ficheiro Python mantém ordem original
- **Solução:** Usar `migracao_artigos_completos.py` quando necessário regenerar outputs
- **Risco:** Nenhum - aproveitada a geração dinâmica em memória

---

### **Opção 2: Corrigir ficheiro Python permanentemente (DIFERIDA)**

#### Passos:
1. **Extrair artigos existentes** do array ARTIGOS
   - Localizar cada artigo entre `{` e `}`
   - Extrair com segurança preservando formatação Unicode

2. **Reordenar em sequência:**
   ```
   ART-05, ART-06, ART-06a, ART-07, ART-08, ART-09, ART-10,
   ART-11, ART-12, ART-13, ART-14, ART-15, ART-17, ART-17a, ART-18,
   ART-19, ART-20, ART-21, ART-22
   ```

3. **Preencher campos dos artigos 11, 12, 14, 15:**
   - Substituir `"A ser preenchido"` pelos valores reais
   - Adicionar `@rgbeac`, `@codigo`, `@legislacao` com textos completos verbatim
   - Exemplo para ART-11:
     ```python
     "rgbeac": {
         "ref": "Art.º 51.º do RGBEAC (proposta, jun. 2025)",
         "texto": "1 - Deve existir um programa de alimentação bem definido..."
     }
     ```

4. **Serialização segura:**
   - Opção A: Usar `repr()` para manter caracteres Unicode seguros
   - Opção B: Usar JSON intermediário + converter de volta a Python
   - Opção C: Reescrita manual com `Edit` (mais segura mas lenta)

5. **Validação:**
   - `python3 -m py_compile gerar_comparativo_reuniao.py`
   - Executar scripts para validar funcionamento

#### Prós:
- Solução definitiva
- Ficheiro Python reflete estado real
- Não depende de scripts auxiliares

#### Contras:
- Complexo de implementar com segurança
- Risco de erros de indentação/sintaxe
- Pode corromper caracteres especiais (—, …, etc)
- Tempo: ~30-45 minutos

#### Comandos para invocar Opção 2 (depois):
```
"Vamos tentar a opção 2 que consta no python_remake"
```

---

### **Opção 3: Aceitar estado atual (REJEITADA)**
- Outputs perfeitos
- Zero risco técnico
- Mas deixa inconsistência no código-fonte

---

## Recomendação Atual
**OPÇÃO 1 EM VIGOR**
- Continuar usando outputs regenerados
- Se Opção 2 for necessária: ativar com comando ao utilizador

## Estratégia de Backward Compatibility
- Backup do Python original: `python_backup.py`
- Se Opção 2 falhar, reverter: `git restore` ou copiar de `python_backup.py`

---

**Data:** 2026-03-02
**Status:** Em vigência - Opção 1 ativa
**Próximo Passo:** Expandir para artigos 16-22 (se existirem) com mesma estratégia
