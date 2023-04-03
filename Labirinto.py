import pygame
from random import randint

nome = str(input('Seja bem vindo ao Labirinto!  Qual é o seu nome? '))
q1 = str(input('Olá, {}! Está preparado para começar? (s/n) '.format(nome)))
print('')

if q1 == 'n':
    input('Então aperta enter e fecha essa merda, bocó!')

elif q1 == 's':

    print('Então vamos lá! Eu sou o Tony e te acompanharei no percurso. O prêmio para o vencedor é um playstation do'
          ' Yudi. Pode ter certeza que estarei torcendo... Contra você, é claro.')
    print('.')
    print('.')
    print('.')
    print('BOOM')
    print('- em um passe de mágica você vira uma galinha e cai em um labirinto gigante com paredes de pedra e chão '
          'lamacento. ')
    print('   ')
    print("Tony: Você não é o único a aceitar esse desafio. Muitos tentaram e eu, em meus 457 anos de vida, "
          "nunca vi um vencedor. Escape desse buraco ou morra tentando (é o que espero que aconteça).")
    q2 = str(input('Chegou a hora de tomar a sua primeira decisão. Na sua frente há dois caminhos. Os dois são escuros '
                   'e nojentos. Pra qual você vai: 1 ou 2? '))

    if q2 == '1':

        pygame.init()
        pygame.mixer.music.load('es/esd.mp3')  # inserir música
        pygame.mixer.music.play()
        pygame.event.wait()

        input('Tony: Você da de cara com uma panela escaldante de canja esperando por você. Morreu, brother, que '
              'felicidade, eu sabia que você não era capaz :)! Aperte enter pra sair.')

    elif q2 == '2':

        print('Tony: Droga, você achou um punhado de milho. Coma e prossiga.')
        q3 = str(input('Dessa vez há 3 caminhos para seguir, escolha 1, 2 ou 3: '))
        print('   ')

        if q3 == '1':
            print('Tony: Um fazendeiro com um machadinho te encara friamente e diz que a única forma de salvar sua '
                  'vida é acertando a pergunta que ele irá fazer.')
            print('   ')
            q4 = input('Fazendeiro Carlos: Qual a peça de roupa que a galinha usa? ')

            if q4 == 'saia':

                print('Tony: Maldição! Essa foi por pouco. O fazendeiro foi pra casa triste e sem jantar.')
                print('   ')
                print('Tony: Calma que ainda não acabou, {}'.format(nome))
                print('   ')
                q6 = str(input('Escolha novamente, seu merdinha, 1 ou 2?'))

                if q6 == '1':

                    print('Dessa vez quem te espera é a esposa do fazendeiro com uma faquinha. A única forma de se '
                          'salvar é respondendo à pergunta dela.')
                    print('   ')
                    q7 = input("Muié do Fazendeiro: Qual é a peça de roupa que o galo usa?  ")

                    if q7 == 'paletó':

                        print('Tony: {}, você é uma galinha safada!! A muié vai ter que comer torrada na janta.'.format(
                            nome))
                        print('   ')
                        print('Desviando dela, vc encontra uma luz, vai em direção à ela e acha a saída.')

                        pygame.init()
                        pygame.mixer.music.load('es/esv.mp3')  # inserir música
                        pygame.mixer.music.play()
                        pygame.event.wait()

                        print('Tony: Odeio ter que dizer isso, mas você ganhou essa porcaria!')
                        print('Tony: O playstation do Yudi chegará em sua casa um dia desses aí.')
                        print('   ')
                        print('- Após te dar um tapa na bunda, Tony te transforma novamente em humano.')
                        input('Aperte enter para sair.')

                    else:

                        pygame.init()
                        pygame.mixer.music.load('es/esd.mp3')  # inserir música
                        pygame.mixer.music.play()
                        pygame.event.wait()

                        input('A muié te meteu a faca!  Morreu, brother, que felicidade, eu sabia que você não era '
                              'capaz :)! Aperte enter pra sair. ')

                elif q6 == '2':

                    q8 = input('Tony: AFF, já tô cansando disso, você não morre nunca! Pra onde você vai agora? '
                               'esquerda ou direita?')
                    print('   ')

                    if q8 == 'esquerda':

                        pygame.init()
                        pygame.mixer.music.load('es/esd.mp3')  # inserir música
                        pygame.mixer.music.play()
                        pygame.event.wait()

                        input('Morreu seu comunista de merda!! Que delícia. Aperte enter para sair.')

                    elif q8 == 'direita':

                        print('Meu deus, morre logo, {}, eu não te aguento mais!'.format(nome))
                        print('   ')
                        q9 = input('Escolhe logo essa merda porque eu já estou sem saco pra você. Caminho 1, 2 ou 3?')
                        print('   ')

                        if q9 == '1':

                            pygame.init()
                            pygame.mixer.music.load('es/esd.mp3')  # inserir música
                            pygame.mixer.music.play()
                            pygame.event.wait()

                            input('Tony: Uma raposa te comeu! Finalmente, perdeu, otário(a). Aperte enter pra sair.')

                        elif q9 == '2':

                            q10 = input(
                                'Você achou um galo!! Ele está preso no labirinto há décadas. Deseja ajudá-lo? (s/n)')

                            if q10 == 's':

                                print(
                                    'Tony: Aprenda uma coisa, {}, nessa vida a gente não deve ajudar ninguém. O galo '
                                    'era um cachorro fantasiado e te comeu.')
                                print('   ')

                                pygame.init()
                                pygame.mixer.music.load('es/esd.mp3')  # inserir música
                                pygame.mixer.music.play()
                                pygame.event.wait()

                                input('Estou muito feliz que você perdeu. Aperte enter para sair.')

                            elif q10 == 'n':

                                print(
                                    'Tony: O egoísmo salva vidas! O galo era um cachorro fantasiado. Ao desviar dele'
                                    ' vc avista uma luz')
                                print('   ')

                                pygame.init()
                                pygame.mixer.music.load('es/esv.mp3')  # inserir música
                                pygame.mixer.music.play()
                                pygame.event.wait()

                                print('Tony: Odeio ter que dizer isso, {}, mas você ganhou essa porcaria!'.format(nome))
                                print('Tony: O playstation do Yudi chegará em sua casa um dia desses aí.')
                                print('   ')
                                print('- Após te arrancar uma pena, Tony te transforma novamente em humano.')
                                input('Aperte enter para sair.')

                        elif q9 == '3':

                            print('Você se depara com um monte de pintinhos. E eles têm uma pergunta pra fazer:')
                            print('   ')
                            q11 = input('Quem nasceu primeiro, o ovo ou a galinha? ')

                            if q11 == ' o ovo' or q11 == 'O ovo' or q11 == 'Ovo' or q11 == 'ovo':

                                print('Tony: Tenho que admitir que você é muito bom, {}. Nada impede que seja um ovo de'
                                      ' dinossauro'.format(nome))
                                q12 = input('Escolha o errado, por favor. Caminho 1 ou 2')

                                if q12 == '1':
                                    print('Tony: Hora hora se não temos uma galinha ninja por aqui... Pra mim vc já foi'
                                          ' longe demais, por isso, passar daqui vai ser sorte')
                                    print('O computador sorteará um número de 1 a 10. vc só passará caso tire >= a 5. '
                                          'Eu sou muito babaca, eu sei')

                                    sorte = randint(1, 10)

                                    if sorte >= 5:

                                        q13 = input('Vc nasceu com o cu virado pra lua, {}. Escolha outro caminho: '
                                                    'esquerda ou direita? '.format(nome))

                                        if q13 == 'esquerda' or q13 == 'Esquerda':

                                            print('Tony: Deu sorte que hoje eu estou bem petista')
                                            print('Você avista um pastor de ovelhas e ele faz a seguinte pergunta: ')
                                            q14 = input('Pastor: Eu estou sem óculos, você é uma de minhas ovelhas?'
                                                        ' (s/n)')

                                            if q14 == 's':

                                                print('Então vambora, a saída e por ali!')
                                                print('   ')
                                                print('Tony: O miserável é um gênio!! Sabe que a mentira te leva à '
                                                      'vitória')

                                                pygame.init()
                                                pygame.mixer.music.load('es/esv.mp3')  # inserir música
                                                pygame.mixer.music.play()
                                                pygame.event.wait()

                                                print(
                                                    'Tony: O playstation do Yudi chegará em sua casa um dia desses aí.')
                                                print(
                                                    'Com 3 estalos de dedos e um shot de tequila, Tony te transforma'
                                                    ' novamente em humano.')
                                                input('Aperte enter para sair.')

                                            elif q14 == 'n':

                                                print('Pastor: Então você vai ser minha janta!')
                                                print('   ')
                                                print('Tony: Você é muito ingênuo. Ainda não aprendeu que nunca deve'
                                                      ' ser sincero?')
                                                print('   ')

                                                pygame.init()
                                                pygame.mixer.music.load('es/esd.mp3')  # inserir música
                                                pygame.mixer.music.play()
                                                pygame.event.wait()

                                                input('Mas fico feliz por você ter morrido. Aperte enter para sair.')

                                    else:

                                        pygame.init()
                                        pygame.mixer.music.load('es/esd.mp3')  # inserir música
                                        pygame.mixer.music.play()
                                        pygame.event.wait()

                                        input('Tony: {}, fico contente em dizer que você vc perdeu! Aperte enter para '
                                              'sair.'.format(nome))

                                elif q12 == '2':
                                    print('Tony: ao ir nessa direção você avista uma luz, mas na frente dela você '
                                          'encontra ninguém mais ninguém menos que eu!!')
                                    print('   ')
                                    print('É um desprazer te conhecer, {}. Para passar por mim você terá uma difícil'
                                          ' missão: me vencer no jokempô!!!'.format(nome))

                                    itens = ('Pedra', 'Papel', 'Tesoura')
                                    tony_jogada = randint(0, 2)

                                    print('''Escolha: 
                                    [0] Pedra
                                    [1] Papel
                                    [2] Tesoura''')

                                    jogador = int(input(''))
                                    print('''
                                    jo
                                    ken
                                    pô!!''')
                                    print('-=' * 11)
                                    print('{} jogou: {}'.format(nome, itens[jogador]))
                                    print('Tony jogou: {}'.format(itens[tony_jogada]))
                                    print('-=' * 11)
                                    if tony_jogada == 0:

                                        if jogador == 0:
                                            print('EMPATE!')
                                            print('-=' * 11)
                                            print('')
                                            print(
                                                'Ora ora, {}, como a programadora ainda não sabe fazer estrutura de '
                                                'laço de repetição, vou considerar um empate a sua derrota! Vou'
                                                ' realizar o meu maior desejo: te matar.'.format(
                                                    nome))
                                            pygame.init()
                                            pygame.mixer.music.load('es/esd.mp3')  # inserir música
                                            pygame.mixer.music.play()
                                            pygame.event.wait()
                                            input(
                                                '- Tony te pega pelas asas e te chacoalha até a morte. Aperte enter'
                                                ' para sair.')

                                        elif jogador == 1:
                                            print('VOCÊ GANHOU!')
                                            print('-=' * 11)
                                            print('')
                                            print('Sua galinha fedida de merda!!! Deu muita sorte')

                                            pygame.init()
                                            pygame.mixer.music.load('es/esv.mp3')  # inserir música
                                            pygame.mixer.music.play()
                                            pygame.event.wait()

                                            input(
                                                '- Tony, após te transformar em humano, abre espaço para que você possa'
                                                ' passar e chegar à saída. Aperte enter para sair.')

                                        elif jogador == 2:
                                            print('TONY GANHOU!')
                                            print('-=' * 11)
                                            print('')
                                            print('HÁHÁHÁ seu merdinha!! Vou finalmente poder te matar, que alegria.')

                                            pygame.init()
                                            pygame.mixer.music.load('es/esd.mp3')  # inserir música
                                            pygame.mixer.music.play()
                                            pygame.event.wait()

                                            print('')
                                            input(
                                                '- Tony, Te parte em pedaços usando suas próprias unhas nojentas. '
                                                'Aperte enter para sair.')

                                    elif tony_jogada == 1:

                                        if jogador == 0:

                                            print('TONY GANHOU!')
                                            print('-=' * 11)
                                            print('')
                                            print('HÁHÁHÁ seu merdinha!! Vou finalmente poder te matar, que alegria.')

                                            pygame.init()
                                            pygame.mixer.music.load('es/esd.mp3')  # inserir música
                                            pygame.mixer.music.play()
                                            pygame.event.wait()

                                            print('')
                                            input(
                                                '- Tony, Te parte em pedaços usando suas próprias unhas nojentas. '
                                                'Aperte enter para sair.')
                                        elif jogador == 1:

                                            print('EMPATE')
                                            print('-=' * 11)
                                            print('')
                                            print(
                                                'Ora ora, {}, como a programadora ainda não sabe fazer estrutura de'
                                                ' laço de repetição, vou considerar um empate a sua derrota! Vou '
                                                'realizar o meu maior desejo: te matar.'.format(
                                                    nome))

                                            pygame.init()
                                            pygame.mixer.music.load('es/esd.mp3')  # inserir música
                                            pygame.mixer.music.play()
                                            pygame.event.wait()

                                            input(
                                                '- Tony te pega pelas asas e te chacoalha até a morte. Aperte enter'
                                                ' para sair.')

                                        elif jogador == 2:

                                            print('VOCÊ GANHOU!')
                                            print('-=' * 11)
                                            print('')
                                            print('Sua galinha fedida de merda!!! Deu muita sorte')

                                            pygame.init()
                                            pygame.mixer.music.load('es/esv.mp3')  # inserir música
                                            pygame.mixer.music.play()
                                            pygame.event.wait()

                                            input(
                                                '- Tony, após te transformar em humano, abre espaço para que você possa'
                                                ' passar e chegar à saída. Aperte enter para sair.')



                                    elif tony_jogada == 2:

                                        if jogador == 0:
                                            print('VOCÊ GANHOU!')
                                            print('-=' * 11)
                                            print('')
                                            print('Sua galinha fedida de merda!!! Deu muita sorte')

                                            pygame.init()
                                            pygame.mixer.music.load('es/esv.mp3')  # inserir música
                                            pygame.mixer.music.play()
                                            pygame.event.wait()

                                            input(
                                                '- Tony, após te transformar em humano, abre espaço para que você possa'
                                                ' passar e chegar à saída. Aperte enter para sair.')

                                        elif jogador == 1:
                                            print('TONY GANHOU!')
                                            print('-=' * 11)
                                            print('')
                                            print('HÁHÁHÁ seu merdinha!! Vou finalmente poder te matar, que alegria.')

                                            pygame.init()
                                            pygame.mixer.music.load('es/esd.mp3')  # inserir música
                                            pygame.mixer.music.play()
                                            pygame.event.wait()

                                            input(
                                                '- Tony, Te parte em pedaços usando suas próprias unhas nojentas. '
                                                'Aperte enter para sair.')

                                        elif jogador == 2:
                                            print('EMPATE')
                                            print('-=' * 11)
                                            print('')
                                            print(
                                                'Ora ora, {}, como a programadora ainda não sabe fazer estrutura de'
                                                ' laço de repetição, vou considerar um empate a sua derrota! Vou'
                                                ' realizar o meu maior desejo: te matar.'.format(
                                                    nome))
                                            pygame.init()
                                            pygame.mixer.music.load('es/esd.mp3')  # inserir música
                                            pygame.mixer.music.play()
                                            pygame.event.wait()
                                            input(
                                                '- Tony te pega pelas asas e te chacoalha até a morte. Aperte enter '
                                                'para sair.')



                        else:

                            input('ERRO 245 reinicie o jogo')
            else:

                pygame.init()
                pygame.mixer.music.load('es/esd.mp3')  # inserir música
                pygame.mixer.music.play()
                pygame.event.wait()

                input('Tony: O fazendeiro te dá uma machadada no pescoço. Morreu, brother, que felicidade, eu sabia que'
                      'você não era capaz :)! Aperte enter pra sair.')
        elif q3 == '2':

            print('Tony: Cacete, {}, você é uma galinha esperta.'.format(nome))
            q5 = input('Na sua frente há mais duas opções de caminho. Escolha 1 ou  2')
            if q5 == '1':

                pygame.init()
                pygame.mixer.music.load('es/esd.mp3')  # inserir música
                pygame.mixer.music.play()
                pygame.event.wait()

                input('Graças a deus! Você caiu de um penhasco.  Morreu, brother, que felicidade, eu sabia que você'
                      ' não era capaz :)! Aperte enter pra sair.')
            elif q5 == '2':
                print('Tony: Eu não acredito que eu vou dizer isso, seu desgraçado, mas você achou a saída!!')

                pygame.init()
                pygame.mixer.music.load('es/esv.mp3')  # inserir música
                pygame.mixer.music.play()
                pygame.event.wait()

                print('Tony: O playstation do Yudi chegará em sua casa um dia desses aí.')
                print('Com 3 estalos de dedos e um shot de tequila, Tony te transforma novamente em humano.')
                input('Aperte enter para sair.')
            else:
                input('ERRO 245 reinicie o jogo')
        elif q3 == '3':

            pygame.init()
            pygame.mixer.music.load('es/esd.mp3')  # inserir música
            pygame.mixer.music.play()
            pygame.event.wait()

            input('Se fudeu, otário, um gavião te comeu.  Morreu, brother, que felicidade, eu sabia que você não era'
                  ' capaz :)! Aperte enter pra sair.')
    else:
        input('ERRO 245 reinicie o jogo')
else:
    input('ERRO 245 reinicie o jogo')
