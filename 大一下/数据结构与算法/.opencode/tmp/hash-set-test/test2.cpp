#include <bits/stdc++.h>
using namespace std;
namespace dsa {

class BitMap {
public:
    explicit BitMap(int n) : n_(n) {
        bytes_.assign((n + 7) / 8, 0);
    }
    void add(int x) {
        assert(x >= 0 && x < n_);
        bytes_[x / 8] |= (1u << (x % 8));
    }
    void remove(int x) {
        assert(x >= 0 && x < n_);
        bytes_[x / 8] &= ~(1u << (x % 8));
    }
    bool contains(int x) const {
        assert(x >= 0 && x < n_);
        return (bytes_[x / 8] >> (x % 8)) & 1u;
    }
    int size() const { return n_; }
    string to_string() const {
        string s;
        s.reserve(n_);
        for (int i = 0; i < n_; ++i)
            s.push_back(contains(i) ? '1' : '0');
        return s;
    }
private:
    int n_;
    vector<uint8_t> bytes_;
};

} // namespace dsa

int main() {
    dsa::BitMap bm(16);
    bm.add(3); bm.add(7); bm.add(15);
    cout << bm.to_string() << endl;        // expect 0001000100000001
    cout << bm.contains(7) << endl;        // expect 1
    bm.remove(7);
    cout << bm.to_string() << endl;        // expect 0001000000000001
    return 0;
}
