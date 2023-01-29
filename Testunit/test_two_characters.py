from project import two_characters  
import unittest

class two_characters_test(unittest.TestCase):
    def test_give_10_beabeefeab_should_5(self):
        n = 10
        s = "beabeefeab"

        expect_result = 5

        result = two_characters.two_characters(n,s)
        self.assertEqual(expect_result,result)

    def test_give_28_asdcbsdcagfsdbgdfanfghbsfdab_should_8(self):
        n = 28
        s = "asdcbsdcagfsdbgdfanfghbsfdab"

        expect_result = 8

        result = two_characters.two_characters(n,s)
        self.assertEqual(expect_result,result)

    def test_give_28_asvkugfiugsalddlasguifgukvsa_should_0(self):
        n = 28
        s = "asvkugfiugsalddlasguifgukvsa"

        expect_result = 0

        result = two_characters.two_characters(n,s)
        self.assertEqual(expect_result,result)

    def test_giv_376_yviazlmiebx__ykulghbsijggnl_should_0(self):
        n = 376
        s = "yviazlmiebxllgsjzsbncdsyhqetbcabuademkpyllahuoactpxolunzmgknxxxuimpyybzynblohxygdmpihyhvkszpbvpkclesljnbgbiccwhmzsykigojxuaqvyyrcoepyynuaagnlrsttfzwhyngnwkcebzdwbmvpbfhocshnczrpdjwuveajxjalguamiunouiivsgeftnggdaeqennlvzcoswrdwogwlpysrjkcdlgkpwsgdzpyognjrxvzilxienerghdtfbcbvkdjtibmyiseaitznkulnoqzugkraswpjcmrabmpzthfkvravvklifydrydbbfmjfqgowdchsghftkssafnjdkwzwykulghbsijggnl"

        expect_result = 0
        result = two_characters.two_characters(n,s)
        self.assertEqual(expect_result,result)

    def test_give_1000_ucw__dknuamcxr_should_0(self):
        n = 1000
        s = "ucwtvajqreigbqszaukfieswtlhdvwhvlzsxswzbfcropnxlektloohamginpsxeooqsnlbaglmhiyednqibglmodhylweshcquhvxtqclqbvmptqglungavqccwlmhhogdlrzufeccpdmwnnrmgcxqlwdvtqqbicqbfgldxgdkkyvpzvlsncotyhwqeilzmguhpyrazsbsfvkzjzabcvrqwqndoqgztxtlpbfjcvbsplvbwlmmuyyqhiknybizxjzmrjvrtrsshgbiidrrcbapdwsxzlzlmcwrtvngokdvywjglorficgxqvatsbnvplqinopcrttpseweeekbypkvdanbcofvziojhpzhzaltgqvpstrrxfrjhdsdhrtwqzcqneicivppiquubsrvvbrtmwyhhqailyaaypfeusuefgqmbxmfadxtznfxfdtqggxeorjpvtmixlykezahzhxjbovglxggwxfcyrfxpefzolryernhmebhvcidocnknucdldlqtfvcoecygvejdrjnfrfrbqagcbellxnodvlzieerarmzrzfrdgxuhcfuwxvjlqmlflciotcylyyeywgtqgmbwghxaqesjgisuarjhqldcvxgyqzkwpecbapxxhevazufbgkrrzgxcnuuqdzzizbethncfhuvfjgccikzkqnksexzdvbhabdbrdspuygmhvmlbsptzejjtqnbdjpnhzamqvwliukpxxvkspgqxkedqcaaqwhglfiteiqnweyyfwswrkitadrayaqpllnnfatktsdlwtggzvjpefjglqbvpkpgtwarolbmsfbqxjsznmlmdohxwuxlasppsmqfcmfggxvimymnyqqoxdljdcyqlleuhfbemkwyysykdnjcazwrjhqpsclzhezqzghsmuzrapkxccniagkzfkntzrufvgqhbkfgyajwczsihigazrwvkdzequtqabdqqixjqudvdkvydknuamcxr"

        expect_result = 0
        result = two_characters.two_characters(n,s)
        self.assertEqual(expect_result, result)

