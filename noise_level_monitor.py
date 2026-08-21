print("🔊 NOISE LEVEL MONITOR")

noise = float(input("Enter noise level in dB: "))

if noise < 50:
    print("🟢 Low noise level")
elif noise < 80:
    print("🟡 Moderate noise level")
else:
    print("🔴 High noise level")
