import time

def main():

    seconds = int(input("Enter the amount of seconds: "))
    readable = time.ctime(seconds)
    print(f"Timestamp: {seconds}")
    print(f"Date and time: {readable}")
    pause = int(input("Enter pause length in seconds: "))
    print("Waiting....")
    pause = time.sleep(pause)
    print("Done...")

if __name__ == "__main__":
    main()