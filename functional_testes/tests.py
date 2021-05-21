# TODO 1: Baixar este arquivo: https://github.com/mozilla/geckodriver/releases ou pode baixar diretamente em
# https://github.com/mozilla/geckodriver/releases/download/v0.29.1/geckodriver-v0.29.1-win64.zip
# Copiar o arquivo geckodriver.exe para a pasta "Scripts" que se encontra dentro da pasta onde o Python foi instalado
# em seu computador

# TODO 2: instalar o selenium executando o comando --> pip install selenium

# ------------------------------------------
# Começam os testes
import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# TODO 3: realizar os testes --> Tutorial em http://pythonclub.com.br/selenium-parte-1.html

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        # Ana ouviu falar de uma nova aplicação online interessante para passe de ônibus. Ela decidiu verificar sua
        # homepage.
        self.navegador = webdriver.Firefox()
        self.navegador.get('http://127.0.0.1:8000')

    def tearDown(self) -> None:
        # self.navegador.quit()
        pass

    def test_cadastro(self):
        # Ela percebeu que o título da página e o cabeçalho mencionam (BussPass).
        self.assertIn('BussPass', self.navegador.title)

        # Ela é convidada a escolher entre entrar no aplicativo ou fazer um cadastro.
        botao_entrar = self.navegador.find_element_by_id('entrar')
        self.assertIn('Entrar', botao_entrar.text)

        botao_cadastrar = self.navegador.find_element_by_id('cadastrar')
        self.assertIn('Cadastrar', botao_cadastrar.text)

        # Ela escolheu se cadastrar e foi levada a outra tela que o título da página e o cabeçalho mencionam (Cadastro),
        # com várias caixas de texto.
        ActionChains(self.navegador).click(botao_cadastrar).perform()
        time.sleep(1.0)
        self.assertIn('Cadastro', self.navegador.title)
        cabecalho = self.navegador.find_element_by_id('cabecalho')
        self.assertIn('Cadastro', cabecalho.text)

        # Ao clicar com o mouse na primeira caixa de texto Ana é convidada a inserir seu nome de usuário
        caixa_texto_usuario = self.navegador.find_element_by_id('id_nome')
        caixa_texto_usuario.send_keys('Ana')
        caixa_texto_usuario.send_keys(Keys.TAB)

        # Ao teclar TAB Ana é convidada a inserir seu e-mail na caixa de texto seguinte. Ao clicar
        # enter novamente, Ana é convidada a inserir seu CPF na caixa de texto seguinte. Ao teclar TAB novamente,
        # Ana é convidada a inserir sua data de nascimento na caixa de texto seguinte. Ao teclar TAB novamente,
        # Ana é convidada a inserir seu número de telefone na caixa de texto seguinte. Ao teclar TAB novamente,
        # Ana é convidada a inserir sua instituição de ensino que frequenta na caixa de texto seguinte. Ana é
        # convidada a prosseguir seu cadastro clicando na opção “Cadastrar” que está no final da tela. Ana é levada a
        # outra tela onde é convidada a finalizar seu cadastro criando uma senha de 8 dígitos ao clicar em
        # “Continuar”. Ana é convidada a inserir sua senha na caixa de texto seguinte. Ana é convidada a inserir sua
        # confirmação de senha na caixa de texto seguinte. No final da tela Ana é convidada a clicar em “Ok” para
        # finalizar seu cadastro. Com o cadastro finalizado, Ana será direcionada a outra tela com título da página e
        # cabeçalho (Login), com duas caixas de texto. Ana é convidada a inserir seu número de cadastro na caixa de
        # texto seguinte. Ana é convidada a inserir sua senha na caixa de texto seguinte. Em seguida Ana é convidada
        # a entrar no site com seu login, clicando em “ENTRAR” no final da tela.

    def test_recargas_e_utilizacoes(self):
        # Ao entrar no site, Ana é direcionada a uma nova tela com duas caixas de texto (Recargas) e (Utilizações).
        # Ana será convidada a escolher entre fazer uma recarga no seu passe ou observar as utilizações do seu passe.
        # Ana escolheu fazer uma recarga ao clicar em “Recargas” com o mouse.
        # Ana será direcionada a outra tela com título da página e cabeçalho (Recargas), com quatro caixas de texto.
        # Ana é convidada a inserir seu nome de usuário caixa de texto seguinte.
        # Ao teclar TAB, Ana é convidada a inserir sua data de nascimento na caixa de texto seguinte.
        # Ao teclar TAB novamente, constará seu saldo atual na caixa de texto seguinte.
        # Ao teclar TAB, Ana é convidada a inserir o valor de sua recarga na caixa de texto seguinte.
        # Ana é convidada a finalizar sua recarga clicando com o mouse em “OK” no final da tela.
        # Ana verifica seu saldo e consta o valor que ela recarregou.
        # Satisfeita ela se prepara para pegar seu ônibus de volta para casa
        pass
