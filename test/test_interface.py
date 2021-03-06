from pdb2sql.interface import interface
import unittest

class TestSim(unittest.TestCase):
	"""Test Interface calculation."""

	def test_interface(self):

		db = interface(self.pdb)
		db.get_contact_atoms()
		db.get_contact_residues()

	def setUp(self):
		self.pdb = 'pdb/1AK4.pdb'

if __name__ == '__main__':
    unittest.main()