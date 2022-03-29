import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_rahan_lataus_toimii(self):
        kortti = Maksukortti(10)
        kortti.lataa_rahaa(20)
        self.assertEqual(str(kortti), "saldo: 0.3")
        
    def test_rahan_ottaminen_toimii(self):
        kortti = Maksukortti(10)
        kortti.ota_rahaa(5)
        self.assertEqual(str(kortti), "saldo: 0.05")

    def test_rahan_ottaminen_ei_toimi(self):
        kortti = Maksukortti(10)
        kortti.ota_rahaa(20)
        self.assertEqual(str(kortti), "saldo: 0.1")
        


    