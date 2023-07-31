import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        a = BookLover('danielle', 'ujj2wd@virginia.edu', 'fiction')
        a.add_book('shoe dog',4)
        self.assertTrue(a.has_read('shoe dog'))
        
    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        expected = 1
        b = BookLover('danielle', 'ujj2wd@virginia.edu', 'fiction')
        b.add_book('shoe dog',4)
        b.add_book('shoe dog',5)
        self.assertTrue(expected == len(b.book_list))
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        c = BookLover('danielle', 'ujj2wd@virginia.edu', 'fiction')
        c.add_book('shoe dog',4)
        self.assertTrue(c.has_read('shoe dog'))
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        d = BookLover('danielle', 'ujj2wd@virginia.edu', 'fiction')
        d.add_book('shoe dog',4)
        self.assertFalse(d.has_read('snow white'))
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        expected = 3
        e = BookLover('danielle', 'ujj2wd@virginia.edu', 'fiction')
        e.add_book('shoe dog',4)
        e.add_book('bugs life',3)
        e.add_book('cat in the hat', 4)
        self.assertTrue(expected == e.num_books_read())
    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        expected_favs = 2
        f = BookLover('danielle', 'ujj2wd@virginia.edu', 'fiction')
        f.add_book('shoe dog',4)
        f.add_book('bugs life',3)
        f.add_book('cat in the hat', 4)
        self.assertTrue(expected_favs == len(f.fav_books()))
        
if __name__ == '__main__':

    unittest.main(verbosity=3)