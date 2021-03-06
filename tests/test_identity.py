import unittest
import rigger


class TestIdentity(unittest.TestCase):

    def test_basic_identity(self):
        identity = rigger.identity()
        self.assertEqual(set(identity.keys()),
                         set(["name", "given", "family", "address", "city",
                              "state", "zip_code", "phone", "email"]))


if __name__ == '__main__':
    unittest.main()
