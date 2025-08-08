import csv
import timeit
from BTrees.OOBTree import OOBTree


def load_items_data(filename):
    """
    Function to load data from a CSV file
    """
    items = []
    with open(filename, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            item = {
                "ID": int(row["ID"]),
                "Name": row["Name"],
                "Category": row["Category"],
                "Price": float(row["Price"]),
            }
            items.append(item)
    return items


def add_item_to_tree(tree, item):
    """
    Function to add an item to an OOBTree
    """
    tree.insert(item["ID"], item)


def add_item_to_dict(items_dict, item):
    """
    Function to add an item to a dict
    """
    items_dict[item["ID"]] = item


def range_query_tree(tree, min_price, max_price):
    """
    Range query function for OOBTree
    """
    result = []
    for key, value in tree.items(min_price, max_price):
        if min_price <= value["Price"] <= max_price:
            result.append(value)
    return result


def range_query_dict(items_dict, min_price, max_price):
    """
    Range query function for dict
    """
    result = []
    for item in items_dict.values():
        if min_price <= item["Price"] <= max_price:
            result.append(item)
    return result


def compare_structures(filename):
    """
    Main function to compare the structures
    """
    items = load_items_data(filename)

    tree = OOBTree()
    items_dict = {}

    for item in items:
        add_item_to_tree(tree, item)
        add_item_to_dict(items_dict, item)

    def time_range_query_tree():
        """
        Function to measure range query time for OOBTree
        """
        return range_query_tree(tree, 10, 100)  

    def time_range_query_dict():
        """
        Function to measure range query time for dict
        """
        return range_query_dict(items_dict, 10, 100)  

    oobtree_time = timeit.timeit(time_range_query_tree, number=100)
    dict_time = timeit.timeit(time_range_query_dict, number=100)

    print(f"Total range_query time for OOBTree: {oobtree_time:.6f} seconds")
    print(f"Total range_query time for Dict: {dict_time:.6f} seconds")
    if oobtree_time < dict_time:
        print("OOBTree is faster than Dict for range queries!")
    else:
        print("Dict is faster than OOBTree for range queries!")


if __name__ == "__main__":
    filename = "csv/generated_items_data.csv"
    compare_structures(filename)
