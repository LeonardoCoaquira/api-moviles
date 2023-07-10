from django.contrib.auth.models import User
from django.test import TestCase
from api.serializer import UserSerializer

class UserSerializerTest(TestCase):
    def setUp(self):
        self.user_data = {
            'id': '1',
            'usuario': 'usuario1',
            'clave': '1234',
            'estado': 'A'
        }
        self.serializer = UserSerializer(data=self.user_data)

    def test_valid_serializer_data(self):
        self.assertTrue(self.serializer.is_valid())

    def test_serialized_fields(self):
        self.assertEqual(
            set(self.serializer.data.keys()),
            {'id', 'usuario', 'clave', 'estado'}
        )

    def test_deserialized_data(self):
        self.serializer.is_valid()
        deserialized_data = self.serializer.validated_data
        self.assertEqual(deserialized_data, self.user_data)
