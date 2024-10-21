# Comandos da API do Google Sheets com gspread

## Conexão e Autenticação

- **`gspread.authorize(credentials)`**: Autentica o cliente usando as credenciais fornecidas.

## Operações com Planilhas

- **`gc.open("Nome_da_Planilha")`**: Abre uma planilha existente pelo nome.
- **`gc.open_by_key("Chave_da_Planilha")`**: Abre uma planilha usando a chave única (ID).
- **`gc.open_by_url("URL_da_Planilha")`**: Abre uma planilha pela URL.
- **`gc.create("Nome_Nova_Planilha")`**: Cria uma nova planilha com o nome especificado.
- **`gc.list_spreadsheet_files()`**: Lista todas as planilhas disponíveis na conta autenticada.

## Operações com Abas

- **`planilha.sheet1`**: Acessa a primeira aba da planilha.
- **`planilha.worksheet("Nome_Aba")`**: Acessa uma aba pelo nome.
- **`planilha.get_worksheet(index)`**: Acessa uma aba pelo índice (começando em 0).
- **`planilha.add_worksheet(title="Nome_Aba", rows="100", cols="20")`**: Adiciona uma nova aba com o título e dimensões especificadas.
- **`planilha.del_worksheet(aba)`**: Remove uma aba da planilha.

## Leitura de Dados

- **`aba.get_all_records()`**: Retorna os dados como uma lista de dicionários.
- **`aba.get_all_values()`**: Retorna todos os valores da planilha.
- **`aba.row_values(n)`**: Retorna os valores da linha `n`.
- **`aba.col_values(n)`**: Retorna os valores da coluna `n`.
- **`aba.cell(linha, coluna)`**: Retorna o valor de uma célula específica.
- **`aba.batch_get(["A1:C10", "D1:E5"])`**: Retorna valores de várias faixas de células.

## Escrita de Dados

- **`aba.update("A1", "Valor")`**: Atualiza a célula A1 com um novo valor.
- **`aba.update_cell(linha, coluna, "Valor")`**: Atualiza uma célula específica.
- **`aba.update("A1:B2", [[1, 2], [3, 4]])`**: Atualiza uma faixa de células com valores fornecidos.
- **`aba.append_row(["valor1", "valor2"])`**: Adiciona uma nova linha ao final da planilha.
- **`aba.insert_row(["valor1", "valor2"], índice)`**: Insere uma nova linha no índice especificado.

## Operações com Células

- **`aba.find("Texto")`**: Encontra a primeira célula que contém o texto especificado.
- **`aba.findall("Texto")`**: Encontra todas as células que contêm o texto especificado.
- **`aba.range("A1:C3")`**: Retorna uma lista de células em uma faixa especificada.
- **`aba.update_acell("A1", "Novo Valor")`**: Atualiza uma célula pelo nome.

## Manipulação de Planilhas

- **`planilha.share("email_do_usuario@dominio.com", perm_type="user", role="writer")`**: Compartilha a planilha com o usuário especificado.
- **`planilha.copy("Chave_da_Planilha")`**: Faz uma cópia da planilha especificada.
- **`planilha.title`**: Obtém ou define o título da planilha.
- **`planilha.id`**: Retorna a chave (ID) única da planilha.
- **`planilha.url`**: Retorna a URL da planilha.

## Permissões de Acesso

- **`planilha.list_permissions()`**: Lista as permissões da planilha.
- **`planilha.add_permission("email_do_usuario@dominio.com", role="writer", perm_type="user")`**: Adiciona uma permissão de acesso.
- **`planilha.remove_permission("email_do_usuario@dominio.com")`**: Remove a permissão de acesso para o usuário especificado.

## Excluir e Manipular Abas

- **`planilha.worksheets()`**: Retorna uma lista de todas as abas da planilha.
- **`aba.clear()`**: Limpa todos os dados da aba.
- **`aba.delete_row(index)`**: Remove a linha no índice especificado.
- **`aba.delete_columns(index)`**: Remove a coluna no índice especificado.

---