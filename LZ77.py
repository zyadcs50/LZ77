class LZ77Compressor:
    def __init__(self, window_size=7, buffer_size=4):
        self.window_size = window_size
        self.buffer_size = buffer_size

    def get_search_window(self, data, current_index):
        window_start = max(0, current_index - self.window_size)
        return data[window_start:current_index]

    def get_look_ahead(self, data, current_index):
        buffer_end = min(len(data), current_index + self.buffer_size)
        return data[current_index:buffer_end]

    def find_longest_match(self, search_window, look_ahead):
        longest_match = 0
        distance = 0
        for i in range(len(search_window)):
            length = 0
            while (
                length < len(look_ahead) and 
                i + length < len(search_window) and
                search_window[i + length] == look_ahead[length]
            ):
                length += 1
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
    print("=" * 55)
    print(" Welcome to the LZ77 Tool!")
    print("=" * 55)

    compressor = LZ77Compressor(window_size=7, buffer_size=4)

    
    print("\nPlease choose an option:")
    print("1. Compress text")
    print("2. Decompress tags")
    
    choice = input("Enter your choice (1 or 2): ").strip()

   
    if choice == '1':
        text = input("\nPlease enter the text you want to compress: ")

        if not text:
            print("No input provided. Exiting program.")
            return

        tags = compressor.compress(text)
        
        print("\n--- Compression Completed Successfully! ---")
        print("Generated Tags:")
        for tag in tags:
            print(f"[distance: {tag[0]}, length: {tag[1]}, next_char: '{tag[2]}']")

       
        decompress_choice = input("\nWould you like to decompress these tags now? (y/n): ").strip().lower()

        if decompress_choice in ['y', 'yes']:
            decompressed_text = compressor.decompress(tags)
            print("\n--- Decompression Result ---")
            print("Decompressed Text:", decompressed_text)
            print("\nThank you for using the LZ77 Tool.")
        else:
            print("\nDecompression skipped.")

 
    elif choice == '2':
        print("\nPlease enter your tags line by line in the format: distance,length,next_char")
        print("Example: 0,0,A  or  2,2,A  or  2,2,Null")
        print("Type 'done' when you are finished entering tags.\n")

        tags = []
        count = 1
        while True:
            tag_input = input(f"Tag #{count}: ").strip()
            if tag_input.lower() == 'done':
                break
            
            try:
                parts = tag_input.split(',')
                distance = int(parts[0].strip())
                length = int(parts[1].strip())
                next_char = parts[2].strip()
                
                tags.append((distance, length, next_char))
                count += 1
            except Exception:
                print("Invalid format! Please use: distance,length,next_char (e.g: 0,0,A)")

        if not tags:
            print("No tags entered. Exiting program.")
            return

        decompressed_text = compressor.decompress(tags)
        print("\n--- Decompression Result ---")
        print("Decompressed Text:", decompressed_text)
        print("\nThank you for using the LZ77 Tool.")

    else:
        print("Invalid choice! Please run the program again and select 1 or 2.")


if __name__ == "__main__":
    main()

