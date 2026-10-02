# 📄 AWS Textract Document Extractor

Script em Python para extração automatizada de texto em documento utilizando o serviço gerenciado **Amazon Textract** via **Boto3**.

---

## 📌 Funcionalidades

- **Extração via OCR:** Identificação de linhas de texto (`LINE`) presentes no documento enviado.
- **Cache Local Inteligente:** Salva o retorno completo da AWS em `response.json`. Se o arquivo de cache existir, evita novas requisições à AWS, reduzindo custos de desenvolvimento e testes.
- **Manipulação Robusta de Arquivos:** Uso de `pathlib` para compatibilidade entre sistemas operacionais (Windows/Linux/macOS).

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **SDK boto3** 
- **Amazon Textract**

---

├── images/
│   └── lista-material-escolar.jpeg
├── main.py
├── response.json          
└── README.md
