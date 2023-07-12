class FlatIterator:

    def __init__(self, list_of_list):
        self.flat_list = list_of_list
        self.flat_list_len = len(self.flat_list)

    def __iter__(self):
        self.flat_item_nom = -1
        self.tmp_list = []
        return self
    
    def __next__(self):
        while True:
            if len(self.tmp_list):
                return self.tmp_list.pop(-1)
            else:
                self.flat_item_nom += 1
                if self.flat_item_nom >= self.flat_list_len:
                    raise StopIteration
                item = self.flat_list[self.flat_item_nom]
                if isinstance(item, list):
                    if not len(item):
                        continue
                    self.tmp_list = list(FlatIterator(item))
                    self.tmp_list = self.tmp_list[::-1]
                    return self.tmp_list.pop(-1)
                return item
            

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()