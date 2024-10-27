
def count_overlap(path1: str, path2: str) -> int:
    """
    Takes the input of 2 files which contain a number of DNA strings.
    If they both contain the same string, count +1.
    Returns the final amount of same strings.
    """
    DNA_count: int = 0
    content1: list[str] = read(path1)
    content1_map: dict[str, int] = list_to_dict(content1)
    content2: list[str] = read(path2)
    for line in content2:
        if line in content1_map:
            DNA_count += 1
    return DNA_count


def read(path: str):
    with open(path, "r", encoding="utf-8") as reader:
        content: list[str] = reader.readlines()
    return content


def list_to_dict(l: list[str]) -> dict[str, int]:
    ret_dict: dict[str, int] = {}
    for i,v in enumerate(l):
        ret_dict.update({v: i})
    return ret_dict


def main():
    from time import time
    start = time()
    test_count_overlap_sample()
    end = time()
    print(end-start) # Averages around 1.2 seconds.


def test_count_overlap_sample():
    print('Tests count_overlap... ', end='')
    assert 2 == count_overlap('sample1.txt', 'sample2.txt')

    # Tests efficiency (the test will take a long time with the wrong solution):
    assert 100001 == count_overlap('id1.txt', 'id2.txt')
    print('OK')


if __name__ == "__main__":
    main()
