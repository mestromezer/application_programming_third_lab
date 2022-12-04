import csv


class SimpleIterator:
    def __init__(self, file_name: str, class_name: str, limit: int, counter = 0):
        self.limit = limit
        self.counter = counter
        self.file_name = file_name
        self.class_name = class_name
        self.rows = list()
        with open(file_name, "r",newline='') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[2] == class_name:
                    self.rows.append(row[0])
                    self.limit += 1


    def __iter__(self):
        return self


    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.rows[self.counter]
        else:
            print('None')
            raise StopIteration
        
if __name__=="__main__":
    s_iter1 = SimpleIterator("dataset_csv_first.csv", "3", 10)
    print(next(s_iter1))
    print(next(s_iter1))
    print(next(s_iter1))
    print(next(s_iter1))
    
