# Biblioteca de Processamento de Imagens
Uma biblioteca em Python voltada para tarefas básicas de processamento de imagens, como redimensionamento, comparação de similaridade estrutural e correspondência de histogramas entre duas imagens.

## Funcionalidades
Encontrar Diferenças Entre Imagens: Calcula o índice de similaridade estrutural entre duas imagens e gera uma imagem de diferença normalizada.
Transferência de Histograma: Ajusta o histograma de cores de uma imagem com base em outra imagem de referência.
Redimensionar Imagem: Redimensiona uma imagem para uma proporção especificada, mantendo a proporção de aspecto original.

## Instalação
As dependências da biblioteca podem ser instaladas através do comando:

```bash
    pip install -r requirements.txt
```

## Como Usar
** Encontrar Diferenças Entre Imagens: Compara duas imagens de entrada e calcula a similaridade entre elas, retornando uma imagem com as diferenças normalizadas.

** Transferir Histogramas: Transfere o histograma de uma imagem para outra, permitindo a harmonização das cores.

** Redimensionamento de Imagens: Permite ajustar o tamanho de uma imagem proporcionalmente, especificando a porcentagem de redução ou ampliação.

## Requisitos
Esta biblioteca requer as seguintes dependências:

numpy
scikit-image
matplotlib
Você pode instalar todas as dependências executando o comando:

```bash
    pip install -r requirements.txt
```