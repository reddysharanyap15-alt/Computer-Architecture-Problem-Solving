#!/usr/bin/env python
# coding: utf-8

# In[3]:


def to_8bit_binary(n):
    return format(n & 0xFF, '08b')


def signed_add(a, b):
    # Convert operands to 8-bit 2's complement
    a_bin = to_8bit_binary(a)
    b_bin = to_8bit_binary(b)

    # Perform addition and keep only 8 bits
    unsigned_sum = (a & 0xFF) + (b & 0xFF)
    result = unsigned_sum & 0xFF

    # Convert the 8-bit result back to signed decimal
    signed_result = result if result < 128 else result - 256

    # Signed overflow occurs when operands have the same sign
    # but the result has the opposite sign
    overflow = ((a ^ b) >= 0 and (a ^ signed_result) < 0)

    print(f"\nExpression: ({a}) + ({b})")
    print(f"First operand  : {a_bin} ({a})")
    print(f"Second operand : {b_bin} ({b})")
    print(f"Binary addition: {a_bin} + {b_bin}")
    print(f"8-bit result   : {to_8bit_binary(result)}")
    print(f"Decimal result : {signed_result}")
    print("Overflow       :", "Yes" if overflow else "No")


# Main program
print("SIGNED 8-BIT 2'S COMPLEMENT ADDITION")
signed_add(25, 18)
signed_add(-25, -18)


# In[ ]:




