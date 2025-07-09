# 📌 PROJETO – DASHBOARD COM DADOS DO RECLAME AQUI
## MBA em Ciência de Dados – Disciplina: Dashboards em Python
* Prof. Túlio Ribeiro
## Alunos
* Igor Florentino
* Rodrigo Galba
* João Paulo

### **Descrição**

* O objetivo é criar um painel interativo com **Streamlit** utilizando dados de reclamações do Reclame Aqui.

### **O painel deve conter**

* **Série temporal** do número de reclamações.
* **Frequência de reclamações por estado.**
* **Frequência por tipo de** `STATUS`.
* **Distribuição do tamanho dos textos** das reclamações (coluna `DESCRIÇÃO`).
* **WordCloud** com as palavras mais frequentes nos textos das descrições.
* **Mapa do Brasil com heatmap** mostrando a quantidade de reclamações por **ano**, com granularidade por **estado ou município**.

  > O mapa **deve conter um seletor para o ano** que será visualizado.

### **Os gráficos devem ser interativos e filtráveis com seletores de:**

* Estado
* Status
* Faixa de tamanho do texto da reclamação