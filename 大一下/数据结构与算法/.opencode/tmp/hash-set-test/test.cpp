#include <bits/stdc++.h>
using namespace std;
namespace dsa {

template <typename K>
struct KNode {
    K key;
    KNode* next;
    KNode(const K& k, KNode* n = nullptr) : key(k), next(n) {}
};

template <typename K>
class HashSetChaining {
public:
    HashSetChaining(int init_cap = 16, double lf = 0.75)
        : size_(0), load_factor_(lf) {
        cap_ = 1;
        while (cap_ < init_cap) cap_ <<= 1;
        buckets_.assign(cap_, nullptr);
    }

    ~HashSetChaining() { clear(); }

    void add(const K& key) {
        if (contains(key)) return;
        if (size_ > cap_ * load_factor_) resize(cap_ << 1);
        int idx = hash_(key) & (cap_ - 1);
        buckets_[idx] = new KNode<K>(key, buckets_[idx]);
        ++size_;
    }

    void remove(const K& key) {
        int idx = hash_(key) & (cap_ - 1);
        KNode<K>* cur = buckets_[idx], *prev = nullptr;
        while (cur) {
            if (cur->key == key) {
                if (prev) prev->next = cur->next;
                else      buckets_[idx] = cur->next;
                delete cur; --size_; return;
            }
            prev = cur; cur = cur->next;
        }
    }

    bool contains(const K& key) const {
        int idx = hash_(key) & (cap_ - 1);
        for (KNode<K>* p = buckets_[idx]; p; p = p->next)
            if (p->key == key) return true;
        return false;
    }

    int size() const { return size_; }

private:
    vector<KNode<K>*> buckets_;
    int size_, cap_;
    double load_factor_;
    hash<K> hash_;

    void clear() {
        for (auto p : buckets_) {
            while (p) { auto n = p->next; delete p; p = n; }
        }
        buckets_.clear(); size_ = 0;
    }

    void resize(int new_cap) {
        vector<KNode<K>*> old = move(buckets_);
        cap_ = new_cap;
        buckets_.assign(cap_, nullptr);
        size_ = 0;
        for (auto p : old) {
            while (p) { auto n = p->next; add(p->key); delete p; p = n; }
        }
    }
};

} // namespace dsa

int main() {
    dsa::HashSetChaining<int> s;
    s.add(1); s.add(2); s.add(3); s.add(1);
    cout << s.size() << endl; // expect 3
    cout << s.contains(2) << endl; // expect 1
    s.remove(2);
    cout << s.contains(2) << endl; // expect 0
    return 0;
}
