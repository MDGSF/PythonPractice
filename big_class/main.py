from big_class import BigClass


def main():
    big = BigClass()
    big.update_shared_value("count", 123)
    num = big.get_shared_value("count")
    print(f"num: {num}")

    num = big.feature_a.process_data()
    print(f"num: {num}")
    num = big.feature_a.process_data()
    print(f"num: {num}")
    num = big.feature_a.process_data()
    print(f"num: {num}")

    big.feature_a.show_context()
    big.call_feature_a_show()

    print("-------------------------")
    big.feature_b.show()


if __name__ == "__main__":
    main()
