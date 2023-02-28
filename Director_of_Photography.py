# Created on 28.02.2023. See description in Director_of_Photography.txt(or doc)
from typing import Tuple

class loop_list:
    def __init__(self, gen_value: int, len: int):
        if len <= 0:
            raise ValueError("list_struct must have at least one element") 
        self.len = len
        self.items = [gen_value for _ in range(len)]
    
    def __getitem__(self, index: int) -> int:
        index = index % self.len
        return self.items[index]

    def __setitem__(self, index: int, value: int):
        index = index % self.len
        self.items[index] = value


class cell_set:
    def __init__(self, len: int):
        if len <= 0:
            raise ValueError("cell must have at least one element") 
        self.len = len
        self.items = loop_list(-1, len)
        self.values = loop_list(-1, len)
        self.first_item_idx = 0
        self.last_item_idx = -1
        self.total = 0

    def __getitem__(self, index: int) -> int:
        return self.items[index]

    def __setitem__(self, index: int, value: int):
        self.items[index] = value

    def get_total(self) -> int:
        return self.total

    def add(self, index: int, value: int):
        self.last_item_idx += 1
        self.items[self.last_item_idx] = index
        self.values[self.last_item_idx] = value
        self.total += value

    def update(self, glob_idx: int, X: int) -> Tuple[int, int]:
        if (self.last_item_idx >= self.first_item_idx) and (glob_idx - self.items[self.first_item_idx] >= X):
            self.total -= self.values[self.first_item_idx]
            self.first_item_idx += 1
            return self.items[self.first_item_idx - 1], self.values[self.first_item_idx - 1]
        else:
            return -1, -1
        

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    queues = ["PAB", "BAP"]
    total = 0
    for queue in queues:
        first_frozen_cell_set  = cell_set(Y)
        first_active_cell_set  = cell_set(Y)
        second_frozen_cell_set = cell_set(Y)
        second_active_cell_set = cell_set(Y)

        for i in range(N):
            C_i = C[i]
            if   C_i == queue[0]:
                first_frozen_cell_set.add(i, 1)
            elif C_i == queue[1]:
                second_frozen_cell_set.add(i, first_active_cell_set.get_total())
            elif C_i == queue[2]:
                total += second_active_cell_set.get_total()

            new_item, value = first_frozen_cell_set.update(i + 1, X)
            if new_item >= 0: #TODO: case new_item = 0 repair (default = -1; >= 0)
                first_active_cell_set.add(new_item, value)

            new_item, value = second_frozen_cell_set.update(i + 1, X)
            if new_item >= 0:
                second_active_cell_set.add(new_item, value)

            first_active_cell_set.update(i + 1, Y + 1)
            second_active_cell_set.update(i + 1, Y + 1)
             
    return total

def dummy_count(N: int, C: str, X: int, Y: int) -> int:
    queues = ["PAB", "BAP"]
    total = 0
    for queue in queues:
        for i in range(N):
            for j in range(i + X, min(i + Y + 1, N)):
                for k in range(j + X, min(j + Y + 1, N)):
                    if (C[i] == queue[0]) and \
                        (C[j] == queue[1]) and \
                        (C[k] == queue[2]):
                        total += 1

    return total


def main():
    C = 'PABPABPAPBPPPBBPABPPPBABPBAPPBABAABPABPAB..P.APB.PP'
    N = len(C)
    X = 3
    Y = 10
    print("Dummy", dummy_count(N, C, X, Y))
    print("Good", getArtisticPhotographCount(N, C, X, Y))
    return


if __name__ == "__main__":
    main()