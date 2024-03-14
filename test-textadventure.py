import unittest
import io
import contextlib
import sys
from unittest.mock import Mock
 
from textadventure import *
 
class RichRoomTest(unittest.TestCase):
    def a_rich_room_can_be_created(self):
        room = RichRoom(None)
