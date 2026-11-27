class HashMap:
    def __init__(self, size=7):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, key):
        total = 0
        for ch in key:
            total += ord(ch)
        return total % self.size

    def put(self, key, value):
        bucket = self.buckets[self.hash_function(key)]
        for pair in bucket:
            if pair[0] == key:  # key exists
                pair[1] = value
                return 
        bucket.append([key, value])

    def get(self, key):
        bucket = self.buckets[self.hash_function(key)]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None

    def contains(self, key):
        bucket = self.buckets[self.hash_function(key)]
        for pair in bucket:
            if pair[0] == key:
                return True
        return False

    def remove(self, key):
        bucket = self.buckets[self.hash_function(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return True
        return False