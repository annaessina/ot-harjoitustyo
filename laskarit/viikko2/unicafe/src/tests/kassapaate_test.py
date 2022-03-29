import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_oikea_rahamaara(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaiden_lounaiden_maara(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edulliset_lounaiden_maara(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_osto_kateisella_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella (300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella (300), 60)
        self.assertEqual(self.kassapaate.edulliset, 2)
        
    def test_osto_kateisella_rahat_eiriita_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella (200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella (200), 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_osto_kateisella_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella (450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella (450), 50)
        self.assertEqual(self.kassapaate.maukkaat, 2)

    def test_osto_kateisella_rahat_eiriita_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kateisella (200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella (200), 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortilla_edullinen(self):
        self.kortti = Maksukortti (1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kortilla_ei_rahaa_edullinen(self):
        self.kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kortilla_maukkaasti(self):
        self.kortti = Maksukortti (1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kortilla_ei_rahaa_maukkaasti(self):
        self.kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_rahaa_kortille(self):
        self.kortti = Maksukortti (1000)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.kortti, 3000), None)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 103000)

    def test_ei_voi_lataa_neg_kortille(self):
        self.kortti = Maksukortti (1000)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.kortti, -3000), None)




    
    
    
        

        

    