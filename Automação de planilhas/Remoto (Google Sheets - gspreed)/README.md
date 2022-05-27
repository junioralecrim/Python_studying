# Acesso e manipulação de dados de planilhas com o gspreed

A biblioteca `gspreed` permite o acesso remoto às planilhas do Google Sheets que estão no Google Drive de forma simples e eficiente.

**NOTA:** Usar essa API de forma gratuita gera algumas limitações, como maior lentidão 
para acesso e manipulação dos dados. 

O número de requisições por segundo também é limitado pela Google, podendo gerar alguns erros
de execução no código, então é utilizado em alguns casos o "time.sleep()" para dar um tempo (em segundos)
no loop.

---

**AVISO:** Deixar o arquivo .json de acesso (chave api) público na internet configura em risco
extremo para o proprietário da conta, já que esta chave permite o acesso a todos os arquivos presentes
no google drive do usuário.

A chave usada é de uma conta criada especificamente para testes de acesso `(manipulacaoapi@gmail.com)`

---
**Planilha:** `https://docs.google.com/spreadsheets/d/1dNsphjNxu9Wv3QEwcHbH2e5nu2O2VaIzj66BgXombUA/edit?usp=sharing`
