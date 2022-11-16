from collections import OrderedDict

def main():

    # dict definitions
    cities_zip = dict()
    cities_zip_ordered = OrderedDict()

    # code to read file
    with open('cities.csv') as f:
        for line in f:
            cities_list = line.strip("\n").split(",")
            # print(cities_list[0])

            cities_zip[cities_list[0]] = cities_list[1]
            cities_zip_ordered[cities_list[0]] = cities_list[1]
            # Todo 1: Add the cities and their zip codes to both dictionaries

    print('\n\nREGULAR DICTIONARY:\n\n')
    for i in cities_zip:
        print(i)
    print('\n\nORDERED DICTIONARY:\n\n')
    for i in cities_zip_ordered:
        print(i)
    # Todo 2: Add code here to iterate over both dictionaries
    print('\n')
    if cities_zip == cities_zip_ordered:
        print("The regular and ordered dictionaries are in the same order.")
    else:
        print("The regular and ordered dictionaries are NOT in the same order.")

if __name__ == "__main__":
   main()

