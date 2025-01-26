def function(a, b):
    try:
        return int(a) + int(b)
    except (ValueError, TypeError):
        return "Error: Inputs must be numbers"

result = function(5, "10")
print(result)

result2 = function(5, 10)
print(result2)

result3 = function("hello", 10)
print(result3)