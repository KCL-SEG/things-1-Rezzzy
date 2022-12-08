from django.core.exceptions import ValidationError
from django.test import TestCase
from things.models import Thing

class ThingsTest(TestCase):
    def setUp(self):
        self.thing = Thing(
            name="hello",
            description="hello 2",
            quantity = 3,
        )

    def test_things_creation(self):
        self.assertTrue(isinstance(self.thing, Thing))
        self.assertTrue(self.thing.name, "hello")
        try:
            self.thing.full_clean()
        except ValidationError:
            self.fail(message)
