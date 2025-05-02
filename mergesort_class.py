
class mergesort:

    def merge_sort_method(points_list):

        if len(points_list) == 1:
            return points_list

        # the above if statement is the base case for which the recursion stops splitting the list and stores the most recent value
        # in the "first_half" variable

        first_half = mergesort.merge_sort_method(
            points_list[0:(len(points_list) // 2)])

        second_half = mergesort.merge_sort_method(
            points_list[(len(points_list) // 2):len(points_list)])

        # recursively split the list they form arrays with a singular element in each array

        merged = mergesort.merge_list(first_half, second_half)

        # then merge each array going back in the system stack to merge each one

        return (merged)  # returns the fully merged array

    def merge_list(first_half, second_half):

        for elemnts in first_half:
            if type(elemnts) != int:
                raise Exception("data type error")

        for elemnts in first_half:
            if type(elemnts) != int:
                raise Exception("data type error")

        # invalid data types (anything other than an integer) should not go through the algorithm
        # therefore an exception is raised

        if first_half == [] or second_half == []:
            raise Exception("Empty Array detected cannot perform mergesort")
        # empty arrays should not go through the algorithm therefore an exceptions is raised

        for item in second_half:  # looks at each element in the "first_half" array and inserts it it into the "second_half" array in order
            change = False
            for i in range(0, len(first_half)):  # goes through each index position
                # goes through the list and identifies which position to insert the element
                if first_half[i] >= item and change == False:
                    # inserts the item at the appropriate position
                    first_half.insert(i, item)
                    change = True
        # when one change occurs this variable is set to true so the below condition is not performed and there is nothing overwritten

            if change == False:  # if there is no change in the array the item must be inserted at the end of the list
                i = len(first_half)
                first_half.insert(i, item)  # the item is inserted at the end

        return first_half  # the first half array now becomes the new merged list and is returned
