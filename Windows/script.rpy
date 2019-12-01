# Declare characters used by this game. The color argument colorizes the
# name of the character.

#definição de variáveis em relação a pronome / forma do corpo
default masculino = False
default feminino = False
default Afeminino = False
default Amasculino = False
default Aandrogino = False
default padrao = False
default mutante = False

#definição de variáveis em relação ao perfil psicológico
default Possante = False
default Agil = False
default Cuidadoso = False
default Esperto = False
default Furtivo = False
default Estiloso = False


#variaives de proseguimento da história do Jhoul
default panfleto = False
default parede = False
default pegarPanfleto = False
default encontrouHitomi = False

#variaveis de proseguimento de história RAONI
default correrbosque = False
default aceitoucorrer = False
default concluiucorrida = False
default derrotado = False
default machucado = False
default encontrouRaoni = False
    #interrogar raoni
default olhos = False
default uniforme = False
default fazNoBosque = False

    #interrogar hitomi

default fazerNaEscola = False

#variaveis de amizade
default amigoJhoul = False
default amigoRaoni = False
default amigob = False

#Variavel de musica
default Welcome = True

#PERSONAGENS
define I = Character("")
define Jhoul = Character('Jhoul', color="#ff44ff")
define raoni = Character('Raoni')
define hitomi = Character('Elise', color="#FF0000")
define d = Character('Desconhecido', color="#964b00")


#image Jhoul = "Jhoul.png"
#image JhoulBravo = "Jhoul Bravo2.png"
image bg TelaPreta = "bg TelaPreta.png"
image gravata1 = "gravata1.png"
image gravata2 = "gravata2.png"
image gravata3 = "gravata3.png"
image bg Quarto = "bg Quarto.png"
image bg Escola = "bg Escola.png"
image credits = Movie(play="video.mp4")




#label definição de pronome
label start:
    scene bg TelaPreta
    "Um sonho estranho percorre sua mente, com balões de escolha bizarros:"

    "Por favor, escolha a maneira que prefere que o texto aponte para você"
    menu:
        "no masculino (ele/um/o).":
            $masculino = True
            python:
                name = renpy.input("qual seu nome?")
                name = name.strip()
                if not name:
                    name = "jogador"
                Nome = name[:10]
            jump masc
        "no feminino (ela/uma/a).":
            $feminino = True
            python:
                name = renpy.input("qual seu nome?")
                name = name.strip()
                if not name:
                    name = "jogadora"
                Nome = name[:10]
            jump masc

#Label definição de aparência
label masc:
    "Personagem é:"
    menu:
        "Forma padrão – corpo humano comum":
            $padrao = True
        "Forma mutante – corpo com características inumanas":
            $mutante = True
    #show gravata1 at right
    #show gravata2 at left
    #show gravata3 at center
    "Agora escolha como imagina a aparência do personagem:"
    menu:
        "Feminina":
            $Afeminino = True
        "Masculina":
            $Amasculino = True
    "De que forma você aborda problemas? Escolha uma"
    menu:
        "Possante":
            $Possante = True
        "Ágil":
            $Agil = True
        "Cuidadoso":
            $Cuidadoso = True
        "Esperto":
            $Esperto = True
        "Furtivo":
            $Furtivo = True
        "Estiloso":
            $Estiloso = True
    "E agora escolha outra"
    menu:
        "Possante" if not Possante:
            $Possante = True
        "Ágil" if not Agil:
            $Agil = True
        "Cuidadoso" if not Cuidadoso:
            $Cuidadoso = True
        "Esperto" if not Esperto:
            $Esperto = True
        "Furtivo" if not Furtivo:
            $Furtivo = True
        "Estiloso" if not Estiloso:
            $Estiloso = True
    "Realmente é um sonho Incomum, mas antes que possa fazer sentido disso, o alarme toca"
    jump quarto


#Introdução no Quarto

label quarto:
    scene bg Quarto
    I "Um misto de euforia e agitação embrulham o estômago."
    I "Há um pouco de medo, sim, e insegurança – mas acima disso tudo há uma vontade maior de querer sair e mostrar do que sou capaz!"
    I "Pois, finalmente, o dia chegou! Vou para o Colégio de Heróis de São Paulo!"
    stop music fadeout 1.0
    jump Escola


#introdução na Escola

label Escola:
    play music "Welcome.mp3" fadein 1.0
    scene bg Escola
    I "Já consigo ver o portão de entrada do colégio. Uma faixa bem grande despende de um lado ao outro dizendo “boas-vindas aos novos alunos”."
    I "Nossa...mesmo com uma faixa tão grande, é difícil de ler."
    I "Os muros da escola são enormes, e o portão de ferro, mesmo aberto, não deixa de impor uma sensação de reverência."
    I "O Colégio de São Paulo é o maior do Brasil, e pessoas do país inteiro fazem o teste de admissão."
    I "Ainda é difícil acreditar que consegui passar – a concorrência desse ano foi a maior de todos os tempos! "
    I "Talvez os avaliadores tenham visto algo de único em meus poderes...com quem estou brincando? Foi sorte, tenho certeza!"
    I "Vou precisar me esforçar bastante...alunos que não conseguem manter o ritmo acabam sendo cortados do curso!"
    I "Vejo uma fila grande se formando. Há alunos por toda parte, todos usando o uniforme da escola."
    I "Confesso que acho meio estranho usar um uniforme com as cores do Brasil,"
    I "parece forçoso – tudo bem que o colégio era militar, e os heróis todos tinham que seguir carreira militar."
    I "Mas agora não é mais assim...então por que não mudar o uniforme?"
    if feminino:
        I "*Suspiro*. Vejo que a fila tá crescendo e resolvo me aproximar. Parece que ser fila de entrega e confirmação da documentação escolar."
        I "Ainda bem que vim preparada. A fila anda rápido, mesmo sendo enorme."
    if masculino:
        I "*Suspiro*. Vejo que a fila tá crescendo e resolvo me aproximar. Parece que ser fila de entrega e confirmação da documentação escolar."
        I "Ainda bem que vim preparado. A fila anda rápido, mesmo sendo enorme."
    I "Chegou minha vez, bem na hora que terminei de revisar minha ficha."
    I "Vou para a frente da fila e descubro porque ela andava tão rápido: um senhor baixinho, de fisionomia oriental, está atendendo os novos alunos..."
    I "mas são muitos, agindo ao mesmo tempo! Há vários deles espalhados pela recepção, como clones idênticos, pegando papéis e conversando com os novos alunos!"
    if feminino:
        I "Chego mais perto. Ele se apresenta como Miaguito, o professor de educação física do colégio."
        I "Ainda um pouco atordoada com a situação, entrego minha ficha para ele."
    if masculino:
        I "Chego mais perto. Ele se apresenta como Miaguito, o professor de educação física do colégio."
        I "Ainda um pouco atordoado com a situação, entrego minha ficha para ele."

    I "O professor Miaguito apenas balança afirmativamente a cabeça e diz:"
    I "“boas-vindas ao Colégio de Heróis de São Paulo, [Nome], espero um futuro brilhante para você”."
    I "Oh não, já sinto a pressão caindo em meus ombros. Será que ele estaria me julgando? Será que as notas já começaram a ser dadas? Mas ainda nem fui para a aula!"
    I "Tento ver alguma pista nos olhos do pequeno professor, mas seu sorriso perene e expressão enigmática não fornecem respostas."
    I "Apenas retribuo para ele com um sorriso meio perdido e dou lugar para o próximo da fila."
    I "Um futuro brilhante...que piada! Eu nem sei mais pra onde ir agora! Vejo vários alunos novos se entreolhando, tão perdidos e confusos quanto eu."
    I "Nervosamente olho para os lados, quando vejo um garoto peculiar se aproximar."
    jump Jhoul


#cena de dialogo com Jhoul das primeiras escolhas TRILHA1

label Jhoul:
    scene bg Escola
    show jhoul neutro
    d "Olá, como vai?"
    I "ele falou com alegria, mas sem conseguir esconder um tantinho de nervosismo na voz. Tem um cabelo rosa, chamativos olhos de pupilas vermelhas e pele branca."
    I "O mais engraçado é que ele não está usando as roupas do colégio."
    I "Ao invés disso, usa o que parece ser um uniforme heroico, com uma capa vermelha brilhante."
    if feminino:
        d "Você é uma estudante nova, não é? Poderia me dizer seu nome e seus poderes?"
    if masculino:
        d "Você é um estudante novo, não é? Poderia me dizer seu nome e seus poderes?"
    menu:
        "Me apresento com um aceno e revelo meus poderes":
            jump trilha2
        "Me apresento gritando, enquanto extravaso meus poderes" if Possante:
            show jhoul bravo
            d "Cuidado! Não use seus poderes assim, pode acabar machucando os outros!"
            I "o garoto fala nervosamente."
            I "Vejo uma onda rosada sair das mãos dele e percebe uma força fantasmagórica segurando meus poderes, impedindo que eles atinjam outros alunos."
            d "Agora você estuda no Colégio de Heróis, e deve ser mais responsável. De qualquer forma…"
            jump trilha2
        "Me apresento fazendo pose e firulas com meus poderes" if Estiloso:
            show jhoul alegre
            d "Nossa, você tem mesmo grande habilidade com os poderes! Vai se adaptar bem ao colégio…"
            jump trilha2
        "Me apresento um tanto desconfiado, observando o garoto" if Cuidadoso:
            show jhoul envergonhado
            if feminino:
                d "Seus poderes são bem interessantes mas não precisa ficar assim, desconfiada. Sou uma pessoa legal. Então…"
            if masculino:
                d "Seus poderes são bem interessantes mas não precisa ficar assim, desconfiado. Sou uma pessoa legal. Então…"
            jump trilha2
        "Me apresento observando o garoto, enquanto demonstro meus poderes" if Esperto:
            show jhoul alegre
            d "Você é uma pessoa bastante atenta, não é mesmo? E seus poderes refletem bem isso..."
            jump trilha2
        "Não digo meu nome nem meus poderes, esperando que ele fale primeiro" if Furtivo:
            show jhoul bravo
            if feminino:
                d "Não precisa ficar arredia assim. Fui escolhido pelo conselho estudantil para ajudar. Por favor, me diga o seu nome e seus poderes."
            if masculino:
                d "Não precisa ficar arredio assim. Fui escolhido pelo conselho estudantil para ajudar. Por favor, me diga o seu nome e seus poderes."
            menu:
                "me apresento com um aceno e revelo meus poderes":
                    jump trilha2
                "me recuso a dizer o nome":
                    show jhoul triste
                    d "Tudo bem, desculpa. Bom, se quiser ajuda, é só falar comigo"
                    I "visivelmente consternado enquanto se afasta."
                    hide jhoul
                    I "Deixo o garoto estranho e resolvo me virar. Vou descobrir as coisas por minha conta!"
                    I "Olho em volta, mas só encontro estudantes igualmente perdidos."
                    I "Enquanto isso, o garoto estranho se aproxima das pessoas, conversa e entrega uma espécie de panfleto."
                    I "Seria um mapa? Droga, o que devo fazer?"
                    menu:
                        "Continuar olhando para os lados e esperar":
                            jump trilhaFurtivo
                        "ir falar com o Jhoul":
                            jump trilhaRevelar
            jump trilha2

#se o jogador se negar a ir falar com o jhoul
label trilhaFurtivo:
    scene bg Escola
    I "Fico de pé, no meio da recepção, como um peixe fora d’água. O que devo fazer? "
    menu:
        "Continuar olhando para os lados e esperar":
            jump trilhaFurtivo
        "ir falar com o Jhoul":
            jump trilhaRevelar

#quando o jogador furtivo finalmente se render ir falar com ele
label trilhaRevelar:
    show jhoul neutro
    scene bg Escola
    I "Me aproximo novamente do garoto, ainda sem saber direito qual é a dele. Apesar de tudo, ele me recebe com a mesma feição solícita."
    d "Olá de novo! Então, gostaria agora de me dizer seu nome?"
    menu:
        "Me apresento com um aceno":
            jump trilha2
        "Me recuso a dizer o nome":
            jump trilhaFurtivo

#FIM DA TRILHA 1







#segunda parte da interação onde há prosseguimento nas etapas de diálogo e não é possivel voltar

label trilha2:
    scene bg Escola
    show jhoul alegre
    d "Boas-vindas [Nome]!”, o garoto fala abrindo um sorriso."
    d "Eu sou o Jhoul...o Jhoul Kinn. Meu nome de herói é ‘Brainstorm’ e possuo um repertório poderes mentais."
    Jhoul "Sou estudante do Colégio e estou hoje aqui para ajudar os novatos"
    Jhoul "por isso estou usando a roupa de herói ao invés do uniforme. Acredito que assim chamo bastante a atenção, não é mesmo?"
    menu:
        "Concordo com a cabeça, em silêncio":
            jump trilha3
        "“Com uma roupa idiota dessas, como não?”, falo com uma risada" if Possante:
            show jhoul bravo
            Jhoul "Não precisa falar assim; esse tipo de temperamento vai criar problemas, acredite."
            Jhoul "Brigões e valentões têm mais chances de serem expulsos"
            menu:
                "olho para baixo, desconcertada." if feminino:
                    Jhoul "O rapaz suspira pesarosamente, mas rapidamente seu bom humor volta."
                "olho para baixo, desconcertado." if masculino:
                    Jhoul "O rapaz suspira pesarosamente, mas rapidamente seu bom humor volta."
                "encaro Jhoul, erguendo uma sobrancelha em desafio." if Estiloso:
                    Jhoul "O rapaz suspira pesarosamente, mas rapidamente seu bom humor volta."
            jump trilha3
        "Fico de cara séria, em silêncio" if Cuidadoso:
            show jhoul envergonhado
            Jhoul "Er...bem..."
            jump trilha3

#FIM TRILHA 2


#inicio trilha 3

label trilha3:
    scene bg Escola
    show jhoul neutro
    Jhoul "Vamos então para os fatos: agora que está no Colégio de Heróis, você deve ter responsabilidade!"
    Jhoul "Todos os estudantes de heróis são emancipados – você agora é considerado um adulto perante a lei, e deve agir como tal!"
    show jhoul alegre
    I "o  rapaz faz uma pausa, dando uma risada."
    show jhoul neutro
    Jhoul "Bom, não é preciso tanta seriedade assim, estou exagerando um pouco...mas, de verdade, você precisa tomar cuidado, sabe?"
    Jhoul "Não deve usar seus poderes fora do Colégio, a menos que tenha uma permissão para isso."
    Jhoul "Precisa se esforçar para conseguir sua licença provisória de herói. Participar de algum estágio, essas coisas."
    I "Ele para um momento para me fitar com aqueles incisivos olhos de pupilas vermelhas."
    Jhoul "Acredito que você já deve saber disso Toma, isso aqui é para você. Estou entregando a todos os alunos novos"
    I "Jhoul entrega um panfleto, com fotos e nomes marcados."
    Jhoul "Este é o mapa da escola, pelo menos das áreas principais."
    Jhoul "É legal ir se acostumando com o terreno, quando as aulas de treinamento começarem você vai ficar feliz se souber para onde pode fugir"
    show jhoul alegre
    I "Será que ele está falando sério?! O sorriso no rosto esconde alguns traços de nervoso e assustadoras experiências passadas."
    show jhoul neutro
    Jhoul "E depois que você andar um pouco pelo Colégio, pode ir para o pátio onde vai ocorrer a festa"
    I "Festa?!"
    show jhoul alegre
    I"Jhoul vê minha expressão de espanto e abre um longo sorriso."
    Jhoul "Ah, sim, a festa. Você não recebeu as notificações?"
    Jhoul "O primeiro dia de aula é livre para os alunos novos conhecerem a escola, e sempre organizamos uma festa de abertura"
    I "Olha, quem diria? Talvez não seja tão ruim assim o curso de heróis."
    I "Talvez todas aquelas histórias de alunos perseguidos por professores enquanto eram alvos de metralhadoras e granadas não passam de um bando de mentiras, não é?"
    show jhoul neutro
    Jhoul "Agora vou continuar o trabalho e entregar mais alguns panfletos aos novatos. Se estiver tendo qualquer problema, é só vir falar comigo, tudo bem?"
    I "Concordo afirmativamente"
    show jhoul alegre
    Jhoul "Ótimo. Ah! Só mais uma coisa. Se eu puder pedir um favor, caso você passe na biblioteca, poderia pegar para mim alguns panfletos informativos que encomendei?"
    Jhoul "Pedi para a gráfica da escola publicar para distribuir mas eles ainda não estavam prontos. Talvez por agora já estejam. É só falar com alguém no pátio"
    menu:
        "Levanto um polegar positivo":
            Jhoul "Obrigado, agradeço pela ajuda. Bom, até depois, [Nome]"
            jump trilha3fim
        "Dou de ombros e digo, com a voz mole, “ehh… pode ser":
            Jhoul "Obrigado, agradeço pela ajuda. Bom, até depois, [Nome]"
            jump trilha3fim
        "Olho longamente nos olhos do Jhoul, dizendo finalmente – “tudo bem, posso fazer isso”." if Cuidadoso:
            Jhoul "Obrigado, agradeço pela ajuda. Bom, até depois, [Nome]"
            jump trilha3fim

label trilha3fim:
    scene bg Escola
    I "Jhoul começa a voar, seus pés levantando acima do solo e indo em direção a um grupo de alunos completamente perdidos."
    I "Agora, com o mapa em mãos, devo decidir o que fazer nesse primeiro dia de escola!"
    jump mapa


#Entrada JHOUL

label Entrada:
    scene bg escola
    I "A entrada continua repleta de estudantes novos revendo sua documentação, enquanto os vários clones do professor Miaguito continuam terminando as inscrições."
    I "Jhoul continua aqui, voando e entregando panfletos, ajudando como pode."
    show jhoul neutro
    Jhoul "Olá novamente, [Nome], como posso ajudar?"
    menu:
        "Só queria saber como você está":
            show jhoul alegre
            Jhoul "Ah! Eu estou bem, fico feliz que tenha perguntado, obrigado"
            show jhoul neutro
            Jhoul "Se precisar de ajuda com alguma coisa, é só vir falar comigo"
            I "Com um aceno de despedida, o garoto de cabelo rosa volta a voar, indo entregar panfletos e ajudar novatos."
            jump mapa
        "Trouxe os panfletos que você havia pedido "if panfleto:
            show jhoul alegre
            Jhoul "É mesmo? Obrigado, precisava mesmo de mais, os meus já estavam acabando."
            Jhoul "Muito obrigado, você é uma boa pessoa. Mais tarde você vai para a festa no pátio?"
            I " Os olhos de pupilas vermelhas brilham quando falam a palavra ‘festa’. Eu dou um sorriso meio sem jeito e confirmo que pretendo ir para a festa."
            Jhoul "Ótimo!"
            I "o garoto diz afirmativamente enquanto gesticula com as mãos"
            Jhoul "então nos encontramos mais tarde lá. Bom, até depois, [Nome]"
            I "Jhoul agradece mais algumas vezes pelos panfletos e volta a voar, abordando novos estudantes."
            $amigoJhoul = True
            $panfleto = False
            jump mapa
#fim da parte da entrada


#BOSQUE RAONI

label bosque:
    scene bg bosque
    if aceitoucorrer:
        if derrotado:
            $derrotado = False
            if masculino:
                I "Acordo ainda atordoado, vendo que me salvaram. Reparo num dos clones do professor Miaguito, sorrindo, e com uma voz branda me diz:"
                I "“Tome cuidado, jovem. Não vá morrer antes da primeira aula, haha"
                I "O clone vai embora e eu agora tenho que ver o que fazer."
            if feminino:
                I "Acordo ainda atordoada, vendo que me salvaram. Reparo num dos clones do professor Miaguito, sorrindo, e com uma voz branda me diz:"
                I "“Tome cuidado, jovem. Não vá morrer antes da primeira aula, haha"
                I "O clone vai embora e eu agora tenho que ver o que fazer."
        menu:
            "sair" if not concluiucorrida:
                jump mapa
            #primeira opção para tentar correr mais uma vez
            "Entrar no bosque e procurar a Raoni" if not concluiucorrida:
                jump bosqueCorrida
            #segunda opção caso ja tenha concluido a corrida
            "A Raoni não está mais aqui. Acho melhor ir para outro lugar"if concluiucorrida:
                jump mapa
    if encontrouRaoni:
        jump interrogar
    if not aceitoucorrer:
        I "Atravesso a gigantesca esplanada do Colégio, passando por ruas internas, estacionamento...nossa, realmente, é inacreditável o tamanho desse lugar!"
        I "Toda a construção remonta à arquitetura militar, apesar de que as proporções daqui são estrondosas!"
        I "Mas sigo em frente, rumo ao conjunto de copas verdejantes que vejo ao fundo."
        I "Logo, com cada passo mais próximo, o chão concretado dá lugar à grama, e começo a enxergar enormes árvores de troncos espessos e folhagens densas."
        I "Este é o famoso bosque do Colégio de São Paulo? Ouvi muitas lendas sobre ele quando estava no curso do Ginásio, me preparando para o teste de admissão."
        I " Dizem que os professores jogam os alunos no bosque, sozinhos para enfrentar monstros, feras criadas em laboratórios e robôs de combate!"
        I "Certa vez, falaram que os próprios professores, armados com fuzis, caçaram os alunos durante uma prova de sobrevivência…"
        I "Balanço a cabeça tentando espantar um calafrio que percorre a espinha."
        I "Olho em volta enquanto caminho pelo perímetro do bosque, não ousando entrar."
        I "Vejo alguns grupos de alunos se aglomerando – parecem já veteranos e me olham com um misto de curiosidade e estranheza."
        I "Será que eu devia me aproximar?"
        I "Andando um pouco mais, vejo uma figura se alongando na entrada do bosque. Está sozinha, o que é bom: o nervosismo é menor ao falar com uma pessoa."
        I "Será que também é novata aqui no Colégio? Suas roupas são bem diferentes."
        I "Enquanto os alunos usam o uniforme da escola – camisa amarela com gola verde e uma calça jeans azul – esta daí está usando o que parece um colete azulado."
        I "Estranho...essa roupa me lembra…"
        I "Oh não, ela agora está olhando pra mim. Tento disfarçar o olhar, mas a situação só fica ainda mais óbvia."
        I "Droga, espero não estar sendo inconveniente...mas ela sorri e acena, indicando que eu me aproxime."
        I "Dou alguns passos a mais, ficando agora de frente a ela."
        show raoni neutro
        I "É uma garota...baixinha, talvez com um metro e meio só, talvez um pouco mais que isso."
        I "Tem a pele queimada por sol e um tipo físico atlético."
        I "Seus cabelos são castanhos e brilhosos, com algumas tranças e um adereço bonito feito com penas de ave entremeado nelas."
        I "Contudo, duas coisas mais chamam a atenção nela: ela usa um colete azul com uma saia curta, bem diferente do uniforme da escola;"
        I "e seus olhos não são humanos – são amarelos cristalinos com pupilas felinas que não param de me fitar."
        I "Há um momento de silêncio em que nenhum dos dois fala até ela quebrar o gelo."
        if masculino:
            d "Eu sinto cheiro de aluno novo”, ela dá um sorrisinho de canto, enquanto parece fungar o ar, “estou errada?"
        if feminino:
            d "Eu sinto cheiro de aluna nova”, ela dá um sorrisinho de canto, enquanto parece fungar o ar, “estou errada?"
        I "Apenas confirmo que sim, comecei hoje na escola e ainda não sei direito o que fazer. Ela parece ficar entretida com essa resposta."
        d "Ora, não precisa ficar aí com medo, vem mais perto, eu não mordo...pelo menos não sempre"
        I "O que será que ela quis dizer com isso?! A garota dá uma risadinha."
        d "Eu sou Raoni Zuratan. E você, quem é?"
        if masculino:
            I "Me apresento para ela, ainda um tanto atordoado com a situação."
        if feminino:
            I "Me apresento para ela, ainda um tanto atordoada com a situação."
        raoni "Olá, [Nome], espero que este seu primeiro dia esteja sendo agradável."
        raoni "A escola pode ser meio assustadora e louca no começo...pelo menos foi para mim."
        raoni "Então, se tiver qualquer pergunta, pode falar."
        raoni "Estava me preparando aqui para fazer uma série de corrida no bosque, mas gostaria de ajudar alguém em apuros."
        jump interrogar


#MENU INTERROGANDO RAONI SOBRE DIVERSOS ASSUNTOS
label interrogar:
    scene bg bosque
    show raoni neutro
    if encontrouRaoni:
        raoni "olá, bom te ver denovo"
    $encontrouRaoni = True
    menu:
        "Perguntar sobre os olhos" if not olhos:
            I "As pupilas felinas de Raoni se estreitam, como se estivesse tentando perfurar minha alma."
            if mutante:
                raoni "eu sou uma mutante do mesmo jeito que você"
            if padrao:
                raoni "Ora, o que tem a responder sobre isso? Eu sou uma mutante"
            I "Ela balança os braços expressivamente "
            raoni "As pessoas costumam ter uma visão negativa sobre nós, mas eu tento olhar pelo lado bom das coisas. Nesse caso, minha visão é ótima! Hahaha"
            I "A risada dela é bem alta, como se tentasse esconder um pouquinho de tristeza atrás de um som bem alto."
            raoni "Mas...falando sério, eu gosto dos meus olhos, mesmo que outras pessoas fiquem arranjando problemas com isso"
            $olhos = True
            jump interrogar

        "Perguntar sobre o uniforme" if not uniforme:
            I "Raoni estica bem o colete, permitindo que eu possa olhar em detalhes."
            raoni "Esse uniforme é de outro colégio de heróis, o do Rio de Janeiro. No caso, as cores seguem mais o padrão da marinha brasileira, enquanto o de São Paulo segue as do exército."
            raoni "Sabe, eu venho de comunidade indígena, da cidade de Ubatuba."
            I "Eu tinha recebido bolsa de estudos num colégio particular de Heróis, mas pelo desempenho acabei sendo cotada para o colégio do Rio."
            raoni "Fiz transferência não tem muito tempo para cá, e ainda estou me adaptando com as coisas aqui em São Paulo."
            I "Raoni volta a mostrar a roupa que usa, esticando."
            raoni "Normalmente não podemos usar uniformes das outras escolas, né? Mas como hoje é um dia livre de apresentação, aí liberam."
            raoni "Eu acho o uniforme do Rio mais bonito, para ser sincera."
            I "Ela termina a fala com um sorriso longo, mostrando caninos afiados."
            $uniforme = True
            $encontrouRaoni = False
            jump interrogar

        "Perguntar sobre o que faz no bosque" if not fazNoBosque:
            raoni "Então, estou me alongando para fazer uma série rápida de treino. Gosto de correr até o centro do bosque e voltar. Aí descanso um pouco e depois tento de novo"
            I "Correr no bosque? Não parece ser algo muito difícil."
            I "É o que eu penso, e parece que minha expressão facial está traindo meus pensamentos, pois a Raoni abre um sorriso desafiante."
            raoni "Acho que você não conhece muito do bosque do Colégio, não é mesmo? Ele é protegido por vários robôs de defesa criados supertecnologia do professor Bit."
            raoni "Além disso, muitas árvores ganham propriedades especiais graças aos poderes da professora Dríade – e algumas acabam tomando gosto por carne, hahah."
            I "Não pode ser! As lendas eram verdade! O bosque do Colégio de Heróis de São Paulo é cheio de coisas horríveis. Como os estudantes conseguem sobreviver aqui?"
            show raoni alegre
            raoni "Parece que agora consegui te assustar, não é mesmo?"
            I "Ela cai na risada, enquanto eu começo a imaginar se conseguirei sobreviver a um semestre dentro desse colégio."
            show raoni neutro
            raoni "Não se preocupe, tanto os robôs quanto os outros perigos foram feitos apenas para nocautear os alunos. Você não corre risco de vida, relaxe."
            I "Sabe, por algum motivo, estas palavras não foram suficientes para me fazer relaxar…"
            raoni "Então...olha essa ideia. Que tal correr comigo?"
            I "O quê? É sério essa pergunta? Ela só pode estar maluca!"
            show raoni alegre
            raoni "É sério! Vai ser divertido, hahaha"
            show raoni neutro
            raoni "Então, o que me diz?"
            #MENU DENTRO DO MENU SOBRE DAR UM ROLÉ EM FORMA DE CORRIDA
            menu:
                "Não":
                    show raoni brava
                    raoni "Nossa, mas que pessoa frouxa. Bom, eu vou continuar aqui caso perca o medo e resolva correr comigo, sim?"
                    $correrbosque = True
                    $fazNoBosque = True
                    $encontrouRaoni = False
                    jump interrogar

                "Sim":
                    show raoni alegre
                    raoni "Ótimo, sabia que você no fundo tinha coragem. Então, podemos começar?"
                    I "Tão logo ela terminar de falar e já começa a correr para dentro do bosque. Sem saber muito o que fazer, sigo meus instintos e corro atrás!"
                    $aceitoucorrer = True
                    jump bosqueCorrida

        #OPCAO DESBLOQUEDA RECUSANDO CORRER
        "Correr no bosque" if correrbosque:
            show raoni neutro
            raoni "Então, mudou de ideia e agora quer correr?"
            menu:
                "Sim":
                    show raoni alegre
                    raoni "Ótimo, sabia que você no fundo tinha coragem. Então, podemos começar?"
                    I "Tão logo ela terminar de falar e já começa a correr para dentro do bosque. Sem saber muito o que fazer, sigo meus instintos e corro atrás!"
                    $aceitoucorrer = True
                    jump bosqueCorrida

                "Não":
                    show raoni brava
                    raoni "Nossa, mas que pessoa frouxa. Bom, eu vou continuar aqui caso perca o medo e resolva correr comigo, sim?"
                    $encontrouRaoni = False
                    jump interrogar

        "Ir embora":
            I "A garota acena e diz"
            raoni "Tchau, tchau, se cuida, tá?."
            I "Depois disso ela então volta a se alongar, olhando para o bosque."
            jump mapa



#PROSEGUIMENTO HISTORIA DA RAONI CORRIDA

label bosqueCorrida:
    scene bg bosquefechado
    play music "bosqueinterno.mp3"
    $Welcome = False
    I "Com grande esforço, consigo me manter perto da Raoni – a agilidade dela é imensa, e por mais que corra não parece perder o fôlego."
    I "Ela olha para trás fazendo um olhar de desafio."
    show raoni neutro
    raoni "Então, tá conseguindo manter o ritmo? Vamos tentar chegar no centro do bosque, lá tem uma clareira, e depois voltar."
    raoni "Só cuidado com os perigos e, não importa o que aconteça, não use seus poderes ofensivos aqui no bosque!"
    I "O quê, como assim? Quer dizer que plantas gigantes malignas me atacarem eu devo aceitar numa boa e fazer nada?"
    show raoni alegre
    raoni "Bom, é basicamente isso, haha. Sabe, a diretora proíbe os poderes de ataque aqui no bosque para não machucar as plantas nem os animais."
    I "Ok...mas e quanto a machucar os estudantes? Isso pode, sem problemas…"
    I "Mas não tenho nem tempo para reclamar. Logo à frente um bando de figuras metálicas aparece voando;"
    I "lembram algo como pequenos cilindros, quase latas de lixo, com o que parecem pistolas montadas nelas."
    show raoni brava
    raoni "Rápido, encontre um abrigo e esquive deles. Qualquer coisa nos encontramos no centro do bosque"
    hide raoni brava
    I "A garota corre para uma outra direção, dividindo a atenção do bando de robôs."
    I "Metade saiu flutuando na direção dela, enquanto os que restaram vêm atrás de mim. O que eu faço?"
    menu:
        "Tento correr entre os robôs, me protegendo como posso":
            I "Busco uma brecha entre a formação dos robôs e corro. Conforme passo, sinto algo ardendo em minha pele."
            I "Parece que as armas deles são algum tipo de laser! Meu corpo queima e se fere, mas consigo atravessá-los e, logo em seguida, correr, os deixando para trás"
            $machucado = True
            jump bosque2
        "Salto sobre os robôs rapidamente, usando as árvores como propulsão" if Agil:
            I "Com reflexos incríveis, vou saltando pelas árvores e consigo ultrapassar facilmente o obstáculo dos robôs!"
            jump bosque2
        "Ataco os robôs com força total" if Possante:
            I "Com um gesto poderoso, invoco meus poderes e despedaço todos os robôs!"
            I "Eles nunca tiveram chance, ha! Me preparo para andar em frente, tentando reencontrar Raoni, quando sinto um braço fortíssimo me agarrando por três, travando o meu pescoço!"
            I "“É proibido usar poderes ofensivos aqui no Bosque, moleque” fala uma voz rouca, grave e assustadora em meu ouvido."
            I "Antes que eu possa sequer tentar entender o que acontece sinto um golpe forte em minha cabeça e tudo fica escuro…"
            $derrotado = True
            jump bosque

#SEGUNDA ETAPA DA CORRIDA

label bosque2:
    scene bg bosquefechado
    I "Vou seguindo pelo bosque, buscando chegar na clareira ao centro para me reencontrar com a Raoni."
    I "Consigo sentir uma elevação suave sobre os pés – parece que o terreno inteiro do solo do bosque se desenvolveu numa pequena colina."
    I "Apresso o passo, apesar do cansaço; quanto mais cedo reencontrar a garota, mais rápido poderei sair."
    I "Mas as coisas não serão fáceis, é lógico! Meu caminho agora está bloqueado por uma parede de vinhas que, ao longe, pareciam normais."
    I "Mas agora, de perto, elas se mexem loucamente, como serpentes!"
    I " Deve ser uma das árvores alteradas que a Raoni falou. Eu tento recuar, voltar pelo mesmo caminho, mas percebo que as vinhas agora já estão me cercando. O que eu faço?"
    menu:
        "Tento rastejar por baixo das vinhas":
            I "Abaixo meu corpo o máximo que posso e tento me arrastar pelo solo da floresta."
            I "Infelizmente, as vinhas esticam, lambendo o chão. Seus espinhos como agulhas perfuram minha pele, e sinto arder um veneno em minhas veias."
            if machucado:
                I "Meu corpo, ferido no ataque dos robôs, não consegue resistir. Tudo fica escuro conforme vou perdendo a consciência."
                $derrotado = True
                jump bosque
            I "Apesar dos espinhos, ainda sim consigo ultrapassar a cortina de vinhas. Estou livre para continuar avançando."
            jump bosque3
        "Me escondo entre os troncos de uma árvore e espero em silêncio" if Furtivo:
            I "As vinhas parece que percebem as coisas através do som, que curioso! Ao me esconder e ficar quieto, elas lentamente foram abrindo espaço."
            I "Aproveito a oportunidade para passar e seguir caminho"
            jump bosque3
#fim segunda etapa de corrida


#COMEÇO DA TERCEIRA ETAPA DE CORRIDA

label bosque3:
    scene bg clareira
    I "Finalmente! Após tantos perigos, consigo atravessar e chegar no centro do bosque, onde uma grande clareira se encontra. Há campos de grama verde e muitas flores crescendo em padrões belos."
    I "Uma sensação de alívio, calma e triunfo percorrem meu peito. Minha primeira vitória no Colégio de Heróis!"
    I "Não tenho tempo para saboreá-la, pois um rugido alto e grosso faz meu coração quase escapar pela boca. Olho em volta, procurando a origem desse som e então vejo…"
    show raoni fera at right
    I "Um enorme tigre...ou leão...gigantesco, com pelagem de um laranja magma ardente, se aproxima. Penso em correr, mas a criatura é absurdamente rápida."
    I "Seus dentes, gigantescos, reluzem e apontam em minha direção conforme se aproxima."
    I "Coloco a postura de combate e preparo meus poderes mas, no momento em que acredito que a criatura vai dar um bote e me devorar ela, ao invés disso...começa a rir? Desde quanto tigres riem?!"
    I "Então, diante dos meus olhos, a criatura vai mudando, mudando…"
    show raoni alegre at center
    raoni "Parece que eu te assustei, não foi?"
    I "É a Raoni!"
    show raoni neutro
    raoni "Pois é, meu poder é o de transformar em minha forma de fera. Legal né?"
    I "Você poderia ter avisado! Quase me matou de susto."
    show raoni alegre
    if feminino:
        raoni "Ah, mas é mais engraçado descobrir assim, haha. E, bom, na forma de fera eu não posso falar. E como você não havia me perguntado do meu poder, então também nem contei."
        raoni "Você não está brava, está?"
    if masculino:
        raoni "Ah, mas é mais engraçado descobrir assim, haha. E, bom, na forma de fera eu não posso falar. E como você não havia me perguntado do meu poder, então também nem contei."
        raoni "Você não está bravo, está?"
    menu:
        "Lógico que estou! Que droga, você é uma idiota! Ridícula!":
            show raoni triste
            raoni "Ah...tudo bem...desculpa"
            hide raoni
            I "Envergonhada, a garota se transforma novamente na criatura e sai correndo, desaparecendo de vista. Não importa, não quero mais saber dela."
            I "Volto pelo caminho que fiz, evitando os perigos e chegando novamente ao início do bosque."
            $concluiucorrida = True
            stop music
            jump mapa

        "Estou um pouco...por favor, não faça mais isso":
            show raoni triste
            raoni "Certo...desculpa por isso. Espero que não fique com raiva de mim"
            I "Suspiro e olho para a garota – seus olhos felinos agora dilatados e cabisbaixos. “Não estou com raiva...talvez só um pouco, mas vai passar”."
            show raoni neutro
            raoni "Que bom, não queria ter te magoado. Bom, é hora de voltarmos, sim?"
            I "Sim, com certeza, já cansei deste bosque!"
            $concluiucorrida = True
            stop music
            jump bosque4

        "Nem, até que foi um pouco engraçado":
            show raoni alegre
            raoni "“Ha! Sabia que você era uma pessoa com senso de humor, haha. Mas então, que tal nós voltarmos?"
            I "Sim, com certeza, já cansei deste bosque!"
            $concluiucorrida = True
            stop music
            jump bosque4
#FIM DA TERCEIRA PARTE DA RAONI

label bosque4:
    scene bg bosque
    I "Junto com a Raoni, voltamos conversando sobre nossas peripécias no bosque e os perigos que superamos."
    I "Conseguimos evitar novos obstáculos e, mal percebemos, já estávamos outra vez de volta no início."
    show raoni neutro
    raoni "Bom, acho que agora vou descansar um pouco. Mais tarde, que tal nos encontrarmos na festa do pátio? Você vai estar lá, não vai?"
    I "Sorrio concordando. É claro que vou estar lá."
    show raoni alegre
    raoni "Ótimo, então nos vemos mais tarde. Té logo, [Nome]"
    I "E com isso, a garota se transforma novamente na sua assustadora forma de fera, desaparecendo ao longe no enorme terreno da escola."
    $amigoRaoni = True
    jump mapa

label patio:
    scene bg patio
    if encontrouHitomi:
        jump interrogar2
    I "Caminho por um tempo até chegar no pátio da escola, um lugar intermediário entre o prédio do pavilhão de aulas, o da coordenação e o da residência estudantil."
    I "Ao longe consigo ver as quadras de esportes, com vários alunos treinando seus poderes – e também várias explosões bastante perigosas!"
    I "Aqui, no pátio, existem diversas árvores e bancos estrategicamente colocados para que as pessoas possam descansar,"
    I "tudo arranjado em volta de um espaço aberto, parte grama, e parte asfalto."
    I " Vejo pessoas sentadas formando círculos de conversa – o clima é bastante agradável."
    I "Quando chego, vejo caixas de som sendo trazidas junto a algumas faixas com o texto ‘Festa de boas-vindas’."
    I "Conforme os aparelhos de som vão sendo instalados, uma agitação começa a crescer entre os estudantes presentes, com sorriso e cochichos sendo trocados."
    if feminino:
         I "Ainda um tanto perdida, me aproximo de um grupo de alunos que parece ser de veteranos e procuro saber mais."
    if masculino:
         I "Ainda um tanto perdido, me aproximo de um grupo de alunos que parece ser de veteranos e procuro saber mais."
    show elise normal
    d "Olá, bom dia!"
    I "diz a pessoa, olhando para mim com uma visão analítica."
    d "Eu sou Elise, mas pode me chamar de ‘Itami’. Eu faço parte do conselho estudantil e estou aqui para ajudar. Do que gostaria?"
    jump interrogar2

label interrogar2:
    scene bg patio
    show elise normal
    if encontrouHitomi:
        hitomi "Olá de volta"
        hitomi "Do que gostaria de falar?"
    $encontrouHitomi = True
    menu:
        "O que tem para fazer na escola?" if not fazerNaEscola:
            $fazerNaEscola = True
            hitomi "A escola está um pouco vazia no momento, tenho até um bilhete sobre isso"
            I "A representante pega um papel que tinha no bolso e começa a ler"
            hitomi "Pessoas que estejam jogando essa Demo, fiquem atentas para o próximo lançamento do projeto Brasil de Heróis, onde mais localidades, personagens e trilhas serão adicionadas."
            hitomi "Espero que estejam gostando dessa primeira versão Demo e que fiquem com vontade de jogarem as próximas!"
            I "Ela dá uma pausa e vira o verso da folha, suspirando pesadoramente"
            hitomi "Assinado por Piruleta...hum, cada vez mais entendo menos das brincadeiras desse cara"
            $encontrouHitomi = False
            jump interrogar2

        "Panfletos para o Jhoul" if not pegarPanfleto:
            $panfleto = True
            $pegarPanfleto = True
            hitomi "Ah, o Jhoul está precisando de mais panfletos? Por sorte, a gráfica acabou de deixar aqui alguns novos."
            hitomi "Vou entregar para você entregar a ele, tudo bem? Agradeço sua prestatividade"
            $encontrouHitomi = False
            jump interrogar2

        "Festa no Pátio":
            hitomi "Sim, estamos arrumando o pátio para uma festa de boas-vindas a todos os alunos novos. Creio que logo deve começar."
            hitomi "Se quiser, pode ir ligando o som. Gostaria?"
            menu:
                "Sim":
                    jump festa
                "Não":
                    I "Tudo bem"
                    $encontrouHitomi = False
                    jump interrogar2
        "Voltar ao mapa":
            jump mapa

label festa:
    play music "festa.mp3"
    $Welcome = False
    scene bg patio
    I "A música começa a tocar e, como um chamariz de vaga-lumes, estudantes espalhados por toda a escola começam a aparecer. Não demora e rodas de dança já começam a se formar."
    I "Alguns estudantes trazem isopores com comidas caseiras e doces. Outros continuam a ajudar na arrumação, melhorando o espaço."
    I "Depois de alguns minutos, o pátio da escola já está transformado. Vejo estudantes usando seus poderes para montar tendas, amplificar a música e alterar as luzes do pátio."
    I "Manipuladores de som usam seu controles de ondas para dar sensações diferentes a cada música."
    I "E uma garota com óculos enormes senta na maior das caixas de som, balançando as mãos e fazendo com que eu literalmente consiga sentir o gosto das notas musicais!"
    I "As barraquinhas de comida estão formadas, e vejo três que parecem estar numa competição amigável, apesar de acirrada."
    I "Uma garota de chiquinhas vendendo bolos com uma placa falando “receita de serpente!”,"
    I "uma outra garota com flores no cabelo vendendo doces “com fragrâncias de criação própria”, e um garoto dizendo “sorvete com glacê direto da Super Glacê!”."
    I "Nisso, as rodas de dança crescem, evoluem e praticamente viram ringues de luta!"
    I "Um aluno alto dança mesclando movimentos de capoeira e termina num movimento espalhafatoso enquanto abre enormes asas de anjo."
    I "Outro, que parece vestir todas as roupas em cima do corpo, parece escorregar a cada segundo, apenas para, com uma cambalhota mortal, voltar a ficar de pé."
    I "E não é só no chão, mas também no céu que as danças ocorrem, com alunos voadores trocando passos em pleno ar!"
    if feminino:
        I "Fico até pasma em meio a tanta coisa! Nunca estive num lugar onde os poderes pudessem ser usados tão livremente"
        I "fora dos colégios e ginásios de heróis, a regulação é forte, exatamente para que a cidade não fique sempre em tanto caos."
    if masculino:
        I "Fico até pasmo em meio a tanta coisa! Nunca estive num lugar onde os poderes pudessem ser usados tão livremente"
        I "fora dos colégios e ginásios de heróis, a regulação é forte, exatamente para que a cidade não fique sempre em tanto caos."
    I "Depois de um tempo, vou acostumando, e procuro decidir o que farei na festa"
    jump amigo

#ESCOLHA DE PAR PARA A FESTA E DISPENSANDO RAONI
label amigo:
    scene bg patio
    menu:
        "Quero me divertir numa das atrações da festa!" if not parede:
            #a opção só é permitida uma vez
            I "Uma voz estridente e incômoda aparece do nada e diz: “Meu Deuss, você quer jogar mais? Nessa versão não dá, tem que esperar na próxima”"
            I "Olho para os lados procurando de onde veio a irritante voz, mas não acho. Seria este o tal do Piruleta? Hum...melhor não tentar algo estranho."
            $parede = True
            jump amigo
            #retorno para o começo sem essa opção
        "Passar a festa só":
            I " Fico olhando em volta, procurando algum rosto conhecido e nada."
            I "Encontro alguma coisa pra beber – um copo de água morna (ugh!) – e, um tanto tontamente, me encosto numa árvore e olho a festa correndo."
            I "*suspiro * Sabe, apesar de estar aqui só, não posso deixar de me sentir feliz."
            I "Passei no exame, faço parte do colégio de heróis de São Paulo. O futuro vai ser legal – tenho certeza de que o futuro será bem legal!"
            jump creditos
            #fim dessa linha
        "Passar a festa com Raoni" if amigoRaoni:
            #caso tenha concluido a corrida com Raoni a opção estará livre
            I "Depois de olhar em volta, acabo encontrando um rosto conhecido"
            show raoni neutro
            raoni "Ei, ei, se não é [Nome]! Veio pra festa também, né? Bom te ver."
            I "Raoni está ainda usando o uniforme batido de terra e grama do treino. Ela observa meu olhar levemente julgador e abre um sorriso."
            show raoni alegre
            raoni "Até parece que você também teve tempo de banho, hahah. Que nada, aqui é festa! A ideia é soltar a fera, balançar a cauda e rugir alto!"
            I "Raoni solta um grito, fazendo umas cinco pessoas em volta saltarem de susto."
            I "Ela gargalha e então crava seus olhos felinos quase que de um esmeralda cristalino sobre mim."
            show raoni neutro
            raoni "E você? Está na prontidão de festejar até a noite cair?"
            I "Os olhos dela piscam apenas uma vez e voltam a cravar sobre mim."
            menu:
                "Balanço a cabeça afirmativamente":
                    show raoni alegre
                    raoni "Então vamos para o centro da roda!"
                    #desvio para proseguimento de romance
                    jump festaRaoni

                "Retribuo o olhar em desafio" if Possante:
                    I "Abro um sorriso fanfarrão e grito para Raoni, “Vamos dançar! E garanto que vou dançar mais do que você!”"
                    show raoni alegre
                    I "A garota repuxa os dentes, numa gargalhada quase que feral."
                    raoni "Ha! Aceito o desafio! Vamos ver se você tem garras para segurar a noite toda!"
                    jump festaRaoni
                "Viro o rosto, com medo dela":
                    menu:
                        "Seus olhos são horríveis e assustadores":
                            show raoni triste
                            raoni "..."
                            I "Ela olha para mim, sem palavras para serem ditas."
                            raoni "..."
                            I "Algumas lágrimas se formam no cristalino do olho."
                            raoni "..."
                            hide raoni
                            I "Ela se transforma em fera e, rapidamente, foge da festa. Muitos rostos se viram para mim, irritados e acusadores."
                            I " Acabo também saindo, antes que alguma coisa aconteça."
                            I "Essa primeira experiência na escola foi estranha, mas tenho certeza que muitas outras histórias me aguardam no futuro!"
                            jump creditos
                            #fim dessa linha
                        "Desculpe...mas acho que prefiro ficar só":
                            show raoni triste
                            raoni "Ah...tudo bem...desculpa qualquer coisa"
                            I "Me afasto da garota de olhos selvagens e resolvo então passar o resto da festa só."
                            I "Essa primeira experiência na escola foi estranha, mas tenho certeza que muitas outras histórias me aguardam no futuro!"
                            jump creditos
                            #fim dessa linha

        "Passar a festa com Jhoul" if amigoJhoul:
            jump festaJhoul


#INTERAÇÂO COM JHOUL NA FESTA
label festaJhoul:
    scene bg patio
    #caso tenha entregado o panfleto a opção estará livre
    I "Depois de olhar em volta, acabo encontrando um rosto conhecido"
    show jhoul neutro
    Jhoul "Olá, [Nome], que bom que você pôde vir para a festa. Então, conseguiu explorar a escola?"
    I "Conto ao Jhoul como foi meu dia e as coisas que descobri. O garoto sorri, sua capa vermelha balançando"
    show jhoul alegre
    Jhoul "Parece então que você aproveitou o dia! Mas sabe, ainda há muita coisa para se ver aqui no colégio. O refeitório está sempre cheio de gente."
    Jhoul " Nas salas dos professores costuma acontecer um monte de coisa estranha."
    Jhoul "Temos também os laboratórios de supertecnologia – só cuidado para não sujar lá, ou o professor Bit vai acabar contigo, talvez literalmente"
    I "Jhoul dá uma risada nervosa antes de prosseguir."
    show jhoul neutro
    Jhoul "Temos a residência também, onde ficam os alunos bolsistas e militares, e o quartel, e biblioteca, as quadras..."
    Jhoul "ah, não dá pra esquecer do subsolo, onde ficam as arenas para combates intensivos."
    Jhoul "Enfim, há muita coisa para ver, quem sabe num outro dia, não é mesmo?"
    menu:
        "Sim, tenho ainda muita coisa para ver!":
            show jhoul alegre
            Jhoul "Esse é o espírito! E no que eu puder te ajudar, pode contar comigo!"
            I "Junto ao Jhoul, passei o resto da festa."
            I "Ele me mostrou mais alunos do Colégio, contou-me de suas aventuras e agora, mais do que nunca, mal posso esperar pelas histórias que irei presenciar!"
            jump creditos
            #fim dessa linha
        "Sim, e você poderia ir ver comigo, não é?":
            #OPÇÂO DE ROMANCE COM JHOUL CASO TENHA A APARENCIA FEMININA
            show jhoul alegre
            if masculino:
                Jhoul "Claro que sim! Vou adorar mostrar a escola para meu novo amigo!"
            if feminino:
                Jhoul "Claro que sim! Vou adorar mostrar a escola para minha nova amiga!"
            menu:
                "Sim, tenho ainda muita coisa para ver!":
                    Jhoul "Esse é o espírito! E no que eu puder te ajudar, pode contar comigo!"
                    I "Junto ao Jhoul, passei o resto da festa."
                    I "Ele me mostrou mais alunos do Colégio, contou-me de suas aventuras e agora, mais do que nunca, mal posso esperar pelas histórias que irei presenciar!"
                    jump creditos
                    #fim dessa linha
                "Isso seria muito bom...aí podíamos ficar mais juntos, não é?":
                    if Afeminino:
                        show jhoul envergonhado
                        Jhoul "Sim, podemos ficar mais juntos! Isso mesmo, podemos...espera...você quer dizer?"
                        I "Olho nos olhos vermelhos dele e sorrio, me aproximando mais. O garoto parece ficar bem nervoso, mas não se afastas."
                        I "Seguindo a música, coloco as mãos na cintura dele. Este, por sua vez, coloca as mãos em meus ombros. Estamos sorrindo, e nossos rostos se aproximam."
                        I "Eitaaa! Vai Jhoul!”, uma voz estridente consegue gritar mais alto que as caixas de som, “mostra sua apalpada telecinética! Vai fundo meu garoto lindo!”"
                        I "Jhoul dá um salto pra trás."
                        show jhoul bravo
                        Jhoul "Piruleta! Pare de ser chato!"
                        show jhoul envergonhado
                        I "Depois, o garoto olha para mim, sorrindo um pouco tímido."
                        Jhoul "Então...bem...o que acha de...bom...dançar?"
                        I "Balanço a cabeça afirmativamente, sorrindo."
                        I "Sabe, tenho certeza que muitas histórias me esperam no Colégio de Heróis de São Paulo, e essa será apenas a primeira delas…"
                        jump creditos
                        #fim dessa linha
                    #JHOUL REJEITA JOGADOR E DIEGO APARECE
                    if Amasculino:
                        show jhoul envergonhado
                        Jhoul "Oh...nossa..."
                        I "o garoto abre um sorriso envergonhado."
                        Jhoul "Você é uma pessoa bem legal, e me ajudou bastante hoje."
                        Jhoul "Não tenho problema de mostrar a escola para você...mas eu não creio que poderia mostrar desse modo, entende?"
                        Jhoul "Tão junto. Eu não sou atraído desse jeito e tal"
                        I "o garoto começa a tropeçar nas palavras."
                        Jhoul "Mas isso não quer dizer que você não seja legal! É só que, bom, eu não sou assim. Entende?"
                        menu:
                            "Olho para o chão, envergonhado":
                                show jhoul alegre
                                Jhoul "Olha, não fica assim. Depois te apresento a uns amigos que tenho certeza que você vai gostar, certo? Vamos curtir a festa por agora!"
                                I "Apesar do primeiro momento embaraçoso, depois ficou legal. Junto ao Jhoul, passei o resto da festa."
                                I "Ele me mostrou mais alunos do Colégio, contou-me de suas aventuras e agora, mais do que nunca, mal posso esperar pelas histórias que irei presenciar!"
                                jump creditos
                            "Antes que o Jhoul perceba, sumo da vista dele." if Furtivo:
                                show jhoul neutro
                                Jhoul "Ué...pra onde ele foi?"
                                hide jhoul neutro
                                scene bg bosque
                                I "Caminho para o bosque da escola – deixei aquela festa idiota de lado."
                                I "Olho para as árvores, ainda irritado com o que ocorreu, procurando algo para fazer, quando vejo uma figura ao longe também caminhando. Ela acena."
                                I "“Vejo que você também parece ter se cansado daquela barulheira, sim?”."
                                I "É um rapaz alto, usando um uniforme bem diferente..."
                                I "parece uma versão mais antiga do uniforme da escola, com um traço até mesmo, como eu poderia dizer? Aristocrático."
                                I "Eu sou o Diego. Vejo que é um aluno novo, sim? Muito bem, muito bem, por que não caminhamos um pouco?"
                                I "Sorrindo, me aproximo dele. Muitas outras histórias me esperam no Colégio de Heróis de São Paulo, e essa será apenas a primeira delas…"
                                jump creditos

        "Nah, acho que não quero mais saber de escola":
            show jhoul triste
            Jhoul "Nossa...hum...ok"
            I "E depois de falar isso, fiquei em silêncio. E o silêncio reinou. Foi estranho e bizarro para todo mundo."
            jump creditos
            #fim dessa linha


#INTERAÇÃO DE ROMANCE COM RAONI
label festaRaoni:
    scene bg patio
    I "Raoni me leva para o centro da roda de dança. Vejo diversos alunos piruetando e dando cambalhotas em passos complexíssimos de dança."
    I "Outros, contudo, são bem mais desengonçados. No caminho esbarro numa garotinha bem pequena, derrubando-a sem querer no chão."
    I "Os amigos dela – um garoto com cabelo de cuia e uma menina com um olho só na testa – se aproximam falando: “Você derrubou Samsa! Ela vai acabar com você!!”"
    I "A garotinha se levanta, com um sorriso no rosto."
    I "“Não foi nada, eu que fui desastrada. Desculpa”. Antes que eu pudesse falar qualquer coisa, Raoni entra no meio das três crianças, as empurrando enquanto dança."
    show raoni neutro
    raoni "E então? Quando vai começar a balançar a cauda, hein?"
    menu:
        "Dou uma risada e começo a dançar":
            I "E assim, junto com a Raoni, passo o resto da festa dançando."
            I "Depois ela me mostrou mais alunos do Colégio, contou-me de suas aventuras e agora, mais do que nunca, mal posso esperar pelas histórias que irei presenciar aqui no futuro!"
            #fim dessa interação com raoni
            jump creditos
        "Estou esperando você chegar mais pertinho":
            if Amasculino:
                show raoni envergonhada
                I "Raoni dá um sorriso, chegando mais próximo, colocando as mãos em minha cintura"
                raoni "Não sabia que você era assim, [Nome]. Então, isso é perto o suficiente?"
                I "Dou um sorriso, colocando as mãos no ombro dela."
                I "Não muito, ainda podia ser mais perto”, digo, aproximando o rosto do dela."
                raoni "Mais perto você diz..."
                I "Ela se aproxima do meu rosto, vejo ela lentamente fechando os olhos."
                raoni "E para eu chegar mais perto...você vai ter que me pegar!"
                hide raoni envergonhada
                I "Num movimento rápido, a garota se afasta e se transforma em fera. Ela então se vira contra mim, balançando a cauda, como em desafio."
                I "Dou uma risada, ativo os poderes, e vou atrás dela. Ela, por sua vez, dispara, comigo em seu encalço."
                I "Sabe, tenho certeza que muitas histórias me esperam no Colégio de Heróis de São Paulo, e essa será apenas a primeira delas!"
                jump creditos

            if Afeminino:
                I "Raoni olha para mim, de cima a baixo, e dá um sorriso amigável."
                raoni "Desculpa...mas hoje não quero dançar junto assim não. Mas, se quiser, ainda podemos dançar, que me diz?"
                menu:
                    "Dou uma risada e começo a dançar":
                        I "E assim, junto com a Raoni, passo o resto da festa dançando."
                        I " Depois ela me mostrou mais alunos do Colégio, contou-me de suas aventuras e agora, mais do que nunca, mal posso esperar pelas histórias que irei presenciar aqui no futuro!"
                        #fim dessa linha
                        jump creditos
                    "Faço uma pose chamativa e olho Raoni nos olhos" if Estiloso:
                        I "“Poxa, mas é tão melhor dançar juntinho, não acha?”, falo para a garota com olhos de fera."
                        show raoni envergonhada
                        raoni "Er...hum...talvez, não sei...bom...té depois"
                        hide raoni envergonhada
                        I "E assim, meio entre gaguejadas, a garota se transforma em sua forma animal e foge da festa."
                        I "Droga! E agora estou aqui, sozinha, fazendo nada. Tudo porque queria mais proximidade. Quanta injustiça."
                        I "Nesse momento, sinto um toque levíssimo resvalando em minha nuca. Arrepio do topo da cabeça ate o dedinho do pé."
                        I "Quando me viro para trás e observo quem seria, fico paralisada."
                        I "Uma das alunas está flutuando acima do solo, com um vestido de festa balançando como se tivesse debaixo da água."
                        I "Ela é linda – mais que isso, ela é impossivelmente linda. Não consigo me mexer nem fazer nada, só olhar para aquela figura perfeita."
                        I "Ela ri e então me fita com olhos roxos claros"
                        I "“Me parece que você é nova por aqui, sim?” Apenas consigo balançar a cabeça em silêncio"
                        I "“Eu sou Nathália...mas todos aqui me conhecem por Fada. Trabalho na enfermaria do colégio, sou aluna do 3o ano."
                        I "Então, vi que você estava querendo dançar, não é?”."
                        I "Apenas consigo balançar a cabeça em silêncio. “Que maravilha, pois eu também”, a Fada chega mais perto, levitando, suas mãos envolvendo minha cintura."
                        I "“Muito melhor dançar juntinho, não acha?”. Abro um cúmplice sorriso."
                        I "Sabe, tenho certeza que muitas histórias me esperam no Colégio de Heróis de São Paulo, e essa será apenas a primeira delas…"
                        jump creditos


label creditos:
    "Obrigado por chegar ao Fim!"
    $ renpy.movie_cutscene("video.webm")
    return

screen mapa(): #Prepara o mapa
    imagemap:
        ground "mapa.png"
        hover "mapahotspot.png"

        hotspot (47, 87, 413, 232) clicked Jump("bosque")
        hotspot (107, 413, 453, 254) clicked Jump("patio")
        hotspot (721, 233, 512, 288) clicked Jump("Entrada")

label mapa:
    if not Welcome:
        play music "Welcome.mp3"
    call screen mapa

return
