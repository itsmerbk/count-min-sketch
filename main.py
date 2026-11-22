import hashlib

class CountMinSketch:
    def __init__(self, w=128, d=4): self.w, self.d, self.tbl = w, d, [[0]*w for _ in range(d)]
    def _idx(self, item, row):
        return int(hashlib.sha256(f"{row}:{item}".encode()).hexdigest(), 16) % self.w
    def add(self, item, n=1):
        for r in range(self.d): self.tbl[r][self._idx(item, r)] += n
    def estimate(self, item):
        return min(self.tbl[r][self._idx(item, r)] for r in range(self.d))

if __name__ == "__main__":
    cms = CountMinSketch(); cms.add("/api/login", 42); cms.add("/api/pay", 7)
    assert cms.estimate("/api/login") >= 42 and cms.estimate("/api/pay") >= 7
    print("[PASS] 023_count_min_sketch")
