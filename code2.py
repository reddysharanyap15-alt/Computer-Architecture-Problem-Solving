#!/usr/bin/env python
# coding: utf-8

# In[1]:


def left_shift(binary, positions):
    print("\nLogical Left Shift")
    print("Original number:", binary)

    result = binary
    for i in range(positions):
        result = result[1:] + '0'
        print(f"After shift {i + 1}: {result}")

    print("Final 8-bit result:", result)
    print("Decimal value:", int(result, 2))


def right_shift(binary, positions):
    print("\nLogical Right Shift")
    print("Original number:", binary)

    result = binary
    for i in range(positions):
        result = '0' + result[:-1]
        print(f"After shift {i + 1}: {result}")

    print("Final 8-bit result:", result)
    print("Decimal value:", int(result, 2))


# Main program
print("8-BIT LOGICAL SHIFT OPERATIONS")

left_shift("10110110", 2)
right_shift("11010100", 2)


# In[ ]:




