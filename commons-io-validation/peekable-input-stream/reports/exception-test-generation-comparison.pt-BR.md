# Geração de testes de exceção a partir de JSON do WIT-UP e código-fonte Java

## Relatório consolidado do estudo piloto

Preparado para avaliação acadêmica em 2026-10-13 (UTC).

Este relatório identifica quais informações estavam ausentes ou insuficientemente utilizáveis no JSON do WIT-UP para gerar testes de exceção em Java, como essas informações poderiam melhorar e como medir os efeitos. Sua evidência vem de duas suítes JUnit já geradas e congeladas para `PeekableInputStream`, do Apache Commons IO. Ambas foram avaliadas com o mesmo protocolo de medições pareadas usando a suíte completa, na revisão 4 da configuração. A suíte da condição JSON foi medida novamente em uma nova avaliação; a avaliação da condição código-fonte Java foi reutilizada a partir de seu registro selado e verificado. Cada baseline foi efetivamente medido. Nenhum teste foi revisado com base no feedback de execução, cobertura ou mutation testing.

A suíte da condição JSON contém 10 casos aprovados, e a suíte da condição código-fonte Java contém 20. As respectivas suítes detectaram 1 e 7 dos mesmos 14 mutantes nativos, classificados pelo PIT como KILLED. A diferença observada de mutation score é de 42,86 pontos percentuais a favor da suíte da condição código-fonte Java nessas duas observações.

As entradas JSON foram suficientes para gerar uma suíte de testes de exceção aprovada sem consultar o código-fonte de produção, mas a suíte gerada a partir delas não alcançou a detecção de mutantes obtida com código-fonte Java neste par. A inspeção dos exports preservados identifica lacunas de informação que podem orientar melhorias: nenhum cenário selecionado descreve `IOException`, enquanto cinco detecções adicionais da condição Java são atribuídas a casos de falha de leitura; 21 candidatos SAT ficaram sem fixtures públicos sustentados; e os registros selecionados não fornecem mensagens esperadas de exceção. A próxima questão de pesquisa é se melhorias específicas nas informações exportadas conseguem reduzir essas lacunas mantendo o uso exclusivo de JSON pelo gerador.

Ambas as suítes foram geradas com GPT-6.1 Sol (`gpt-6.1-sol`), com reasoning effort Extra High (`xhigh`), em chats novos e separados, sem histórico anterior de conversa. Os registros originais das sessões e a confirmação do responsável pelo experimento estabelecem essas condições de geração. O tamanho e a composição das suítes são resultados observados da geração em cada condição de fonte de informação. Este estudo piloto descritivo contém uma geração por condição; novas gerações aguardam o feedback do Professor Rodrigo e Doutorando Adriano. Os resultados caracterizam este par, sem estimar sua repetibilidade ou uma superioridade geral.

## Objetivo e escopo

O estudo investiga se o JSON do WIT-UP fornece informações suficientes para gerar testes de exceção eficazes em Java sem disponibilizar o código-fonte de produção ao gerador e, quando isso não ocorre, quais informações devem ser melhoradas e como medir essa melhoria. A condição código-fonte Java fornece uma comparação para identificar comportamentos e observações ausentes na geração baseada em JSON; ela não constitui uma suíte de referência completa nem um resultado máximo alcançável.

A geração teve como alvo o comportamento excepcional dos construtores públicos e das sobrecargas declaradas de `peek` em `org.apache.commons.io.input.buffer.PeekableInputStream`. Cada caso gerado deveria conter uma asserção de exceção lançada por uma chamada ao alvo; operações normais só poderiam estabelecer o estado do fixture. A suficiência envolve, portanto, fixtures executáveis, oráculos de exceção sustentados e detecção de alterações no comportamento excepcional, em vez de uma quantidade fixa de testes ou um limiar de line coverage.

A condição JSON utilizou as exportações originais de resultados e resumos do WIT-UP. A condição código-fonte Java utilizou o código de produção designado e a implementação permitida da superclasse e do buffer. Os prompts preservados especificam integralmente esses limites nos apêndices. Geração e medição são fases distintas; os suplementos de avaliação não acrescentam gerações independentes.

Neste estudo, gerar sem código-fonte significa que o gerador não inspeciona código de produção, Javadoc, bytecode, código decompilado ou outros materiais sobre o comportamento específico do alvo fora do JSON atribuído. O build e o avaliador podem consumir artefatos de produção. Este piloto não estabelece que todo o processo anterior de análise e build funcione sem disponibilidade de código-fonte.

## Lacunas de informação no JSON, melhorias e medição dos efeitos

As prioridades abaixo conectam cada lacuna nas entradas JSON selecionadas a informações que o gerador poderia utilizar e a um resultado observável a medir. A coluna de evidência descreve este piloto; os acréscimos e as medições propostos ainda não foram implementados nem executados.

| Lacuna nas informações do JSON | O que o JSON deveria fornecer | Evidência deste estudo | Como medir o efeito da melhoria |
| --- | --- | --- | --- |
| Ausência de cenários de falha de leitura | Condições sustentadas em que a dependência de entrada lança `IOException`, uma forma acessível de configurar essa falha e como a exceção é propagada pela chamada ao alvo `peek`. | Nenhum dos 100 registros selecionados descreve `IOException`. Cinco detecções adicionais de mutantes na suíte da condição código-fonte Java são atribuídas a casos de falha de leitura. | Comparar JSON inalterado com JSON contendo esse acréscimo: registrar se casos sustentados de `IOException` são gerados e aprovados por chamadas ao alvo, quais das cinco lacunas de mutação associadas são resolvidas e se as detecções anteriores são mantidas. |
| Preparação pública do estado exigido insuficientemente sustentada | Argumentos válidos do construtor, relações entre capacidades, conteúdo e contagem de bytes iniciais e sequências de operações públicas que estabeleçam o estado exigido. Identificar condições de estado cuja alcançabilidade continue não resolvida. | Havia condições simbólicas, mas 21 candidatos SAT ficaram sem fixtures públicos suficientemente sustentados, incluindo 12 de `ArrayIndexOutOfBoundsException`. | Acompanhar cada candidato que passa a ter um fixture público justificado e uma exceção observada no alvo. Registrar estados ainda sem suporte, suposições e eventual impossibilidade demonstrada; examinar as mudanças resultantes na cobertura e nos status dos mutantes. |
| Origem da exceção esperada insuficientemente distinguida | Mensagem esperada sustentada ou outra propriedade observável, como causa, identidade ou condições que distingam a validação pretendida. Incluir a evidência que sustenta cada expectativa. | Os tipos de exceção estavam disponíveis, mas validações concorrentes podem lançar `IllegalArgumentException`. Uma detecção adicional da condição código-fonte Java depende de distingui-las pela mensagem; os registros selecionados não fornecem essa mensagem. | Verificar se as asserções geradas distinguem a exceção pretendida de outra do mesmo tipo produzida por uma validação diferente. Comparar o mutante de limite da linha 85 e o sobrevivente comum do guard de tamanho, mantendo a aprovação no alvo sem mutação. |

A primeira prioridade de conteúdo é investigar e representar falhas de leitura sustentadas, pois essa família ausente está associada a cinco lacunas observadas de detecção. A prioridade seguinte é conectar o estado simbólico à preparação pública executável, seguida do fortalecimento das observações que identificam a exceção esperada. Cada acréscimo proposto precisa ser derivado dos artefatos de análise permitidos; a causa das omissões atuais e a viabilidade de extrair todos os detalhes propostos ainda precisam ser investigadas.

O JSON já contém constraints e metadados de propagação. A melhoria é conectar esses fatos em uma descrição utilizável de **como preparar o cenário, qual chamada ao alvo executar e o que verificar na exceção**. Preservar a rastreabilidade entre o registro de entrada, o fixture, o oráculo e o resultado observado.

Para medir a informação acrescentada, comparar gerações independentes com JSON inalterado e gerações que recebam um acréscimo por vez; depois, examinar combinações. Manter fixos o prompt comum, o modelo e suas configurações, o alvo e o protocolo de medição quando reproduzíveis. Acompanhar ganhos de comportamento e mudanças específicas nos status dos mutantes junto às métricas existentes do JaCoCo e PIT, mantendo os 14 mutantes no score reportado. Reexecutar uma suíte congelada não mede a variação da geração; novas gerações exigem runs próprios preservados. As comparações detalhadas adiante neste relatório especificam os controles e os limites.

## O que o estudo piloto estabelece sobre a suficiência do JSON

| Sentido de suficiente | Resposta neste estudo piloto | Evidência e alcance |
| --- | --- | --- |
| Permite gerar testes de exceção executáveis sem consultar código-fonte? | Sim, para os casos gerados. | Os 10 casos gerados com JSON foram aprovados; a medição alinhada detectou 1 mutante. Os tipos esperados de exceção e as suposições dos fixtures são rastreáveis aos registros preservados. |
| Deu suporte a um fixture público para cada candidato SAT selecionado? | Não, nesta geração. | 10 dos 31 candidatos SAT produziram testes; 21 ficaram sem fixtures públicos suficientemente sustentados. Essas são associações com candidatos, e não path coverage medida ou prova de que todos os modelos remanescentes sejam alcançáveis publicamente. |
| A suíte resultante alcançou a eficácia observada da suíte gerada com código-fonte Java? | Não, neste par. | As suítes detectaram 1 versus 7 dos mesmos 14 mutantes, apesar da mesma line coverage do JaCoCo. A suíte da condição código-fonte Java também apresenta lacunas. |
| Isso estabelece que código-fonte seja indispensável ou que JSON não possa representar informações suficientes? | Não. | Os exports atuais apresentam lacunas concretas, mas exports enriquecidos não foram avaliados. Os registros também não estabelecem a melhor suíte que outra geração independente poderia produzir com o mesmo JSON. |

A resposta sustentada é, portanto, **viabilidade demonstrada, com lacunas nas informações fornecidas e na eficácia da suíte resultante**. A suficiência do JSON depende das informações exportadas e de seu uso pelo gerador; não é uma conclusão sobre o formato de serialização isoladamente. Nenhum limiar numérico de suficiência foi registrado antes deste piloto; os critérios abaixo são propostas para comparações futuras, e não critérios retroativos de aprovação ou reprovação.

## Registros e preservação

| Item | WIT-UP JSON | Código-fonte Java |
| --- | --- | --- |
| Geração | json-001 | java-source-001 |
| Avaliação | json-001/evaluation-001 | java-source-001/evaluation-005 |
| Origem registrada | retrospective_import | prospective |
| Modelo de geração | GPT-6.1 Sol (`gpt-6.1-sol`) | GPT-6.1 Sol (`gpt-6.1-sol`) |
| Reasoning effort | Extra High (`xhigh`) | Extra High (`xhigh`) |
| Contexto do chat | Chat novo e separado; sem histórico anterior de conversa | Chat novo e separado; sem histórico anterior de conversa |
| Casos gerados executados na fase alinhada após a inclusão | 10 | 20 |
| SHA-256 do código Java congelado | a29b1141af4aa61b9081d22e2056f69596e5ec602062773a4618b5567c3de926 | 365a763fbc4b383087d993e659e05bf04952a4d4333a2ff16ac4417fe9eb43dd |
| SHA-256 do selo da geração | 482c9deffe47d4fc69f8fee5e4380610991893d447a38fe0ca6973baece488fd | 28ac9b72af259f32261cb569e3ce65515007f3089213024d5065b60adcec9d5d |
| SHA-256 do selo da avaliação | 8e2bc78d5bcca8f8bf064566a855ada4dbb840c3fb22b6b2c5063c852ff5d461 | 57d892f347416957333f373348d08d1def6a87f282769e9e78ea9b0511346c69 |

Ambas as condições utilizam o commit `11f0abe7a3fb6954b2985ca4ab0697b2fb489e84` do Commons IO. Os checkouts de antes e depois são distintos, e seus inventários completos de arquivos rastreados são iguais. O único código-fonte acrescentado em cada checkout da fase após a inclusão é o arquivo Java congelado daquela geração, preservado exatamente. Os testes existentes, o código de produção, os arquivos de recursos e a configuração de build dos checkouts permanecem inalterados.

O SHA-256 da classe de produção é `7ab6a91f3618ccf5949692f1fc5d39b97174deab23925f872f0e31cb5a2591a1` nas oito fases de medição selecionadas. Os quatro artefatos do PIT contêm as mesmas 14 identidades de mutantes, incluindo classe, método, descriptor, linha do código-fonte, mutator, indexes e blocks. Os 23 JARs distintos do projeto e do launcher têm bytes idênticos nas duas avaliações; a ordem dos classpaths também é igual após a substituição dos caminhos específicos de cada avaliação.

## Resultados alinhados de antes e depois

Todas as linhas abaixo descrevem a classe de produção alvo, e não a cobertura da biblioteca Commons IO inteira. As porcentagens são calculadas a partir dos contadores inteiros nativos. Antes designa um checkout limpo do baseline, medido durante a avaliação; não se afirma que a medição tenha ocorrido antes da geração. As medições históricas da condição JSON utilizaram seleções diferentes e são preservadas separadamente; nenhum desses valores históricos foi usado nesta tabela comparativa.

| Métrica | JSON antes | JSON depois | Java antes | Java depois |
| --- | --- | --- | --- | --- |
| JaCoCo instruction coverage (instruções) | 0/98 (0,00%) | 77/98 (78,57%) | 0/98 (0,00%) | 77/98 (78,57%) |
| JaCoCo branch coverage (ramificações) | 0/8 (0,00%) | 7/8 (87,50%) | 0/8 (0,00%) | 8/8 (100,00%) |
| JaCoCo line coverage (linhas) | 0/16 (0,00%) | 11/16 (68,75%) | 0/16 (0,00%) | 11/16 (68,75%) |
| JaCoCo complexity (complexidade) | 0/8 (0,00%) | 6/8 (75,00%) | 0/8 (0,00%) | 7/8 (87,50%) |
| JaCoCo method (métodos) | 0/4 (0,00%) | 3/4 (75,00%) | 0/4 (0,00%) | 3/4 (75,00%) |
| JaCoCo class (classes) | 0/1 (0,00%) | 1/1 (100,00%) | 0/1 (0,00%) | 1/1 (100,00%) |
| PIT mutation score | 0/14 (0,00%) | 1/14 (7,14%) | 0/14 (0,00%) | 7/14 (50,00%) |
| PIT test strength | N/A (0/0) | 1/9 (11,11%) | N/A (0/0) | 7/10 (70,00%) |
| PIT line coverage nativa | 0/16 (0,00%) | 13/16 (81,25%) | 0/16 (0,00%) | 15/16 (93,75%) |
| PIT KILLED | 0 | 1 | 0 | 7 |
| PIT SURVIVED | 0 | 8 | 0 | 3 |
| PIT NO_COVERAGE | 14 | 5 | 14 | 4 |
| PIT TIMED_OUT | 0 | 0 | 0 | 0 |
| PIT RUN_ERROR | 0 | 0 | 0 | 0 |
| PIT MEMORY_ERROR | 0 | 0 | 0 | 0 |
| PIT NON_VIABLE | 0 | 0 | 0 | 0 |
| PIT execuções acumuladas de mutation testing | 0 | 26 | 0 | 42 |

Mutation score corresponde a `KILLED / all native mutants`, mantendo `NO_COVERAGE` no denominador. Test strength corresponde a `KILLED / (KILLED + SURVIVED)`; quando o denominador é zero, o resultado é N/A, mesmo que o console nativo do PIT mostre 100%. Não foram introduzidas exclusões de mutantes equivalentes. Um mutante com status SURVIVED não foi detectado por um teste que o cobriu; este relatório não afirma que cada sobrevivente represente um defeito real distinto. Consulte as [definições de resultados do PIT](https://pitest.org/quickstart/basic_concepts/).

As medições de line coverage do JaCoCo e do PIT são observações distintas e não são usadas uma em substituição à outra. A definição de branch coverage do JaCoCo não considera o tratamento de exceções como branches; portanto, 100% de branch coverage não comprova cobertura completa do comportamento excepcional. Consulte as [definições dos contadores do JaCoCo](https://www.jacoco.org/jacoco/trunk/doc/counters.html). Medições de cobertura e mutation testing não comprovam correção em relação a uma especificação independente.

## Resultados das execuções

As oito fases selecionadas de antes e depois foram concluídas com exit code 0 e resultados nativos preservados. Os contadores abaixo foram conferidos nos XMLs arquivados do Surefire, nos XMLs de mutação do PIT, nos registros das execuções e nos logs.

### JUnit/Surefire com instrumentação do JaCoCo

| Condição | Fase | Exit code do processo | Casos reportados | Aprovados | Falhas | Erros | Skips |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WIT-UP JSON | [jacoco-before](../supplements/json/001/001/executions/002/result.json) | 0 | 1541 | 1535 | 0 | 0 | 6 |
| WIT-UP JSON | [jacoco-after](../supplements/json/001/001/executions/004/result.json) | 0 | 1551 | 1545 | 0 | 0 | 6 |
| Código-fonte Java | [jacoco-before](../supplements/java-source/001/005/executions/002/result.json) | 0 | 1541 | 1535 | 0 | 0 | 6 |
| Código-fonte Java | [jacoco-after](../supplements/java-source/001/005/executions/004/result.json) | 0 | 1561 | 1555 | 0 | 0 | 6 |

Os totais reportados incluem seis skips intrínsecos da suíte existente do projeto. Os casos aprovados correspondem aos casos reportados menos falhas, erros e skips. O teste gerado acrescenta 10 casos no depois da condição JSON e 20 no depois da condição código-fonte Java, todos aprovados, sem falhas, erros ou skips. As medições de antes executaram a suíte existente do projeto; cobertura zero do alvo não significa ausência de execução dos testes do projeto.

Arquivos nativos do Surefire: [JSON antes](../supplements/json/001/001/executions/002/surefire-reports.zip), [JSON depois](../supplements/json/001/001/executions/004/surefire-reports.zip), [Java antes](../supplements/java-source/001/005/executions/002/surefire-reports.zip) e [Java depois](../supplements/java-source/001/005/executions/004/surefire-reports.zip).

### Validação e mutation testing do PIT

| Condição | Fase | Exit code do processo | Classes enviadas ao worker | Execuções acumuladas contra mutantes | KILLED | SURVIVED | NO_COVERAGE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| WIT-UP JSON | [pit-before](../supplements/json/001/001/executions/003/output.log) | 0 | 374 | 0 | 0 | 0 | 14 |
| WIT-UP JSON | [pit-after](../supplements/json/001/001/executions/005/output.log) | 0 | 375 | 26 | 1 | 8 | 5 |
| Código-fonte Java | [pit-before](../supplements/java-source/001/005/executions/003/output.log) | 0 | 374 | 0 | 0 | 0 | 14 |
| Código-fonte Java | [pit-after](../supplements/java-source/001/005/executions/005/output.log) | 0 | 377 | 42 | 7 | 3 | 4 |

Cada fase do PIT produziu 14 resultados nativos de mutantes. As classes enviadas ao worker vêm da entrada `Sending ... test classes to minion` do log. As execuções acumuladas vêm de `Ran ... tests` e correspondem à soma dos atributos `numberOfTestsRun` dos mutantes. Essas contagens são distintas dos totais de casos JUnit. Nas duas fases de antes, o PIT concluiu o cálculo inicial de cobertura, classificou os 14 mutantes como `NO_COVERAGE` e, portanto, realizou zero execuções contra mutantes. Esse zero não descreve a etapa inicial de validação e cobertura.

O PIT usa seu próprio runner e não emite um resumo de casos, falhas, erros e skips no formato Surefire nessas invocações. Seus resultados coletados são os contadores nativos acima e as métricas de cobertura e mutação da seção anterior. Os quatro processos foram concluídos com `--skipFailingTests false`; o campo genérico `suiteCounts: null` nos registros dessas execuções indica a ausência de um resumo Surefire, e não a falta de medição do PIT. Falhas de infraestrutura de outras invocações ficam fora desses totais e permanecem em seus registros originais de diagnóstico.

Artefatos nativos de mutação do PIT: [JSON antes](../supplements/json/001/001/executions/003/artifacts/001-mutations.xml), [JSON depois](../supplements/json/001/001/executions/005/artifacts/001-mutations.xml), [Java antes](../supplements/java-source/001/005/executions/003/artifacts/001-mutations.xml) e [Java depois](../supplements/java-source/001/005/executions/005/artifacts/001-mutations.xml).

## Insights e oportunidades de melhoria

### O que explica as detecções adicionais de mutantes

A suíte da condição código-fonte Java detecta o único mutante detectado pela suíte JSON e outros seis. Nenhum mutante foi detectado exclusivamente pela condição JSON neste par. O mapeamento abaixo vem diretamente dos [XMLs de mutação da condição JSON](../supplements/json/001/001/executions/005/artifacts/001-mutations.xml) e da [condição código-fonte Java](../supplements/java-source/001/005/executions/005/artifacts/001-mutations.xml). As linhas referem-se a `PeekableInputStream.java` no [arquivo preservado do código de produção](../runs/java-source/001/inputs/production-source.zip).

| Sobrecarga e linha do código-fonte | Mutação | Resultado JSON | Resultado código-fonte Java | Caso registrado pelo PIT como responsável pela detecção na condição Java |
| --- | --- | --- | --- | --- |
| `peek(byte[])`, 63 | Limite do guard de tamanho: `>` torna-se `>=` | SURVIVED | KILLED | `peekArrayPropagatesReadFailureDuringRefill`, comprimento do prefixo 1 |
| `peek(byte[])`, 67 | Condição de refill forçada para false | SURVIVED | KILLED | `peekArrayPropagatesReadFailureDuringRefill`, comprimento do prefixo 1 |
| `peek(byte[])`, 68 | Chamada a `fillBuffer()` removida | NO_COVERAGE | KILLED | `peekArrayPropagatesReadFailureDuringRefill`, comprimento do prefixo 1 |
| `peek(byte[],int,int)`, 85 | Limite do guard de tamanho: `>` torna-se `>=` | SURVIVED | KILLED | `peekSliceRejectsNegativeLength` |
| `peek(byte[],int,int)`, 89 | Condição de refill forçada para false | SURVIVED | KILLED | `peekSlicePropagatesReadFailureBeforeInvalidSlice`, comprimento do prefixo 0 |
| `peek(byte[],int,int)`, 90 | Chamada a `fillBuffer()` removida | SURVIVED | KILLED | `peekSlicePropagatesReadFailureBeforeInvalidSlice`, comprimento do prefixo 0 |

Cinco detecções adicionais têm, portanto, casos registrados que injetam uma `IOException` pela dependência pública `InputStream`. O [teste congelado da condição código-fonte Java](../runs/java-source/001/evidence/test-source/PeekableInputStreamTest.java) exige a propagação dessa exceção pela chamada ao alvo e verifica sua identidade com `assertSame`. O [teste congelado da condição JSON](../runs/json/001/evidence/test-source/PeekableInputStreamTest.java) usa apenas fixtures com `ByteArrayInputStream` vazio e asserções do tipo da exceção. Seus casos não exercitam as mesmas observações de falhas de leitura. Isso fornece uma explicação concreta, no nível dos fixtures, para a maior parte da diferença medida na detecção.

A detecção adicional restante mostra por que verificar apenas o tipo da exceção pode ser insuficiente. Em `peekSliceRejectsNegativeLength`, o comprimento do array solicitado é igual à capacidade 1, e o comprimento da fatia solicitada é -1. O alvo original alcança o guard delegado de comprimento e lança `IllegalArgumentException` com `Invalid length: -1`. A alteração do guard de tamanho do alvo para `>=` lança `IllegalArgumentException` na verificação anterior de tamanho. O tipo continua igual; a asserção da mensagem esperada distingue os dois caminhos. Essa explicação resulta do rastreamento no código-fonte e no teste preservados, sustentado pelo caso registrado pelo PIT como responsável pela detecção. As mensagens são observações de caracterização derivadas da fonte, e não garantias da API estabelecidas de forma independente.

O PIT registra um caso responsável pela detecção de cada mutante, sem listar exaustivamente todos os casos que poderiam detectá-lo. Esse mapeamento não mede o que ocorreria com a remoção de casos nem isola o efeito da quantidade de testes das escolhas de fixtures e oráculos. Os 14 mutantes nativos modificam `peek`; nenhum modifica um construtor. Casos adicionais de construtores não podem explicar a detecção dessas mutações específicas.

### Lacunas específicas que permanecem

As duas suítes deixam os mesmos três mutantes cobertos com status `SURVIVED`. Os candidatos abaixo foram derivados da inspeção do código-fonte e dos testes; não foram implementados nem executados.

| Mutação remanescente | Por que as observações existentes podem não detectá-la | Candidato concreto de melhoria |
| --- | --- | --- |
| `peek(byte[])`, linha 63: guard de tamanho removido | Uma solicitação maior que a capacidade ainda pode produzir `IllegalArgumentException` no guard delegado de comprimento do buffer. Uma asserção apenas do tipo pode aceitar uma exceção da etapa errada de validação. | Capacidade 1 e solicitação de dois bytes: distinguir o guard original de tamanho pela mensagem sustentada pela fonte ou usar uma entrada com falha de leitura para tornar observável um refill indevido. O resultado original esperado continua sendo `IllegalArgumentException`. |
| `peek(byte[])`, linha 67: limite de refill `<` torna-se `<=` | O caso existente de igualdade usa uma entrada vazia; um refill adicional não altera a exceção de offset verificada. | Array de comparação vazio, capacidade 1, buffer inicialmente vazio e entrada que lança exceção na primeira leitura. O original não faz refill e lança a `IllegalArgumentException` delegada; um refill indevido exporia `IOException`. |
| `peek(byte[],int,int)`, linha 89: limite de refill `<` torna-se `<=` | O caso correspondente de igualdade não torna observável a diferença de um refill adicional. | O mesmo fixture com array vazio e falha de leitura, offset 0 e comprimento 0 distingue a exceção delegada de offset de uma falha de refill. |

As transformações dos limites seguem as [definições oficiais dos mutators do PIT](https://pitest.org/quickstart/mutators/#CONDITIONALS_BOUNDARY). Esses candidatos identificam diferenças observáveis por chamadas públicas, sem exigir alteração de estado privado. Sua capacidade de detecção em execução ainda não foi medida, e nenhum sobrevivente foi excluído ou declarado equivalente.

Os quatro mutantes que substituem retornos booleanos nas linhas 70 e 92 têm status `NO_COVERAGE` nas duas suítes. Eles dizem respeito a resultados normais de correspondência ou divergência dos bytes, explicitamente excluídos pelos prompts de geração. Sua ausência é, portanto, uma observação sobre o escopo, e não evidência de quatro casos de exceção ausentes. Os mutation scores publicados mantêm os 14 mutantes. Investigar essas quatro mutações de retorno exigiria um experimento definido separadamente que permitisse asserções de retorno bem-sucedido.

### Onde as informações do JSON atual são insuficientes

Uma revisão somente de leitura dos exports originais, usando as cópias verificadas no [inventário de backup das entradas](../../../docs/input-backups.json), selecionou o package `org.apache.commons.io.input.buffer`, a classe `PeekableInputStream` e os métodos `<init>` ou `peek`. O join por `artifact` e `pathId` resulta nos mesmos 100 pares consistentes documentados na [auditoria de cenários](../runs/json/001/evidence/test-scenarios.json): 31 SAT e 69 UNSAT. Cada export contém 49 registros para cada sobrecarga de `peek` e 2 para o construtor de dois argumentos; nenhum corresponde ao construtor de um argumento. As contagens a seguir referem-se apenas a esses registros selecionados.

| Tipo de exceção | Todos os registros de resumo selecionados | Registros SAT | Registros SAT associados a testes gerados | Registros SAT sem fixtures sustentados |
| --- | --- | --- | --- | --- |
| `IllegalArgumentException` | 17 | 15 | 8 | 7 |
| `NullPointerException` | 58 | 4 | 2 | 2 |
| `ArrayIndexOutOfBoundsException` | 24 | 12 | 0 | 12 |
| `NegativeArraySizeException` | 1 | 0 | 0 | 0 |
| `IOException` | 0 | 0 | 0 | 0 |
| Total | 100 | 31 | 10 | 21 |

Esses registros apontam para três problemas diferentes, que exigem intervenções distintas:

1. **Cenários ausentes.** Nenhum registro selecionado descreve `IOException`. Sob o prompt original, o gerador não poderia inventar um cenário de falha de leitura sem suporte nos exports. Cinco detecções nativas adicionais de mutantes são atribuídas justamente a essa família na suíte da condição código-fonte Java. Isso motiva investigar a modelagem de falhas de dependências e a completude da exportação. Não se trata de ausência geral de metadados de propagação: 84 resumos selecionados já possuem `throwSiteKind: CALLEE_PROPAGATED` e informações de propagação. A ausência da família de falhas de leitura está estabelecida; a razão de sua omissão pela versão produtora do WIT-UP ainda não está.
2. **Cenários presentes, mas sem construção pública sustentada.** Os 12 candidatos SAT de `ArrayIndexOutOfBoundsException` ficaram sem representação. Os [motivos registrados](../runs/json/001/evidence/peekable-input-stream-report.md#sat-records-without-generated-public-fixtures) incluem offsets privados de início, contagens de bytes, relações de capacidade e condições de correspondência de conteúdo. Outros candidatos exigem um buffer privado nulo ou um estado preenchido sem preparação sustentada. A melhoria é conectar o estado simbólico à construção válida e a sequências públicas de preparação, distinguindo alcançabilidade sem suporte de impossibilidade demonstrada. Mais registros SAT, por si só, não resolveriam esse problema, e a evidência não estabelece que todos os 21 candidatos devam se tornar testes.
3. **Tipo de exceção presente, mas origem insuficientemente distinguida.** Os campos dos resumos selecionados incluem `exceptionType`, `constraints`, `throwSiteKind`, `provenance` e `provenances`, mas não um campo de mensagem esperada. Por exemplo, o path `#31` da sobrecarga com fatia, nas posições 13773 dos resultados e 61230 dos resumos, sustenta comprimento negativo e `IllegalArgumentException` delegada; ele não fornece a mensagem `Invalid length: -1` usada pelo oráculo da condição código-fonte Java. O mutante associado à linha 85 preserva a classe da exceção, mas altera sua origem. Uma mensagem, causa, identidade ou outra observação pública sustentada pode fortalecer essa distinção, conforme o que as informações extraídas efetivamente estabeleçam.

Esses achados separam informações ausentes nos exports de informações existentes que não foram convertidas em um fixture ou oráculo eficaz. Repetir a geração com o JSON inalterado permite investigar o segundo caso; isso não autoriza acrescentar um cenário que continue fora das entradas permitidas. Mensagens esperadas derivadas da implementação permanecem oráculos de caracterização, e não garantias independentes da API.

### Melhorias e medições que responderiam à questão de pesquisa

As comparações abaixo são propostas de investigação, e não experimentos recém-executados. Seu propósito é descobrir o mínimo de informações úteis para um gerador que continua recebendo JSON em vez de código-fonte de produção.

| Comparação proposta | O que muda na entrada ou no processo | Hipótese e observação a medir |
| --- | --- | --- |
| Repetir a geração com o JSON inalterado | Manter os exports brutos e as regras de geração; usar chats novos e checkouts independentes. | Verificar se as constraints e os metadados de propagação existentes produzem mais fixtures sustentados ou oráculos mais fortes entre gerações. Registrar todos os resultados e sua variação, e não apenas o melhor score. |
| Acrescentar informações de falhas de dependências | Exportar condições sustentadas de falha de leitura, como configurar a dependência por uma API acessível e qual exceção é propagada pelo alvo. Comparar com um controle de JSON inalterado sob as mesmas regras de geração. | Verificar se chamadas ao alvo passam a conter asserções de `IOException`, se as cinco lacunas de mutação associadas são resolvidas e se os mutantes antes detectados continuam detectados. Esta é a primeira melhoria de conteúdo sugerida pela diferença observada de detecção. |
| Acrescentar informações de construção pública e estado | Fornecer constraints sustentadas de construtores, relações de capacidade, estado inicial, sequências públicas de preparação e alcançabilidade ainda não resolvida de forma explícita. Avaliar esse acréscimo separadamente. | Contar candidatos antes sem suporte que passam a ter um fixture público justificado e uma exceção observada no alvo; examinar cenários de limites de arrays e registrar casos ainda sem suporte ou demonstrados inalcançáveis. Não forçar estado privado para converter todos os modelos SAT. |
| Acrescentar informações observáveis sobre a origem da exceção | Fornecer mensagens, causas, relações de identidade ou observações sustentadas que distingam validações concorrentes. Avaliar esse acréscimo separadamente. | Verificar se um oráculo detecta a origem incorreta da validação apesar do mesmo tipo de exceção, especialmente na mutação da linha 85 e no sobrevivente comum do guard de tamanho. Avaliar os sobreviventes do limite de refill com um fixture público que torne a diferença observável. |
| Combinar os acréscimos e comparar com código-fonte Java | Examinar tanto as contribuições individuais quanto as combinações; manter JSON inalterado e código-fonte Java como condições de comparação. | Determinar se a geração baseada em JSON resolve as lacunas identificadas de comportamento e detecção de mutantes sem perder detecções existentes. Scores semelhantes, isoladamente, não estabelecem equivalência de cenários, repetibilidade ou independência geral de código-fonte. |

Alguns acréscimos podem depender uns dos outros: um oráculo informativo não compensa um fixture que nunca alcança o comportamento relevante. A ausência de ganho com um acréscimo isolado, portanto, não descarta sua utilidade em combinação nem uma limitação da geração. Registrar essas interações evita atribuir toda mudança a um único campo.

Antes de uma nova comparação, congelar as variantes de entrada, as instruções comuns de geração, a quantidade planejada de gerações independentes e os critérios de decisão. Não alterar prompt e conteúdo JSON simultaneamente quando a afirmação pretendida se refere a apenas um deles. Se o próprio prompt for melhorado, comparar essa mudança com JSON inalterado como uma intervenção separada. Manter modelo e reasoning effort quando reproduzíveis, registrar as configurações efetivas e tratar o tamanho da suíte como resultado, sem fixá-lo em 10 ou 20.

Para cada suíte gerada, medir: compilação e resultados dos testes executados; fixtures públicos sustentados versus não resolvidos; famílias de exceção e sobrecargas exercitadas por chamadas ao alvo; fonte de cada oráculo e possibilidade de distinguir a origem da exceção; e os contadores pareados existentes do JaCoCo e PIT. Manter as 14 identidades de mutantes no score reportado e comparar quais mutantes mudam de status. Explicar separadamente as quatro mutações de retorno normal fora do escopo exclusivo de exceções. Os 31 candidatos SAT originais permanecem um conjunto de rastreabilidade, e não um denominador de path coverage; cenários recém-exportados precisam de identidades próprias registradas. O comportamento dos construtores também exige observações explícitas de exceção, pois as 14 mutações atuais estão em `peek`.

Um sinal proposto de avanço é um teste sustentado e aprovado para um comportamento excepcional antes ausente ou um oráculo mais forte que detecte uma mutação antes sobrevivente, sem perder detecções anteriores. Uma afirmação de suficiência exige critérios registrados antes das novas gerações e evidência nas repetições planejadas; igualar 7/14 apenas neste alvo conhecido não provaria suficiência geral. Seriam necessários outros alvos para uma afirmação além de `PeekableInputStream`.

As informações acrescentadas ao JSON precisam de proveniência e de uma derivação reproduzível. Se os campos forem preenchidos manualmente após consulta ao código-fonte Java, identificar a condição como JSON enriquecido manualmente: isso permite testar se esses fatos ajudam o gerador, mas não demonstra extração automática pelo WIT-UP nem um processo completo sem acesso a código-fonte. Investigar se as informações necessárias podem ser extraídas dos artefatos analisados permitidos e recuperar a identidade do JAR analisado e a revisão da ferramenta produtora antes de atribuir a melhoria ao WIT-UP. Um JSON contendo código-fonte copiado ou um teste pronto responderia a outra questão. Melhorias concebidas a partir deste piloto são exploratórias neste alvo; alvos posteriores não devem expor seus testes de referência nem feedback de avaliação aos geradores.

Qualquer comparação aceita exige novas gerações reservadas, snapshots atribuídos das entradas, congelamento antes da execução e suplementos de avaliação autorizados separadamente, conforme a [metodologia de preservação](../../../docs/run-methodology.md). Os testes existentes e os runs selados permanecem como evidência de baseline. Estas propostas não iniciam uma geração, não alteram o WIT-UP nem executam medições; a continuidade do trabalho experimental aguarda o feedback do Professor Rodrigo e Doutorando Adriano.

## Conclusões

**O JSON do WIT-UP foi suficiente para gerar 10 testes de exceção aprovados sem consultar código-fonte de produção. A suíte resultante não alcançou a detecção de mutantes observada na suíte da condição código-fonte Java: 1/14 versus 7/14. Isso estabelece viabilidade com lacunas específicas; não estabelece que código-fonte seja indispensável.**

O resultado aplicável é um conjunto priorizado de melhorias no JSON: representar cenários sustentados de falha de leitura ausentes nos registros selecionados, conectar condições simbólicas existentes a fixtures públicos construíveis e fornecer detalhes observáveis que distingam a origem da exceção esperada. A questão central é se esses acréscimos permitem ao gerador preparar mais cenários sustentados e verificar seus resultados excepcionais de forma eficaz, continuando a receber apenas JSON. Fixtures e oráculos mais informativos explicam detecções nativas específicas de mutantes; contar testes ou linhas cobertas, por si só, não responde se a informação é suficiente.

A próxima medição deve investigar se testes gerados independentemente a partir de cada melhoria específica no JSON resolvem as lacunas identificadas de comportamento e detecção sob o mesmo protocolo. Comparações separadas de JSON inalterado, acréscimos individuais e sua combinação permitem distinguir limitações das informações exportadas da variação em seu uso pelo gerador. Até que essas comparações sejam realizadas, JSON enriquecido permanece uma melhoria plausível a avaliar, e eficácia equivalente sem acesso do gerador ao código-fonte permanece não estabelecida.

## Interpretação e alcance do estudo piloto

A comparação sustenta uma observação delimitada sobre estas duas suítes: a cobertura de execução do alvo e a detecção das mesmas mutações geradas sob a configuração de medição registrada. Ela não estima um efeito médio, significância estatística ou uma classificação geral de fontes de informação.

Os prompts não fixaram uma quantidade de testes: os 10 versus 20 casos e as diferentes asserções são resultados a explicar, e não uma falha do protocolo. O mapeamento entre mutantes e testes acima identifica mecanismos específicos de detecção. Ele não quantifica efeitos separados do acesso à fonte, da quantidade de casos, da escolha de fixtures e da força dos oráculos, nem estabelece a reprodução de todos os caminhos internos simbólicos.

A interação inicial de geração em cada sessão original registra `model: gpt-6.1-sol` e `effort: xhigh`. Os cabeçalhos das duas sessões registram o runtime do Codex com `cli_version: 0.162.0-alpha.17.2`. Os inícios distintos das sessões e seus prompts iniciais, junto à confirmação do responsável pelo experimento, estabelecem o uso de chats novos sem histórico anterior de conversa. As evidências recuperadas e as localizações exatas nas sessões estão preservadas em anotações vinculadas à [geração com JSON](../supplements/json/001/002/report.md) e à [geração com código-fonte Java](../supplements/java-source/001/006/report.md). Os campos antes desconhecidos permanecem literais nos registros selados e nas cópias dos ambientes reproduzidas neste relatório; as anotações fornecem os fatos recuperados sem reescrever esses registros.

A geração com JSON continua sendo uma importação retrospectiva, e seu horário original de congelamento não foi registrado. A versão da CLI registrada na sessão não identifica um build separado da interface desktop. Os bytes do JAR analisado pelo WIT-UP e a revisão do WIT-UP que produziu as exportações continuam não verificados. Esses limites específicos de proveniência não tornam desconhecidos o modelo, o reasoning effort ou as condições de uso de chats novos recuperados dos registros.

## Diagnósticos preservados fora dos totais dos resultados

As falhas históricas de inicialização da condição JSON e as falhas de execuções exploratórias do PIT permanecem no registro original de diagnóstico selado. Quatro avaliações anteriores da condição código-fonte Java permanecem seladas como incompletas, abrangendo erros de parsing na preparação, descoberta de testes pelo PIT que resultou em execução ignorada e falhas relacionadas a recursos com caminhos relativos e ao diretório nativo de execução. Essas operações não fornecem as métricas válidas da comparação e não são contadas como falhas de casos gerados que não chegaram a executar. As falhas reais dos processos e eventuais falhas de testes existentes na execução sem mutação permanecem preservadas.

A geração da condição código-fonte Java também preserva dois achados de uma verificação direta e separada do Checkstyle sobre o teste congelado: ausência de package-info.java e ausência de Javadoc em um construtor privado de fixture. Esses achados não foram corrigidos após o congelamento e são distintos dos resultados do JUnit. Os ciclos de execução Maven com a suíte completa e os processos PIT selecionados foram bem-sucedidos; essa afirmação não reclassifica a verificação de estilo separada como aprovada.

## Ambiente e configuração para reprodução

| Componente | Versão ou configuração exata |
| --- | --- |
| Modelo de geração / reasoning effort | GPT-6.1 Sol (`gpt-6.1-sol`) / Extra High (`xhigh`) |
| Runtime do Codex registrado (`cli_version`) | 0.162.0-alpha.17.2 |
| Fornecedor/runtime Java | Eclipse Temurin; 1.8.0_504-b01 |
| JVM / javac | 25.504-b01 / 1.8.0_504 |
| Java source/target | 1.8 / 1.8 |
| Maven | 3.9.16; build 2bdd9fddda4b155ebf8000e807eb73fd829a51d5 |
| Commons IO / parent Apache Commons | 2.7-SNAPSHOT / 50 |
| JUnit Jupiter / Platform | 5.5.2 / 1.5.2 |
| Surefire | 2.22.2 |
| JaCoCo agent e CLI | 0.8.4 |
| PIT CLI, entry, core / JUnit 5 adapter | 1.15.2 / 1.2.2 |
| Plugins dependency / help do Maven | 3.6.1 / 3.5.1 |
| Python | 3.13.15 |
| PowerShell | 7.6.5 |
| Sistema operacional (OS) | Microsoft Windows 10.0.26300; X64 |

As localizações exatas dos executáveis, as flags, as observações do sistema operacional e os valores do ambiente do processo são registrados antes de cada invocação. Os comandos selecionam o JDK 8 para o processo e direcionam TEMP/TMP e o repositório Maven para o diretório de trabalho exclusivo da avaliação em D:. A configuração das dependências e seus bytes são idênticos entre as condições; o inventário completo do runtime aparece a seguir.

```json
{
  "schemaVersion": 1,
  "protocol": "paired-full-suite",
  "configurationRevision": 4,
  "baselineCommit": "11f0abe7a3fb6954b2985ca4ab0697b2fb489e84",
  "javaRuntime": "1.8.0_504-b01",
  "javac": "1.8.0_504",
  "maven": "3.9.16",
  "surefire": "2.22.2",
  "junitJupiter": "5.5.2",
  "jacoco": "0.8.4",
  "pit": "1.15.2",
  "pitJunit5Adapter": "1.2.2",
  "targetClass": "org.apache.commons.io.input.buffer.PeekableInputStream",
  "jacocoTestSelection": "all existing project tests; add only the frozen generated file after",
  "pitTestSelection": "org.apache.commons.io.*",
  "pitSourceDiscovery": "Use the assigned checkout's src/main/java and src/test/java, with compiled outputs from its own preceding JaCoCo build.",
  "pitLauncher": "PIT 1.15.2 command-line launcher executed natively from the phase checkout; both native and Java relative fixture roots match Surefire.",
  "mutationEngine": "gregor",
  "mutators": ["DEFAULTS"],
  "threads": 1,
  "timeoutFactor": 1.25,
  "timeoutConstantMilliseconds": 3000,
  "jvmArguments": ["-Xmx256m"],
  "jacocoAppend": true,
  "jacocoFreshExecutionFileRequired": true,
  "pairing": "Identical production class bytes, configuration, and existing tests; only the frozen generated test differs.",
  "mutationScore": "KILLED / total native mutants, retaining NO_COVERAGE; zero denominator is not applicable.",
  "testStrength": "KILLED / (KILLED + SURVIVED); zero denominator is not applicable.",
  "invalidMutationStatuses": ["TIMED_OUT", "RUN_ERROR", "MEMORY_ERROR", "NON_VIABLE"],
  "baselineFailurePolicy": "Preserve diagnostics and seal the evaluation incomplete; do not change scope, skip tests, or relax gates."
}
```

### Inventário completo dos JARs do runtime

Os caminhos são relativos ao diretório `maven-repository` de cada avaliação e identificam grupo, artefato e versão exata. A coluna de hashes é comum às duas avaliações. Os classpaths registrados preservam a ordem das entradas e distinguem o Commons Lang 3.9 do projeto e o Commons Lang 3.12.0 do launcher.

| Caminho do artefato Maven | SHA-256 | Bytes |
| --- | --- | --- |
| `com/google/guava/guava/18.0/guava-18.0.jar` | `d664fbfc03d2e5ce9cab2a44fb01f1d0bf9dfebeccc1a473b1f9ea31f79f6f99` | 2256213 |
| `com/google/jimfs/jimfs/1.1/jimfs-1.1.jar` | `c4828e28d7c0a930af9387510b3bada7daa5c04d7c25a75c7b8b081f1c257ddd` | 206691 |
| `net/bytebuddy/byte-buddy-agent/1.9.10/byte-buddy-agent-1.9.10.jar` | `8ed739d29132103250d307d2e8e3c95f07588ef0543ab11d2881d00768a5e182` | 43420 |
| `net/bytebuddy/byte-buddy/1.9.10/byte-buddy-1.9.10.jar` | `2936debc4d7b6c534848d361412e2d0f8bd06f7f27a6f4e728a20e97648d2bf3` | 3272730 |
| `org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar` | `d919d904486c037f8d193412da0c92e22a9fa24230b9d67a57855c5c31c7e94e` | 587402 |
| `org/apache/commons/commons-lang3/3.9/commons-lang3-3.9.jar` | `de2e1dcdcf3ef917a8ce858661a06726a9a944f28e33ad7f9e08bea44dc3c230` | 503880 |
| `org/apache/commons/commons-text/1.10.0/commons-text-1.10.0.jar` | `770cd903fa7b604d1f7ef7ba17f84108667294b2b478be8ed1af3bffb4ae0018` | 238400 |
| `org/apiguardian/apiguardian-api/1.1.0/apiguardian-api-1.1.0.jar` | `a9aae9ff8ae3e17a2a18f79175e82b16267c246fbbd3ca9dfbbb290b08dcfdd4` | 2387 |
| `org/junit-pioneer/junit-pioneer/0.3.0/junit-pioneer-0.3.0.jar` | `e8569ccd96843a1f1a3d5330fa731cdaf9038c1f7c5b9ba0b47cf89346357d32` | 26655 |
| `org/junit/jupiter/junit-jupiter-api/5.5.2/junit-jupiter-api-5.5.2.jar` | `249a2fdbd3931987c0298d00ca08ed248496e0fc11e0463c08c4f82e0cc79b1c` | 141766 |
| `org/junit/jupiter/junit-jupiter-engine/5.5.2/junit-jupiter-engine-5.5.2.jar` | `6d777da9876e2ef7a0336e8f098f8d74a5a64f810aa3a4a2f5f3b766ce97837b` | 219630 |
| `org/junit/jupiter/junit-jupiter-params/5.5.2/junit-jupiter-params-5.5.2.jar` | `fd49c7fd9d0f7f1e5b5f6982254cee79177fa2e76a37fdee0466e64f975567b5` | 549435 |
| `org/junit/jupiter/junit-jupiter/5.5.2/junit-jupiter-5.5.2.jar` | `72fb607d1778cb870a6e009432b51619a70b88d7056f708ab1e0aaf72ef25452` | 6161 |
| `org/junit/platform/junit-platform-commons/1.5.2/junit-platform-commons-1.5.2.jar` | `fc44afdfc0f20c85e71a66e7943281aef3bc1e0fd62d2d69a36cb6901e682c10` | 91709 |
| `org/junit/platform/junit-platform-engine/1.5.2/junit-platform-engine-1.5.2.jar` | `ff20ba4ad8c00ef17baef9c55512f9c02d9a68740f7f1ac01a9a6aa0239931f8` | 163866 |
| `org/junit/platform/junit-platform-launcher/1.5.2/junit-platform-launcher-1.5.2.jar` | `c1f6473ddd343550b42e94072aff9417ff38398f8b6bafe27b785aebcdaa660b` | 99589 |
| `org/mockito/mockito-core/3.0.0/mockito-core-3.0.0.jar` | `ae2efd8f05ceda5ed9c802a43265a95adfa885ca5535a8476a7aaa0b15b95abb` | 591095 |
| `org/objenesis/objenesis/2.6/objenesis-2.6.jar` | `5e168368fbc250af3c79aa5fef0c3467a2d64e5a7bd74005f25d8399aeb0708d` | 55684 |
| `org/opentest4j/opentest4j/1.2.0/opentest4j-1.2.0.jar` | `58812de60898d976fb81ef3b62da05c6604c18fd4a249f5044282479fc286af2` | 7653 |
| `org/pitest/pitest-command-line/1.15.2/pitest-command-line-1.15.2.jar` | `1b1d66ae14ffc162625c7c49cc4c55f9cebce49083239648ed2139b41570e5b3` | 741431 |
| `org/pitest/pitest-entry/1.15.2/pitest-entry-1.15.2.jar` | `ebcfcd29387a8c60a965a484482995330fd57a4fa9831f3b7553eb93578e2b0d` | 751223 |
| `org/pitest/pitest-junit5-plugin/1.2.2/pitest-junit5-plugin-1.2.2.jar` | `2dbf5bbbc714ff702eb2e82c047a5b44a74c47cc9171c3a7a8dc78783bf099b9` | 12724 |
| `org/pitest/pitest/1.15.2/pitest-1.15.2.jar` | `29befcf6733680375aff5089ad02dab9166aa18760f82fc085adb6c4959362b6` | 611950 |

### Plugins e goals Maven executados

| Plugin | Versão | Goal |
| --- | --- | --- |
| animal-sniffer | 1.18 | check |
| antrun | 1.8 | run |
| apache-rat | 0.13 | check |
| build-helper | 3.0.0 | parse-version |
| buildnumber | 1.4 | create |
| bundle | 4.2.1 | manifest |
| clean | 3.1.0 | clean |
| compiler | 3.8.1 | compile |
| compiler | 3.8.1 | testCompile |
| dependency | 3.6.1 | build-classpath |
| dependency | 3.6.1 | copy |
| dependency | 3.6.1 | list |
| enforcer | 3.0.0-M2 | enforce |
| help | 3.5.1 | effective-pom |
| remote-resources | 1.5 | process |
| resources | 3.1.0 | resources |
| resources | 3.1.0 | testResources |
| surefire | 2.22.2 | test |

## Comandos e parâmetros específicos de cada avaliação

O comando de teste prescrito para a geração era `mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test`. Seu resultado suplementar histórico na condição JSON foi de 10 casos aprovados; seu resultado inicial na condição código-fonte Java foi de 20 casos aprovados. Esta avaliação não gerou novamente nenhuma das suítes.

A seguir estão os comandos efetivamente reservados para as medições selecionadas, executados a partir de `D:/Projects/wit-up`. Cada script de fase, suas atribuições de ambiente e todos os comandos nativos estão reproduzidos no relatório de avaliação vinculado. Os comandos comuns e os caminhos resolvidos de cada fase aparecem abaixo, sem deixar a descoberta dos parâmetros a cargo do leitor.

| Condição | Fase | Comando reservado |
| --- | --- | --- |
| WIT-UP JSON | preflight | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/preflight.ps1"` |
| WIT-UP JSON | jacoco-before | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/jacoco-before.ps1"` |
| WIT-UP JSON | pit-before | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/pit-before.ps1"` |
| WIT-UP JSON | jacoco-after | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/jacoco-after.ps1"` |
| WIT-UP JSON | pit-after | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/pit-after.ps1"` |
| Código-fonte Java | preflight | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/preflight.ps1"` |
| Código-fonte Java | jacoco-before | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/jacoco-before.ps1"` |
| Código-fonte Java | pit-before | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/pit-before.ps1"` |
| Código-fonte Java | jacoco-after | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/jacoco-after.ps1"` |
| Código-fonte Java | pit-after | `pwsh -NoProfile -File "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/pit-after.ps1"` |

| Condição | Fase | Reserva (UTC) | Registro (UTC) |
| --- | --- | --- | --- |
| WIT-UP JSON | preflight | 2026-10-13T01:01:41.056505+00:00 | 2026-10-13T01:02:14.353446+00:00 |
| WIT-UP JSON | jacoco-before | 2026-10-13T01:03:04.753039+00:00 | 2026-10-13T01:06:16.599848+00:00 |
| WIT-UP JSON | pit-before | 2026-10-13T01:07:46.362553+00:00 | 2026-10-13T01:08:28.060212+00:00 |
| WIT-UP JSON | jacoco-after | 2026-10-13T01:08:52.120850+00:00 | 2026-10-13T01:11:44.532157+00:00 |
| WIT-UP JSON | pit-after | 2026-10-13T01:12:36.601361+00:00 | 2026-10-13T01:13:18.307792+00:00 |
| Código-fonte Java | preflight | 2026-10-12T23:45:12.858575+00:00 | 2026-10-12T23:45:29.019738+00:00 |
| Código-fonte Java | jacoco-before | 2026-10-12T23:46:20.082759+00:00 | 2026-10-12T23:49:09.297710+00:00 |
| Código-fonte Java | pit-before | 2026-10-12T23:49:25.149708+00:00 | 2026-10-12T23:50:06.158356+00:00 |
| Código-fonte Java | jacoco-after | 2026-10-12T23:51:06.761782+00:00 | 2026-10-12T23:53:58.618563+00:00 |
| Código-fonte Java | pit-after | 2026-10-12T23:54:19.521526+00:00 | 2026-10-12T23:55:01.261218+00:00 |

### WIT-UP JSON: substituições exatas

```json
{
  "evaluationRoot": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001",
  "workingDirectory": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001",
  "javaHome": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1",
  "agentJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.agent-0.8.4-runtime.jar",
  "cliJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.cli-0.8.4-nodeps.jar",
  "phases": {
    "jacoco-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/jacoco-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/jacoco-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-before/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-before/jacoco.exec"
      }
    },
    "pit-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/pit-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/pit-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-before/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-before/linecoverage.xml"
      },
      "phaseClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-before-classpath.txt",
      "toolClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt"
    },
    "jacoco-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/jacoco-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/jacoco-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-after/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/jacoco-after/jacoco.exec"
      }
    },
    "pit-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/pit-build/pit-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/pit-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-after/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/measurements/pit-after/linecoverage.xml"
      },
      "phaseClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-after-classpath.txt",
      "toolClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt"
    },
    "preflight": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/evidence/scripts/preflight.ps1",
      "scope": "Fetch and verify pinned JaCoCo tools; preserve effective POM and exact resolved project dependencies; no test execution",
      "reports": null,
      "artifacts": {
        "effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/effective-pom.xml",
        "dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependencies.txt",
        "dependency-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependency-hashes.json",
        "launcher-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt",
        "project-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/project-classpath.txt",
        "launcher-effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-effective-pom.xml",
        "launcher-dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-dependencies.txt",
        "runtime-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/runtime-hashes.json",
        "before-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-before-classpath.txt",
        "after-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-after-classpath.txt"
      }
    }
  },
  "pitLauncherPom": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml"
}
```

### WIT-UP JSON: ambiente de preparação observado

```json
{
  "observedAt": "2026-10-13T01:00:45.7609866Z",
  "java": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\bin\\java.exe",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "openjdk version \"1.8.0_504\"",
      "OpenJDK Runtime Environment (Temurin)(build 1.8.0_504-b01)",
      "OpenJDK 64-Bit Server VM (Temurin)(build 25.504-b01, mixed mode)"
    ]
  },
  "javac": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\bin\\javac.exe",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "javac 1.8.0_504"
    ]
  },
  "maven": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16\\bin\\mvn.cmd",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "Apache Maven 3.9.16 (2bdd9fddda4b155ebf8000e807eb73fd829a51d5)",
      "Maven home: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16",
      "Java version: 1.8.0_504, vendor: Temurin, runtime: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\jre",
      "Default locale: en_US, platform encoding: Cp1252",
      "OS name: \"windows 11\", version: \"10.0\", arch: \"amd64\", family: \"windows\""
    ]
  },
  "python": {
    "executable": "D:\\Projects\\wit-up\\.venv\\Scripts\\python.exe",
    "arguments": [
      "--version"
    ],
    "exitCode": 0,
    "output": [
      "Python 3.13.15"
    ]
  },
  "os": {
    "description": "Microsoft Windows 10.0.26300",
    "version": "Microsoft Windows NT 10.0.26300.0",
    "architecture": "X64",
    "powershell": "7.6.5"
  },
  "processEnvironment": {
    "JAVA_HOME": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1",
    "PATH": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16\\bin;D:\\Projects\\wit-up\\.venv\\Scripts;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-25.0.4+101.0.LTS\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16/bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\node\\22.23.2;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\Scripts;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\uv\\0.12.23;C:\\Users\\edyko\\AppData\\Local\\mise\\shims;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\.codex\\tmp\\arg0\\codex-arg0pgGc3k;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\libheif\\libheif\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\jxrlib\\jxrlib\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\poppler\\Library\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\override;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA App\\NvDLISR;C:\\Program Files\\dotnet\\;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\platform-tools;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\emulator;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\cmdline-tools\\latest\\bin;C:\\Program Files\\GitHub CLI\\;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\cmd;C:\\Users\\edyko\\AppData\\Local\\codegraph\\current\\bin;C:\\Users\\edyko\\AppData\\Local\\Programs\\OpenAI\\Codex\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\edyko\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files\\JetBrains\\PyCharm 2026.2.1\\bin;C:\\Program Files\\JetBrains\\IntelliJ IDEA 2026.2.1\\bin;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WinGet\\Packages\\jdx.mise_Microsoft.Winget.Source_8wekyb3d8bbwe\\mise\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\fallback;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\node\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\git\\cmd;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\9a7ba4b9ea0c44a3;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\2e5e00daee91c61d",
    "MAVEN_OPTS": "-DargLine=",
    "MAVEN_ARGS": null,
    "TEMP": "D:\\Projects\\experiment-workspaces\\peekable-input-stream\\.preparation\\json-001-evaluation-001\\temp",
    "TMP": "D:\\Projects\\experiment-workspaces\\peekable-input-stream\\.preparation\\json-001-evaluation-001\\temp",
    "JAVA_TOOL_OPTIONS": null,
    "JDK_JAVA_OPTIONS": null,
    "_JAVA_OPTIONS": null
  },
  "generator": {
    "model": null,
    "settings": null,
    "applicationBuild": null,
    "reason": "This is an evaluation of preserved test bytes, not a generation. Original generation settings remain unknown in the parent record."
  }
}
```

### Código-fonte Java: substituições exatas

```json
{
  "evaluationRoot": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005",
  "workingDirectory": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005",
  "javaHome": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1",
  "agentJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools/org.jacoco.agent-0.8.4-runtime.jar",
  "cliJar": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools/org.jacoco.cli-0.8.4-nodeps.jar",
  "phases": {
    "jacoco-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/pit-build/jacoco-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/jacoco-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-before/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-before/jacoco.exec"
      }
    },
    "pit-before": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-before",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/pit-build/pit-before",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/pit-before.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-before/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-before/linecoverage.xml"
      },
      "phaseClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-before-classpath.txt",
      "toolClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt"
    },
    "jacoco-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/pit-build/jacoco-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/jacoco-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/surefire-reports",
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "jacoco-xml": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-after/jacoco.xml",
        "jacoco-exec": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/jacoco-after/jacoco.exec"
      }
    },
    "pit-after": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005",
      "output": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-after",
      "build": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/pit-build/pit-after",
      "temp": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/temp",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/pit-after.ps1",
      "scope": "Full existing project suite; frozen generated test present only after; target production class only",
      "reports": null,
      "artifacts": {
        "production-class": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class",
        "pit-mutations": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-after/mutations.xml",
        "pit-linecoverage": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/measurements/pit-after/linecoverage.xml"
      },
      "phaseClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-after-classpath.txt",
      "toolClasspathFile": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt"
    },
    "preflight": {
      "checkout": "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005",
      "script": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/evidence/scripts/preflight.ps1",
      "scope": "Fetch and verify pinned JaCoCo tools; preserve effective POM and exact resolved project dependencies; no test execution",
      "reports": null,
      "artifacts": {
        "effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/effective-pom.xml",
        "dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependencies.txt",
        "dependency-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependency-hashes.json",
        "launcher-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt",
        "project-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/project-classpath.txt",
        "launcher-effective-pom": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/launcher-effective-pom.xml",
        "launcher-dependencies": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/launcher-dependencies.txt",
        "runtime-hashes": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/runtime-hashes.json",
        "before-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-before-classpath.txt",
        "after-classpath": "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-after-classpath.txt"
      }
    }
  },
  "pitLauncherPom": "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml"
}
```

### Código-fonte Java: ambiente de preparação observado

```json
{
  "observedAt": "2026-10-12T23:44:07.8430530Z",
  "java": {
    "executable": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1/bin\\java.exe",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "openjdk version \"1.8.0_504\"",
      "OpenJDK Runtime Environment (Temurin)(build 1.8.0_504-b01)",
      "OpenJDK 64-Bit Server VM (Temurin)(build 25.504-b01, mixed mode)"
    ]
  },
  "javac": {
    "executable": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1/bin\\javac.exe",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "javac 1.8.0_504"
    ]
  },
  "maven": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16/bin\\mvn.cmd",
    "arguments": [
      "-version"
    ],
    "exitCode": 0,
    "output": [
      "Apache Maven 3.9.16 (2bdd9fddda4b155ebf8000e807eb73fd829a51d5)",
      "Maven home: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16",
      "Java version: 1.8.0_504, vendor: Temurin, runtime: C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-8.0.504+1\\jre",
      "Default locale: en_US, platform encoding: Cp1252",
      "OS name: \"windows 11\", version: \"10.0\", arch: \"amd64\", family: \"windows\""
    ]
  },
  "python": {
    "executable": "C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\python.exe",
    "arguments": [
      "--version"
    ],
    "exitCode": 0,
    "output": [
      "Python 3.13.15"
    ]
  },
  "os": {
    "description": "Microsoft Windows 10.0.26300",
    "version": "Microsoft Windows NT 10.0.26300.0",
    "architecture": "X64",
    "powershell": "7.6.5"
  },
  "processEnvironment": {
    "JAVA_HOME": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1",
    "PATH": "C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1/bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\java\\temurin-25.0.4+101.0.LTS\\bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\maven\\3.9.16\\apache-maven-3.9.16/bin;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\node\\22.23.2;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\python\\3.13.15\\Scripts;C:\\Users\\edyko\\AppData\\Local\\mise\\installs\\uv\\0.12.23;C:\\Users\\edyko\\AppData\\Local\\mise\\shims;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\.codex\\tmp\\arg0\\codex-arg0pgGc3k;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\libheif\\libheif\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\jxrlib\\jxrlib\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\poppler\\Library\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\override;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Program Files (x86)\\NVIDIA Corporation\\PhysX\\Common;C:\\Program Files\\NVIDIA Corporation\\NVIDIA App\\NvDLISR;C:\\Program Files\\dotnet\\;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\platform-tools;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\emulator;C:\\Users\\edyko\\AppData\\Local\\Android\\Sdk\\cmdline-tools\\latest\\bin;C:\\Program Files\\GitHub CLI\\;C:\\Program Files\\Docker\\Docker\\resources\\bin;C:\\Program Files\\Git\\cmd;C:\\Users\\edyko\\AppData\\Local\\codegraph\\current\\bin;C:\\Users\\edyko\\AppData\\Local\\Programs\\OpenAI\\Codex\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\powershell;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\edyko\\AppData\\Local\\Programs\\Microsoft VS Code\\bin;C:\\Program Files\\JetBrains\\PyCharm 2026.2.1\\bin;C:\\Program Files\\JetBrains\\IntelliJ IDEA 2026.2.1\\bin;C:\\Users\\edyko\\AppData\\Local\\Microsoft\\WinGet\\Packages\\jdx.mise_Microsoft.Winget.Source_8wekyb3d8bbwe\\mise\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\bin\\fallback;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\node\\bin;C:\\Users\\edyko\\.cache\\codex-runtimes\\codex-primary-runtime\\dependencies\\native\\git\\cmd;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\9a7ba4b9ea0c44a3;C:\\Users\\edyko\\AppData\\Local\\OpenAI\\Codex\\bin\\2e5e00daee91c61d",
    "MAVEN_OPTS": "-DargLine=",
    "MAVEN_ARGS": "-Dmaven.repo.local=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/maven-repository",
    "TEMP": "D:/Projects/experiment-workspaces/peekable-input-stream/.preparation/java-source-001-evaluation-005/temp",
    "TMP": "D:/Projects/experiment-workspaces/peekable-input-stream/.preparation/java-source-001-evaluation-005/temp",
    "JAVA_TOOL_OPTIONS": null,
    "JDK_JAVA_OPTIONS": null,
    "_JAVA_OPTIONS": null
  },
  "generator": {
    "model": null,
    "settings": null,
    "applicationBuild": null,
    "reason": "This is an evaluation of preserved test bytes, not a generation. Original generation settings remain unknown in the parent record."
  }
}
```

### Comandos comuns às fases

As variáveis abaixo são resolvidas diretamente a partir do mapa de substituições de cada avaliação: `$workingDirectory`, `$agentJar` e `$cliJar` são campos de nível superior; `$phaseCheckout`, `$phaseOutput` e `$temporaryDirectory` correspondem aos campos `checkout`, `output` e `temp` daquela fase; `$phaseClasspathFile` e `$toolClasspathFile` correspondem aos campos da fase PIT. Os comandos completos de preflight estão preservados em cada relatório de avaliação e nos scripts com hashes registrados.

```powershell
$env:JAVA_HOME = 'C:/Users/edyko/AppData/Local/mise/installs/java/temurin-8.0.504+1'
$env:PATH = "$env:JAVA_HOME/bin;$env:PATH"
$env:TEMP = "$workingDirectory/temp"
$env:TMP = $env:TEMP
$env:MAVEN_ARGS = "-Dmaven.repo.local=$workingDirectory/maven-repository"
Set-Location -LiteralPath $phaseCheckout
$executionData = "$phaseOutput/jacoco.exec"
$coverageXml = "$phaseOutput/jacoco.xml"
$env:MAVEN_OPTS = "-DargLine=-javaagent:$agentJar=destfile=$executionData,append=true,includes=org.apache.commons.io.input.buffer.PeekableInputStream"
mvn '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' clean test
$classFile = "$phaseCheckout/target/classes/org/apache/commons/io/input/buffer/PeekableInputStream.class"
java -jar $cliJar report $executionData --classfiles $classFile --xml $coverageXml --name 'PeekableInputStream paired measurement'
```

Os scripts efetivamente executados verificam e registram imediatamente o exit code de cada processo, recusam a reutilização de diretórios de saída e interrompem a execução após um comando que falhou. `begin` reserva a invocação antes da execução, e `record` captura os logs e os artefatos nativos depois.

```powershell
Set-Location -LiteralPath $phaseCheckout
$env:MAVEN_OPTS = '-DargLine='
$toolClasspath = (Get-Content -LiteralPath $toolClasspathFile -Raw).Trim()
java "-Djava.io.tmpdir=$temporaryDirectory" -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport --reportDir $phaseOutput --targetClasses org.apache.commons.io.input.buffer.PeekableInputStream --targetTests 'org.apache.commons.io.*' --sourceDirs "$phaseCheckout/src/main/java" --classPathFile $phaseClasspathFile --includeLaunchClasspath false --mutationEngine gregor --mutators DEFAULTS --threads 1 --timeoutFactor 1.25 --timeoutConst 3000 --jvmArgs "-Xmx256m,-Djava.io.tmpdir=$temporaryDirectory" --outputFormats XML --timestampedReports false --exportLineCoverage true --failWhenNoMutations true --skipFailingTests false --projectBase $phaseCheckout --inputEncoding UTF-8 --outputEncoding UTF-8
```

A CLI com versão fixada é executada a partir do diretório real do checkout, de modo que os fixtures existentes com recursos relativos tenham o mesmo diretório de trabalho usado pelo Surefire. Isso resolve o problema registrado de diretório de execução do POM auxiliar sem reduzir a seleção de testes nem ignorar casos que falharam. Consulte a [documentação oficial da CLI](https://pitest.org/quickstart/commandline/); a ajuda local da CLI com versão fixada e os logs das invocações reais estabelecem quais opções foram usadas neste caso.

## Navegação pelas evidências

- WIT-UP JSON: [relatório da geração](../runs/json/001/evidence/peekable-input-stream-report.md), [relatório da avaliação selecionada](../supplements/json/001/001/report.md), [execuções nativas](../supplements/json/001/001/executions/), [selo da avaliação](../supplements/json/001/001/seal.json).
- Código-fonte Java: [relatório da geração](../runs/java-source/001/report.md), [relatório da avaliação selecionada](../supplements/java-source/001/005/report.md), [execuções nativas](../supplements/java-source/001/005/executions/), [selo da avaliação](../supplements/java-source/001/005/seal.json).
- [Diagnósticos originais de execução da condição JSON](../runs/json/001/evidence/execution-diagnostics.md).
- [Registro das avaliações seladas e das tentativas malsucedidas preservadas](../README.md).

### WIT-UP JSON: comandos completos de preparação

O wrapper da invocação seleciona o ambiente de processo registrado antes de executar estes comandos. Os registros da reserva e da captura dos artefatos nativos estão vinculados acima.

```powershell
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001'
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.agent:0.8.4:jar:runtime' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.cli:0.8.4:jar:nodeps' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$expectedTools = @{ 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.agent-0.8.4-runtime.jar'='1a7c1dc7280e535b9b6f383915bac5afbb9208c1af2019b4e674ca590c925c22'; 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/tools/org.jacoco.cli-0.8.4-nodeps.jar'='65de07ff32bcf2f945f18180d1d10cdf0e155eee2b508519bbc5f31904cd8288' }
foreach ($toolPath in $expectedTools.Keys) {
    $actualHash = (Get-FileHash -LiteralPath $toolPath -Algorithm SHA256).Hash.ToLowerInvariant()
    Write-Output "$actualHash  $toolPath"
    if ($actualHash -ne $expectedTools[$toolPath]) { throw 'Measurement tool checksum mismatch.' }
}
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$dependencyHashes = @()
foreach ($dependencyLine in Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependencies.txt') {
    $dependencyParts = $dependencyLine.Trim() -split ':', 6
    if ($dependencyParts.Count -eq 6) {
        $artifactPath = $dependencyParts[5]
        if (!(Test-Path -LiteralPath $artifactPath -PathType Leaf)) { throw "A resolved dependency is missing: $artifactPath" }
        $dependencyHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
    }
}
if ($dependencyHashes.Count -eq 0) { throw 'No resolved dependency artifacts were captured.' }
$dependencyHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/dependency-hashes.json' -Encoding utf8
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-DincludeScope=test' '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/project-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/json/001/001/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/launcher-dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$toolClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/tool-classpath.txt' -Raw).Trim()
$projectClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/project-classpath.txt' -Raw).Trim()
java -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport -h
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$runtimeArtifacts = @($projectClasspath -split ';') + @($toolClasspath -split ';')
$runtimeHashes = @()
foreach ($artifactPath in @($runtimeArtifacts | Select-Object -Unique)) {
    $runtimeHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
}
$runtimeHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/runtime-hashes.json' -Encoding utf8
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/before-checkout/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-before-classpath.txt' -Encoding utf8NoBOM
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/json-001-evaluation-001/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/json-001-evaluation-001/preflight/pit-after-classpath.txt' -Encoding utf8NoBOM
exit 0
```

### WIT-UP JSON: versões das ferramentas de preservação e de geração do relatório

```json
{
  "uv": [
    "uv 0.12.23 (46b84fd0b 2026-10-03 x86_64-pc-windows-msvc)"
  ],
  "git": [
    "git version 2.56.0.windows.2"
  ],
  "ruff": [
    "ruff 0.16.10"
  ],
  "pyright": [
    "pyright 1.1.414"
  ]
}
```

### Código-fonte Java: comandos completos de preparação

O wrapper da invocação seleciona o ambiente de processo registrado antes de executar estes comandos. Os registros da reserva e da captura dos artefatos nativos estão vinculados acima.

```powershell
$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005'
$env:MAVEN_OPTS = '-DargLine='
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.agent:0.8.4:jar:runtime' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:copy '-Dartifact=org.jacoco:org.jacoco.cli:0.8.4:jar:nodeps' '-DoutputDirectory=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$expectedTools = @{ 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools/org.jacoco.agent-0.8.4-runtime.jar'='1a7c1dc7280e535b9b6f383915bac5afbb9208c1af2019b4e674ca590c925c22'; 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/tools/org.jacoco.cli-0.8.4-nodeps.jar'='65de07ff32bcf2f945f18180d1d10cdf0e155eee2b508519bbc5f31904cd8288' }
foreach ($toolPath in $expectedTools.Keys) {
    $actualHash = (Get-FileHash -LiteralPath $toolPath -Algorithm SHA256).Hash.ToLowerInvariant()
    Write-Output "$actualHash  $toolPath"
    if ($actualHash -ne $expectedTools[$toolPath]) { throw 'Measurement tool checksum mismatch.' }
}
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$dependencyHashes = @()
foreach ($dependencyLine in Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependencies.txt') {
    $dependencyParts = $dependencyLine.Trim() -split ':', 6
    if ($dependencyParts.Count -eq 6) {
        $artifactPath = $dependencyParts[5]
        if (!(Test-Path -LiteralPath $artifactPath -PathType Leaf)) { throw "A resolved dependency is missing: $artifactPath" }
        $dependencyHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
    }
}
if ($dependencyHashes.Count -eq 0) { throw 'No resolved dependency artifacts were captured.' }
$dependencyHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/dependency-hashes.json' -Encoding utf8
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp '-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:build-classpath '-DincludeScope=test' '-Dmdep.outputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/project-classpath.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-help-plugin:3.5.1:effective-pom '-Doutput=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/launcher-effective-pom.xml'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
mvn -B -ntp -f 'D:/Projects/wit-up/commons-io-validation/peekable-input-stream/supplements/java-source/001/005/inputs/pit-cli-pom.xml' org.apache.maven.plugins:maven-dependency-plugin:3.6.1:list '-DoutputAbsoluteArtifactFilename=true' '-DoutputFile=D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/launcher-dependencies.txt'
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$toolClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/tool-classpath.txt' -Raw).Trim()
$projectClasspath = (Get-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/project-classpath.txt' -Raw).Trim()
java -cp $toolClasspath org.pitest.mutationtest.commandline.MutationCoverageReport -h
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$runtimeArtifacts = @($projectClasspath -split ';') + @($toolClasspath -split ';')
$runtimeHashes = @()
foreach ($artifactPath in @($runtimeArtifacts | Select-Object -Unique)) {
    $runtimeHashes += [ordered]@{ path=$artifactPath; sha256=(Get-FileHash -LiteralPath $artifactPath -Algorithm SHA256).Hash.ToLowerInvariant(); bytes=(Get-Item -LiteralPath $artifactPath).Length }
}
$runtimeHashes | ConvertTo-Json -Depth 3 | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/runtime-hashes.json' -Encoding utf8
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/before-checkout/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-before-classpath.txt' -Encoding utf8NoBOM
$phaseClasspath = @('D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/classes', 'D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001-evaluation-005/target/test-classes') + $runtimeArtifacts
$phaseClasspath | Select-Object -Unique | Set-Content -LiteralPath 'D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001-evaluation-005/preflight/pit-after-classpath.txt' -Encoding utf8NoBOM
exit 0
```

### Código-fonte Java: versões das ferramentas de preservação e de geração do relatório

```json
{
  "git": {
    "command": "git --version",
    "output": [
      "git version 2.56.0.windows.2"
    ],
    "exitCode": 0
  },
  "uv": {
    "command": "uv --version",
    "output": [
      "uv 0.12.23 (46b84fd0b 2026-10-03 x86_64-pc-windows-msvc)"
    ],
    "exitCode": 0
  },
  "ruff": {
    "command": "uv run --frozen ruff --version",
    "output": [
      "ruff 0.16.10"
    ],
    "exitCode": 0
  },
  "pyright": {
    "command": "uv run --frozen pyright --version",
    "output": [
      "pyright 1.1.414"
    ],
    "exitCode": 0
  }
}
```

## Apêndice A: Código Java completo e congelado da condição JSON

```java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.commons.io.input.buffer;

import static org.junit.jupiter.api.Assertions.assertThrows;

import java.io.ByteArrayInputStream;
import java.io.InputStream;

import org.junit.jupiter.api.Test;

public class PeekableInputStreamTest {

    @Test
    public void testConstructorRejectsZeroBufferSize() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final int bufferSize = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> new PeekableInputStream(input, bufferSize));
    }

    @Test
    public void testPeekArrayRejectsNullBuffer() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = null;

        // Act and Assert
        assertThrows(NullPointerException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekArrayRejectsBufferLargerThanCapacity() {
        // Arrange
        // Assume the constructor size becomes the receiver's buffer size.
        // Change modeled capacity 0 to 1 and array length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekArrayRejectsEmptyBuffer() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate));
    }

    @Test
    public void testPeekSliceRejectsNullBuffer() {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = null;
        final int offset = 0;
        final int length = 0;

        // Act and Assert
        assertThrows(NullPointerException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsBufferLargerThanCapacity() {
        // Arrange
        // Assume the constructor size becomes the receiver's buffer size.
        // Change modeled capacity 0 to 1 and array length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[2];
        final int offset = 0;
        final int length = 1;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsOffsetAtEmptyBufferEnd() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];
        final int offset = 0;
        final int length = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsNegativeOffset() {
        // Arrange
        // Assume size 1 creates a non-null, empty buffer. Modeled receiver size 0 becomes 1.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[0];
        final int offset = -1;
        final int length = 0;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsNegativeLength() {
        // Arrange
        // Assume size 1 creates a non-null buffer with an initial byte count of 0.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[1];
        final int offset = 0;
        final int length = -1;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }

    @Test
    public void testPeekSliceRejectsLengthLargerThanCapacity() {
        // Arrange
        // Assume size 1 creates a non-null buffer of capacity 1 with an initial byte count of 0.
        // Change modeled internal capacity 0 to 1 and requested length 1 to 2, preserving length > capacity.
        final InputStream input = new ByteArrayInputStream(new byte[0]);
        final PeekableInputStream stream = new PeekableInputStream(input, 1);
        final byte[] candidate = new byte[1];
        final int offset = 0;
        final int length = 2;

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(candidate, offset, length));
    }
}
```

## Apêndice B: Código Java completo e congelado da condição código-fonte Java

```java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.commons.io.input.buffer;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertSame;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;

/**
 * Exception tests for the declared constructors and peek overloads.
 * Fixtures use only memory streams and require no external resources.
 */
public class PeekableInputStreamTest {

    /** Tests null input validation in the default-size constructor. */
    @Test
    public void defaultConstructorRejectsNullInput() {
        // Arrange
        final InputStream input = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> new PeekableInputStream(input));
        assertEquals("InputStream", exception.getMessage());
    }

    /** Tests that null input validation precedes invalid buffer-size validation. */
    @Test
    public void sizedConstructorRejectsNullInputBeforeInvalidBufferSize() {
        // Arrange
        final InputStream input = null;
        final int bufferSize = 0;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> new PeekableInputStream(input, bufferSize));
        assertEquals("InputStream", exception.getMessage());
    }

    /**
     * Tests both the zero boundary and the negative side of the size guard.
     * @param bufferSize the nonpositive internal buffer size
     */
    @ParameterizedTest
    @ValueSource(ints = {0, -1})
    public void sizedConstructorRejectsNonpositiveBufferSize(final int bufferSize) {
        // Arrange
        final InputStream input = new ByteArrayInputStream(new byte[0]);

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> new PeekableInputStream(input, bufferSize));
        assertEquals("Invalid buffer size: " + bufferSize, exception.getMessage());
    }

    /** Tests null array validation for the whole-array overload. */
    @Test
    public void peekArrayRejectsNullBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class, () -> stream.peek(requested));
        assertEquals("Buffer", exception.getMessage());
    }

    /** Tests null validation before slice validation. */
    @Test
    public void peekSliceRejectsNullBufferBeforeInvalidSlice() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = null;

        // Act and Assert
        final NullPointerException exception = assertThrows(NullPointerException.class,
                () -> stream.peek(requested, -1, -1));
        assertEquals("Buffer", exception.getMessage());
    }

    /** Tests the whole-array size guard. */
    @Test
    public void peekArrayRejectsArrayLargerThanInternalBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(requested));
    }

    /** Tests that the sliced overload checks the entire array even for an empty slice. */
    @Test
    public void peekSliceRejectsOversizedArrayEvenForZeroLength() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(IllegalArgumentException.class, () -> stream.peek(requested, 0, 0));
    }

    /** Tests the delegated offset guard for an empty whole array. */
    @Test
    public void peekArrayRejectsEmptyArrayAtDelegatedOffsetGuard() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[0];

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> stream.peek(requested));
        assertEquals("Invalid offset: 0", exception.getMessage());
    }

    /** Tests the delegated offset guard for an empty sliced array. */
    @Test
    public void peekSliceRejectsEmptyArrayAtDelegatedOffsetGuard() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[0]), 1);
        final byte[] requested = new byte[0];

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, 0));
        assertEquals("Invalid offset: 0", exception.getMessage());
    }

    /**
     * Tests both sides of offset validation before negative-length validation.
     * @param offset the negative offset or the array-length boundary
     */
    @ParameterizedTest
    @ValueSource(ints = {-1, 1})
    public void peekSliceRejectsInvalidOffsetBeforeInvalidLength(final int offset) {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, offset, -1));
        assertEquals("Invalid offset: " + offset, exception.getMessage());
    }

    /** Tests negative-length validation after a valid offset. */
    @Test
    public void peekSliceRejectsNegativeLength() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, -1));
        assertEquals("Invalid length: -1", exception.getMessage());
    }

    /** Tests the delegated length guard against internal capacity. */
    @Test
    public void peekSliceRejectsLengthLargerThanInternalBuffer() {
        // Arrange
        final PeekableInputStream stream = new PeekableInputStream(new ByteArrayInputStream(new byte[] {0}), 1);
        final byte[] requested = new byte[] {0};

        // Act and Assert
        final IllegalArgumentException exception = assertThrows(IllegalArgumentException.class,
                () -> stream.peek(requested, 0, 2));
        assertEquals("Invalid length: 2", exception.getMessage());
    }

    /**
     * Tests original read-failure propagation immediately and after one byte is buffered.
     * @param prefixLength the number of successful one-byte reads before failure
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 1})
    public void peekArrayPropagatesReadFailureDuringRefill(final int prefixLength) {
        // Arrange
        final IOException failure = new IOException("Fixture read failure");
        final InputStream input = new PrefixThenFailInputStream(prefixLength, failure);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        final IOException exception = assertThrows(IOException.class, () -> stream.peek(requested));
        assertSame(failure, exception);
    }

    /**
     * Tests that read failures precede delegated offset and length validation.
     * @param prefixLength the number of successful one-byte reads before failure
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 1})
    public void peekSlicePropagatesReadFailureBeforeInvalidSlice(final int prefixLength) {
        // Arrange
        final IOException failure = new IOException("Fixture read failure");
        final InputStream input = new PrefixThenFailInputStream(prefixLength, failure);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        final IOException exception = assertThrows(IOException.class, () -> stream.peek(requested, -1, -1));
        assertSame(failure, exception);
    }

    /**
     * Tests slice-array overrun after a matching prefix, with an empty or full internal buffer.
     * @param inputLength zero for immediate end of input, or two for a full buffer
     */
    @ParameterizedTest
    @ValueSource(ints = {0, 2})
    public void peekSlicePropagatesArrayBoundsFailureAfterMatchingPrefix(final int inputLength) {
        // Arrange
        // Zero-filled input and request arrays prevent an earlier comparison mismatch.
        // With empty input, the internal array also retains its initial zero values.
        final InputStream input = new ByteArrayInputStream(new byte[inputLength]);
        final PeekableInputStream stream = new PeekableInputStream(input, 2);
        final byte[] requested = new byte[2];

        // Act and Assert
        assertThrows(ArrayIndexOutOfBoundsException.class, () -> stream.peek(requested, 1, 2));
    }

    /** Supplies a small zero-byte prefix followed by the same checked read failure. */
    private static final class PrefixThenFailInputStream extends InputStream {
        private int remainingBytes;
        private final IOException failure;

        private PrefixThenFailInputStream(final int prefixLength, final IOException failure) {
            remainingBytes = prefixLength;
            this.failure = failure;
        }

        @Override
        public int read() throws IOException {
            if (remainingBytes > 0) {
                remainingBytes--;
                return 0;
            }
            throw failure;
        }

        @Override
        public int read(final byte[] bytes, final int offset, final int length) throws IOException {
            final int value = read();
            bytes[offset] = (byte) value;
            return 1;
        }
    }
}
```

## Prompt de geração preservado: WIT-UP JSON

Esta é a instrução original de geração, preservada como evidência de proveniência, e não como uma nova solicitação de execução.

```text
Use this prompt in a fresh chat for one independent generation attempt.
Work in "D:/Projects/wit-up/commons-io" using an already prepared checkout.
Run the two source conditions in separate fresh chats and separate prepared
attempts. Do not share generated tests, candidate inventories, or execution
feedback between them.

Before inspecting behavioral material or generating anything, verify that HEAD
is "11f0abe7a3fb6954b2985ca4ab0697b2fb489e84", that all tracked files match
that commit, and that
"src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java"
does not exist. Check existence without opening an earlier test. Use metadata-only
Git checks such as "git rev-parse HEAD", "git status --short", and
"git diff --quiet 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 --".
Do not print source diffs during preflight. If a condition is not met, report
the preparation required and stop. Do not reset the checkout, create or switch
branches, delete files, or modify the baseline to satisfy these checks.

Target production file:
"D:/Projects/wit-up/commons-io/src/main/java/org/apache/commons/io/input/buffer/PeekableInputStream.java".
This path identifies the target; permission to read production source depends
on the designated scenario source below.

Write JUnit tests only for exceptional behavior of the public constructors and
declared peek overloads of "org.apache.commons.io.input.buffer.PeekableInputStream",
in "src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java".
Keep overloaded signatures distinct. Every test case, including each parameterized
invocation, must assert an exception thrown by a target constructor or peek call.
Exceptions propagated from dependencies qualify only through that target call
and when supported by the designated source. Do not test inherited operations
or dependency classes as independent targets. Normal calls may establish fixture
state; do not add cases whose oracle is a successful return value, matching bytes,
normal end of input, or another non-exception outcome. A "throws" declaration
on a test method is not an exception assertion. Do not target a fixed test count.

BEGIN SCENARIO SOURCE
Source kind: WIT-UP JSON exports only.
Source files:
"D:/Projects/wit-up/legacy/commons-io-analysis-results/witup-results-commons-io-11f0abe7a.json"
"D:/Projects/wit-up/legacy/commons-io-analysis-results/witup-summaries-commons-io-11f0abe7a.json"

These two original raw exports are the only permitted inputs under "legacy".
Read them directly; do not use historical extracted records, analysis scripts,
derived datasets, reports, or generated tests as substitutes.

Process the JSON programmatically with an inline, read-only parser. Select
package "org.apache.commons.io.input.buffer", class "PeekableInputStream", and
the target constructors and peek overloads. Join results and summaries on both
"artifact" and "pathId". Preserve full method signatures and source-array
positions. Check key uniqueness and counterpart metadata/status consistency;
do not silently choose among conflicting records. Report unusable records
separately and derive tests only from consistent joined SAT records.

Check the selected artifact label against "commons-io-11f0abe7a.jar".
The label identifies the supplied export; it does not independently verify
the analyzed JAR bytes or the WIT-UP revision that produced it. Report missing
provenance as unverified without claiming source/binary equivalence.

Derive conditions from constraints together with "truthValue"; use "modelValues"
as candidate concrete assignments and the summary's "exceptionType" as the
exception candidate. SAT is not proof that a Java fixture is constructible.
Do not treat every model symbol as a public argument or interpret a serialized
reference identity as a Java scalar. Do not invent missing records or infer
behavior absent from the exports.

Do not read any Commons IO production source, source excerpts, Javadocs,
source-bearing CodeGraph output, bytecode, or decompiled code. Do not use
"git show", source diffs, dependency source JARs, or external implementations
to recover this information. Compilation and test execution may consume
production files mechanically; that does not authorize inspecting them.
END SCENARIO SOURCE

Use the designated source as the sole source of target-specific scenarios,
input conditions, fixture behavior, and expected outcomes. The following rules
are identical for both source conditions.

Read and follow applicable repository instructions and project conventions.
They may supply working rules, licensing, formatting, framework configuration,
and build requirements, but not additional target-specific behavioral oracles.
Use the Java level and JUnit version already configured in the checkout.
Built-in language/framework knowledge may support test syntax and standard
library fixture mechanics; it must not supply additional Commons IO scenarios.

Only Codex built-in skills are permitted. Do not load, invoke, follow, or use
guidance from user-defined, repository-defined, user-installed, or
plugin-provided skills. Do not install or create skills.

You may inspect build configuration and unrelated existing tests solely for
framework, formatting, and project conventions. Do not inspect tests for the
target, its superclasses, or its buffer dependencies. Do not use other tests
as scenario sources. Avoid broad searches that expose prohibited content.

Do not retrieve earlier versions of "PeekableInputStreamTest.java" from the
workspace, Git history, other branches, backups, compiled classes, artifacts,
or previous chats. Do not consult "D:/Projects/wit-up/reference-suite", other
generation prompts, previous attempts, study findings, coverage or mutation
reports, external test examples, or behavioral documentation outside the
designated source. Apart from the explicitly permitted JSON files in the JSON
condition, "legacy" is outside the permitted inputs. Do not consult the
alternative scenario source. Do not reuse or reconstruct a prior gold standard.

If a tool, attachment, or supplied context exposes prohibited behavioral
material, disclose the exposure and stop before generating or revising tests.
Ignoring already exposed material does not establish an independent attempt.

Construct fixtures through accessible APIs without reflection, private-state
mutation, bytecode manipulation, or special production changes. Use small,
deterministic fixtures. A custom dependency stub is allowed only when its
behavior and the target's expected propagation are supported by the designated
source. Do not count an exception thrown directly by a stub as a target test.

Keep fixture setup outside the exception assertion. The asserted executable
must invoke only the intended target constructor or peek call; setup or cleanup
failure must not satisfy the assertion. Assert a specific supported exception
type, rather than Exception or Throwable as a catch-all. Assert exact runtime
type, message, cause, or identity only when the source supports that detail.

Make fixture assumptions explicit. Disclose concrete values changed from the
supporting source, why the change was necessary, and whether the original
conditions still hold. Do not claim reproduction of a particular path when
the fixture does not establish its conditions. Report candidates lacking a
supported fixture or exception oracle instead of inventing behavior or adding
disabled/skipped tests. Avoid redundant tests with the same conditions and
exception outcome, but do not equate distinct paths merely by exception class.
A passing assertion alone is not proof of an exact internal path or of the
implementation's correctness against an independent specification.

Modify only the target test file. Keep production, other tests, dependencies,
and configuration unchanged at the required baseline, even if you discover
an apparent implementation defect. Do not apply any correction or select a
different commit. Report source ambiguities or defects without changing the
experiment. Keep all project files and generated artifacts on D:; do not
create auxiliary tooling files or caches inside the Java checkout.

Include the repository's required license header. Import Java types and use
simple names, except where qualification is necessary to resolve a collision.
Use descriptive behavior-based test names and clear Arrange, Act, and Assert
sections; Act and Assert may be combined for an exception assertion. Write
generated identifiers, comments, and any saved report in United States English.

Complete one initial test suite using only the permitted inputs, then run it
once from "D:/Projects/wit-up/commons-io" with:

mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test

These profile selections keep coverage outside the generation phase; they do
not authorize skipping tests, license checks, or other quality gates.
Record the Java and Maven versions. Preserve the generated file after the
first compilation/execution attempt, including failures. Do not repair tests,
add cases, adjust fixtures, change assertions, or infer new cases from runtime
feedback. Do not perform a second generation attempt in this chat.

Perform additional checks only when repository instructions require them and
report their scope separately. Do not run coverage or mutation analysis.
Do not suppress diagnostics, skip failing tests, or relax quality gates.
If no supported test can be written, report that result; do not create an empty
or disabled suite or report unexecuted tests as passing.

In the final response, report:
- The exact checkout commit, designated source files, toolchain versions,
  and isolation/preflight result. Recheck that tracked baseline files remain
  unchanged and identify the generated target file.
- The exact commands, exit statuses, and executed test counts, including
  failures, errors, and skips. Distinguish a build that stopped before test
  execution from executed tests that failed. State checks not performed.
- For every generated test: target signature, expected exception, fixture
  assumptions, changed source values, and supporting source locator.
  For Java, use file path, signature, and relevant line numbers.
  For JSON, use both "artifact" and "pathId", the overload signature, and the
  zero-based positions in the two input arrays.
- Exception candidates left unrepresented and the reason: inconsistent data,
  insufficient fixture support, missing oracle, or justified redundancy.
  Keep solver verdicts and source-derived candidates separate from observed
  runtime outcomes. Do not label record associations or counts as path coverage.
```

## Prompt de geração preservado: código-fonte Java

Esta é a instrução original de geração, preservada como evidência de proveniência, e não como uma nova solicitação de execução.

```text
Use this prompt in a fresh chat for one independent generation attempt.
Work in "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001" using an already prepared checkout.
Run the two source conditions in separate fresh chats and separate prepared
attempts. Do not share generated tests, candidate inventories, or execution
feedback between them.

Run evidence directory: "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001".
Assigned log/tool/temp directory: "D:/Projects/experiment-workspaces/peekable-input-stream/.working/java-source-001"; do not use another run's files.
Read only the process instructions in "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001/inputs/process/AGENTS.md" and
"D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001/inputs/process/docs/run-methodology.md", your rendered prompt, and your
assigned run metadata. Do not browse the study's other runs or source prompt.
These process instructions do not supply target-specific behavioral oracles.
Keep generated Java names independent of the run identifier.
Before the first compilation or execution, freeze the completed initial suite:
python "D:/Projects/wit-up/tools/experiment_runs.py" freeze --run "D:/Projects/wit-up/commons-io-validation/peekable-input-stream/runs/java-source/001" --fresh-chat-attested
Attest only if this chat has not seen prohibited material. Before the command,
reserve its execution with the methodology's begin operation and an empty native
report destination. Capture both output streams at the returned log path, then
finish with record. Never overwrite earlier execution records. Prepare process-only JDK 8,
MAVEN_OPTS=-DargLine=, and an attempt-specific D: TEMP/TMP before the original
Maven command. Preserve actual tool versions and stdout/stderr. Coverage and
mutation remain outside generation and require separate authorization.

Before inspecting behavioral material or generating anything, verify that HEAD
is "11f0abe7a3fb6954b2985ca4ab0697b2fb489e84", that all tracked files match
that commit, and that
"src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java"
does not exist. Check existence without opening an earlier test. Use metadata-only
Git checks such as "git rev-parse HEAD", "git status --short", and
"git diff --quiet 11f0abe7a3fb6954b2985ca4ab0697b2fb489e84 --".
Do not print source diffs during preflight. If a condition is not met, report
the preparation required and stop. Do not reset the checkout, create or switch
branches, delete files, or modify the baseline to satisfy these checks.

Target production file:
"D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001/src/main/java/org/apache/commons/io/input/buffer/PeekableInputStream.java".
This path identifies the target; permission to read production source depends
on the designated scenario source below.

Write JUnit tests only for exceptional behavior of the public constructors and
declared peek overloads of "org.apache.commons.io.input.buffer.PeekableInputStream",
in "src/test/java/org/apache/commons/io/input/buffer/PeekableInputStreamTest.java".
Keep overloaded signatures distinct. Every test case, including each parameterized
invocation, must assert an exception thrown by a target constructor or peek call.
Exceptions propagated from dependencies qualify only through that target call
and when supported by the designated source. Do not test inherited operations
or dependency classes as independent targets. Normal calls may establish fixture
state; do not add cases whose oracle is a successful return value, matching bytes,
normal end of input, or another non-exception outcome. A "throws" declaration
on a test method is not an exception assertion. Do not target a fixed test count.

BEGIN SCENARIO SOURCE
Source kind: Java production source only.
Source location: "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001/src/main/java".
Start with:
"D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001/src/main/java/org/apache/commons/io/input/buffer/PeekableInputStream.java".

Read the target at the required commit. Follow only constructor delegation,
superclasses, and callees needed to understand its exceptional behavior, using
production files within the designated source location at that same commit.
Embedded comments and Javadocs are part of this input.

Derive candidates from actual guards, implicit exceptions, delegation, and
propagation supported by these files. Keep branch conditions and their polarity,
validation order, and required public fixture state together. A visible throw
site or a declared exception alone does not prove that a public invocation can
reach it with a constructible fixture. Do not invent exceptional behavior when
the permitted code does not establish it.

Do not consult WIT-UP JSON exports, summaries, solver models, derived datasets,
or any material under "D:/Projects/wit-up/legacy". Do not inspect another commit
or apply a later correction to interpret the required source version.
END SCENARIO SOURCE

Use the designated source as the sole source of target-specific scenarios,
input conditions, fixture behavior, and expected outcomes. The following rules
are identical for both source conditions.

Read and follow applicable repository instructions and project conventions.
They may supply working rules, licensing, formatting, framework configuration,
and build requirements, but not additional target-specific behavioral oracles.
Use the Java level and JUnit version already configured in the checkout.
Built-in language/framework knowledge may support test syntax and standard
library fixture mechanics; it must not supply additional Commons IO scenarios.

Only Codex built-in skills are permitted. Do not load, invoke, follow, or use
guidance from user-defined, repository-defined, user-installed, or
plugin-provided skills. Do not install or create skills.

You may inspect build configuration and unrelated existing tests solely for
framework, formatting, and project conventions. Do not inspect tests for the
target, its superclasses, or its buffer dependencies. Do not use other tests
as scenario sources. Avoid broad searches that expose prohibited content.

Do not retrieve earlier versions of "PeekableInputStreamTest.java" from the
workspace, Git history, other branches, backups, compiled classes, artifacts,
or previous chats. Do not consult "D:/Projects/wit-up/reference-suite", other
generation prompts, previous attempts, study findings, coverage or mutation
reports, external test examples, or behavioral documentation outside the
designated source. Apart from the explicitly permitted JSON files in the JSON
condition, "legacy" is outside the permitted inputs. Do not consult the
alternative scenario source. Do not reuse or reconstruct a prior gold standard.

If a tool, attachment, or supplied context exposes prohibited behavioral
material, disclose the exposure and stop before generating or revising tests.
Ignoring already exposed material does not establish an independent attempt.

Construct fixtures through accessible APIs without reflection, private-state
mutation, bytecode manipulation, or special production changes. Use small,
deterministic fixtures. A custom dependency stub is allowed only when its
behavior and the target's expected propagation are supported by the designated
source. Do not count an exception thrown directly by a stub as a target test.

Keep fixture setup outside the exception assertion. The asserted executable
must invoke only the intended target constructor or peek call; setup or cleanup
failure must not satisfy the assertion. Assert a specific supported exception
type, rather than Exception or Throwable as a catch-all. Assert exact runtime
type, message, cause, or identity only when the source supports that detail.

Make fixture assumptions explicit. Disclose concrete values changed from the
supporting source, why the change was necessary, and whether the original
conditions still hold. Do not claim reproduction of a particular path when
the fixture does not establish its conditions. Report candidates lacking a
supported fixture or exception oracle instead of inventing behavior or adding
disabled/skipped tests. Avoid redundant tests with the same conditions and
exception outcome, but do not equate distinct paths merely by exception class.
A passing assertion alone is not proof of an exact internal path or of the
implementation's correctness against an independent specification.

Modify only the target test file. Keep production, other tests, dependencies,
and configuration unchanged at the required baseline, even if you discover
an apparent implementation defect. Do not apply any correction or select a
different commit. Report source ambiguities or defects without changing the
experiment. Keep all project files and generated artifacts on D:; do not
create auxiliary tooling files or caches inside the Java checkout.

Include the repository's required license header. Import Java types and use
simple names, except where qualification is necessary to resolve a collision.
Use descriptive behavior-based test names and clear Arrange, Act, and Assert
sections; Act and Assert may be combined for an exception assertion. Write
generated identifiers, comments, and any saved report in United States English.

Complete one initial test suite using only the permitted inputs, then run it
once from "D:/Projects/experiment-workspaces/peekable-input-stream/java-source-001" with:

mvn "-P!jacoco,!cobertura,!travis-jacoco,!travis-cobertura" "-Dtest=org.apache.commons.io.input.buffer.PeekableInputStreamTest" clean test

These profile selections keep coverage outside the generation phase; they do
not authorize skipping tests, license checks, or other quality gates.
Record the Java and Maven versions. Preserve the generated file after the
first compilation/execution attempt, including failures. Do not repair tests,
add cases, adjust fixtures, change assertions, or infer new cases from runtime
feedback. Do not perform a second generation attempt in this chat.

Perform additional checks only when repository instructions require them and
report their scope separately. Do not run coverage or mutation analysis.
Do not suppress diagnostics, skip failing tests, or relax quality gates.
If no supported test can be written, report that result; do not create an empty
or disabled suite or report unexecuted tests as passing.

In the final response, report:
- The exact checkout commit, designated source files, toolchain versions,
  and isolation/preflight result. Recheck that tracked baseline files remain
  unchanged and identify the generated target file.
- The exact commands, exit statuses, and executed test counts, including
  failures, errors, and skips. Distinguish a build that stopped before test
  execution from executed tests that failed. State checks not performed.
- For every generated test: target signature, expected exception, fixture
  assumptions, changed source values, and supporting source locator.
  For Java, use file path, signature, and relevant line numbers.
  For JSON, use both "artifact" and "pathId", the overload signature, and the
  zero-based positions in the two input arrays.
- Exception candidates left unrepresented and the reason: inconsistent data,
  insufficient fixture support, missing oracle, or justified redundancy.
  Keep solver verdicts and source-derived candidates separate from observed
  runtime outcomes. Do not label record associations or counts as path coverage.
```
