#!/usr/bin/python3
"""This module contains Test Cases of Console interpreter"""

from unittest import TestCase, skipIf
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.place import Place
from models import storage
from tests import clear_output
import os
from models import storage_type
import sqlalchemy
import MySQLdb


class TestConsole_create(TestCase):
    """Represents test class for create command"""

    @skipIf(storage_type == 'db',
            'Test for FileStorage')
    def test_file_storage_create(self):
        """Test case for create command by
        using the file storage
        """
        with patch("sys.stdout", new=StringIO()) as out:
            HBNBCommand().onecmd('create User first_name="Ian" \
                    last_name="Mbai" email="ianmbayyz@gmail.com" \
                    age=23')
            user_id = out.getvalue().strip()
            self.assertIn("User.{}".format(user_id), storage.all().keys())
            clear_output(out)
            HBNBCommand().onecmd('show User {}'.format(user_id))
            output = out.getvalue().strip()
            self.assertIn("'first_name': 'Ian'", output)
            self.assertIn("'last_name': 'Mbai'", output)
            self.assertIn("'email': 'ianmbayyz@gmail.com'", output)
            self.assertIn("'age': 23", output)
            clear_output(out)
            HBNBCommand().onecmd('create Place city_id="0001" user_id="0001" \
                    name="My_little_house" number_rooms=4 number_bathrooms=2 \
                    max_guest=10 price_by_night=300 latitude=37.773972 \
                    longitude=-122.431297')
            place_id = out.getvalue().strip()
            self.assertIn("Place.{}".format(place_id), storage.all().keys())
            clear_output(out)
            HBNBCommand().onecmd('show Place {}'.format(place_id))
            output = out.getvalue().strip()
            self.assertIn("'city_id': '0001'", output)
            self.assertIn("'user_id': '0001'", output)
            self.assertIn("'name': 'My little house'", output)
            self.assertIn("'number_rooms': 4", output)
            self.assertIn("'number_bathrooms': 2", output)
            self.assertIn("'max_guest': 10", output)
            self.assertIn("'price_by_night': 300", output)
            self.assertIn("'latitude': 37.773972", output)
            self.assertIn("'longitude': -122.431297", output)
            clear_output(out)
            HBNBCommand().onecmd('create City name="Sale"')
            city_id = out.getvalue().strip()
            self.assertIn("City.{}".format(city_id), storage.all().keys())

    @skipIf(storage_type != 'db', 'Test for DBStorage')
    def test_db_storage_create(self):
        """Tests create command with database storage"""
        with patch('sys.stdout', new=StringIO()) as out:
            HBNBCommand().onecmd('create User first_name="Ian" \
                    last_name="Njuguna" email="test@test.ma" \
                    password="ianian23@"')
            output = out.getvalue().strip()
            db_create = MySQLdb.connect(
                    host=os.getenv('HBNB_MYSQL_HOST'),
                    port=3306,
                    user=os.getenv('HBNB_MYSQL_USER'),
                    passwd=os.getenv('HBNB_MYSQL_PWD'),
                    db=os.getenv('HBNB_MYSQL_DB')
                    )
            cur = db_create.cursor()
            cur.execute('SELECT * FROM users WHERE id="{}"'.format(output))
            result = cur.fetchone()
            self.assertFalse(result is None)
            self.assertIn('Ian', result)
            self.assertIn('Njuguna', result)
            self.assertIn('test@test.ma', result)
            self.assertIn('ianian@', result)
            cur.close()
            db_create.close()

    @skipIf(storage_type != 'db', 'DBStorage test case')
    def test_db_storage_show(self):
        """Tests show command by using database storage"""
        with patch('sys.stdout', new=StringIO()) as out:
            user1 = User(email='wayne@test.com', password='gunznlove999')
            c_db = MySQLdb.connect(
                    host=os.getenv('HBNB_MYSQL_HOST'),
                    port=3306,
                    user=os.getenv('HBNB_MYSQL_USER'),
                    passwd=os.getenv('HBNB_MYSQL_PWD'),
                    db=os.getenv('HBNB_MYSQL_DB')
                    )
            cur = c_db.cursor()
            cur.execute('SELECT * FROM users WHERE id="{}"'.format(user1.id))
            result = cur.fetchone()
            self.assertFalse(result is not None)
            HBNBCommand().onecmd('show User {}'.format(user1.id))
            output = out.getvalue().strip()
            expected = '** no instance found **'
            self.assertEqual(output, expected)
            user1.save()
            c_db = MySQLdb.connect(
                    host=os.getenv('HBNB_MYSQL_HOST'),
                    port=3306,
                    user=os.getenv('HBNB_MYSQL_USER'),
                    passwd=os.getenv('HBNB_MYSQL_PWD'),
                    db=os.getenv('HBNB_MYSQL_DB')
                    )
            cur = c_db.cursor()
            cur.execute('SELECT * FROM users WHERE id="{}"'.format(user1.id))
            result = cur.fetchone()
            self.assertTrue(result is not None)
            self.assertIn('wayne@test.com', result)
            self.assertIn('gunznlove999', result)
            clear_output(out)
            HBNBCommand().onecmd('show User {}'.format(user1.id))
            output = out.getvalue()
            # self.assertIn('wayne@test.com', out.getvalue())
            # self.assertIn('gunznlove999', out.getvalue())
            cur.close()
            c_db.close()