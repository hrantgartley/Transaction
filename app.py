from trans import Item


def main():
    item = Item("item 1", 19.99)
    item_list = [item]

    item.add_item(19.99, item_list)


if __name__ == "__main__":
    main()
