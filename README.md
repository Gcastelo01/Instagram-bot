# Instagram-bot

<h2>Pré Requisitos</h2>

Para poder fazer o código funcionar, é necessário instalar a biblioteca selenium e o navegador web Firefox.
    
    pip3 install selenium

Além disso, é necessário ter o arquivo texto com todos os comentários que serão feitos separados por ponto-e-vírgula, como no exemplo à seguir:
   
    @Fábio; @Stênio; @Weverton; @RaúlCáceres; @MarcoAntônio;

(No caso o exemplo considera que estamos marcando usuários, mas qualquer coisa colocada entre os ponto-e-vírgula será comentada.)
Se quiséssemos marcar duas contas ao invés de uma:

    @Fábio @Stênio; @Weverton @RaúlCáceres; 
    
E por ai vai...
Como regra geral:

    'Este é um comentário'; 'Esse é outro'; 'Aqui é mais um';

<h2>Execução do programa</h2>
Basta rodar o comando a seguir em um terminal:

    python3 main.py
