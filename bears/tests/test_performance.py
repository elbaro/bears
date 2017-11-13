import unittest
import bears
import numpy as np
import time


class TestPerformance(unittest.TestCase):
    def test_performance(self):
        n = 10000
        rep = 100
        a = np.arange(n)
        b = np.arange(n - 1, -1, -1)
        df = bears.DataFrame({'num1': a, 'num2': b})

        t = time.time()
        for _ in range(rep):
            for i in range(n):
                _ = {'num1': a[i], 'num2': b[i]}
        dt_manual = time.time() - t

        t = time.time()
        for _ in range(rep):
            for i in range(n):
                _ = df[i]
                # _ = df.rows_value(i)
        dt_df = time.time() - t

        print('manual:', dt_manual)
        print(' bears:', dt_df)

        # manual: 2.0039987564086914
        # bears: 7.6304779052734375
        self.assertLess(dt_df / 4, dt_manual, msg="more than 3 times slower than manual iteration")


if __name__ == '__main__':
    unittest.main()
