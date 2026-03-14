"""
Test file for Trie implementation
"""
import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
    
    def test_insert_and_search(self):
        # Insert some words
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("application")
        
        # Test exact searches
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("application"))
        self.assertFalse(self.trie.search("apples"))
        self.assertFalse(self.trie.search("ap"))
    
    def test_starts_with(self):
        # Insert some words
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("application")
        self.trie.insert("banana")
        
        # Test prefix searches
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("appl"))
        self.assertTrue(self.trie.starts_with("a"))
        self.assertFalse(self.trie.starts_with("apples"))  # Should return False since no word starts with "apples"
        self.assertFalse(self.trie.starts_with("bananz"))  # Should return False since no word starts with "bananz"
        self.assertFalse(self.trie.starts_with("z"))
    
    def test_delete(self):
        # Insert some words
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("application")
        self.trie.insert("banana")
        
        # Test deleting a word that exists
        self.trie.delete("app")
        self.assertFalse(self.trie.search("app"))
        self.assertTrue(self.trie.search("apple"))  # Should still exist
        self.assertTrue(self.trie.search("application"))  # Should still exist
        
        # Test deleting a word that is a prefix of another word
        self.trie.delete("apple")
        self.assertFalse(self.trie.search("apple"))
        self.assertTrue(self.trie.search("application"))  # Should still exist
        
        # Test deleting a word that shares a prefix with others
        self.trie.delete("application")
        self.assertFalse(self.trie.search("application"))
        self.assertTrue(self.trie.search("banana"))  # Should still exist
        
        # Test deleting a non-existent word
        self.trie.delete("nonexistent")
        self.assertTrue(self.trie.search("banana"))  # Should still be there
        
        # Test that deleting cleans up nodes
        # After deleting "banana", the trie should be empty
        self.trie.delete("banana")
        self.assertFalse(self.trie.search("banana"))
        self.assertFalse(self.trie.starts_with("b"))  # Should be False since "banana" is gone
        
        # Test empty trie after all deletions
        self.assertFalse(self.trie.search(""))
        self.assertFalse(self.trie.starts_with("a"))
        self.assertFalse(self.trie.starts_with("b"))
    
    def test_empty_trie(self):
        # Test with empty trie
        self.assertFalse(self.trie.search(""))
        self.assertTrue(self.trie.starts_with(""))  # Empty string is prefix of everything
    
    def test_single_char(self):
        self.trie.insert("a")
        self.assertTrue(self.trie.search("a"))
        self.assertTrue(self.trie.starts_with("a"))
        self.assertFalse(self.trie.search("b"))
        self.assertFalse(self.trie.starts_with("b"))
        
        # Test deleting single character
        self.trie.delete("a")
        self.assertFalse(self.trie.search("a"))
        self.assertFalse(self.trie.starts_with("a"))

if __name__ == '__main__':
    unittest.main()