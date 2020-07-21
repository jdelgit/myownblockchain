import unittest
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

import models.keymanager as km
from utils.config import SEED_LENGTH


class keymanagerTest(unittest.TestCase):
    def test_generate_new_seed(self):
        seed_words = km.generate_new_seed()
        self.assertEqual(len(seed_words), SEED_LENGTH)

    def test_generate_private_key(self):
        seed = [
            "mirror",
            "lay",
            "dust",
            "critic",
            "finding",
            "text",
            "attorney",
            "instruction",
            "official",
            "sure",
        ]
        seed_hex_control = (
            "97dfa9bfb4247533ae0b4f53bf6e26f133d98abe06d5c4850a1ea2f87c7a2e99"
        )
        generated_key = km.generate_private_key(seed)
        self.assertEqual(generated_key, seed_hex_control)

    def test_generate_public_key(self):
        private_key_hex = (
            "97dfa9bfb4247533ae0b4f53bf6e26f133d98abe06d5c4850a1ea2f87c7a2e99"
        )
        nonce = 0

        public_key_control = (
            "8d71dd37f43962973c8ee1c48a15ab8b8a03506f4a6343d4ec351abe3b27d99f"
        )
        public_key = km.generate_public_key(private_key_hex, 0)
        self.assertEqual(public_key, public_key_control)

    def test_generate_keypair_from_seed(self):
        wallet_data_control = {
            "private": "97dfa9bfb4247533ae0b4f53bf6e26f133d98abe06d5c4850a1ea2f87c7a2e99",
            "public": "8d71dd37f43962973c8ee1c48a15ab8b8a03506f4a6343d4ec351abe3b27d99f",
            "wallet_seed": [
                "mirror",
                "lay",
                "dust",
                "critic",
                "finding",
                "text",
                "attorney",
                "instruction",
                "official",
                "sure",
            ],
        }
        wallet_data = km.generate_keypair_from_seed(wallet_data_control["wallet_seed"])
        self.assertDictEqual(wallet_data, wallet_data_control)

    def test_generate_keypair_from_privatekey(self):
        wallet_data_control = {
            "private": "97dfa9bfb4247533ae0b4f53bf6e26f133d98abe06d5c4850a1ea2f87c7a2e99",
            "public": "8d71dd37f43962973c8ee1c48a15ab8b8a03506f4a6343d4ec351abe3b27d99f",
        }
        wallet_data = km.generate_keypair_from_privatekey(
            wallet_data_control["private"]
        )
        self.assertDictEqual(wallet_data, wallet_data_control)

    # def test_generate_digital_signature(self):
    #     pass


if __name__ == "__main__":
    unittest.main()
