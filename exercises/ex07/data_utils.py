"""Dictionary related utility functions."""

__author__ = "730490949"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data files
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # CLose the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(column_based_table: dict[str, list[str]], number_rows: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N (a parameter) rows of data for each column."""
    resulting_dict: dict[str, list[str]] = {}
    for column in column_based_table:
        store_N_values: list[str] = []
        if number_rows > len(column_based_table[column]):
            return column_based_table
        for N in range(0, number_rows):
            item: str = (column_based_table[column])[N]
            store_N_values.append(item)
        resulting_dict[column] = store_N_values
    return resulting_dict


def select(new_column_table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based table with only a specific subset of the original columns."""
    returned_dict: dict[str, list[str]] = {}
    for column in column_names:
        returned_dict[column] = new_column_table[column]
    return returned_dict


def concat(first_column: dict[str, list[str]], second_column: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based table with two column-based tables combined."""
    empty_dict: dict[str, list[str]] = {}
    for column in first_column:
        empty_dict[column] = first_column[column]
    for column in second_column:
        if column in empty_dict:
            empty_dict[column] += second_column[column]
        else:
            empty_dict[column] = second_column[column]
    return empty_dict


def count(frequency_count: list[str]) -> dict[str, int]:
    """Given a list, produce a dictionary where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    empty: dict[str, int] = {}
    for value in frequency_count:
        if value in empty:
            empty[value] += 1
        else:
            empty[value] = 1
    return empty