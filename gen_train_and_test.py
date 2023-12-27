import json


def gen_train_and_test():
    dataset = json.load(open('cleaned_dataset.json', 'r', encoding='utf-8'))
    valid_len = len(dataset) - (len(dataset) % 1000)
    print(f'[*] valid len: {valid_len}')
    train_len = int(valid_len * 4 / 5)
    train = dict(list(dataset.items())[:train_len])
    test = dict(list(dataset.items())[train_len:valid_len])
    print(f'[*] train len: {len(train)}')
    print(f'[*] test len: {len(test)}')
    json.dump(train, open('./dataset/train/train.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)
    json.dump(test, open('./dataset/test/test.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


if __name__ == '__main__':
    gen_train_and_test()
