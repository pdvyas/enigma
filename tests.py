import unittest
import enigma

class TestTrivial(unittest.TestCase):

    def test_trivial(self):
        self.assertTrue(True)


class TestForward(unittest.TestCase):

    def test_forward(self):
        r = enigma.Rotor("I")
        r.set("F")
        self.assertEqual("I", r.forward_convert("F"))


class TestStep(unittest.TestCase):

    def test_step_forward(self):
        r = enigma.Rotor("I")
        r.set("E")
        r.step()
        self.assertEqual("I", r.forward_convert("F"))

class TestBackward(unittest.TestCase):

    def test_forward(self):
        r = enigma.Rotor("III")
        r.set("X")
        self.assertEqual("Z", r.backward_convert("X"))


class TestIndex(unittest.TestCase):

    def test_index(self):
        self.assertEqual(0,  enigma.char_index["A"])
        self.assertEqual(5,  enigma.char_index["F"])
        self.assertEqual(1,  enigma.char_index["B"])
        self.assertEqual(25, enigma.char_index["Z"])

class TestExample(unittest.TestCase):

    def test_char(self):
        m = enigma.Machine("B", "BETA", ["III", "IV", "I"], "AXLE")
        self.assertEqual("H", m.convert("F"))

    def test_block(self):
        m = enigma.Machine("B", "BETA", ["III", "IV", "I"], "AXLE")
        self.assertEqual("HYIHL", m.convert("FROMH"))

    def test_hello(self):
        m = enigma.Machine("B", "BETA", ["I", "II", "III"], "AAAA")
        self.assertEqual("ILBDAAMTAZ", m.convert("HELLOWORLD"))

    def test_aa(self):
        m = enigma.Machine("B", "BETA", ["III", "II", "I"], "AAEA")
        self.assertEqual("JW", m.convert("AA"))

    def test_example2(self):
        m = enigma.Machine("B", "BETA", ["III", "II", "VI"], "AAAZ")
        self.assertEqual("DNLERUIWXPEEQZTPZOMKSYZFICQT", m.convert("AAAAAAAAAAAAAAAAAAAAAAAAAAAA"))

    def test_sample(self):
        m = enigma.Machine("B", "BETA", ["III", "IV", "I"], "AXLE")
        msg = 'FROMHISSHOULDERHIAWATHATOOKTHECAMERAOFROSEWOODMADEOFSLIDINGFOLDINGROSEWOODNEATLYPUTITALLTOGETHERINITSCASEITLAYCOMPACTLYFOLDEDINTONEARLYNOTHINGBUTHEOPENEDOUTTHEHINGESPUSHEDANDPULLEDTHEJOINTSANDHINGESTILLITLOOKEDALLSQUARESANDOBLONGSLIKEACOMPLICATEDFIGUREINTHESECONDBOOKOFEUCLID'
        enc = 'HYIHLBKOMLIUYDCMPPSFSZWSQCNJEXNUOJYRZEKTCNBDGUFLIIEGEPGRSJUJTCALGXSNCTMKUFWMFCKWIPRYSODJCVCFYQLVQLMBYUQRIRXEPOVEUHFIRIFKCGVSFPBGPKDRFYRTVMWGFUNMXEHFHVPQIDOACGUIWGTNMKVCKCFDZIOPYEVXNTBXYAHAOBMQOPGTZXVXQXOLEDRWYCMMWAONVUKQOUFASRHACKKXOMZTDALHUNVXKPXBHAVQXVXEPUNUXTXYNIFFMDYJVKH'
        self.assertEqual(enc, m.convert(msg))



if __name__ == "__main__":
    unittest.main()
