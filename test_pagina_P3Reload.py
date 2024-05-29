#Importação de bibliotecas
import time
import re
from playwright.sync_api import sync_playwright, expect

#Teste 1: Verifica o nome
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E verificar o nome
#Então o nome que deve aparecer é "Persona 3 Reload"

def teste_nome():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página será redirecionada
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Confirma se o nome está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[3]/div[2]/h1') == "Persona 3 Reload"
        print("NOME CORRETO")

#Teste 2: Verificação as avaliações, empresa e gênero
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E verificar a empresa e as avaliações
#Então eu devo visualizar a empresa Sega, o gênero RPG e 5 estrelas com 631 avaliações

def teste_empresa_genero_avaliação():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a pagina
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o usuário deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Confirma se o nome da empresa é "SEGA" e o gênero é "RPG"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[3]/div[2]/div[2]/span') == "SEGA • RPG"
        print('GÊNERO CORRETO')

        #Confirma se possui avaliações
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[3]/div[2]/div[2]/div/div/div[2]') != "0"
        print('AVALIAÇÕES CORRETAS')

#Teste 3: Verificação das features do jogo
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E verificar o nome, a otimização, a entrega inteligente, se o jogo é novo, se possui xbox anywhere, os recursos de acessibilidade, e os idiomas de suporte
#Então o python deve te retornar que as verificações estão corretas.

def teste_features():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página será redirecionada
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica a label "Otimizado para Xbox Series X|S"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[3]/div[2]/div[4]/div[1]/span') == "Otimizado para Xbox Series X|S"
        print("OTIMIZAÇÃO CORRETA")

        #Verifica a label "Entrega inteligente"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[3]/div[2]/div[4]/div[2]/span') == "Entrega inteligente"
        print("ENTREGA INTELIGENTE CORRETA")

        #Verifica a label "Xbox Play Anywhere"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[3]/div[2]/div[4]/div[3]/span') == "Xbox Play Anywhere"
        print("XBOX PLAY ANYWHERE CORRETO")

        #Verifica a label "9 Recursos de acessibilidade"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[3]/div[2]/div[4]/div[4]/span') == "9 Recursos de acessibilidade"
        print("RECURSOS DE ACESSIBILIDADE CORRETOS")

        #Verifica a label "15 Idiomas com suporte"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[3]/div[2]/div[4]/div[5]/span') == "15 Idiomas com suporte"
        print("IDIOMAS DE SUPORTE CORRETOS")

#Teste 4: Verificação das opções de nuvem, instalação, compra, edição e opções de carrinho
#Dado que eu tenha um dispositivo com acesso do site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E verificar as opções
#Então eu terei as opções de nuvem, instalação, compra, edição e opções de carrinho

def teste_opções_compra():
    with sync_playwright() as p:
        #Criando a navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o usuário será direcionado
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica se a opção de jogar com a nuvem está disponível
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[1]/button/div[1]') == "OBTER O GAME PASS"
        print("NUVEM CORRETO")

        #Verifica se a opção Comprar está disponível
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[2]/button/div[1]') == "COMPRAR"
        print("COMPRA CORRETA")

        #Verifica a opção de escolher edição
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[3]/button/div/div[1]') == "ESCOLHER EDIÇÃO"
        print("EDIÇÃO CORRETA")

        #Verifica se o nome da opção padrão está correta
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[3]/button/div/div[2]') == "Persona 3 Reload"
        print("EDIÇÃO CORRETA")

        #Verifica se as outras opções estão disponíveis na lista colapsável

        #Colapsa a lista com as edições
        pagina.click('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[3]/button')

        #Verifica a Digital Deluxe edition
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[3]/div[1]/div/ul/li[2]/a/div/div[1]') == "Persona 3 Reload Digital Deluxe Edition"
        print("EDIÇÃO DIGITAL DELUXE CORRETA")

        #Verifica a Digital Premium Edition
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[3]/div[1]/div/ul/li[3]/a/div/div[1]') == "Persona 3 Reload Digital Premium Edition"
        print("EDIÇÃO DIGITAL PREMIUM CORRETA")

        #Testa se o item é adicionado ao carrinho verificando se uma bola com um "1" aparece ao lado do ícone do carrinho
        pagina.click('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[4]/button')
        if pagina.inner_text('xpath=//*[@id="uhf-shopping-cart"]/span[1]') != "0":
            assert pagina.inner_text('xpath=//*[@id="uhf-shopping-cart"]/span[1]') == "1"
        print("CARRINHO CORRETO")

        #Testa se o colapsável com mais opções está funcionando
        pagina.click('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[5]/div/button')

        #Verifica se a opção "Comprar como presente" está entre as opções
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[5]/div/div[1]/div/div/button[1]') == "Comprar como presente"
        print("COMPRAR PARA PRESENTE CORRETO")

        #Verifica se a opção "Adicionar à lista de desejos" está entre as opções
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[5]/div/div[1]/div/div/button[2]') == "Adicionar à lista de desejos"
        print("LISTA DE DESEJOS CORRETA")

        #Verifica se a opção "Resgatar um código" está entre as opções
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[5]/div/div[1]/div/div/a') == "Resgatar um código"
        print("RESGATAR CÓDIGO CORRETO")

#Teste 5: Verificação da classificação indicativa e das informações da nuvem
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E verificar a classificação indicativa e as informações da nuvem
#Então aparecerá a classificação de 16 anos e informações explicando como funciona jogar em nuvem

def teste_classificação_informação():
    with sync_playwright() as p:
        #Criando a navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o usuário será direcionado
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica se a classificação indicativa está 16 anos
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[2]/div/div[1]/div/div/div/a') == "16 ANOS"
        print("CLASSIFICAÇÃO CORRETA")

        #Verifica a descrição da classificação indicativa
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[2]/div/div[1]/div/div/div/div') == "Violência, Temas\xa0sensíveis, Conteúdo\xa0Sexual"
        print("DESCRIÇÃO CLASSIFICAÇÃO INDICATIVA")

        #Verifica se as informações sobre o jogo em nuvem estão corretas
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[2]/div/div[2]/p[1]') == "Jogo habilitado para Nuvem enquanto estiver no Xbox Game Pass Ultimate. Saiba mais"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[1]/div[2]/div/div[2]/p[2]') == "+ Ofertas em compras no aplicativo."
        print("INFO NUVEM CORRETA")

#Teste 6: Testa a aba detalhes
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E verificar a aba "Detalhes"
#Então eu verei as seções "Galeria", "Descrição", "Reproduzível em" e "Funcionalidade"

def teste_aba_detalhes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica se a aba detalhes está disponível
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[1]/button') == "DETALHES"
        print("DETALHES CORRETO")

        #Verifica se as funcionalidades da aba estão disponíveis
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]') == "Galeria"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[1]/section/div[1]/div/h2') == "Descrição"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/h2') == "Reproduzível em"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/h2') == "Funcionalidades"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[1]/h2') == "Comparar edições"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[4]/div/div/div[1]/h2') == "Inclusão em"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[1]/h2') == "Incluído nessas assinaturas"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[1]/h2') == "Complementos para este jogo"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[1]/h2') == "As pessoas também gostam"
        print("FUNCIONALIDADES CORRETO")

#Teste 7: Testa a galeria da aba detalhes
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E verificar a aba "Detalhes"
#E inserir minha idade
#Então eu verei as fotos da seção Galeria

def teste_galeria():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica se as iamgens estão bloqueadas
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/section/div[2]/ol/li[1]/span/div/div[2]/span') == "Este conteúdo está bloqueado"
        print("GALERIA BLOQUEADA CORRETA")

        #Insera a data de nascimento
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/section/div[2]/ol/li[1]/span/div/div[2]/button')
        #Dia
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/button')
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div/button[2]')
        print("DIA INSERIDO")

        #Mês
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/button')
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div[2]/div[2]/div/button[2]')
        print("MÊS INSERIDO")

        #Ano
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div[1]/div[3]/div/div/div/button')
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div[1]/div[3]/div/div/div[2]/div[2]/div/button[25]')
        print("ANO INSERIDO")

        #Verifica se a data foi salva
        #Dia
        assert pagina.inner_text('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/button') == '1'
        print("DIA CORRETO")

        #Mês
        assert pagina.inner_text('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div[1]/div[2]/div/div/div/button') == '1'
        print("MÊS CORRETO")

        #Ano
        assert pagina.inner_text('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div[1]/div[3]/div/div/div/button') == "2000"
        print("ANO CORRETO")

        #Insere a data
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div[2]/button')
        print("DATA INSERIDA")

        #Verifica se as imagens estão desbloqueadas
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/section/div[2]/ol/li[1]/span/button') == ""
        print("DATA CORRETA")

#Teste 8: Testa a descrição na aba detalhes
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E verificar a aba "Detalhes"
#E verificar a parte da "Descrição"
#Então eu verei os dados da descrição.

def teste_descrição():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica o título
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[1]/section/div[1]/div/h2') == "Descrição"
        print("TÍTULO DESCRIÇÃO CORRETO")

        #Verifica o texto da descrição
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[1]/section/div[1]/div/div') == ('Assuma o papel de um estudante transferido que acaba vivendo um destino '
        'inesperado ao ingressar na hora "oculta" entre um dia e outro. Desperte um '
        'poder incrível, investigue a misteriosa Hora Sombria, lute em nome dos seus '
        'amigos e deixe sua marca para sempre nas memórias deles.\n'
        '\n'
        'Persona 3 Reload é uma reimaginação cativante do RPG que redefiniu o gênero, '
        'agora repensado para a era moderna.\n'
        '\n'
        'Destaques:\n'
        '- Experimente o jogo fundamental da série Persona fielmente recriado com '
        'gráficos de ponta, recursos de usabilidade modernizados e uma interface '
        'estilosa característica.\n'
        '\n'
        '- Mergulhe em uma jornada emocionante e envolvente, incluindo novas cenas e '
        'interações com personagens e dublagem adicional.\n'
        '\n'
        '- Escolha como passar cada dia de maneira significativa com diversas '
        'atividades disponíveis, desde explorar a Port Island até formar laços '
        'genuínos com personagens queridos.\n'
        '\n'
        '- Monte e controle sua equipe ideal e derrote Sombras de outro mundo para '
        'subir cada vez mais e alcançar a verdade.')
        print("TEXTO DESCRIÇÃO CORRETO")

        #Verifica a editora, desenvolvedora e a data de lançamento

        #Editora
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[1]/section/div[2]/div[1]/h3') == "Publicado por"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[1]/section/div[2]/div[1]/div') == "SEGA"
        print("EDITORA CORRETA")

        #Desenvolvedora
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[1]/section/div[2]/div[2]/h3') == "Desenvolvido por"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[1]/section/div[2]/div[2]/div') == "ATLUS"
        print("DESENVOLVEDORA CORRETA")

        #Data de lançamentos
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[1]/section/div[2]/div[3]/h3') == "Data de lançamento"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[1]/section/div[2]/div[3]/div') == "01/02/2024"
        print("DATA DE LANÇAMENTO CORRETA")

#Teste 9: Testa a aba "Reproduzível em" na aba detalhes
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba detalhes
#E ir até a aba "Reproduzível em"
#Então eu devo ver 3 opções "Xbox One" "Xbox Series X|S" e "Computador"

def teste_detalhes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica o título da seção
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/h2') == "Reproduzível em"
        print("TÍTULO CORRETO")

        #Verifica os dispositivos disponíveis

        #Xbox One
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[1]') == "Xbox One"
        print("XBOX ONE CORRETO")

        #Xbox Series X|S
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[2]') == "Xbox Series X|S"
        print("XBOX SERIES X|S CORRETO")

        #Computador
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/ul/li[3]') == "Computador"
        print("PC CORRETO")

#Teste 10: Testa a aba "Funcionalidades"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba detalhes
#E ir até a aba "Funcionalidades"
#Então eu devo ver as funcionalidades "4K Ultra HD", "Um jogador", "Taxa de Atualização Variável", "60fps+", "Otimizado para o Xbox Series X|S", "Entrega inteligente",
#"Teclado e mouse de console", "Conquistas do Xbox", "Salvamentos na nuvem do Xbox", "Xbox Play Anywhere" e "Xbox Live".

def teste_funcionalidades():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica o título da seção
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/h2') == "Funcionalidades"
        print("TÍTULO CORRETO")

        #Verifica se as funcionalidades estão presentes

        #4K Ultra HD
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[1]') == "4K Ultra HD"
        print("4K CORRETO")

        #Um jogador
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[2]') == "Um jogador"
        print("UM JOGADOR CORRETO")

        #Taxa de Atualização Variável
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[3]') == "Taxa de Atualização Variável"
        print("TAXA CORRETA")

        #60fps+
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[4]') == "60fps+"
        print("FPS CORRETO")

        #Otimizado para o Xbox Series X|S
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[5]') == "Otimizado para o Xbox Series X|S"
        print("OTIMIZAÇÃO CORRETA")

        #Entrega inteligente
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[6]') == "Entrega inteligente"
        print("ENTREGA CORRETA")

        #Teclado e mouse de console
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[7]') == "Teclado e mouse de console"
        print("TECLADO E MOUSE CORRETO")

        #Conquistas do Xbox
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[8]') == "Conquistas do Xbox"
        print("CONQUISTAS CORRETAS")

        #Salvamentos na nuvem de Xbox
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[9]') == "Salvamentos na nuvem do Xbox"
        print("SALVAMENTO EM NUVEM CORRETO")

        #Xbox Play Anywhere
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[10]') == "Xbox Play Anywhere"
        print("PLAY ANYWHERE CORRETO")

        #Xbox Live
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/ul/li[11]') == "Xbox Live"
        print("XBOX LIVE CORRETA")

#Teste 11: Testa a aba "Comparar edições"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba detalhes
#E ir até a aba "Comparar edições"
#Então eu verei as edições "Persona 3 Reload", "Persona 3 Reload Digital Deluxe Edition" e "Persona 3 Reload Digital Premium Edition"

def teste_edicoes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica o título da seção
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[1]/h2') == "Comparar edições"
        print("TÍTULO CORRETO")

        #Verifica os nomes das edições

        #Persona 3 Reload
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[1]/span/div/div[1]/div[2]/h3') == "Persona 3 Reload"
        print("EDIÇÃO PADRÃO CORRETA")

        #Persona 3 Reload Digital Deluxe Edition
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[2]/span/div/div[1]/div[2]/h3') == "Persona 3 Reload Digital Deluxe Edition"
        print("EDIÇÃO DIGITAL DELUXE CORRETA")

        #Persona 3 Reload Digital Premium Edition
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[3]/span/div/div[1]/div[2]/h3') == "Persona 3 Reload Digital Premium Edition"
        print("EDIÇÃO DIGITAL PREMIUM CORRETA")

        #Verifica os preços

        #Persona 3 Reload Digital Deluxe Edition
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[2]/span/div/div[1]/div[2]/div/span') == "R$399,50+"
        print("PREÇO EDIÇÃO DIGITAL DELUXE CORRETA")

        ##Persona 3 Reload Digital Premium Edition
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[3]/span/div/div[1]/div[2]/div/span') == "R$499,50+"
        print("PREÇO EDIÇÃO DIGITAL PREMIUM CORRETA")

        #Verifica o conteúdo da edição Persona 3 Reload Digital Deluxe Edition

        #Verifica o título "Jogos Incluídos"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[2]/span/div/div[3]/div/div/h4') == "Jogos incluídos"
        print("TITÚLO CORRETO")

        #Verifica os jogos incluídos
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[2]/span/div/div[3]/div/div/span') == "Persona 3 Reload"
        print("JOGOS INCLUÍDOS CORRETOS")

        #Verifica o conteúdo da edição Persona 3 Reload Digital Premium Edition

        #Verifica o título "Jogos Incluídos"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[3]/span/div/div[3]/div/div[1]/h4') == "Jogos incluídos"
        print("TITÚLO CORRETO")

        #Verifica os jogos incluídos
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[3]/span/div/div[3]/div/div[1]/span') == "Persona 3 Reload"
        print("JOGOS INCLUÍDOS CORRETOS")

        #Verifica o título "Complementos Incluídos
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[3]/span/div/div[3]/div/div[2]/h4') == "Complementos incluídos"
        print("COMPLEMENTOS INCLUÍDOS")

        #Verifica o conteúdo incluído
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[3]/span/div/div[3]/div/div[2]/span') == "Pacote de DLC de Persona 3 Reload"
        print("COMPLEMENTO CORRETO")

#Teste 12: Testa a aba "Inclusão em"
#Dado que eu tenha um dispositvo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba detalhes
#E ir até a seção "Inclusão em"
#Então eu verei a inclusão de "Persona 3 Reload" nas edições "Persona 3 Reload Digital Deluxe Edition" e "Persona 3 Reload Digital Premium Edition".

def teste_inclusão():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica o título da seção
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[4]/div/div/div[1]/h2') == "Inclusão em"
        print("TÍTULO INCLUIDO")

        #Verifica se as edições "Persona 3 Reload Digital Deluxe Edition" e "Persona 3 Reload Digital Premium Edition" estão presentes e com os preços corretos

        #Persona 3 Reload Digital Deluxe Edition
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[4]/div/div/div[2]/section/div/ol/li[1]/span/div/a/div[2]/span') == "Persona 3 Reload Digital Premium Edition"
        print("DIGITAL DELUXE EDITION CORRETO")

        #Verifica se o preço está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[4]/div/div/div[2]/section/div/ol/li[1]/span/div/a/div[2]/div/div/span') == "R$499,50+"
        print("PREÇO CORRETO")

        #Persona 3 Reload Digital Premium Edition
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[4]/div/div/div[2]/section/div/ol/li[2]/span/div/a/div[2]/span') == "Persona 3 Reload Digital Deluxe Edition"
        print("DIGITAL PREMIUM EDITION CORRETO")

        #Verifica se o preço está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[4]/div/div/div[2]/section/div/ol/li[2]/span/div/a/div[2]/div/div/span') == "R$399,50+"
        print("PREÇO CORRETO")

#Teste 13: Testa a aba "Incluído nessas assinaturas"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba detalhes
#E ir até a seção "Incluído nessas assinaturas"
#Então eu verei a inclusão de "Persona 3 Reload" nas assinaturas "Xbox Game Pass Ultimate", "PC Game Pass" e "Xbox Game Pass para Console"

def teste_assinaturas():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica o título da seção
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[1]/h2') == "Incluído nessas assinaturas"
        print("TÍTULO CORRETO")

        #Verifica se as três assinaturas estão corretas

        #Xbox Game Pass Ultimate
        #Verifica o título
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[1]/span/div/div[1]/h3') == "Xbox Game Pass Ultimate"
        print("TÍTULO CORRETO 2")

        #Verifica o preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[1]/span/div/div[1]/div/div[1]/span') == "R$49,99/mês"
        print("PREÇO CORRETO")

        #Verifica os benefícios
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[1]/span/div/div[2]/div/ul/li[1]/span') == "Centenas de jogos de alta qualidade no console, no PC e na nuvem"
        print("CENTENAS DE JOGOS CORRETO")
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[1]/span/div/div[2]/div/ul/li[2]/span') == "Novos jogos no primeiro dia"
        print("NOVOS JOGOS CORRETO")
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[1]/span/div/div[2]/div/ul/li[3]/span') == "Ofertas, descontos e vantagens de Membros"
        print("OFERTAS CORRETO")
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[1]/span/div/div[2]/div/ul/li[4]/span') == "Multijogador de console online"
        print("MULTIJOGADOR CORRETO")
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[1]/span/div/div[2]/div/ul/li[5]/span') == "Assinatura do EA Play"
        print("EA PLAY CORRETO")

        #Verifica o "INGRESSAR AGORA"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[1]/span/div/div[3]/a') == "INGRESSAR AGORA"
        print("INGRESSO CORRETO")

        #PC Game Pass
        #Verifica o título
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[2]/span/div/div[1]/h3') == "PC Game Pass"
        print("PC GAME PASS CORRETO")

        #Verifica o preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[2]/span/div/div[1]/div/div[1]/span') == "R$29,99/mês"
        print("PREÇO CORRETO")

        #Verifica os benefícios
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[2]/span/div/div[2]/div/ul/li[1]/span') == "Centenas de jogos de alta qualidade no computador"
        print("CENTENAS DE JOGOS CORRETOS")
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[2]/span/div/div[2]/div/ul/li[2]/span') == "Novos jogos no primeiro dia"
        print("NOVOS JOGOS CORRETOS")
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[2]/span/div/div[2]/div/ul/li[3]/span') == "Ofertas e descontos para membros"
        print("OFERTAS CORRETAS")
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[2]/span/div/div[2]/div/ul/li[4]/span') == "Assinatura do EA Play"
        print("ASSINATURA CORRETA")

        #Verifica o "INGRESSAR AGORA"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[2]/span/div/div[3]/a') == "INGRESSAR AGORA"
        print("TÍTULO CORRETO")

        #Xbox Game Pass para Console

        #Verifica o título
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[3]/span/div/div[1]/h3') == "Xbox Game Pass para Console"
        print("TÍTULO CORRETO")

        #Verifica o preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[3]/span/div/div[1]/div/div[1]/span') == "R$32,99/mês"
        print("PREÇO CORRETO")

        #Verifica os benefícios
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[3]/span/div/div[2]/div/ul/li[1]/span') == "Centenas de jogos de alta qualidade no console"
        print("CENTENAS DE JOGOS CORRETOS")
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[3]/span/div/div[2]/div/ul/li[2]/span') == "Novos jogos no primeiro dia"
        print("NOVOS JOGOS CORRETOS")
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[3]/span/div/div[2]/div/ul/li[3]/span') == "Ofertas e descontos para membros"
        print("OFERTAS CORRETAS")

        #Verifica o "INGRESSAR AGORA"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[3]/span/div/div[3]/a') == "INGRESSAR AGORA"
        print("INGRESSO CORRETO")

#Teste 14: Testa a seção "Complementos para este jogo"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba detalhes
#E ir até a seção "Complementos para este jogo"
#Então eu devo ver 9 complementos.

def teste_complementos():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica o título da seção
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[1]') == "Complementos para este jogo"
        print("TÍTULO CORRETO")

        #Verifica os complementos e seus preços
        #Persona 3 Reload: Kit Personas Persona 5 Royal 2
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[1]/span/div/a/div[2]/span') == "Persona 3 Reload: Kit Personas Persona 5 Royal 2"
        print("NOME DLC P5R 2 CORRETO")

        #Preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[1]/span/div/a/div[2]/div/div/span') == "R$31,90"
        print("PREÇO CORRETO")

        #Persona 3 Reload: Conjunto Trajes dos Phantom Thieves Persona 5 Royal
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[2]/span/div/a/div[2]/span') == "Persona 3 Reload: Conjunto Trajes dos Phantom Thieves Persona 5 Royal"
        print("NOME DLC TRAJE P5R CORRETO")

        #Preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[2]/span/div/a/div[2]/div/div/span') == "R$15,90"
        print("PREÇO CORRETO")

        #Persona 3 Reload: Kit Personas Persona 4 Golden
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[3]/span/div/a/div[2]/span') == "Persona 3 Reload: Kit Personas Persona 4 Golden"
        print("NOME DLC P4G CORRETO")

        #Preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[3]/span/div/a/div[2]/div/div/span') == "R$21,50"
        print("PREÇO CORRETO")

        #Persona 3 Reload: Kit Personas Persona 5 Royal 1
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[4]/span/div/a/div[2]/span') == "Persona 3 Reload: Kit Personas Persona 5 Royal 1"
        print("NOME DLC P5R CORRETO")

        #Preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[4]/span/div/a/div[2]/div/div/span') == "R$31,90"
        print("PREÇO CORRETO")

        #Persona 3 Reload: Kit MF Persona 5 Royal
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[5]/span/div/a/div[2]/span') == "Persona 3 Reload: Kit MF Persona 5 Royal"
        print("NOME DLC P5R MF CORRETO")

        #Preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[5]/span/div/a/div[2]/div/div/span') == "R$21,50"
        print("PREÇO CORRETO")

        #Persona 3 Reload: Conjunto Uniformes do Yasogami Persona 4 Golden
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[6]/span/div/a/div[2]/span') == "Persona 3 Reload: Conjunto Uniformes do Yasogami Persona 4 Golden"
        print("NOME DLC P4G Y CORRETO")

        #Preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[6]/span/div/a/div[2]/div/div/span') == "R$15,90"
        print("PREÇO CORRETO")

        #Pacote de DLC de Persona 3 Reload
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[7]/span/div/a/div[2]/span') == "Pacote de DLC de Persona 3 Reload"
        print("NOME DLC PACK P3R CORRETO")

        #Preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[7]/span/div/a/div[2]/div/div/span') == "R$143,90"
        print("PREÇO CORRETO")

        #Persona 3 Reload: Conjunto Uniformes da Shujin Persona 5 Royal
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[8]/span/div/a/div[2]/span') == "Persona 3 Reload: Conjunto Uniformes da Shujin Persona 5 Royal"
        print("NOME DLC P5R S CORRETO")

        #Preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[8]/span/div/a/div[2]/div/div') == "R$15,90"
        print("PREÇO CORRETO")

        #Persona 3 Reload: Passe de Expansão
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[9]/span/div/a/div[2]/span') == "Persona 3 Reload: Passe de Expansão"
        print("NOME PACOTE DE EXPANSÃO CORRETO")

        #Preço
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[9]/span/div/a/div[2]/div/div/span') == "R$187,90"
        print("PREÇO CORRETO")

        #Verifica os botões

        #Seta direita
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[1]/div/button[2]')
        print('SETA DIREITA CORRETA')

        #Seta esquerda
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[1]/div/button[1]')
        print('SETA ESQUERDA CORRETA')

#Teste 15: Testa a seção "As pessoas também gostam"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba detalhes
#E ir até a seção "As pessoas também gostam"
#Então eu devo ver 25 jogos.

def teste_pessoas():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica o título
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[1]') == "As pessoas também gostam"
        print("TÍTULO CORRETO")

        #Verifica se existem 25 jogos e se ele possuem suas características
        #Lista para cada xpath de nome
        xpaths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

        #Laço de repetição para cada xpath de nome
        for xpath in xpaths:
            assert pagina.inner_text(f'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[{xpath}]/span/div/a/div[2]/span') != 'Undefined'
        print("JOGOS RECOMENDADOS CORRETOS")

        #Lista para cada xpath de preço
        xpathsp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

        for xpathp in xpathsp:
            assert pagina.inner_text(f'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[{xpathp}]/span/div/a/div[2]/div/div/span') != 'Undefined'
        print("PREÇOS CORRETOS")

#Teste 16: Testa a seção avaliações da aba "Avaliações"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#Então eu devo ver a nota e a porcentagem de avaliações

def teste_avaliacoes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica se o título está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button') == "AVALIAÇÕES"
        print("TÍTULO CORRETO")

        #Clica na aba Avaliações
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO CORRETA")

        #Verifica se a nota é 4.9
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[1]') == '4.9'
        print("AVALIAÇÃO CORRETA")

        #Verifica o títuloo "Total de análises"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[2]') != 'Undefined'
        print("TOTAL DE ANÁLISES CORRETAS")

        #Verifica se os números de estrelas estão presentes
        #Dicionários com os números e estrelas
        estrelas = {"5": 3, "4": 4, "3": 5, "2": 6, "1": 7}

        for estrela, xpath in estrelas.items():
            assert pagina.inner_text(f'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/div/div[{xpath}]/div[1]/div') == estrela
        print("ESTRELAS CORRETAS")

#Teste 17: Testa o botão "FAÇA LOGIN PARA ADICIONAR UMA RESENHA" na aba "Avaliações"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#Então eu devo ver um botão escrito "FAÇA LOGIN PARA ADICIONAR UMA RESENHA" que ao ser clicado, me redirecionará para uma página de login.

def teste_botao_adicionar_avaliação():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba Avaliações
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO DISPONÍVEL")

        #Verifica se o botão se login está disponível
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/a') == "FAÇA LOGIN PARA ADICIONAR UMA RESENHA"
        print('BOTÃO DE LOGIN DISPONÍVEL')

        #Clica no botão de login e verifica sua funcionalidade
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/a')
        assert pagina.inner_text('xpath=//*[@id="usernameTitle"]') == "Entrar"
        print('BOTÃO DE LOGIN FUNCIONAL')

#Teste 18: Testa o botão "FILTRAR/CLASSIFICAR" na aba "Avaliações"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#Então eu devo ver um botão escrito "FILTRAR/CLASSIFICAR" na aba "Avaliações" que me dará diversas opções de filtros.

def teste_botao_filtro_class():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando a página
        pagina = navegador.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba Avaliações
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO DISPONÍVEL")

        #Verifica se o botão escrito "FILTRAR/CLASSIFICAR" está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button') == "FILTRAR/CLASSIFICAR"
        print("BOTÃO FILTRAR/CLASSIFICAR DISPONÍVEL")

        #Clica no botão
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        assert pagina.inner_text('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[1]/h2') == "Filtrar/Classificar Revisões"
        print("BOTÃO FILTRAR/CLASSIFICAR FUNCIONAL")

        #Verifica se os filtros e as classificações por estrelas estão disponíveis
        assert pagina.inner_text('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[1]') == "Classificações por Estrelas"
        assert pagina.inner_text('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[3]') == "Classificar por"

        #Abre o dropdown das classificações de estrelas para verificar se as opções estão disponíveis
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA ABERTO')

        #Classificação de Estrelas

        #Dicionário com as estrelas e seus xpaths
        classestrela = {1: "Todas as Classificações", 2: "5 Estrelas", 3: "4 Estrelas", 4: "3 Estrelas", 5: "2 Estrelas", 6: "1 Estrela"}

        #Faz um laço para cada estrela
        for xpath, estrela in classestrela.items():
            assert pagina.inner_text(f'xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[{xpath}]') == estrela
            print(f"{estrela} PRESENTE")

        #Fecha o dropdown
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[1]')
        print('DROPDOWN ESTRELA FECHADO')

        #Classificação de filtros

        #Abre o dropdown de filtros
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN FILTRO ABERTO')

        #Dicionário com filtros e seus xpaths
        classfiltro = {1: "Mais Úteis", 2: "Mais Recentes", 3: "Classificação Mais Alta", 4: "Menor Classificação"}

        #Faz um laço para cada filtro
        for xpath_, filtro in classfiltro.items():
            assert pagina.inner_text(f'xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[{xpath_}]') == filtro
            print(f"{filtro} PRESENTE")

        #Fecha o dropdown de filtros
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[1]')
        print('DROPDOWN FILTRO FECHADO')

        #Fecha a janela com opção de filtros
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[3]/button')
        print('JANELA DE CLASSIFICAÇÕES FECHADA')

#Teste 19: Testa o botão "Sobre classificações e opiniões"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Sobre classificações e opiniões"
#Então outra aba com as informações devem ser abertas

def teste_sobre():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica no link com as informações para avaliações
        with pagina.expect_popup() as popup_info:
            pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/a')
            print('LINK ABERTO')
        pagina2 = popup_info.value

        #Verifica se o título está correto
        assert pagina2.inner_text('xpath=//*[@id="page-header"]') == "Avaliar e revisar jogos e aplicativos na Microsoft Store"
        print('TÍTULO CORRETO')

#Teste 20: Testa o fitro "Todas as classificações"/"Mais úteis"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#Então a primeira avaliação que deve aparecer é do usuário "Lile2155"

def teste_todas_class_mais_uteis():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Verifica se a avaliação está correta
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') == 'Lile2155'
        print('FILTRO FUNCIONAL')

#Teste 21: Testa o fitro "Todas as classificações"/"Mais Recentes"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdwon "Classificar por" e clicar em "Mais Recentes"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_todas_class_mais_recentes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN FUNCIONAL')

        #Clica na opção "Mais recentes"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[2]')
        print('BOTÃO MAIS RECENTES FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 22: Testa o fitro "Todas as classificações"/"Classificações mais altas"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdwon "Classificar por" e clicar em "Classificações mais altas"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_todas_class_mais_altas():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN FUNCIONAL')

        #Clica na opção "Mais altas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[3]')
        print('BOTÃO MAIS ALTAS FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 23: Testa o fitro "Todas as classificações"/"Menor classificação"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdwon "Classificar por" e clicar em "Menor classificação"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_todas_class_mais_baixas():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN FUNCIONAL')

        #Clica na opção "Menor classificação"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[4]')
        print('BOTÃO MENOR CLASSIFICAÇÃO FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 24: Testa o fitro "5 Estrelas"/"Mais úteis"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "5 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Mais úteis"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_5_estrela_mais_uteis():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "5 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[2]')
        print('BOTÃO 5 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Mais úteis"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[1]')
        print('BOTÃO MAIS ÚTEIS FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') == 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 25: Testa o fitro "5 Estrelas"/"Mais recentes"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "5 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Mais recentes"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é do usuário "Lile2155"

def teste_5_estrela_mais_recentes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "5 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[2]')
        print('BOTÃO 5 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Mais recentes"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[2]')
        print('BOTÃO MAIS RECENTES FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 26: Testa o fitro "5 Estrelas"/"Classificação mais alta"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "5 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Classificação mais alta"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_5_estrela_mais_alta():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "5 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[2]')
        print('BOTÃO 5 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Classificação mais alta"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[3]')
        print('BOTÃO CLASSIFICAÇÃO MAIS ALTA FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 27: Testa o fitro "5 Estrelas"/"Menor Classificação"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "5 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Menor Classificação"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_5_estrela_mais_baixa():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "5 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[2]')
        print('BOTÃO 5 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Classificação mais baixa"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[4]')
        print('BOTÃO CLASSIFICAÇÃO MAIS BAIXA FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 28: Testa o fitro "4 Estrelas"/"Mais úteis"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "4 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Mais úteis"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_4_estrela_mais_uteis():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "4 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[3]')
        print('BOTÃO 4 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Mais úteis"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[1]')
        print('BOTÃO MAIS ÚTEIS FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 29: Testa o fitro "4 Estrelas"/"Mais recentes"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "4 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Mais recentes"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_4_estrela_mais_recentes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "4 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[3]')
        print('BOTÃO 4 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Mais recentes"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[2]')
        print('BOTÃO MAIS RECENTES FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 30: Testa o fitro "4 Estrelas"/"Classificação mais alta"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "4 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Classificação mais alta"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_4_estrela_mais_alta():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "4 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[3]')
        print('BOTÃO 4 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Classificação mais alta"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[3]')
        print('BOTÃO CLASSIFICAÇÃO MAIS ALTA FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 31: Testa o fitro "4 Estrelas"/"Menor Classificação"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "4 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Menor Classificação"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_4_estrela_mais_baixa():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "4 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[3]')
        print('BOTÃO 4 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Classificação mais baixa"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[4]')
        print('BOTÃO CLASSIFICAÇÃO MAIS BAIXA FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 32: Testa o fitro "3 Estrelas"/"Mais úteis"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "3 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Mais úteis"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_3_estrela_mais_uteis():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "3 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[4]')
        print('BOTÃO 3 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Mais úteis"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[1]')
        print('BOTÃO MAIS ÚTEIS FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 33: Testa o fitro "3 Estrelas"/"Mais recentes"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "3 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Mais recentes"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_3_estrela_mais_recentes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "3 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[4]')
        print('BOTÃO 3 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Mais recentes"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[2]')
        print('BOTÃO MAIS RECENTES FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 34: Testa o fitro "3 Estrelas"/"Classificação mais alta"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "3 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Classificação mais alta"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_3_estrela_mais_alta():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "3 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[4]')
        print('BOTÃO 3 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Classificação mais alta"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[3]')
        print('BOTÃO CLASSIFICAÇÃO MAIS ALTA FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 35: Testa o fitro "3 Estrelas"/"Menor Classificação"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "3 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Menor Classificação"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_3_estrela_mais_baixa():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "3 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[4]')
        print('BOTÃO 3 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Classificação mais baixa"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[4]')
        print('BOTÃO CLASSIFICAÇÃO MAIS BAIXA FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 36: Testa o fitro "2 Estrelas"/"Mais úteis"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "2 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Mais úteis"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_2_estrela_mais_uteis():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "2 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[5]')
        print('BOTÃO 2 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Mais úteis"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[1]')
        print('BOTÃO MAIS ÚTEIS FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 37: Testa o fitro "2 Estrelas"/"Mais recentes"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "2 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Mais recentes"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_2_estrela_mais_recentes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "2 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[5]')
        print('BOTÃO 2 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Mais recentes"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[2]')
        print('BOTÃO MAIS RECENTES FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 38: Testa o fitro "2 Estrelas"/"Classificação mais alta"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "2 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Classificação mais alta"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_2_estrela_mais_alta():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "2 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[5]')
        print('BOTÃO 2 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Classificação mais alta"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[3]')
        print('BOTÃO CLASSIFICAÇÃO MAIS ALTA FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 39: Testa o fitro "2 Estrelas"/"Menor Classificação"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "2 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Menor Classificação"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_2_estrela_mais_baixa():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "2 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[5]')
        print('BOTÃO 2 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Classificação mais baixa"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[4]')
        print('BOTÃO CLASSIFICAÇÃO MAIS BAIXA FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 40: Testa o fitro "1 Estrelas"/"Mais úteis"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "1 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Mais úteis"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_1_estrela_mais_uteis():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "1 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[6]')
        print('BOTÃO 1 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Mais úteis"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[1]')
        print('BOTÃO MAIS ÚTEIS FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 41: Testa o fitro "1 Estrelas"/"Mais recentes"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "1 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Mais recentes"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_1_estrela_mais_recentes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "1 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[6]')
        print('BOTÃO 1 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Mais recentes"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[2]')
        print('BOTÃO MAIS RECENTES FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 42: Testa o fitro "1 Estrelas"/"Classificação mais alta"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "1 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Classificação mais alta"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_1_estrela_mais_alta():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "1 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[6]')
        print('BOTÃO 1 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Classificação mais alta"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[3]')
        print('BOTÃO CLASSIFICAÇÃO MAIS ALTA FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 43: Testa o fitro "1 Estrelas"/"Menor Classificação"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Filtrar/Classificar"
#E clicar no dropdown "Classificar por estrelas" e clicar em "1 Estrelas"
#E clicar no dropdown "Classificar por" e clicar em "Menor Classificação"
#E clicar no botão "Confirmar"
#Então a primeira avaliação que deve aparecer é diferente do usuário "Lile2155"

def teste_1_estrela_mais_baixa():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Clica em "Filtrar/Classificar"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[3]/button')
        print('BOTÃO FUNCIONAL')

        #Clica no Dropdown "Classificações por Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div/button')
        print('DROPDOWN ESTRELA FUNCIONAL')

        #Clica na opção "1 Estrelas"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[2]/div/div[2]/div[2]/div/button[6]')
        print('BOTÃO 1 ESTRELAS FUNCIONAL')

        #Clica no Dropdown "Classificar por"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div/button')
        print('DROPDOWN CLASSIFICAR FUNCIONAL')

        #Clica na opção "Classificação mais baixa"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/div/div[4]/div/div[2]/div[2]/div/button[4]')
        print('BOTÃO CLASSIFICAÇÃO MAIS BAIXA FUNCIONAL')

        #Clica no botão "Confirmar"
        pagina.click('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[2]/div/button')
        print('BOTÃO CONFIRMAR FUNCIONAL')

        #Espera o carregamento da página
        time.sleep(1)

        #Verifica se a avaliação é diferente do usuário "Lile2155"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/span/div[2]') != 'Lile2155'
        print('COMBINAÇÃO DE FILTROS FUNCIONAL')

#Teste 44: Testa o botão "Carregar mais da aba de avaliações"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba avaliações
#E clicar em "Carregar mais"
#Então mais 5 avaliações devem aparecer.

def teste_carregar_mais():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliação
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')
        print("ABA AVALIAÇÃO ABERTA")

        #Verifica se o botão "Carregar Mais" está disponível
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[6]/button') == "CARREGAR MAIS"
        print("BOTÃO CARREGAR MAIS DISPONÍVEL")

        #Clica no botão "Carregar Mais"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[6]/button')
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[2]/div[6]/span/div[2]') != "None"
        print("BOTÃO CARREGAR MAIS FUNCIONAL")

#Teste 45: Testa a aba "Mais"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba "Mais"
#Então eu devo ver as seções "Requisitos mínimos", "Exigências recomendadas", "Recursos de acessibilidade", "Idiomas Suportados" e "Informações adicionais"

def teste_aba_mais():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba "Mais"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[3]/button')

        #Verifica se a seção "Requisitos mínimos" está presente na aba
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/h2') == "Requisitos mínimos"
        print('SEÇÃO REQUISITOS MÍNIMOS DISPONÍVEL')

        #Verifica se a seção "Exigências recomendadas" está presente na aba
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/h2') == "Exigências recomendadas"
        print('SEÇÃO EXIGÊNCIAS RECOMENDADAS DISPONÍVEL')

        #Verifica se a seção "Recursos de acessibilidade" está presente na aba
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/h2[1]') == "Recursos de acessibilidade"
        print('SEÇÃO RECURSOS DE ACESSIBILIDADE DISPONÍVEL')

        #Verifica se a seção "Idiomas Suportados" está presente na aba
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/caption/h2') == "Idiomas Suportados"
        print('SEÇÃO IDIOMAS SUPORTADOS DISPONÍVEL')

        #Verifica se a seção "Informações adicionais" está presente na aba
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/h2') == "Informações adicionais"
        print('SEÇÃO INFORMAÇÕES ADICIONAIS DISPONÍVEL')

#Teste 46: Testa a seção "Requisitos mínimos"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba "Mais"
#E ir até a seção "Requisitos Mínimos"
#Então deve aparecer que os requisitos são "Sistema Operacional Windows 10 versão 18362.0 ou superior", "Arquitetura x64",
#"Elementos gráficos Nvidia GeForce GTX 650 Ti, AMD Radeon HD 7850", "Processador Intel Core i5-2300, AMD FX-4350", "DirectX API DirectX 12, Recurso de Hardware Nível 11"
#"Memória 8 GB", "Memória de Vídeo 2 GB", "Teclado Teclado Integrado", "Mouse Mouse Integrado" e "Controle Controle ou gamepad Xbox"

def teste_requisitos_min():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba "Mais"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[3]/button')

        #Verifica se a seção "Requisitos mínimos" está presente na aba
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/h2') == "Requisitos mínimos"
        print('SEÇÃO REQUISITOS MÍNIMOS DISPONÍVEL')

        #Verifica se o sistema operacional está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[1]/td[1]') == "Sistema Operacional"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[1]/td[3]') == "Windows 10 versão 18362.0 ou superior"
        print('SISTEMA OPERACIONAL CORRETO')

        #Verifica se a arquiteura está correta
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[2]/td[1]') == "Arquitetura"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[2]/td[3]') == "x64"
        print('ARQUITETURA CORRETA')

        #Verifica de os elementos estão corretos
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[3]/td[1]') == "Elementos gráficos"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[3]/td[3]') == "Nvidia GeForce GTX 650 Ti, AMD Radeon HD 7850,"
        print('ELEMENTOS GRÁFICOS CORRETOS')

        #Verifica se o processador está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[4]/td[1]') == "Processador"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[4]/td[3]') == "Intel Core i5-2300, AMD FX-4350"
        print('PROCESSADOR CORRETO')

        #Verifica se o DirectX está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[5]/td[1]') == "DirectX"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[5]/td[3]') == "API DirectX 12, Recurso de Hardware Nível 11"
        print('DIRECTX CORRETO')

        #Verifica se a Memória está correta
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[6]/td[1]') == "Memória"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[6]/td[3]') == "8 GB"
        print('MEMÓRIA CORRETA')

        #Verifica se a Memória de Vídeo está correta
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[7]/td[1]') == "Memória de Vídeo"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[7]/td[3]') == "2 GB"
        print('MEMÓRIA DE VÍDEO CORRETA')

        #Verifica se o Teclado está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[8]/td[1]') == "Teclado"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[8]/td[3]') == "Teclado Integrado"
        print('TECLADO CORRETO')

        #Verifica se o Mouse está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[9]/td[1]') == "Mouse"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[9]/td[3]') == "Mouse Integrado"
        print('MOUSE CORRETO')

        #Verifica se o Controle está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[10]/td[1]') == "Controle"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[1]/table/tr[10]/td[3]') == "Controle ou gamepad Xbox"
        print('CONTROLE CORRETO')

#Teste 47: Testa a seção "Exigências recomendadas"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba "Mais"
#E ir até a seção "Exigências recomendadas"
#Então deve aparecer que as exigências são " Sistema Operacional Windows 10 versão 18362.0 ou superior", "Arquitetura x64",
#"Elementos gráficos NVIDIA GeForce GTX 1650, AMD Radeon R9 290X", "Processador Intel Core i7-4790, AMD Ryzen 5 1400", "DirectX API DirectX 12, Recurso de Hardware Nível 11",
#"Memória 8 GB", "Memória de Vídeo 4 GB", "Mouse Mouse Integrado" e "Controle Controle ou gamepad Xbox"

def teste_exigencias_rec():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba "Mais"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[3]/button')

        #Verifica se a seção "Exigências recomendadas" está presente na aba
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/h2') == "Exigências recomendadas"
        print('SEÇÃO EXIGÊNCIAS RECOMENDADAS DISPONÍVEL')

        #Verifica se o sistema operacional está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[1]/td[1]') == "Sistema Operacional"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[1]/td[3]') == "Windows 10 versão 18362.0 ou superior"
        print('SISTEMA OPERACIONAL CORRETO')

        #Verifica se a arquiteura está correta
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[2]/td[1]') == "Arquitetura"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[2]/td[3]') == "x64"
        print('ARQUITETURA CORRETA')

        #Verifica de os elementos estão corretos
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[3]/td[1]') == "Elementos gráficos"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[3]/td[3]') == "NVIDIA GeForce GTX 1650, AMD Radeon R9 290X"
        print('ELEMENTOS GRÁFICOS CORRETOS')

        #Verifica se o processador está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[4]/td[1]') == "Processador"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[4]/td[3]') == "Intel Core i7-4790, AMD Ryzen 5 1400"
        print('PROCESSADOR CORRETO')

        #Verifica se o DirectX está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[5]/td[1]') == "DirectX"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[5]/td[3]') == "API DirectX 12, Recurso de Hardware Nível 11"
        print('DIRECTX CORRETO')

        #Verifica se a Memória está correta
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[6]/td[1]') == "Memória"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[6]/td[3]') == "8 GB"
        print('MEMÓRIA CORRETA')

        #Verifica se a Memória de Vídeo está correta
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[7]/td[1]') == "Memória de Vídeo"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[7]/td[3]') == "4 GB"
        print('MEMÓRIA DE VÍDEO CORRETA')

        #Verifica se o Teclado está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[8]/td[1]') == "Teclado"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[8]/td[3]') == "Teclado Integrado"
        print('TECLADO CORRETO')

        #Verifica se o Mouse está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[9]/td[1]') == "Mouse"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[9]/td[3]') == "Mouse Integrado"
        print('MOUSE CORRETO')

        #Verifica se o Controle está correto
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[10]/td[1]') == "Controle"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[1]/div/div[2]/table/tr[10]/td[3]') == "Controle ou gamepad Xbox"
        print('CONTROLE CORRETO')

#Teste 48: Testa a seção "Recursos de acessibilidade"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba "Mais"
#E ir até a seção "Recursos de acessibilidade"
#Então devo ver os recursos de Áudio como "Controles de volume personalizados" e recursos de Vídeo como "Dificuldade ajustável" e "Pausável"

def teste_recursos_acessibilidade():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba "Mais"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[3]/button')

        #Verifica se os recursos de acessibilidade estão disponíveis na seção
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/h2[1]') == "Recursos de acessibilidade"
        print('SEÇÃO RECURSOS DE ACESSIBILIDADE DISPONÍVEL')

        #Verifica se a seção de áudio está presente na seção
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/h2[2]') == "Áudio"
        print('SEÇÃO RECURSOS DE ACESSIBILIDADE DE ÁUDIO DISPONÍVEL')

        #Verifica se os recursos de áudio estão disponíveis
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/ul[1]/li') == "Controles de volume personalizados"
        print('CONTROLES DE VOLUME DISPONÍVEIS')

        #Verifica se a seção de jogabilidade está presente na seção
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/h2[3]') == "Jogabilidade"
        print('SEÇÃO RECURSOS DE ACESSIBILIDADE DE JOGABILIDADE DISPONÍVEL')

        #Verifica se os recursos de jogabilidade estão disponíveis
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/ul[2]/li[1]') == "Dificuldade ajustável"
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[2]/ul[2]/li[2]') == "Pausável"
        print('RECURSOS DE JOGABILIDADE DISPONÍVEIS')

#Teste 49: Testa a seção "Idiomas Suportados"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba "Mais"
#E ir até a seção "Idiomas Suportados"
#E clica no botão Mostrar Mais
#Então devo ver os idiomas suportados

def teste_idiomas_suportados():

    #Dicionário com os xpaths e seus subtítulos
    subtitulos_xpath = {'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/thead/tr/th[1]/span': "LÍNGUA",
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/thead/tr/th[2]/span': "ÁUDIO",
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/thead/tr/th[3]/span': "INTERFACE",
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/thead/tr/th[4]/span': "LEGENDAS"}

    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba "Mais"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[3]/button')

        #Verifica se os Idiomas Suportados estão disponíveis na seção
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/caption/h2') == "Idiomas Suportados"
        print('SEÇÃO IDIOMAS SUPORTADOS DISPONÍVEL')

        #Verifica se os subtítulos estão presentes
        for xpath, sub in subtitulos_xpath.items():
            assert pagina.inner_text(xpath) == sub
            print(f'SUBTÍTULO {sub} PRESENTE')

        #Clica no botão mostrar mais
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/button')
        print('BOTÃO MOSTRAR MAIS CLICADO')

        #Dicionário com os idiomas e seus xpaths
        idiomas_xpath = {'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[1]/td[1]': 'Português (Brasil)',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[2]/td[1]': 'Albanês',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[3]/td[1]': 'Árabe',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[4]/td[1]': 'Búlgaro',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[5]/td[1]': 'Catalão',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[6]/td[1]': 'Croata',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[7]/td[1]': 'Tcheco',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[8]/td[1]': 'Dinamarquês',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[9]/td[1]': 'Holandês',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[10]/td[1]': 'Alemão',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[11]/td[1]': 'Grego',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[12]/td[1]': 'Inglês (Estados Unidos)',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[13]/td[1]': 'Inglês (Reino Unido)',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[14]/td[1]': 'Estoniano',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[15]/td[1]': 'Espanhol (Espanha)',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[16]/td[1]': 'Espanhol (México)',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[17]/td[1]': 'Finlandês',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[18]/td[1]': 'Francês',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[19]/td[1]': 'Hebraico',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[20]/td[1]': 'Húngaro',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[21]/td[1]': 'Italiano',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[22]/td[1]': 'Japonês',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[23]/td[1]': 'Coreano',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[24]/td[1]': 'Letão',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[25]/td[1]': 'Lituano',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[26]/td[1]': 'Norueguês',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[27]/td[1]': 'Polonês',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[28]/td[1]': 'Português (Portugal)',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[29]/td[1]': 'Romeno',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[30]/td[1]': 'Russo',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[31]/td[1]': 'Sérvio (Latino)',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[32]/td[1]': 'Chinês (Simplificado)',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[33]/td[1]': 'Eslovaco',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[34]/td[1]': 'Sueco',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[35]/td[1]': 'Tailandês',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[36]/td[1]': 'Chinês (Tradicional)',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[37]/td[1]': 'Turco',
                        'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/div/table/tbody/tr[38]/td[1]': 'Vietnamita'}

        #Cria um laço de for para verificar cada idioma
        for xpath, idioma in idiomas_xpath.items():
            assert pagina.inner_text(xpath) == idioma
            print(f'IDIOMA {idioma} DISPONÍVEL')
        print('MOSTRAR MAIS FUNCIONAL')

        #Clica no botão Mostrar menos
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/button')
        print('BOTÃO MOSTRAR MENOS CLICADO')

        #Verifica se a lista fechou verificando o botão mostrar mais
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/section/div/button')
        print('BOTÃO MOSTRAR MENOS FUNCIONAL')

#Teste 50: Testa a seção "Informações adicionais"
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até a a aba "Mais"
#E ir até até a seção "Informações adicionais"
#Então eu devo ver informações sobre instalação, tamanho do jogo, informações do fornecedor, avisos sobre epilepsia, este aplicativo pode, termos adicionais e denunciar esse produto a microsoft

def teste_info_adi():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba "Mais"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[3]/button')

        #Verifica se os títulos e seus textos estão corretos

        #Abre o mostrar mais em "Este aplicativo pode"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div[1]/button')

        #Lista com os xpaths e seus textos

        xpaths_textos = {'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/h2': 'Informações adicionais',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[1]/div[1]/h3': 'Instalação',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[1]/div[1]/div': 'Instale na sua consola Xbox One doméstica e em um computador Windows 10 e tenha acesso quando estiver ligado à sua conta Microsoft',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[1]/div[2]/h3': 'Tamanho aproximado',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[1]/div[2]/div': '19.23 GB',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/h3': 'Informações do fornecedor',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/a': 'Suporte ao Persona 3 Reload',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div[2]': 'Este vendedor certificou que oferecerá somente produtos ou serviços que estão em conformidade com as leis aplicáveis',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/h3': 'Avisos sobre epilepsia',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div/a': 'Aviso sobre epilepsia fotossensível',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/h3': 'Este aplicativo pode',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div[2]/a': 'Informações de permissões',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[3]/div[1]/h3': 'Termos adicionais',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[3]/div[1]/div[1]/a': 'Código de conduta do Xbox Live',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[3]/div[1]/div[2]/a': 'Persona 3 Reload política de privacidade',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[3]/div[1]/div[3]/a': 'Termos da transação',
                         'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[3]/div[2]/button': 'Denunciar este produto à Microsoft'}

        for xpath, texto in xpaths_textos.items():
            assert pagina.inner_text(xpath) == texto
            print(f'TEXTO {texto} CORRETO')

        #Verifica o botão menos
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div[1]/button') == 'Mostrar menos'
        print('BOTÃO MOSTRAR MENOS DISPONÍVEL')

        #Clica no botão mostrar menos
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div[1]/button')

        #Verifica se o botão mostrar mais voltou
        assert pagina.inner_text('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div[1]/button')
        print('BOTÃO MENOS FUNCIONAL')

#Teste 51: Testa o final da página
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até o final da página
#Então eu devo ver os subtítulos "Navegue", "Recursos", "Microsoft Store" e "Para Desenvolvedor".

def teste_final_pag():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Dicionários com os textos e seus xpaths
        xpaths_textos = {'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[1]/div': 'Navegue', 'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[1]/ul/li[1]/a': 'Xbox consoles',
                         'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[1]/ul/li[2]/a': 'Jogos Xbox', 'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[1]/ul/li[3]/a': 'Xbox Game Pass',
                         'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[1]/ul/li[4]/a': 'Acessórios do Xbox', 'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/div': 'Recursos',
                         'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/ul/li[1]/a': 'Notícias do Xbox', 'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/ul/li[2]/a': 'Suporte do Xbox',
                         'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/ul/li[3]/a': 'Feedback', 'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/ul/li[4]/a': 'Padrões da Comunidade',
                         'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/ul/li[5]/a': 'Aviso de potenciais convulsões por fotossensibilidade',
                         'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[3]/div': 'Microsoft Store',
                         'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[3]/ul/li[1]/a': 'Conta Microsoft', 'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[3]/ul/li[2]/a': 'Suporte da Microsoft Store',
                         'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[3]/ul/li[3]/a': 'Devoluções', 'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[3]/ul/li[4]/a': 'Rastreamento de pedidos',
                         'xpath=//*[@id="uhf-footer"]/nav/div[2]/div/div': 'Para desenvolvedores', 'xpath=//*[@id="uhf-footer"]/nav/div[2]/div/ul/li/a': 'Jogos'}

        #Laço de repetição para verificar se os textos estão presentes
        for xpath, texto in xpaths_textos.items():
            assert pagina.inner_text(xpath) == texto
            print(f'TEXTO {texto} CORRETO')

#Teste 52: Testa o rodapé da página
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até o final da página
#Então eu devo ver os subtítulos "Português (Brasil)", "Suas opções de privacidade", "Privacidade dos Dados de Saúde do Consumidor", "Entre em contato com a Microsoft", "Privacidade e Cookies", "Gerenciar cookies", "Ética e Compliance", "Nota Legal", "Marcas", "Avisos de terceiros", "Sobre os nossos anúncios" e "© Microsoft 2024"

def teste_rodape():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Dicionários com os textos e seus xpaths
        xpaths_textos = {'xpath=//*[@id="locale-picker-link"]': 'Português (Brasil)', 'xpath=//*[@id="uhf-footer"]/div/a[2]/span': 'Suas opções de privacidade',
                         'xpath=//*[@id="uhf-footer"]/div/a[3]': 'Privacidade dos Dados de Saúde do Consumidor', 'xpath=//*[@id="c-uhff-footer_contactus"]': 'Entre em contato com a Microsoft',
                         'xpath=//*[@id="c-uhff-footer_privacyandcookies"]/a': 'Privacidade e Cookies', 'xpath=//*[@id="c-uhff-footer_managecookies"]/a': 'Gerenciar cookies',
                         'xpath=//*[@id="c-uhff-footer_compliance"]/a': 'Ética e Compliance', 'xpath=//*[@id="c-uhff-footer_termsofuse"]/a': 'Nota Legal',
                         'xpath=//*[@id="c-uhff-footer_trademarks"]/a': 'Marcas', 'xpath=//*[@id="c-uhff-third_party_notices"]/a': 'Avisos de terceiros',
                         'xpath=//*[@id="c-uhff-footer_aboutourads"]/a': 'Sobre os nossos anúncios', 'xpath=//*[@id="uhf-footer"]/div/nav/ul/li[9]': '© Microsoft 2024'}

        #Laço de repetição para verificar se os textos estão presentes
        for xpath, texto in xpaths_textos.items():
            assert pagina.inner_text(xpath) == texto
            print(f'TEXTO {texto} CORRETO')

#Teste 53: Testa os links da página na seção detalhes
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até até a seção detalhes
#E clicar nos links na página
#Então eu devo ser redirecionado para outra página

def teste_links_detalhes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Lista com os xpaths dos links que serão clicados
        links_detalhes = {'//*[@id="PageContent"]/div/div[1]/div[1]/div[6]/div/div[2]/button': 'COMPRAR', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[2]/span/div/a': 'Persona 3 Reload Digital Deluxe Edition',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[3]/span/div/a': 'Persona 3 Reload Digital Premium Edition', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/section/div/ol/li[3]/span/div/a': 'Persona 3 Reload Digital Deluxe Edition',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[4]/div/div/div[2]/section/div/ol/li[1]/span/div/a/div[2]/span': 'Persona 3 Reload Digital Premium Edition', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[4]/div/div/div[2]/section/div/ol/li[2]/span/div/a/div[2]/span': 'Xbox Game Pass Ultimate',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[1]/span/div/div[3]/a': 'PC Game Pass', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[5]/div/div/div[2]/section/div/ol/li[2]/span/div/div[3]/a': 'Xbox Game Pass para Console',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[1]/span/div/a/div[2]/span': 'Complemento 1', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[2]/span/div/a/div[2]/span': 'Complemento 2',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[3]/span/div/a/div[2]/span': 'Complemento 3', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[4]/span/div/a/div[2]/span': 'Complemento 4',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[5]/span/div/a/div[2]/span': 'Complemento 5', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[6]/span/div/a/div[2]/span': 'Complemento 6',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[7]/span/div/a/div[2]/span': 'Complemento 7', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[8]/span/div/a/div[2]/span': 'Complemento 8',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[2]/ol/li[9]/span/div/a/div[2]/span': 'Complemento 9', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[6]/div/div/div[2]/section/div[1]/div/a': 'Mostrar tudo Complementos', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[1]/span/div/a/div[2]/span': 'Jogo 1',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[2]/span/div/a/div[2]/span': 'Jogo 2', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[3]/span/div/a/div[2]/span': 'Jogo 3',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[4]/span/div/a/div[2]/span': 'Jogo 4', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[5]/span/div/a/div[2]/span': 'Jogo 5',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[6]/span/div/a/div[2]/span': 'Jogo 6', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[7]/span/div/a/div[2]/span': 'Jogo 7',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[8]/span/div/a/div[2]/span': 'Jogo 8', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[9]/span/div/a/div[2]/span': 'Jogo 9',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[10]/span/div/a/div[2]/span': 'Jogo 10', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[11]/span/div/a/div[2]/span': 'Jogo 11',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[12]/span/div/a/div[2]/span': 'Jogo 12', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[13]/span/div/a/div[2]/span': 'Jogo 13',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[14]/span/div/a/div[2]/span': 'Jogo 14', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[15]/span/div/a/div[2]/span': 'Jogo 15',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[16]/span/div/a/div[2]/span': 'Jogo 16', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[17]/span/div/a/div[2]/span': 'Jogo 17',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[18]/span/div/a/div[2]/span': 'Jogo 18', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[19]/span/div/a/div[2]/span': 'Jogo 19',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[20]/span/div/a/div[2]/span': 'Jogo 20', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[21]/span/div/a/div[2]/span': 'Jogo 21',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[22]/span/div/a/div[2]/span': 'Jogo 22', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[23]/span/div/a/div[2]/span': 'Jogo 23',
                 '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[24]/span/div/a/div[2]/span': 'Jogo 24', '//*[@id="PageContent"]/div/div[2]/div[2]/div/div[7]/div/div/div[2]/section/div[2]/ol/li[25]/span/div/a/div[2]/span': 'Jogo 25'}

        #Laço de repetição para cada link
        for xpath, link in links_detalhes.items():
            pagina.click(f'xpath={xpath}')
            try:
               assert pagina.url != 'https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2'
               print(f'Link {link} funcional')
            except:
                print(f'Link {link} não funcional')
            #Retorna a página incial para testar o próximo link
            pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Verifica se o link da classificação indicativa está correta
        with pagina.expect_popup() as popup_info:
            try:
                pagina.click('xpath=//*[@id="PageContent"]/div/div[1]/div[2]/div/div[1]/div/div/div/a')
                print('LINK ABERTO')
                pagina2 = popup_info.value
                assert pagina2.url != 'https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2'
                print('Link classificação funcional')
            except:
                print('Link classificação não funcional')

#Teste 54: Testa os links da página na seção avaliações
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até até a seção avaliações
#E clicar nos links na página
#Então eu devo ser redirecionado para outra página

def teste_links_avaliacoes():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba avaliações
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[2]/button')

        #Clica no link "Sobre classificações e opiniões"
        with pagina.expect_popup() as popup_info:
            pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[4]/a')
            print('LINK ABERTO')
        pagina2 = popup_info.value

        #Verifica se a URL mudou
        try:
            assert pagina2.url != 'https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2'
            print('LINK "SOBRE CLASSIFICAÇÕES E OPINIÕES" FUNCIONAL')
        except:
            print('LINK "SOBRE CLASSIFICAÇÕES E OPINIÕES" NÃO FUNCIONAL')

        #Clica no link "FAÇA LOGIN PARA ADICIONAR UMA RESENHA"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div/div/div[1]/div[2]/a/span')

        #Verifica se a URL mudou
        try:
            assert pagina.url != 'https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2'
            print('LINK "FAÇA LOGIN PARA ADICIONAR UMA RESENHA" FUNCIONAL')
        except:
            print('LINK "FAÇA LOGIN PARA ADICIONAR UMA RESENHA" NÃO FUNCIONAL')

#Teste 55: Testa os links da página na seção avaliações
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E ir até até a seção avaliações
#E clicar nos links na página
#Então eu devo ser redirecionado para outra página

def teste_links_mais():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Clica na aba "Mais"
        pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[1]/div/ul/li[3]/button')
        print('Aba "Mais" aberta')

        #Dicionários com os xpaths e os nomes dos links
        xpaths_link = {'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[1]/div[1]/a': 'Suporte ao Persona 3 Reload',
                       'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[2]/div/a': 'Aviso sobre epilepsia fotossensível',
                       'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[2]/div[3]/div[2]/a': 'Informações de permissões',
                       'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[3]/div[1]/div[1]/a': 'Código de conduta do Xbox Live',
                       'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[3]/div[1]/div[2]/a': 'Persona 3 Reload política de privacidade',
                       'xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[3]/div[1]/div[3]/a': 'Termos da transação'}

        #Laço de repetição para verificar os links
        for xpath, link in xpaths_link.items():
            try:
                with pagina.expect_popup() as popup_info:
                    pagina.click(xpath)
                    pagina2 = popup_info.value
                    assert pagina2.url != 'https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2'
                    print(f'Link {link} funcional')
            except:
                print(f'Link {link} não funcional')

        #Verifica o botão de denúncia
        try:
            pagina.click('xpath=//*[@id="PageContent"]/div/div[2]/div[2]/div/div[3]/div/div[3]/div[2]/button')
            assert pagina.inner_text('xpath=/html/body/reach-portal/div[3]/div/div/div/div/div[1]/h2') == 'Denunciar este produto à Microsoft'
            print('Denunciar produto funcional')
        except:
            print('Denunciar produto não funcional')

#Teste 56: Testa os links da página na parte final
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E clicar nos links no final da página
#Então eu devo ser redirecionado para outra página

def teste_links_final():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Dicionário com xpaths e seus links
        xpaths_links = {'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[1]/ul/li[1]/a': 'Xbox consoles',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[1]/ul/li[2]/a': 'Jogos Xbox',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[1]/ul/li[3]/a': 'Xbox Game Pass',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[1]/ul/li[4]/a': 'Acessórios do Xbox',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/ul/li[1]/a': 'Notícias do Xbox',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/ul/li[2]/a': 'Suporte do Xbox',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/ul/li[3]/a': 'Feedback',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/ul/li[4]/a': 'Padrões da Comunidade',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[2]/ul/li[5]/a': 'Aviso de potenciais convulsões por fotossensibilidade',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[3]/ul/li[1]/a': 'Conta Microsoft',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[3]/ul/li[2]/a': 'Suporte da Microsoft Store',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[3]/ul/li[3]/a': 'Devoluções',
                        'xpath=//*[@id="uhf-footer"]/nav/div[1]/div[3]/ul/li[4]/a': 'Rastreamento de pedidos',
                        'xpath=//*[@id="uhf-footer"]/nav/div[2]/div/ul/li/a': 'Jogos'}

        #Laço de repetição para cada link
        for xpath, link in xpaths_links.items():
            try:
                pagina.click(xpath)
                assert pagina.url != 'https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2'
                print(f'Link {link} funcional')
                pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')
            except:
                print(f'Link {link} não funcional')
                pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

#Teste 57: Testa os links da página no rodapé
#Dado que eu tenha um dispositivo com acesso ao site do Gamepass
#Quando eu acessar a página do jogo "Persona 3 Reload"
#E clicar nos links no rodapé
#Então eu devo ser redirecionado para outra página

def teste_links_rodape():
    with sync_playwright() as p:
        #Criando o navegador
        navegador = p.chromium.launch(headless=False)

        #Criando o contexto
        context = navegador.new_context()

        #Criando a página dentro do contexto
        pagina = context.new_page()

        #Maximiza a janela do navegador
        pagina.set_viewport_size({'width': 1500, 'height': 1080})

        #Indica a qual página o código deve ir
        pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

        #Dicionário com os xpaths e os nomes dos links no rodapé
        xpaths_links = {'xpath=//*[@id="locale-picker-link"]': 'Português (Brasil)', 'xpath=//*[@id="uhf-footer"]/div/a[2]': 'Suas opções de privacidade',
                        'xpath=//*[@id="uhf-footer"]/div/a[3]/span': 'Privacidade dos Dados de Saúde do Consumidor', 'xpath=//*[@id="c-uhff-footer_contactus"]/a': 'Entre em contato com a Microsoft',
                        'xpath=//*[@id="c-uhff-footer_privacyandcookies"]/a': 'Privacidade e Cookies', 'xpath=//*[@id="c-uhff-footer_managecookies"]/a': 'Gerenciar cookies',
                        'xpath=//*[@id="c-uhff-footer_compliance"]/a': 'Ética e Compliance', 'xpath=//*[@id="c-uhff-footer_termsofuse"]/a': 'Nota Legal',
                        'xpath=//*[@id="c-uhff-footer_trademarks"]/a': 'Marcas', 'xpath=//*[@id="c-uhff-third_party_notices"]/a': 'Avisos de terceiros',
                        'xpath=//*[@id="c-uhff-footer_aboutourads"]/a': 'Sobre os nossos anúncios'}

        #Laço de repetição
        for xpath, link in xpaths_links.items():
            try:
                pagina.click(xpath)
                assert pagina.url != 'https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2'
                print(f'Link {link} funcional')
                pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')
            except:
                print(f'Link {link} não funcional')
                pagina.goto('https://www.xbox.com/pt-BR/games/store/persona-3-reload/9nkk6z0k3rh2')

