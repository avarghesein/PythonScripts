import unittest

from FindWorkShiftByDate import ShiftManager

class ShiftManager_TestClass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.x = ShiftManager()

    def test_randomShifts(self):
        val = self.x.GetShiftByDate("12-12-2019 01:01:00","15-12-2019 22:1:00")
        self.assertDictEqual(val,{'11-12-2019': '3', '12-12-2019': '1,2,3', '13-12-2019': '1,2,3', '14-12-2019': '1,2,3', '15-12-2019': '1,2'})

    def test_dayShifts(self):
        val = self.x.GetShiftByDate("09-02-2019 10:01:00","09-02-2019 14:31:00")
        self.assertDictEqual(val,{'09-02-2019': '1'})

    def test_secondShifts(self):
        val = self.x.GetShiftByDate("09-02-2019 18:35:00","09-02-2019 22:15:00")
        self.assertDictEqual(val,{'09-02-2019': '2'})

    def test_prevDayNightShifts(self):
        val = self.x.GetShiftByDate("09-02-2019 02:00:00","09-02-2019 07:00:00")
        self.assertDictEqual(val,{'08-02-2019': '3'})

    def test_nightShifts(self):
        val = self.x.GetShiftByDate("09-02-2019 22:35:00","09-02-2019 23:00:00")
        self.assertDictEqual(val,{'09-02-2019': '3'})

if __name__ == '__main__':
    unittest.main()
