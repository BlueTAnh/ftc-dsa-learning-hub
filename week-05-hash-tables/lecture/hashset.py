class HashSet:
    def __init__(self, size=7):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        return total % self.size

    def add(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        if key not in bucket:
            bucket.append(key)

    def search(self, key):
        index = self.hash_function(key)
        return key in self.buckets[index]

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        if key in bucket:
            bucket.remove(key)

s = HashSet()
for animals in ["cat", "dog", "cow", "owl", "act"]:
    s.add(animals)
print(s.buckets)
