# File Operations Flow

## Descrição
Este projeto implementa um sistema de operações de arquivo usando FastAPI, Celery e RabbitMQ, permitindo o upload e processamento assíncrono de arquivos de texto. O sistema permite aos usuários fazer upload de arquivos, que são então convertidos para maiúsculas pelo worker do Celery. Também suporta o download dos arquivos processados.

## Funcionalidades
- **Upload de arquivos:** Os usuários podem fazer upload de arquivos para serem processados.
- **Processamento assíncrono:** Arquivos de texto (.txt) são processados para converter seu conteúdo em letras maiúsculas.
- **Download de arquivos:** Os usuários podem baixar os arquivos que foram processados.

## Tecnologias Utilizadas
- **FastAPI:** Framework web para construir APIs com Python 3.7+ baseado em type hints padrão.
- **Celery:** Biblioteca de filas distribuídas para processamento de tarefas assíncronas e agendadas.
- **RabbitMQ:** Broker de mensagens que suporta vários protocolos de mensagens.

## Como Executar

### Pré-requisitos
- Docker
- Docker Compose

### Instruções de Configuração e Execução

1. **Clone o repositório**
   ```bash
   git clone [URL do repositório]
   cd [Nome do diretório do projeto]
   ```
2. Construa e inicie os contêineres:
    ```bash
    docker-compose up --build
    ```

3. Ajustando Permissões de Arquivo:
    * Após a construção dos contêineres, é necessário ajustar as permissões do diretório de uploads para garantir que o usuário do contêiner possa escrever nele:

    ```bash
    sudo chown -R 33:33 uploads
    ```

    * Este comando ajusta as permissões do diretório de uploads para o usuário padrão do servidor web no contêiner do Docker.

4. Para fazer o upload de um arquivo, utilize o seguinte comando cURL:
    ```bash
    curl -X POST "http://localhost:8001/upload/" -F "file=@caminho-para-seu-arquivo"
    ```
5. Para baixar um arquivo processado, acesse:
    ```bash
    curl -O http://localhost:8001/download/nome-do-arquivo_processado.txt
    ```
6. Para parar e remover os contêineres, redes e volumes criados, execute:
    ```bash
    docker-compose down
    ```
