FROM python:3.12-slim
WORKDIR /app

ARG OLLAMA_URL
ARG OLLAMA_MODELO
ENV OLLAMA_URL=${OLLAMA_URL} OLLAMA_MODELO=${OLLAMA_MODELO}

COPY teste_devel.py ollama_cliente.py ./
COPY examples/casos_avaliacao.json examples/

EXPOSE 8080
CMD ["python", "-B", "teste_devel.py"]
