# Using Unicode characters
print("\U0001F604", "😄")  # Grinning Face
print("\U0001F609", "😉")  # Winking Face
print("\U0001F60D", "😍")  # Heart Eyes
print("\U0001F680", "🚀")  # Rocket
print("\U0001F4A1", "💡")  # Light Bulb
print("\U0001F44D", "👍")  # Thumbs Up

try:
    import emoji

    print(emoji.emojize(":grinning_face:"))
    print(emoji.emojize(":winking_face:"))
    print(emoji.emojize(":heart_eyes:"))
    print(emoji.emojize(":rocket:"))
    print(emoji.emojize(":light_bulb:"))
    print(emoji.emojize(":thumbs_up:"))
except ImportError:
    print("Emoji library is not installed. You can install it using: pip install emoji")