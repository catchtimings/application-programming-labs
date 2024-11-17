import csv

class ImageIterator:
    def __init__(self, filename: str):
        self.file = filename
        self.images = self._open_csv()
        self.index = 0
        self.limit = len(self.images)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.limit:
            next_image = self.images[self.index]
            self.index += 1
            return next_image
        else:
            raise StopIteration

    def _open_csv(self) -> list:
        """
        Открывает CSV файл и извлекает путь к изображениям из второй колонки.
        """
        with open(self.file, 'r') as my_file:
            reader = csv.reader(my_file)
            next(reader)
            return [item[1] for item in reader]
