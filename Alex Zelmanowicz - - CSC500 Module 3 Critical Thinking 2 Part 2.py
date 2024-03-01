Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> time = int(input("Enter Current time(0-23): "))
Enter Current time(0-23): 13
>>> wait = int(input("Enter hours to wait for the alarm: "))
Enter hours to wait for the alarm: 50
>>> alarm = (time + wait) % 24
>>> print(f"The clock alarm will ring at {alarm}:00.")
The clock alarm will ring at 15:00.
