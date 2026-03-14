"""
Trie (Prefix Tree) Implementation
Supports: insert(word), search(word), starts_with(prefix)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        """Search for a complete word in the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        """Check if any word in the trie starts with the given prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def delete(self, word):
        """Delete a word from the trie and clean up unused nodes"""
        def _delete_helper(node, word, index):
            # Base case: if we've processed all characters in the word
            if index == len(word):
                # If this is not the end of a word, the word doesn't exist
                if not node.is_end_of_word:
                    return False
                # Mark this node as not the end of a word
                node.is_end_of_word = False
                # Return True if this node has no children (can be deleted)
                return len(node.children) == 0
            
            char = word[index]
            # If the character doesn't exist in the trie, the word doesn't exist
            if char not in node.children:
                return False
            
            # Recursively delete the next character
            should_delete_child = _delete_helper(node.children[char], word, index + 1)
            
            # If the child should be deleted, remove it from the current node's children
            if should_delete_child:
                del node.children[char]
                
            # Return True if the current node should be deleted:
            # - It's not the end of a word
            # - And it has no remaining children
            return not node.is_end_of_word and len(node.children) == 0
        
        # Start the deletion process from the root
        _delete_helper(self.root, word, 0)