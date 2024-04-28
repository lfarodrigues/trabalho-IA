Alunos: Luis Filipe Antunes Rodrigues(00314848)

Regressão Linear - Dataset Alegrete
Parâmetros 
* b = 0
* w = 0
* alpha = 0.01
* num_iterations = 100

* Erro quadrático médio final = 8.529433040552066

Redes Convolucionais - Datasets MNIST, FASHION MNIST, CIFAR10 e CIFAR100
Observações
1. Complexidade
    Datasets com imagens em tons de cinza e poucas classes como MNIST e FASHION MNIST foram mais fáceis de treinar e
com poucas camadas convolucionais conseguimos bons resultados para os conjuntos de dados de treino e teste.
    Nos datasets com imagens coloridas CIFAR10 e CIFAR100 tivemos maior dificuldade em encontrar uma rede neural que se ajustasse bem ao conjunto de dados, encontrando problemas como overfitting e revanescimento de gradiente, além do tempo de treinamento ser maior. Para contornar esses problemas consultamos técnicas comumente utilizadas para mitigá-los, como o uso de blocos residuais e normalização de batch. Implementamos blocos residuais na criação do modelo para o dataset CIFAR10 e com isso conseguimos reduzir o tempo de convergência da rede e melhorar a acurácia em poucas épocas de treinamento. Decidimos não implementar a técnica no modelo do CIFAR100, percebemos que a rede demora mais a convergir, e que são necessárias mais épocas de treino até que a rede convirja. 
    
2. Acurácia obtida
    * MNIST         0.9515
    * FASHION_MNIST 0.9309  
    * CIFAR10       0.7672
    * CIFAR100      0.3944

    * Observações 
        * Para CIFAR10 consguimos um upgrade de acc = 0.5192 em 50 eps para acc = 0.7672 em 10 eps usando blocos residuais e normalização de batch
    