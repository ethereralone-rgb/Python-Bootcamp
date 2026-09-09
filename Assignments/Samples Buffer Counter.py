def main():
    sample_rate = int(input("Enter Sample Rate (in Hz): "))
    buffer_size = int(input("Enter Buffer Size: "))
    track_length = int(input("Enter track length (in seconds): "))
    buffers = (track_length * sample_rate) // buffer_size
    leftover = (sample_rate * track_length) - buffer_size * buffers
    print(f"Processed {buffers} full buffers with {leftover} leftover samples.")
if __name__ == "__main__":
    main()