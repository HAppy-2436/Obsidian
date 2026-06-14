#include <bits/stdc++.h>
using namespace std;
namespace dsa {

class BloomFilter {
public:
    explicit BloomFilter(int64_t expected_n,
                         double target_fpp = 0.01,
                         int64_t m_override = -1,
                         int k_override = -1)
        : n_(0) {
        if (m_override > 0 && k_override > 0) {
            m_ = m_override; k_ = k_override;
        } else {
            m_ = (int64_t)ceil(-expected_n * log(target_fpp)
                                / (log(2) * log(2)));
            k_ = max(1, (int)round((double)m_ / expected_n * log(2)));
        }
        int64_t pow2 = 1;
        while (pow2 < m_) pow2 <<= 1;
        m_ = pow2;
        mask_ = m_ - 1;
        bits_.assign(m_, 0);
    }
    void add(const string& s) {
        for (int i = 0; i < k_; ++i) {
            int64_t h = hash_i(s, i);
            bits_[h & mask_] = 1;
        }
        ++n_;
    }
    bool contains(const string& s) const {
        for (int i = 0; i < k_; ++i) {
            int64_t h = hash_i(s, i);
            if (!bits_[h & mask_]) return false;
        }
        return true;
    }
    int64_t size() const { return n_; }
    int64_t bit_capacity() const { return m_; }
    int hash_count() const { return k_; }
    double estimated_fpp() const {
        double exponent = -((double)k_ * n_) / m_;
        double base = 1.0 - exp(exponent);
        return pow(base, k_);
    }
private:
    vector<uint8_t> bits_;
    int64_t m_, n_, mask_;
    int k_;
    static uint64_t hash_i(const string& s, int i) {
        uint64_t h = 0xcbf29ce484222325ULL ^ (uint64_t)i * 0x9e3779b97f4a7c15ULL;
        for (unsigned char c : s) {
            h ^= c;
            h *= 0x100000001b3ULL;
        }
        h ^= (h >> 33);
        h *= 0xff51afd7ed558ccdULL;
        h ^= (h >> 33);
        return h;
    }
};

} // namespace dsa

int main() {
    dsa::BloomFilter bf(10000, 0.01);
    for (int i = 0; i < 10000; ++i)
        bf.add("https://example.com/page?id=" + to_string(i));
    int hits = 0;
    for (int i = 0; i < 10000; ++i)
        if (bf.contains("https://example.com/page?id=" + to_string(i))) ++hits;
    cout << "true_pos_rate=" << (double)hits / 10000 << endl;
    int fps = 0;
    for (int i = 10000; i < 20000; ++i)
        if (bf.contains("https://example.com/page?id=" + to_string(i))) ++fps;
    cout << "false_pos_rate=" << (double)fps / 10000 << endl;
    return 0;
}
