#ifndef _HASH_TABLE_H_
#define _HASH_TABLE_H_

#include <iostream>
using namespace std;


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
        dummy = new HashNode<K, V>(-1, -1);
    }

    int hashCode(K key) {
        return key % _capacity;
    }
    
    void insert(K key, V value) {
        HashNode<K, V> *nnode = new HashNode<K, V>(key, value);
        int hashidx = hashCode(key);
        while (map[hashidx] != nullptr && map[hashidx]->key != key && map[hashidx]->key == -1) {
            hashidx++;
            hashidx %= _capacity;
        }
        map[hashidx] = nnode;
        _size++;

        cout << "<" << key << ", " << value << "> inserted!" << endl;
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
        int hashidx = hashCode(key);
        while (map[hashidx] != nullptr) {
            if (map[hashidx]->key == key) {
                map[hashidx] = dummy;
                _size--;
                cout << "key <" << key << "> deleted!" << endl;
            }
            hashidx++;
            hashidx %= _capacity;
        }
        cout << "key <" << key << "> not found!" << endl;
    }

    int isEmpty() {
        return _size == 0;
    }

    int size() {
        return _size;
    }

private:
    HashNode<K, V> **map;
    HashNode<K, V> *dummy;
    int _size;
    int _capacity;
};

#endif
