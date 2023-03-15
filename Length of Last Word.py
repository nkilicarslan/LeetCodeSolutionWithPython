class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # create a list to store the splitted by space char
        splitted_list_by_space_char = s.split(' ')
        # iterate over the list from the end to the beginning
        for i in range(len(splitted_list_by_space_char)-1,0,-1):
            # if the current element is '', continue
            if splitted_list_by_space_char[i] == '':
                continue
            # if the current element is not '', return the length of the current element
            else:
                return len(splitted_list_by_space_char[i])
        # if the list does not contain any space char, return the length of the first element
        return len(splitted_list_by_space_char[0])
