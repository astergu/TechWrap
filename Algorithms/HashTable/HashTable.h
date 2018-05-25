#ifndef _HASH_TABLE_H_
#define _HASH_TABLE_H_

template<typename K, typename V>
class HashNode {
public:
    HashNode(K key, V value) {
        this->key = key;
        this->value = value;
    }

public:
    K key;
    V value;
};


template<typename K, typename V>
class HashTable {
public:
    HashTable() {
        _capacity = 20;
        _size = 0;
        map = new HashNode<K, V>*[_capacity];

        // initialize
        for (int i = 0; i < _capacity; ++i) {
            map[i] = nullptr;
        }
    }

    int hashCode(K key) {
        return key % _capacity;
    }
    
    void insert(K key, V value) {
        HashNode<K, V> nnode = new HashNode(key, value);
        int hashidx = hashCode(key);
        while (map[hashidx] != nullptr && map[hashidx]->key != key) {
            hashidx++;
            hashidx %= _capacity;
        }
        map[hashidx] = nnode;
        _size++;
    }

    HashNode<K, V> find(K key) {
        int hashidx = hashCode(key);
        while (map[hashidx] != nullptr) {
            if (map[hashidx]->key == key) {
                return map[hashidx];
            }
            hashidx++;
            hashidx %= _capacity; 
        }
        return nullptr;
    }

    void deleteKey(K key) {
    }

    int isEmpty() {
        return size == 0;
    }

private:
    HashNode<K, V> **map;
    HashNode<K, V> *dummy;
    int _size;
    int _capacity;
};

#endif
