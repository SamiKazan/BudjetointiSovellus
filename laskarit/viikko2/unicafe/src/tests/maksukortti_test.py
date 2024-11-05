import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_oikea_saldo(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_pystyy_lataa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_rahan_ottaminen(self):
        self.maksukortti.ota_rahaa(1)

        self.maksukortti.ota_rahaa(5000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 9.99)

        self.assertEqual(self.maksukortti.ota_rahaa(1), True)
