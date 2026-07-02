class TrieNode {
    TrieNode[] child;
    boolean isLeaf;

    TrieNode() {
        child = new TrieNode[26];
        isLeaf = false;
    }
}

class Trie {
    TrieNode root;

    Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode curr = root;

        for (int i = 0; i < word.length(); i++) {
            int idx = word.charAt(i) - 'a';

            if (curr.child[idx] == null) {
                curr.child[idx] = new TrieNode();
            }

            curr = curr.child[idx];
        }

        curr.isLeaf = true;
    }

    public String longestCommonPrefix() {
        TrieNode curr = root;
        StringBuilder res = new StringBuilder();

        while (true) {
            int count = 0;
            int index = -1;

            
            for (int i = 0; i < 26; i++) {
                if (curr.child[i] != null) {
                    count++;
                    index = i;
                }
            }

            
            if (count != 1 || curr.isLeaf) {
                break;
            }

            res.append((char) ('a' + index));
            curr = curr.child[index];
        }

        return res.toString();
    }
}



class Solution {
    public String longestCommonPrefix(String arr[]) {
        Trie obj = new Trie();
        for(String x : arr){
            obj.insert(x);
        }
        
        return obj.longestCommonPrefix();
        
    }
}