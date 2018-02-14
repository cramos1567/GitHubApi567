import unittest

from GitRepo import getUserCommits

class testAPI(unittest.TestCase):
    def test_inputType(self):
        self.assertEqual(getUserCommits(12), "InvalidInput")
        self.assertNotEqual(getUserCommits("cramos1567"), "InvalidInput")
        self.assertEqual(getUserCommits(""), "InvalidInput")

    def test_validUsername(self):
        self.assertNotEqual(getUserCommits("cramos1567"), "Invalid Username")
        self.assertEqual(getUserCommits("crramos1567"), "Invalid Username")

if __name__ == '__main__':
    print("Running unit test")
    unittest.main()
