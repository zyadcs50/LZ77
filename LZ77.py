string = input("Please enter a string: ")

window_size = 7
buffer_size = 4

current_index = 0
string_length = len(string)

while current_index < string_length:
    window_start = max(0, current_index - window_size)    
    window_end = current_index
    search_window = string[window_start:window_end]
    buffer_end = min(string_length, current_index + buffer_size)
    look_ahead = string[current_index:buffer_end]
    # print("Search Window:", search_window)
    # print("Look Ahead:", look_ahead)
    longest_match = 0
    position = 0
    # current_index += 1
    for i in range(len(search_window)):
        length = 0
        while (length < len(look_ahead)
        and i + length < len(search_window)
        and search_window[i + length] == look_ahead[length]
        ):
            length += 1
            
        if length > longest_match:
            longest_match = length
            position = len(search_window) - i
        
    if current_index + longest_match < string_length:
                next_char = string[current_index + longest_match]
    else:
         next_char = "Null"
                
    print("[position:", position, ", Length:", longest_match, ", Next Char:", next_char, "]")
    if longest_match == 0:
        current_index += 1
    else:
            current_index += longest_match + 1
    
           