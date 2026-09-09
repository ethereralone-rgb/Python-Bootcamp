def main():
    temperature_F = float(input("Enter temperature(F): "))
    temperature_C = (temperature_F - 32) * 5 / 9
    speed_of_sound = 331 + (0.6 * temperature_C)
    print(f"Sound Travels at: {speed_of_sound:.1f} ms")
if __name__ == "__main__":
    main()