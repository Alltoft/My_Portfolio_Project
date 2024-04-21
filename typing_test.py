import time
import sys
import tty
import termios


def key_check(key, par_letter):
    if key == par_letter:
        return True
    else:
        return False

    

def typing_test():
    # paragraph = input("type your paragraph here:\n")
    paragraph = "something"
    par_length = len(paragraph)
    input("Press Enter when you ready...")
    i = 0
    total_time = 0
    number_of_faults = 0
    while i < par_length:
        i = max(0, i)
        print(i)
        Time = time.time()
        original_settings = termios.tcgetattr(sys.stdin)  # Store original terminal settings
        tty.setcbreak(sys.stdin.fileno())  # Set the terminal to raw mode
        key = sys.stdin.read(1)
        if ord(key) == 127:
            number_of_faults -= 1
            i -= 1
            termios.tcsetattr(sys.stdin, termios.TCSANOW, original_settings)
            continue
        if key_check(key, paragraph[i]) == False:
            number_of_faults += 1

        current_time = time.time()

        time_passed = current_time - Time
        total_time += time_passed
        time_str = str(time_passed)

        # print(f"last press is {time_str[:5]}s far away")
        termios.tcsetattr(sys.stdin, termios.TCSANOW, original_settings)
        number_of_faults = max(0, number_of_faults)
        i += 1
    percentage = number_of_faults / par_length * 100
    letter_per_sec = int(par_length / total_time)
    word_per_min = int(letter_per_sec * 60 / 5)
    accuracy = 100 - percentage
    result = word_per_min * accuracy / 100
    print("Accuracy:", str(accuracy)[:5] + "%", "LPS:", letter_per_sec, "WPM:", word_per_min,
          "Faults:", number_of_faults, "Duration:", str(total_time)[:5] + "s", f"Result: {result}w/m")
