# Descomplica Enunciado

Projeto P0 — TrendsIA, de Kayke Andrade.

**Estado atual** — Na Devel, uma página web recebe o enunciado colado em um campo de texto, consulta o Ollama institucional e mostra o checklist com os trechos de apoio conferidos. A imagem v4 foi testada na Devel com os casos fictícios C01 a C06, com falhas registradas na [avaliação](docs/AVALIACAO.md), como uma condição perdida no C06. O terminal (`main.py`) usa a mesma lógica, mas o endereço do Ollama institucional só é acessível de dentro da Devel, então ele só funciona com um Ollama acessível a partir da sua máquina ou com `--simulado`.

## Problema

Estudantes precisam identificar entregáveis, requisitos e prazos em enunciados longos, porque essas informações ficam espalhadas entre explicações e orientações, aumentando o risco de esquecer algo na entrega.

## Solução pretendida

Aplicação Python local que recebe um enunciado colado no terminal e apresenta uma lista de conferência organizada por entregáveis, requisitos/restrições, prazos explícitos e pontos a esclarecer.

Cada item extraído deve incluir um trecho de apoio copiado do texto recebido. Informações ausentes serão indicadas como “não identificado no texto”; ambiguidades serão sinalizadas. A lista não declara que uma exigência já foi cumprida.

A entrada será encerrada com `FIM` em uma linha isolada. Se um trecho de apoio não for localizado no texto recebido, o item terá o aviso “Não foi possível verificar no enunciado” e não será apresentado como requisito confirmado. O objetivo é produzir citações fiéis; essa verificação é uma proteção para eventuais erros.

Um LLM será utilizado para interpretar instruções com redações variadas e reunir requisitos espalhados pelo texto. A conferência final permanece com o estudante.

## Escopo

- Um enunciado textual por envio, colado em um campo de texto na página (Devel) ou digitado no terminal.
- Um único LLM, o Ollama institucional. O guia da plataforma informa que seu endereço só é acessível por aplicações dentro da Devel.
- Sem leitura de PDF ou acesso a links.
- A página web foi adotada na Devel porque o portal só executa containers e não oferece terminal interativo. Veja [Decisões](docs/DECISOES.md).
- Sem inventar obrigações ou transformar estimativas de duração em datas de entrega.

## Documentação

### Executar na Devel (página web)

1. Construa a imagem e exporte o TAR com `docker build` e `docker save`.
2. Envie o TAR no portal e configure a porta interna `8080`.
3. Em **Editar**, defina `OLLAMA_URL` e `OLLAMA_MODELO`, uma por linha, no formato `NOME=valor` (nomes no `.env.example`). As alterações valem no próximo início do container.
4. Inicie o container, abra o endereço e a porta pública mostrados no dashboard, cole o enunciado e clique em **Gerar checklist**. O link "Usar o exemplo fictício C01" preenche o campo.

O log do container registra apenas metadados (tamanho da consulta e resultado), nunca o texto do enunciado. A opção `OLLAMA_TESTE_SEM_VERIFICACAO_TLS=1` é temporária e desativa a validação do certificado; veja [Evolução](docs/EVOLUCAO.md).

### Executar no terminal

Use Python 3.10 ou superior. O projeto usa apenas a biblioteca padrão (veja `requirements.txt`) e foi verificado no Python 3.13.

O endereço e o modelo ficam fora do código, em variáveis de ambiente. O `.env.example` mostra os nomes; o programa não carrega esse arquivo sozinho. Isso exige um Ollama acessível a partir da sua máquina; o da Devel não é. No PowerShell, defina as variáveis na sessão atual e execute:

```powershell
$env:OLLAMA_URL = "<endereço do servidor Ollama>"
$env:OLLAMA_MODELO = "<nome do modelo>"
python -B main.py
```

Cole o enunciado e finalize com `fim` em uma linha separada. O programa envia o texto ao modelo e mostra o checklist. Cada trecho de apoio é conferido no enunciado, em aspas curvas ou retas, e os que não forem encontrados aparecem como “[Não foi possível verificar no enunciado]”. Se a resposta não trouxer nenhum trecho de apoio, o programa avisa no topo que nada foi verificado. Se as variáveis não estiverem definidas, ou se a chamada falhar, o programa mostra uma mensagem e termina.

### Executar a demonstração simulada

Sem acesso ao modelo, a demonstração usa a resposta de exemplo do C01:

```bat
python -B main.py --simulado
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
| Citação que atravessa uma quebra de linha do enunciado | A conferência ignora diferenças de espaços e quebras de linha; a citação é aceita. |
| Servidor Ollama falso local (resposta normal) | O terminal envia o modelo, `think: false` e o enunciado delimitado, e mostra o checklist com a citação inventada marcada. |
| Servidor falso devolvendo HTTP 500; servidor fora do ar | Mensagem compreensível e término com código 1. |
| Variáveis `OLLAMA_URL` e `OLLAMA_MODELO` ausentes | Mensagem orientando a configuração e término com código 1. |
| Página: GET, link do C01 e envio com quebras `\r\n` | A página mostra o campo de texto, o link preenche o C01 e o envio devolve o checklist verificado (servidor falso). |
| Página: enunciado vazio e com 10.001 caracteres | A página mostra a mesma mensagem de validação do terminal, sem consultar o modelo. |
| Página: servidor falso com HTTP 500; texto com `<script>` | Mensagem de erro na página; o texto é exibido escapado. |
| Página: conteúdo dos logs | Só tamanho e resultado da consulta; o texto do enunciado não é registrado. |
| Resposta real da Devel (3ª execução, aspas retas) | As três citações verdadeiras são mantidas; uma citação reta inventada é marcada. |
| Linha "Trecho de apoio:" com aspas curvas, aspas retas ou sem aspas | Cada forma é conferida no enunciado; aspas retas em prosa fora dessas linhas não são alteradas. |
| Resposta sem nenhum "Trecho de apoio:" | Aviso no topo de que nada foi verificado; com ao menos um trecho, sem aviso. |
| "Trecho de apoio:" no meio da linha (formato visto na v3) | Citações verdadeiras mantidas; inventadas marcadas. |

As verificações usam texto fictício e execução local. A conferência de citações verifica a presença literal do trecho. A interpretação é avaliada pelos critérios e exemplos do projeto.

### Referências do projeto

- [Decisões e próximos passos](docs/DECISOES.md)
- [Evolução do projeto e testes na Devel](docs/EVOLUCAO.md)
- [Registro de uso de IA](docs/USO_DE_IA.md)
- [Organização: Project, issues, milestones e releases](docs/ORGANIZACAO.md)
- [Contrato de entrada](docs/CONTRATO_ENTRADA.md)
- [Formato da resposta e critérios de avaliação](docs/AVALIACAO.md)
