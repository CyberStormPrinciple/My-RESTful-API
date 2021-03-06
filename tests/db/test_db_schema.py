import unittest
from src.db.user_db import *
from src.db.item_db import *
from src.db.db_utils import connect
from load_json import *

class TestDBSchema(unittest.TestCase):

    def test_rebuild_tables(self):
        """Rebuild the tables"""
        rebuild_items_table()
        rebuild_users_table()
        self.assertEqual(0, get_num_all_users()[0][0],
            "Number of users is not correct")

    def test_rebuild_tables_is_idempotent(self):
        """Drop and rebuild the tables twice"""
        rebuild_items_table()
        rebuild_users_table()
        rebuild_items_table()
        rebuild_users_table()
        self.assertEqual(0, get_num_all_users()[0][0],
            "Number of users is not correct")

    def test_seed_data_works(self):
        """Attempt to insert the seed data"""
        rebuild_items_table()
        rebuild_users_table()
        insert_json_file()
        self.assertEqual(6, get_num_all_users()[0][0],
            "Number of users is not correct")
