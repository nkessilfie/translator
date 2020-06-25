import unittest
import translate_1


class TestTranslate(unittest.TestCase):

    # checking if home is a variable
    def test_homeInput(self):
        self.assertIsNotNone(translate_1.home)
        self.assertFalse(translate_1.home)

    # checking if option is a variable
    def test_optionInput(self):
        self.assertIsNotNone(translate_1.option)
        self.assertTrue(translate_1.option)

    if translate_1.option == 1:
        # checking the french dictionary
        def test_freDict(self):
            self.assertIn("hello", translate_1.fre_dict)
            self.assertIn("bye", translate_1.fre_dict)
            self.assertIn("yes", translate_1.fre_dict)
            self.assertNotIn("hi", translate_1.fre_dict)
            self.assertNotIn("_go_", translate_1.fre_dict)
            self.assertNotIn("123", translate_1.fre_dict)

        # assert insert variable isn't empty
        def test_frenchWord(self):
            self.assertIsNotNone(translate_1.french_word)

        # assert lower-cases in words
        def test_lowerFreCasing(self):
            self.assertEqual(translate_1.french_word.islower(), True)

        # assert that a key brings up its value
        def test_checkingFre(self):
            test_dictFre = translate_1.fre_dict
            for key in test_dictFre:
                if test_dictFre[key] == 'bonjour':
                    self.assertIn('hello', test_dictFre)



    if translate_1.option == 2:
        # checking the spanish dictionary
        def test_spaDict(self):
            self.assertIn("hello", translate_1.spa_dict)
            self.assertIn("bye", translate_1.spa_dict)
            self.assertIn("yes", translate_1.spa_dict)
            self.assertNotIn("hi", translate_1.spa_dict)
            self.assertNotIn("_go_", translate_1.spa_dict)
            self.assertNotIn("123", translate_1.spa_dict)

        # assert insert variable isn't empty
        def test_spanishWord(self):
            self.assertIsNotNone(translate_1.spanish_word)

        # assert lower-cases in words
        def test_lowerSpaCasing(self):
            self.assertEqual(translate_1.spanish_word.islower(), True)

        def test_checkingFre(self):
            test_dictSpa = translate_1.spa_dict
            for key in test_dictSpa:
                if test_dictSpa[key] == 'ola':
                    self.assertIn('hello', test_dictSpa)

    if translate_1.option == 3:
        # checking the pidgin dictionary
        def test_pidgDict(self):
            self.assertIn("hello", translate_1.pidg_dict)
            self.assertIn("bye", translate_1.pidg_dict)
            self.assertIn("yes", translate_1.pidg_dict)
            self.assertNotIn("hi", translate_1.pidg_dict)
            self.assertNotIn("_go_", translate_1.pidg_dict)
            self.assertNotIn("123", translate_1.pidg_dict)

        # assert insert variable isn't empty
        def test_pidginWord(self):
            self.assertIsNotNone(translate_1.pidgin_word)

        # assert lower-cases in words
        def test_lowerPidgCasing(self):
            self.assertEqual(translate_1.pidgin_word.islower(), True)


    # assert that a key brings up its value

# finally assert the exceptions

if __name__ == '__main__':
    unittest.main()
