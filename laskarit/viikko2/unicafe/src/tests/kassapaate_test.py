import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassaPaate(unittest.TestCase):
    def setUp(self):
        self.kp = Kassapaate()
        self.kortti = Maksukortti(10)

    def test_alustettu_oikein(self):
        self.assertEqual(self.kp.maukkaat, 0)
        self.assertEqual(self.kp.edulliset, 0)
        self.assertEqual(self.kp.kassassa_rahaa, 100000)

    def test_syo_kateisella_vahan(self):
        self.kp.syo_edullisesti_kateisella(10)
        self.kp.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kp.edulliset, 0)
        self.assertEqual(self.kp.maukkaat, 0)
        self.assertEqual(self.kp.kassassa_rahaa, 100000)
    
    def test_syo_kateisella_tarpeeks(self):
        self.kp.syo_edullisesti_kateisella(240)
        self.kp.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kp.edulliset, 1)
        self.assertEqual(self.kp.maukkaat, 1)
        self.assertEqual(self.kp.kassassa_rahaa_euroina(), (100000+640)/100)

    def test_syo_kortilla_vahan(self):
        self.kp.syo_edullisesti_kortilla(self.kortti)
        self.kp.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kp.edulliset, 0)
        self.assertEqual(self.kp.maukkaat, 0)

    def test_syo_kortilla_tarpeeks(self):
        self.kortti.lataa_rahaa(990)
        self.kp.syo_edullisesti_kortilla(self.kortti)
        self.kp.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kp.edulliset, 1)
        self.assertEqual(self.kp.maukkaat, 1)

    def test_lataa_kortille(self):
        self.kp.lataa_rahaa_kortille(self.kortti, 10)

        self.assertEqual(self.kortti.saldo, 20)
        self.assertEqual(self.kp.kassassa_rahaa, 100010)

        self.assertEqual(self.kp.lataa_rahaa_kortille(self.kortti, -10), None)
