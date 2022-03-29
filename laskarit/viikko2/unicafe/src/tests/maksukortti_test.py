import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

        self.assertEqual(self.maksukortti.ota_rahaa(5), True)

        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 3.0")

        self.assertEqual(self.maksukortti.ota_rahaa(100), False)