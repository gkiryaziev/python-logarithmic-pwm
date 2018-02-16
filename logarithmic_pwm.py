from math import log10, pow

# pwm range
pwm = 256


def calculate():

    r = (pwm * log10(2)) / (log10(pwm))

    log_pwm = [round(pow(2, (x / r)) - 1) for x in range(1, pwm + 1)]

    with open("logarithmic_pwm.h", "w") as f:
        text_start = "const int logarithmic_pwm[%d] = " % len(log_pwm)
        text = str(str(log_pwm)).replace("[", "{").replace("]", "}")
        text_end = ";"
        f.write(text_start + text + text_end)


if __name__ == "__main__":
    calculate()
    print("done.")