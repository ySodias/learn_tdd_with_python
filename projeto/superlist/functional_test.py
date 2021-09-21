from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser = quit()

	def test_can_start_a_list_and_retrive_in_later(self):
	#Edith ouviu falar de uma aplicação online interessante
	#Lista de tarefa. Ela decide verificar sua homepage
		self.browser.get('http://localhost:8000')

	# Ela percebe que o título da página e o cabeçalho mencionam listas de tarefas (todo)
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main(warnings='ignore')

#Ela é convidada a inserir um item de tarefa imediatamente

#Ela digita "Buy peacock feathers" (Comprar penas de pavão) em uma caixa de texto ( o hobby de Edith é fazer iscas para pesca com fly)

#Quando ela tecla enter, a página é atualizada e agora a página lista "1: Buy peacock feathers" como um item em uma lista de tarefas

#Ainda continua havendo uma caixa de texto convidado-a a acrescentar outro item. Ela insere "Use peacok feathers to make a fly" (usar penas de pavão para fazer um fly - Edith é bem metódica)

#A página é atualizada novamentee agora mostra os dois itens em sua lista

#Edith se pergunta se o site lembrará de sua lista. Então ela nota que o site gerou uma url único para ela -- há um pequeno texto explicativo para isso.

# Ela acessa esse URL - sua lista de tarefas continua lá

# Satisfeita, ela volta a dormir





