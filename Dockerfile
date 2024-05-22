# Usando uma imagem base Python slim
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /code

# Copia o arquivo de requisitos e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o diretório do aplicativo para o contêiner
COPY ./app /code/app

# Cria o diretório de uploads e ajusta as permissões
RUN mkdir /code/uploads \
    && chown -R www-data:www-data /code

# Muda para um usuário não-root para melhor segurança
USER www-data

# Expõe a porta em que a aplicação FastAPI irá rodar
EXPOSE 8000

# Comando para iniciar a aplicação usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload"]
