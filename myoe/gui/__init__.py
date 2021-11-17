import myoe

eco = 3
ex = 4
rel = 5
soc = 6
opts = [
    ['A religiosidade anda em baixa no reino.', 'Devemos punir os hereges?', '', 'Sim', 'Não', [rel, 2, -2], [soc, -2, 0]],
    ['Nossas tropas estão com o pagamento atrasado.', 'Devemos resolver isso?', '', 'Sim', 'Não', [ex, 2, -2], [eco, 1, -1]],
    ['Seu povo está enfraquecendo.', 'Devemos investir no bem-estar social?', '', 'Sim', 'Não', [soc, 2, -1], [eco, -1, 0]],
    ['Nossos rendimentos foram ótimos nessa última colheita.', '', '', 'Investir na sociedade', 'É tudo meu', [eco, 0, -2], [soc, 2, -1]],
    ['Há pagãos não muito distante de vosso reino.', 'O que devemos fazer?', '', 'Construir mais igrejas', 'Não é nosso problema', [rel, 2, -1], [soc, 1, -1]],
    ['Cultos clandestinos estão se proliferando pelo reino…', '', '', 'Acendam o fogo da inquisição', 'Torture-os', [rel, 1, -1], [soc, -1, -1]],
    ['A população está pedindo por democracia.', 'O que devemos fazer?', '', 'Nada', 'Prenda-os', [soc, -1, -3], [ex, -1, 2]],
    ['Rola um boato no reino de que o senhor anda meio... autoritário.', '', '', 'Não me importo', 'Me dê nomes, farei pagar por tal calúnia', [soc, -1, -2], [ex, 0, 2]],
    ['Estrangeiros estão trazendo uma cultura pagã.', 'O que devemos fazer?', '', 'Queime-os', 'Viva a liberdade', [rel, 1, -2], [soc, -1, 2]],
    ['Temos territórios estratégicos próximo ao reino do norte.', 'Poderíamos tomar proveito dessa vantagem…', '', 'Construa bases militares nessa região', 'Acho melhor não', [ex, 2, -1], [eco, -1, 0]],
    ['O reino do norte está desconfiado da movimentação de nossas tropas.', '', '', 'Devemos propor um tratado de paz', 'Não devo explicação a ninguém', [ex, -1, 1], [soc, 1, -1]],
    ['Curandeiros do reino dizem que têm a cura da peste que nos assombra há décadas.', '', '', 'Ótimo, coloque o plano em ação', 'Balela! Isso está além da compreensão humana', [soc, 2, -2], [rel, -1, 2]],
    ['Ótimas notícias, nossos mineradores encontraram metais preciosos', '', '', 'Estamos ricos', 'Estou rico', [eco, 2, 0], [soc, 2, -2]],
    ['Os médicos dizem que temos um grande problema sanitário.', 'Precisamos tratar a água que bebemos.', '', 'Vamos investir na saúde da população', 'Não precisamos nos preocupar com isso', [soc, 2, -2], [eco, -1, 1]],
    ['Devemos investir no ensino religioso nas escolas?', '', '', 'Sim', 'Não', [rel, 1, -1], [soc, 1, -1]],
    ['Tropas inimigas avistadas no norte.', 'O que devemos fazer?', '', 'Feche os portões', 'Ataque-os de volta', [ex, 1, -1], [soc, -1, 1]],
    ['Um reino próximo está pedindo ajuda para se recuperar de um ataque.', '', '', 'Ajudar', 'Não é problema nosso', [ex, -1, 1], [eco, -1, 1]],
    ['Um estranho está querendo comprar parte de suas terras', '', '', 'Aceitar', 'Rejeitar', [eco, 2, 0], [ex, -1, 2]],
    ['Um mago desconhecido está oferecendo ajuda contra o terrível dragão.', '', '', 'Aceitar', 'Rejeitar', [ex, 1, 0], [rel, -2, 2]],
    ['A cidade está muito perigosa ultimamente.', 'Devemos aumentar a vigilância nas ruas?', '', 'Sim', 'Não', [ex, 1, -1], [soc, 1, -1]],
    ['Muitas pessoas querem se redimir de seus pecados.', 'Devemos aumentar o preço do dízimo', '', 'Sim', 'Não', [rel, 2, -1], [soc, -1, 1]],
    ['Tem certeza que deseja excluir todo o seu progresso?', '', '', 'Sim', 'Não', '0 - Excluir progresso', '9 - Mudar nome', '1 - ', '2 - ']
]

hint = [
    ['',
    'Sinto muito por ontem, ninguém poderia imaginar que aquilo iria acontecer...',
    'Ele foi o melhor rei que nosso império já viu.',
    'Não entendo porquê ele tentou fazer aquilo com o macaco...',
    ''],

    ['Mas não podemos desanimar, temos muito trabalho para fazer.',
    'Como você é o único herdeiro, o reino agora pertence a ti.',
    'Você poderia ter a ajuda do seu irmão se ele não fosse tão burro...',
    'Tentar adestrar um dragão...? Que péssima ideia...',
    ''],

    ["Sou Irineu, 'O Conselheiro'.",
    'Sempre que precisar eu estarei aqui para lhe auxiliar!',
    'Será uma árdua tarefa manter a ordem depois do furdúncio que ocorreu ontem.',
    'Tome suas decisões com sabedoria para deixar seu povo feliz e manter sua popularidade.',
    'Caso contrário, sua população ficara infeliz e seu reinado entrará em colapso.']
]

death = [
    [['Seu governo foi tomado pela corrupção.', 'Você foi condenado à pena de morte.'],
    ['Sua ganância foi longe demais, lucrar em cima da ilegalidade?', 'Você foi morto pela máfia.']],
    
    [['Seu exército ficou tão debilitado que o reino vizinho invadiu suas terras.', 'E eles não tiveram piedade...'],
    ['Seu exército ganhou tanta força que instaurou uma ditadura militar.', 'Eles dizem que você conseguiu fugir...']],
    
    [['As igrejas foram praticamente extintas, o vazio pairava pelo ar.', 'Um grupo de radicais te mata após queimar bíblias em praça pública.'],
    ['Os líderes religiosos dizem que só Deus tem o direito de dar e tirar a vida.', 'Um grupo de radicais te mata pela sua posição sobre pena de morte.']],
    
    [['A sociedade entrou em colapso. Eles imploram por vacinas.', 'Você foi mais uma vítima da gripe espanhola.'],
    ['A sociedade evoluida?', 'Seu povoado evoluiu tanto que não precisa mais de um líder.']]
]


def main_menu(i, x = opts):
    nome = myoe.save.read_save(0)
    dias = myoe.save.read_save(2)
    eco = myoe.util.show_st(3)
    ex = myoe.util.show_st(4)
    rel = myoe.util.show_st(5)
    soc = myoe.util.show_st(6)
    opt0 = opts[len(opts) - 1][5]
    opt9 = opts[len(opts) - 1][6]
    if myoe.save.read_save(1) == 'True':
        irineu = 'O Conselheiro'
    else:
        irineu = 'Desconhecido'
    if x == opts:
        x1 = opts[len(opts) - 1][7] + x[i][3]
        x2 = opts[len(opts) - 1][8] + x[i][4]
    else:
        x1 = x[i][3]
        x2 = x[i][4]
    print(f'''\
v=====================================================================================================================<
|{f'Seja bem-vindo, {nome}. Este é o seu reino.'.center(118)}
|{f'Você está há {dias} dias no poder.'.center(118)}
|=====================================================================================================================+
|                                                                                     |
|         _                  .                   __                                   |
|      __|_|___             / \                 |  |                o      ~o         |{'Outras opções:'.center(32)}
|     (  _____/             |.|              ___|  |___            <|\     /|\        |
|     | (|_|__              |:|             |___    ___|            |   ~o/ | \o      |
|     (_____  )             |:|                 |  |                |\  /|  |\ |\     |
|     /\_|_|) |          `-=<o>=-´              |  |               / |  / \ |// \     |
|     \_______)              |                  |  |              `` ` ```  ` ` ``    |
|        |_|                 °                  |__|               ``  ``  ` ``` `    |
|                                                                                     |
|     Economia           Exército             Religião                Sociedade       |
|                                                                                     |{opt9.center(32)}
|   [{eco}]       [{ex}]         [{rel}]            [{soc}]      |{opt0.center(32)}
|                                                                                     |
|                                                                                     |
|=====================================================================================================================+
|{irineu.center(17)}|
|        ,,,      |{x[i][0].center(100)}
|      ///..)     |{x[i][1].center(100)}
|     <||  >\     |{x[i][2].center(100)}
|      || --/     |{x1.center(100)}
|       |\_/      |{x2.center(100)}
|      /___\_     |
|=====================================================================================================================+
V                                                                                              Desenvolvido por Grupo 6\
''')


def start_menu():
    print(f'''\
v=====================================================================================================================<
|
|                         ___  ___      _         __   __                 _____
|                         |  \/  |     | |        \ \ / /                |  _  |
|                         | .  . | __ _| | _____   \ V /___  _   _ _ __  | | | |_      ___ __
|                         | |\/| |/ _` | |/ / _ \   \ // _ \| | | | '__| | | | \ \ /\ / / '_ \ 
|                         | |  | | (_| |   <  __/   | | (_) | |_| | |    \ \_/ /\ V  V /| | | |
|                         \_|  |_/\__,_|_|\_\___|   \_/\___/ \__,_|_|     \___/  \_/\_/ |_| |_|
|
|                                             _____                _
|                                            |  ___|              (_)
|                                      />>>  | |__ _ __ ___  _ __  _ _ __ ___
|                                    (*>     |  __| '_ ` _ \| '_ \| | '__/ _ \ 
|                         ()%\%\%\%\%|*|33333| |__| | | | | | |_) | | | |  __/3333333333333333>
|                                    (*>     \____/_| |_| |_| .__/|_|_|  \___|
|                                      \>>>                 | |
|                                                           |_|
|
|
|
|
|
|
|
|
|{'Insira seu nome (Max: 25 caracteres):'.center(118)}
|
|
V                                                                                              Desenvolvido por Grupo 6\
''')


def death_menu(n, nn):
    print(f'''\
v=====================================================================================================================<
|
|
|
|
|
|                     ▄██   ▄    ▄██████▄  ███    █▄       ████████▄   ▄█     ▄████████ ████████▄
|                     ███   ██▄ ███    ███ ███    ███      ███   ▀███ ███    ███    ███ ███   ▀███
|                     ███▄▄▄███ ███    ███ ███    ███      ███    ███ ███▌   ███    █▀  ███    ███
|                     ▀▀▀▀▀▀███ ███    ███ ███    ███      ███    ███ ███▌  ▄███▄▄▄     ███    ███
|                     ▄██   ███ ███    ███ ███    ███      ███    ███ ███▌ ▀▀███▀▀▀     ███    ███
|                     ███   ███ ███    ███ ███    ███      ███    ███ ███    ███    █▄  ███    ███
|                     ███   ███ ███    ███ ███    ███      ███   ▄███ ███    ███    ███ ███   ▄███
|                      ▀█████▀   ▀██████▀  ████████▀       ████████▀  █▀     ██████████ ████████▀
|
|
|
|
|
|
|
|{death[n][nn][0].center(118)}
|{death[n][nn][1].center(118)}
|
|
|
|
|
V                                                                                              Desenvolvido por Grupo 6\
''')
