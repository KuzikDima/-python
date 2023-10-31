# TODO Найдите количество книг, которое можно разместить на дискете
from typing import Tuple

volume_of_disk = 1.44 #мб

weight_of_each_symbol = 4 #кб
number_of_symbols_on_line = 25
number_of_lines_on_page = 50
number_of_pages_in_book = 100

volume_of_disk_1 = volume_of_disk * 1024 * 1024

number_symbols_in_whole_book = number_of_pages_in_book * number_of_lines_on_page * number_of_symbols_on_line

onebook = number_symbols_in_whole_book * weight_of_each_symbol
number_of_books = volume_of_disk_1 // onebook
fin = int(number_of_books)

print("Количество книг, помещающихся на дискету:", fin)
