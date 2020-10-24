Test.describe("Basic tests")
Test.assert_equals(pass_hash('password'), '5f4dcc3b5aa765d61d8327deb882cf99');
Test.assert_equals(pass_hash('abc123'), 'e99a18c428cb38d5f260853678922e03');

import random
import hashlib
Test.describe("Random Tests")
for _ in range(198):
    _s=''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(5))
    _m=hashlib.md5()
    _m.update(_s.encode('utf-8'))
    Test.assert_equals(pass_hash(_s), _m.hexdigest());
