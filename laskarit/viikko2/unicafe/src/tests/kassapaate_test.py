import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassassa_on_oikea_maara_rahaa_senteissa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kassassa_on_oikea_maara_rahaa_euroissa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_edulliset_lounaat_nolla_kun_ei_myyty_vielä(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukkaat_lounaat_nolla_kun_ei_myyty_vielä(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_voi_ostaa_kateisella_ja_kassa_kasvaa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_kateisella_ostettu_edullinen_lounas_kasvattaa_edullisten_maaraa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisella_ostettu_edullisen_lounaan_vaihtorahat_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(1000), 760)      

    def test_kateisella_edullinen_osto_ei_onnistu_jos_rahaa_liian_vahan(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_kateisella_edullinen_osto_palautuu_takaisin_jos_rahaa_liian_vahan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
    
    def test_kateisella_edullinen_osto_ei_lisaa_myytyjen_lounaiden_maaraa_jos_rahaa_liian_vahan(self):
        self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_lounaan_voi_ostaa_kateisella_kassa_kasvaa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisella_ostettu_maukas_lounas_kasvattaa_maukkaiden_maaraa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisella_ostettu_maukkaan_lounaan_vaihtorahat_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(1000), 600)
    
    def test_kateisella_maukas_osto_ei_onnistu_jos_rahaa_liian_vahan(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisella_maukas_osto_palautuu_takaisin_jos_rahaa_liian_vahan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(390), 390)
    
    def test_kateisella_maukas_osto_ei_lisaa_myytyjen_lounaiden_maaraa_jos_rahaa_liian_vahan(self):
        self.kassapaate.syo_maukkaasti_kateisella(390)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_voi_ostaa_kortilla_ja_palautuu_True(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)
    
    def test_edullisen_lounaan_osto_kasvattaa_ostettujen_lounaiden_maaraa_jos_rahaa_tarpeeksi(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullisen_lounaan_osto_ei_onnistu_jos_kortilla_ei_rahaa_tarpeeksi(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_edullisen_lounaan_osto_ei_kasvata_ostettujen_lounaiden_maaraa_jos_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_jos_kortilla_ei_tarpeeksi_rahaa_ei_veloiteta_edulliset(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)

    def test_maukkaan_lounaan_voi_ostaa_kortilla_ja_palautuu_True(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_maukkaan_lounaan_osto_kasvattaa_ostettujen_lounaiden_maaraa_jos_rahaa_tarpeeksi(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_lounaan_osto_ei_onnistu_jos_kortilla_ei_rahaa_tarpeeksi(self):
        kortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_maukkaan_lounaan_osto_ei_kasvata_ostettujen_lounaiden_maaraa_jos_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_jos_kortilla_ei_tarpeeksi_rahaa_ei_veloiteta_maukkaat(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)        

    def test_kassassa_oleva_raha_ei_muutu_kortilla_ostaessa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_kortille_voi_ladata_rahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(self.maksukortti.saldo, 2000)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(self.maksukortti.saldo, 1000)
