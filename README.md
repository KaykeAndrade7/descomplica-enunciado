# Descomplica Enunciado

Projeto P0 — TrendsIA, de Kayke Andrade.

**Estado em 03/11/2026:** definição do problema e decisões iniciais. A implementação está prevista para começar em 04/11/2026; ainda não há aplicação executável ou resultados de testes.

## Problema

Estudantes precisam identificar entregáveis, requisitos e prazos em enunciados longos, porque essas informações ficam espalhadas entre explicações e orientações, aumentando o risco de esquecer algo na entrega.

## Solução pretendida

Aplicação Python local que recebe um enunciado colado no terminal e apresenta uma lista de conferência organizada por entregáveis, requisitos/restrições, prazos explícitos e pontos a esclarecer.

Cada item extraído deve incluir um trecho de apoio copiado do texto recebido. Informações ausentes serão indicadas como “não identificado no texto”; ambiguidades serão sinalizadas. A lista não declara que uma exigência já foi cumprida.

Um LLM será utilizado para interpretar instruções com redações variadas e reunir requisitos espalhados pelo texto. A conferência final permanece com o estudante.

## Escopo

- Um enunciado textual por execução, inserido manualmente no terminal.
- Um único LLM, preferencialmente o institucional; acesso técnico a confirmar.
- Sem leitura de PDF ou acesso a links.
- Sem interface web, banco de dados ou agentes.
- Sem inventar obrigações ou transformar estimativas de duração em datas de entrega.

## Documentação

- [Decisões e próximos passos](docs/DECISOES.md)
- [Registro de uso de IA](docs/USO_DE_IA.md)

Instalação, configuração, execução e testes serão documentados conforme forem implementados e verificados. Exemplos públicos serão fictícios ou autorizados para divulgação.
