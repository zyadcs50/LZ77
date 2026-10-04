# string = input("Please enter a string: ")

# window_size = 7
# buffer_size = 4

# current_index = 0
# string_length = len(string)

# while current_index < string_length:
#     window_start = max(0, current_index - window_size)    
#     window_end = current_index
#     search_window = string[window_start:window_end]
#     buffer_end = min(string_length, current_index + buffer_size)
#     look_ahead = string[current_index:buffer_end]
#     # print("Search Window:", search_window)
#     # print("Look Ahead:", look_ahead)
#     longest_match = 0
#     position = 0
#     # current_index += 1
#     for i in range(len(search_window)):
#         length = 0
#         while (length < len(look_ahead)
#         and i + length < len(search_window)
#         and search_window[i + length] == look_ahead[length]
#         ):
#             length += 1
            
#         if length > longest_match:
#             longest_match = length
#             position = len(search_window) - i
        
#     if current_index + longest_match < string_length:
#                 next_char = string[current_index + longest_match]
#     else:
#          next_char = "Null"
                
#     print("[position:", position, ", Length:", longest_match, ", Next Char:", next_char, "]")
#     if longest_match == 0:
#         current_index += 1
#     else:
#             current_index += longest_match + 1
    
    
#REFACTAR CODE
class LZ77Compressor:
    def __init__(self , window_size=7, buffer_size=4):
        self.window_size = window_size
        self.buffer_size = buffer_size

    def get_search_window(self, data, current_index):
        window_start = max(0 , current_index - self.window_size)
        return data[window_start:current_index]

    def get_look_ahead(self, data, current_index):
        buffer_end = min(len(data), current_index + self.buffer_size)
        return data[current_index:buffer_end]
    

    def find_longest_match(self, search_window, look_ahead):
        longest_match = 0
        distance = 0
        for i in range(len(search_window)):
            length = 0
            while(
                length < len(look_ahead) and 
                i + length < len(search_window) and
                search_window[i+length] == look_ahead[length]
            ):
                length +=1
            if length > longest_match:
                longest_match = length
                distance = len(search_window) - i
        return distance, longest_match
                    

    def compress(self, data):
        tags = []
        current_index = 0
        while current_index < len(data):
            search_window = self.get_search_window(data, current_index)
            look_ahead = self.get_look_ahead(data, current_index)
            distance, length = self.find_longest_match(search_window, look_ahead)
            
            if current_index + length < len(data):
                next_char = data[current_index + length]
            else:
                next_char = "Null"
            
            tags.append((distance, length, next_char))
            if length == 0:
                current_index += 1
            else:
                current_index += length + 1
        return tags  
    
    def decompress(self, tags):
        result = []
        for distance, length, next_char in tags:
            if length > 0:
               start_index = len(result) - distance
               for i in range(length):
                   result.append(result[start_index + i])
        
            if next_char != "Null":
               result.append(next_char)
            
        return "".join(result)

def main():
    # 1. Welcome and introduction message
    print("=" * 55)
    print(" Welcome to the LZ77 Text Compression Tool!")
    print("=" * 55)

    compressor = LZ77Compressor(window_size=7, buffer_size=4)

    # 2. Prompt user for text input
    text = input("\nPlease enter the text you want to compress: ")

    if not text:
        print("No input provided. Exiting program.")
        return

    # 3. Perform compression
    tags = compressor.compress(text)
    
    print("\n--- Compression Completed Successfully! ---")
    print("Generated Tags:")
    for tag in tags:
        print(f"[distance: {tag[0]}, length: {tag[1]}, next_char: '{tag[2]}']")

    # 4. Ask user for decompression
    choice = input("\nWould you like to decompress the text? (y/n): ").strip().lower()

    if choice in ['y', 'yes']:
        decompressed_text = compressor.decompress(tags)
        print("\n--- Decompression Result ---")
        print("Decompressed Text:", decompressed_text)
        print("\nThank you for using the LZ77 Compressor. Goodbye! 👋")
    else:
        # 5. Goodbye message on decline
        print("\nDecompression skipped. Thank you and goodbye! 👋")

if __name__ == "__main__":
    main()   


#for test 

# com = LZ77Compressor( window_size=7, buffer_size=4)
# text = "ABABABABA"
# tags = com.compress(text)

# for tag in tags:
#     print("[position:", tag[0], ", Length:", tag[1], ", Next Char:", tag[2], "]")           
           