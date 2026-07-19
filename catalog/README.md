# Catálogo de publicações (Google Sheets)

O site lê um CSV com as colunas:

| Coluna | Nome   | Uso |
|--------|--------|-----|
| A      | `tag`  | Categoria do contador ou do carrossel |
| B      | `title`| Título da obra |
| C      | `date` | Ano ou data |
| D      | `link` | URL da obra (opcional) |
| E      | `cover`| URL da capa (opcional; carrossel Skoob) |

## Tags aceitas

**Contadores** (abaixo de Contos & Poemas):

- `books` — livros solo
- `tales` — contos
- `poems` — poemas
- `articles` — artigos
- `anthologies` — antologias

**Carrossel Skoob:**

- `skoob` — cada linha vira um card no carretel (clique abre `link` em nova aba)

O contador de cada categoria = número de linhas com aquela `tag`.

## Como usar no Google Drive / Sheets

1. Abra [Google Sheets](https://sheets.google.com) → **Arquivo → Importar → Upload** e envie `publications.template.csv` (ou `publications.csv`).
2. Preencha/edite as linhas (uma obra por linha).
3. **Arquivo → Compartilhar → Publicar na web**
   - Escolha a aba da planilha
   - Formato: **Valores separados por vírgula (.csv)**
   - Publique e copie o link
4. Alternativa de URL (troque `SHEET_ID` e `gid`):

```
https://docs.google.com/spreadsheets/d/SHEET_ID/export?format=csv&gid=0
```

5. No site, em `index.html`, cole a URL em:

```js
const CATALOG_CSV_URL='COLE_AQUI_O_LINK_CSV';
```

6. Me envie o link publicado (ou o `SHEET_ID`) para eu plugar no código.

Enquanto `CATALOG_CSV_URL` estiver vazio, o site usa o arquivo local `catalog/publications.csv`.

## Observações

- Não use vírgulas no título sem aspas (o Sheets exporta com aspas automaticamente).
- Links do Skoob: abra o livro no Skoob → copie a URL da página do livro na coluna `link`.
- Capas: URL pública de imagem (Drive “qualquer pessoa com o link” ou capa hospedada).
