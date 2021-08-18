from selenium.webdriver import Firefox
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randrange


class InstaBot():
  """Classe responsável por comentar dentro de uma foto."""

  def __init__(self, login: str, senha: str, link: str, path: str):
    """
    Parâmetros:
      login: nome de usuário da conta 
      
      senha: a senha da conta
      
      link: o link completo da imagem onde os comentários serão realizados

      path: caminho para o arquivo .txt onde estão as strings com o texto que será comentado, separado por ponto-e-vírgula (;)
    """
    self.browser = Firefox()
    self.__playersList =  open(path).read().split(';')
    self.__link = link
    self.__login = login
    self.__senha = senha
    self.__numberOfComments = 0

  
  def __login_operation__(self):
    """Classe responsável por realizar o login na página do instagram através do post onde os comentários serão realizados. É implementada internamente,
       logo não deve ser utilizada pelo usuário da classe
    """
    _login_button = self.browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF')
    _login_button.click()

    sleep(0.3)
    __username_field = self.browser.find_element_by_name('username')
    __username_field.click()
    __username_field.send_keys(self.__login)

    __password_field = self.browser.find_element_by_name('password')
    __password_field.click()
    __password_field.send_keys(self.__senha)

    _enter_button = self.browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF')
    _enter_button.click()

    sleep(7)

    __denial = self.browser.find_element_by_class_name('sqdOP.yWX7d.y3zKF')
    __denial.click()

    sleep(4)


  def __final_report(self):
    print("[ RELATÓRIO FINAL ] \n\n\n")
    print(f"NÚMERO DE COMENTÁRIOS: {self.__numberOfComments}\n")
    input('PRESSIONE [ENTER] PARA SAIR')
    self.browser.quit()


  def comment(self):

    """
    Operação de comentar dentro de uma publicação cujo link foi passado como parâmetro na declaração da classe. Possui um timer para não ser classificada como spam
    """

    self.browser.get(self.__link)
    self.__login_operation__()

    __comment_box = self.browser.find_element_by_class_name('X7cDz')
    __comment_box.click()

    __comment_box = self.browser.find_element_by_class_name('Ypffh')
    counter = 0

    for name in self.__playersList:
      __comment_box.send_keys(name)
      __comment_box.send_keys(Keys.ENTER)
      
      counter += 1
      self.__numberOfComments += 1

      if (name == self.__playersList[-1]):
        self.__final_report()
        
      sleep(randrange(25, 35))
      
      if counter == 4:
        sleep(45)
        counter = 0

    
