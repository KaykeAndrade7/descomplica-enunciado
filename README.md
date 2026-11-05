# Descomplica Enunciado

Projeto P0 — TrendsIA, de Kayke Andrade.

**Estado atual** — Demonstração local no terminal com resposta simulada para o caso fictício C01.

## Problema

Estudantes precisam identificar entregáveis, requisitos e prazos em enunciados longos, porque essas informações ficam espalhadas entre explicações e orientações, aumentando o risco de esquecer algo na entrega.

## Solução pretendida

Aplicação Python local que recebe um enunciado colado no terminal e apresenta uma lista de conferência organizada por entregáveis, requisitos/restrições, prazos explícitos e pontos a esclarecer.

Cada item extraído deve incluir um trecho de apoio copiado do texto recebido. Informações ausentes serão indicadas como “não identificado no texto”; ambiguidades serão sinalizadas. A lista não declara que uma exigência já foi cumprida.

A entrada será encerrada com `FIM` em uma linha isolada. Se um trecho de apoio não for localizado no texto recebido, o item terá o aviso “Não foi possível verificar no enunciado” e não será apresentado como requisito confirmado. O objetivo é produzir citações fiéis; essa verificação é uma proteção para eventuais erros.

Um LLM será utilizado para interpretar instruções com redações variadas e reunir requisitos espalhados pelo texto. A conferência final permanece com o estudante.

## Escopo

- Um enunciado textual por execução, inserido manualmente no terminal.
- Um único LLM, preferencialmente o institucional; acesso técnico a confirmar.
- Sem leitura de PDF ou acesso a links.
- Sem interface web, banco de dados ou agentes.
- Sem inventar obrigações ou transformar estimativas de duração em datas de entrega.

## Documentação

### Executar a demonstração

Na pasta do projeto, use Python 3.10 ou superior. A demonstração usa apenas a biblioteca padrão e foi verificada no Python 3.13.

```bat
python -B main.py
```

Cole o exemplo abaixo e finalize com `fim` em uma linha separada.

```text
Crie um programa Python que leia uma lista de números e mostre a média.
Entregue o código-fonte e um README com instruções de execução.
Envie os arquivos até 18/11/2026 às 23h59.
fim
```

O terminal exibe **Resposta simulada — C01**, seguida de objetivo, entregáveis e requisitos, prazo e pontos a esclarecer. O checklist vem do [gabarito do C01](docs/EXEMPLO_RESPOSTA.md). Para outro enunciado válido, o terminal informa que a demonstração usa o C01.

### Verificações locais

| Cenário | Resultado observado |
|---|---|
| Várias linhas com acentos, espaços e linhas em branco | Conteúdo preservado até o marcador. |
| Entrada termina sem marcador | O leitor devolve o conteúdo recebido. |
| Entrada vazia, apenas espaços ou quebras | A validação informa que o enunciado está vazio. |
| 10.000 e 10.001 caracteres | O primeiro é aceito. O segundo é recusado com a contagem e o limite. |
| Opção inválida, nova tentativa e saída | O menu se repete após opção inválida. A opção 1 recebe novo texto e a opção 2 encerra. |
| Interrupção simulada por Ctrl+C | O programa informa que a entrada foi cancelada. |
| C01 e enunciado diferente | O primeiro exibe o checklist simulado. O segundo recebe o aviso da demonstração. |
| Citação presente e citação inventada para o teste | A primeira é preservada. A segunda é substituída por “Não foi possível verificar no enunciado”. |

As verificações usam texto fictício e execução local. A conferência de citações verifica a presença literal do trecho. A interpretação é avaliada pelos critérios e exemplos do projeto.

### Referências do projeto

- [Decisões e próximos passos](docs/DECISOES.md)
- [Registro de uso de IA](docs/USO_DE_IA.md)
- [Organização: Project, issues, milestones e releases](docs/ORGANIZACAO.md)
- [Contrato de entrada](docs/CONTRATO_ENTRADA.md)
- [Formato da resposta e critérios de avaliação](docs/AVALIACAO.md)
