import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_oikein(self):
        self.asserEqual(str(self.maksukortti), "saldo: 5.0")

    def test_rahan_lataus_toimii(self):
        self.maksukortti.lataa_rahaa(10)
        self.asserEqual(str(self.maksukortti), "saldo: 20.0")