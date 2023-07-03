# ukupan broj tacnih predikcija/ukupan broj predikcija, ako je uzorak neuravnotezen nije merodavan
def calculate_accuracy(predictions, true_values):
    success = 0
    for i in range(len(predictions)):
        if predictions[i] == true_values[i]:
            success += 1
    return success / len(predictions) * 100


# preciznost predikcije za odredjenu klasu npr od predikcija za klasu 1, 3 su tacne 2 netacne 60%
def calculate_precision(predictions, true_values):
    class_precisions = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(len(predictions)):
        if predictions[i] == true_values[i]:
            class_precisions[predictions[i] - 1][0] += 1
            class_precisions[predictions[i] - 1][1] += 1
        else:
            class_precisions[predictions[i] - 1][1] += 1
    return [(element[0] / element[1]) * 100 if element[1] != 0 else 0 for element in class_precisions]


# koliko dobro prepoznaje pozitivan uzorak npr od pravih klasa 1 koje ima 3, 2 je predvideo da su 1 a jednu nije 66%
def calculate_recall(predictions, true_values):
    class_precisions = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(len(predictions)):
        if predictions[i] == true_values[i]:
            class_precisions[predictions[i] - 1][0] += 1
            class_precisions[predictions[i] - 1][1] += 1
        else:
            class_precisions[true_values[i] - 1][1] += 1
    return [(element[0] / element[1]) * 100 if element[1] != 0 else 0 for element in class_precisions]


if __name__ == '__main__':
    pred = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3]
    true = [1, 1, 2, 1, 2, 2, 2, 3, 3, 1]
    print(calculate_accuracy(pred, true))
    print(calculate_precision(pred, true))
    print(calculate_recall(pred, true))
