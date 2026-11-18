def main():
    hours = hours_to_float(input("How many hours have you driven today? "))
    left = hours_left(hours)
    print(f"You can drive {left:.1f} more hours")
    
def hours_to_float(text):
    text = text.replace("hours", "").replace("h", "")
    text = float(text)
    return text

def hours_left(driven):
    driven = 11 - driven    
    return driven

main()               