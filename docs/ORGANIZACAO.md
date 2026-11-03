# Organização do desenvolvimento

## Quadro e marcos

- [Project — Descomplica Enunciado — P0](https://github.com/users/KaykeAndrade7/projects/1)
- [Milestones](https://github.com/KaykeAndrade7/descomplica-enunciado/milestones)
- [Issues](https://github.com/KaykeAndrade7/descomplica-enunciado/issues)

Os marcos evoluem a mesma aplicação. Sem datas institucionais confirmadas, as milestones ficam sem vencimento.

| Milestone | Issues iniciais | Versão ao concluir |
|---|---|---|
| P0 — Básico | #1 contrato e exemplos; #2 terminal; #3 integração real; #4 validação e release | p0-basico |
| P0 — Intermediário | #5 organização e erros; #6 validação das citações; #7 documentação e release | p0-intermediario |
| P0 — Avançado | #8 parâmetros e logs; #9 ambiente limpo; #10 relatório, vídeo e release | p0-avancado |

Planejamento de 03/11/2026, ajustável conforme a aprendizagem. Hoje foram organizadas as tarefas; nenhuma implementação ou release está concluída.

## Fluxo por tarefa

1. Escolher uma issue e revisar seus critérios antes de começar. Registrar dependências e bloqueios na própria issue.
2. Criar branch curta, por exemplo `feat/1-contrato-entrada`, e marcar a tarefa como em andamento no quadro quando iniciar.
3. Fazer commits pequenos com referência à issue: `docs: definir contrato de entrada (#1)` ou `test: cobrir entrada vazia (#2)`.
4. Abrir PR para `main`, explicando mudança, verificação e limitações. Usar `Closes #1` na descrição quando o PR resolver integralmente a issue; para trabalho parcial, usar `Refs #1`.
5. Revisar o diff, confirmar ausência de segredos e executar as verificações pertinentes. Manter a issue aberta enquanto houver critérios pendentes.
6. Integrar o PR. Um PR integrado na branch padrão com a referência de fechamento encerra a issue. Confirmar também o status no quadro.

Revisão é uma etapa do PR; uma coluna extra poderá ser incluída se fizer falta. Não fechar tarefas apenas por criar commits. Para tarefas operacionais, como publicar uma release, fechar depois da ação e da conferência do resultado, registrando seu link; elas não precisam de um PR artificial.

Documentação histórica anterior à criação das issues permanece como foi realizada. Não fabricar vínculos, testes ou etapas retroativas.

## Tag e release

Uma **tag** nomeia um commit específico. Uma **release** é a apresentação dessa versão no GitHub, vinculada à tag, com notas e eventuais arquivos adicionais. Publicar release não implanta a aplicação nem substitui uma entrega no Moodle.

Ao concluir cada marco:

- Conferir as issues e evidências correspondentes.
- Identificar o commit validado de `main`.
- Criar a tag exata do marco e a release associada: `p0-basico`, `p0-intermediario` ou `p0-avancado`.
- Descrever funcionalidades disponíveis, instalação/execução, verificações reais, limitações e issues relacionadas.
- Preservar a versão. Correções posteriores geram novos commits, sem mover silenciosamente a tag de uma versão entregue.

Não criar releases antecipadas. A sequência de testes começa por exemplos fictícios offline, mas a conclusão do Básico requer demonstrar chamada real a um LLM.

## Disponibilidade do modelo

O aluno informou em 03/11/2026 que o fórum anuncia liberação futura do LLM institucional, ainda sem data divulgada. Essa informação não foi reconferida pelo assistente no fórum. A escolha continua sendo o institucional; outro provedor é uma opção a decidir, sem contratação obrigatória. O trabalho inicial de contrato, exemplos e avaliação pode avançar offline.
