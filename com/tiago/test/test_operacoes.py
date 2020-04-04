from unittest import TestCase
from com.tiago.operacoes import Operacoes

class TestOperacoes(TestCase):
    def setUp(self):
        self.operacoes = Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([1,5]), 6, "Deveria ser 6")
    
    def test_subracao(self):
        self.assertEqual(self.operacoes.subtracao([5,1]), -6, "Deveria ser 4")
    