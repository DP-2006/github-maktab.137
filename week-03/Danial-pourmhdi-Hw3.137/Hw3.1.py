import copy
import itertools


def main():
    usser_inout = input("please enter the sentenses or word ")
    word = list(set(usser_inout))
    combinations_1 = list(itertools.combinations(word, 2))
    combinations_2 = list(itertools.combinations(word, 3))
    combinations_3 = list(itertools.combinations(word, 4))
    all_combinations = combinations_1 + combinations_2 + combinations_3
    shallow_copy = all_combinations.copy()

    deep_copy = copy.deepcopy(all_combinations)
    print(f'all_combinations: {all_combinations[0]}')
    print(f'shallow_copy: {shallow_copy[0]}')
    print(f'deep_copy: {deep_copy[0]}')

    if len(all_combinations[0]) > 0 and len(all_combinations[0]) :
        # for change the list to tuple
        temo_list = list(all_combinations[0])
        temo_list[0] = "MAKTAB.137"
        all_combinations[0] = tuple(temo_list)

        print(f"all_combinations: {all_combinations[0]}")
        print(f"shallow_copy: {shallow_copy[0]}")
        print(f"deep_copy: {deep_copy[0]}")
        print(f"temo_list: {temo_list[0]}")

def check_diffrance(orginal, shallow, deep):
    for i, (orig, shal, dep) in enumerate(zip(orginal, shallow, deep)):
        if orig != shal:
            print(f" : {orig} : {shal} ")
            if orig != dep:
                print(f" {orig}  {dep}")
        check_diffrance(orig, shal, dep)
        break
main()






