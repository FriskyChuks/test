from play_ground import *
# from another_ground import *
from base_folder.sub_folder import another_ground


def product_of_sum(n1,n2,n3):

    sums = sum_numbers(n1,n2)
    result = sums * n3
    return f" {greet('somto')} the result is {result}"

print(product_of_sum(3,4,5))


print(another_ground.find_modulus(5,3))