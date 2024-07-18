**1) Explique, com suas palavras, o que é machine learning?**

O Machine Learning é uma subárea da inteligência artificial que cria algoritmos para que computadores realizem tarefas sem instruções específicas. Em vez de seguir regras fixas, esses programas aprendem a partir de dados para fazer previsões ou tomar decisões. É dividido em 3 tipos principais, sendo eles:
Aprendizado supervisionado: O programa é treinado com exemplos de entradas e saídas conhecidas, como prever o preço de um imóvel com base em suas características.
Aprendizado não supervisionado: O programa é treinado com dados sem rótulos e precisa encontrar padrões escondidos, como agrupar clientes com comportamentos de compra semelhantes.
Aprendizado por reforço: O programa aprende a tomar decisões recebendo incentivos ou penalidades por suas ações, como fazer um algoritmo que joga xadrez.

**2) Explique o conceito de conjunto de treinamento, conjunto de validação e
conjunto de teste em machine learning.**

Conjunto de Treinamento:
Tem a função de treinar o modelo. Contém exemplos rotulados que são usados para ensinar o modelo a identificar padrões. Durante o treinamento, o modelo ajusta seus parâmetros internos (pesos) para minimizar o erro na previsão dos rótulos para esses exemplos.
Conjunto de Validação:
Tem a função de ajustar hiperparâmetros e avaliar a performance do modelo durante o desenvolvimento. É usado para testar o modelo durante o treinamento, mas não para ajustar os pesos diretamente. Serve para ajustar hiperparâmetros, que são configurações do modelo que não são aprendidas a partir dos dados (como a taxa de aprendizado ou a estrutura da rede neural).
Conjunto de Teste:
Tem a função de avaliar a performance final do modelo de forma imparcial. É um conjunto de dados separado que não foi usado durante o treinamento ou validação. É usado para fornecer uma avaliação final e imparcial do desempenho do modelo. Garantia de que os resultados obtidos representam a capacidade do modelo de generalizar para novos dados.

**3) Explique como você lidaria com dados ausentes em um conjunto de dados
de treinamento.**

Há diversas técnicas que podem ser utilizadas para lidar com dados ausentes em conjuntos de dados de treinamento a depender de contexto, caso o dado fosse fundamental para o funcionamento do algoritmo eu procuraria outros conjuntos de dados com as informações necessárias, ou então tentaria prever o valor dos dados ausentes usando métodos estatísticos como a média, moda e mediana dos valores não ausentes.

**4) O que é uma matriz de confusão e como ela é usada para avaliar o
desempenho de um modelo preditivo?**

Uma matriz de confusão é uma ferramenta usada para avaliar o desempenho de um modelo de classificação. Ela fornece uma visão detalhada sobre o desempenho do modelo, mostrando não apenas a taxa de acerto, mas também os erros que o modelo comete. A partir da matriz de confusão, várias métricas podem ser calculadas para avaliar a precisão do modelo.

**5) Em quais áreas (tais como construção civil, agricultura, saúde, manufatura,
entre outras) você acha mais interessante aplicar algoritmos de machine
learning?**

As áreas mais interessantes para a aplicação de machine learning, na minha opinião, são o agronegócio e a saúde. A análise e classificação de imagens na saúde poderia nos levar a conseguir prevenir e identificar diversas doenças, enquanto no agronegócio ajudaria a trazer informações do solo com base em imagens de satélite.
