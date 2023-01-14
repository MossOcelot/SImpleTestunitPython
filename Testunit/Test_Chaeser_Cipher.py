from project import Chaeser_Cipher
import unittest

class ChaeserCipher(unittest.TestCase):
    def test_Hello_World_4_should_Lipps_Asvph(self):
        s = "Hello_World!"
        k = 4

        expected_result = "Lipps_Asvph!"
        result = Chaeser_Cipher.caesarCipher(s,k)
        self.assertEqual(expected_result, result)

    def test_Hello_WorldCiphering_26_should_Ciphering(self):
        s = "Ciphering."
        k = 26

        expected_result = "Ciphering."
        result = Chaeser_Cipher.caesarCipher(s,k)
        self.assertEqual(expected_result, result)

    def test_string_62_62_should_rotated(self):
        s = "!m-rB`-oN!.W`cLAcVbN/CqSoolII!SImji.!w/`Xu`uZa1TWPRq`uRBtok`xPT`lL-zPTc.BSRIhu..-!.!tcl!-U"
        k = 62

        expected_result = "!w-bL`-yX!.G`mVKmFlX/MaCyyvSS!CSwts.!g/`He`eJk1DGZBa`eBLdyu`hZD`vV-jZDm.LCBSre..-!.!dmv!-E"
        result = Chaeser_Cipher.caesarCipher(s,k)
        self.assertEqual(expected_result, result)

    def test_www_abc_xy_87_should_fff_jkl_gh(self):
        s = "www.abc.xy"
        k = 87

        expected_result = "fff.jkl.gh"
        result = Chaeser_Cipher.caesarCipher(s,k)
        self.assertEqual(expected_result, result)

    