import csv_validator
import arithmetic
import text_merger
import password_generator


def main():
    # Ex1
    data_rules = {'age': int, 'name': str}
    valid_rows = csv_validator.validate_csv(
        'C:\\Users\\haske\\OneDrive\\Desktop\\Python Facultate\\Python-FII\\Lab7\\ceva.csv', data_rules)

    # Ex2
    result1 = arithmetic.add(10, 5)
    result2 = arithmetic.subtract(10, 5)
    result3 = arithmetic.multiply(10, 5)
    result4 = arithmetic.divide(10, 5)
    result5 = arithmetic.divide(10, 0)

    # Ex3
    file_paths = [
        'C:\\Users\\haske\\OneDrive\\Desktop\\Python Facultate\\Python-FII\\Lab7\\merge3.txt',
        'C:\\Users\\haske\\OneDrive\\Desktop\\Python Facultate\\Python-FII\\Lab7\\merge2.txt',
        'C:\\Users\\haske\\OneDrive\\Desktop\\Python Facultate\\Python-FII\\Lab7\\merge1.txt'
        # ordinea este data de ordinea din lista
    ]
    output_path = 'C:\\Users\\haske\\OneDrive\\Desktop\\Python Facultate\\Python-FII\\Lab7\\outputfile.txt'
    separator = '\n---\n'

    text_merger.merge_files(file_paths, output_path, separator)

    # Ex4
    password = password_generator.generate_password(length=12, use_special_chars=True, use_numbers=True,
                                                    use_mixed_case=True)
    print(password)


if __name__ == '__main__':
    main()
