import pytest
import tempfile
from src.utils import read_speeds_from_file, populate_table
from unittest.mock import MagicMock
from unittest.mock import MagicMock, call

def test_read_speeds_from_file_basic():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as tmp_file:
        tmp_file.write("0,00\n10,5\n20,5\n30,5\n")

    result = read_speeds_from_file(tmp_file.name)
    tmp_file.close()
    assert result == [10.5, 20.5, 30.5]

def test_read_speeds_from_file_with_invalid_data():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as tmp_file:
        tmp_file.write("0,00\n10,5\ninvalid\n20,5\n30,5\n")

    result = read_speeds_from_file(tmp_file.name)
    tmp_file.close()
    assert result == [10.5, 20.5, 30.5]

def test_read_speeds_from_file_no_start_marker():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as tmp_file:
        tmp_file.write("10,5\n20,5\n30,5\n")

    result = read_speeds_from_file(tmp_file.name)
    tmp_file.close()
    assert result == []

def test_read_speeds_from_file_empty_file():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as tmp_file:
        pass

    result = read_speeds_from_file(tmp_file.name)
    tmp_file.close()
    assert result == []

def test_read_speeds_from_file_handle_commas():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as tmp_file:
        tmp_file.write("0,00\n1.000,50\n")

    result = read_speeds_from_file(tmp_file.name)
    tmp_file.close()
    assert result == [1000.50]

def test_populate_table():
    table = MagicMock()
    speeds = [10.5, 20.5, 30.5]
    distance_per_revolution = 2.0

    populate_table(table, speeds, distance_per_revolution)

    # 0 delete chiamate alla prima iterazione di polulate table
    assert table.delete.call_count == 0
    
    assert table.insert.call_count == len(speeds)

    expected_calls = [
        call('', 'end', values=('2.00', '10.50')),
        call('', 'end', values=('4.00', '20.50')),
        call('', 'end', values=('6.00', '30.50'))
    ]

    assert table.insert.call_args_list == expected_calls



def test_populate_table_empty():
    table = MagicMock()
    speeds = []
    distance_per_revolution = 2.0

    populate_table(table, speeds, distance_per_revolution)

    assert table.delete.call_count == 0
    assert table.insert.call_count == 0
