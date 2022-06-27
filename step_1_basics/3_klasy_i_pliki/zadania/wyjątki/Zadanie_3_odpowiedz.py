"""
Opis:
Kod oblicza i wypisuje BMI z podanej wagi i wzrostu.

Popraw błędy (zdebuguj kod)
"""
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]


def calculate_bmi(height, weight):
    """
    Calculates BMI based on height and weight

    (int, float) -> (float)
    :param height:
    :param weight:
    :return: bmi
    """
    return weight / (height ** 2)


# wersja karty
for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(height, weight)
    print(patient)
    print(*patient)
    print(bmi)
    print("Patient's BMI is: {:.2f}".format(bmi))

# wersja 2
for patient in patients:
    bmi = calculate_bmi(*reversed(patient))
    print("Patient's BMI is: {:.2f}".format(bmi))
