import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)
    
    def test_rahan_lataaminen_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)
    
    def test_rahan_maara_ei_muutu(self):
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(15)
        self.assertNotEqual(self.maksukortti.ota_rahaa, True)

    def test_raha_ei_riita(self):
        self.maksukortti.ota_rahaa(8)
        self.assertNotEqual(self.maksukortti.ota_rahaa, False)
