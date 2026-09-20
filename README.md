# Organizador de Arquivos

Aplicação desenvolvida em Python para organizar automaticamente arquivos de uma pasta de acordo com seus tipos.

## Tecnologias utilizadas

- Python 3.14
- PyCharm
- pathlib
- shutil

## Funcionalidades

- Organização automática de arquivos
- Separação por tipo
- Criação automática das pastas de destino
- Suporte para imagens
- Suporte para documentos
- Suporte para planilhas
- Suporte para áudios
- Suporte para vídeos
- Suporte para arquivos compactados
- Separação de arquivos não reconhecidos em `Outros`
- Tratamento de arquivos com nomes repetidos

## Categorias

Os arquivos são organizados nas seguintes pastas:

- PDFs
- Imagens
- Documentos
- Planilhas
- Áudios
- Vídeos
- Compactados
- Outros

## Como funciona

O programa solicita o caminho da pasta que será organizada.

Depois, verifica os arquivos existentes e identifica a extensão de cada um.

Cada arquivo é movido para uma pasta correspondente ao seu tipo.

Por exemplo:

```text
foto.jpg      → Imagens
documento.pdf → PDFs
planilha.xlsx → Planilhas
musica.mp3    → Áudios
video.mp4     → Vídeos
arquivo.zip   → Compactados
```

## Estrutura do projeto

```text
OrganizadorArquivos
├── main.py
├── README.md
└── .gitignore
```

## Como executar

1. Instale o Python 3.14.
2. Abra o projeto no PyCharm.
3. Execute o arquivo `main.py`.
4. Informe o caminho da pasta que deseja organizar.
5. O programa criará as categorias necessárias e moverá os arquivos.

## Observação

Recomenda-se testar primeiro com uma pasta criada especificamente para o projeto, contendo arquivos de teste.

## Status do projeto

Versão inicial concluída e publicada no GitHub.