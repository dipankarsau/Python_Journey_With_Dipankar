# # Types of Errors in Python

# Python errors are mainly divided into three types:

# ## 1. Syntax Error

# A Syntax Error occurs when the rules or grammar of Python are not followed.

# Example:

# ```python
# print("Hello"
# ```

# Here, the closing `)` is missing, so Python gives a `SyntaxError`.

# ---

# ## 2. Runtime Error

# A Runtime Error occurs while the program is running. The code syntax is correct, but something goes wrong during execution.

# Example:

# ```python
# x = 10
# y = 0

# print(x / y)
# ```

# Output:

# ```text
# ZeroDivisionError
# ```

# Some common Runtime Errors are:

# * `NameError`
# * `TypeError`
# * `ValueError`
# * `IndexError`
# * `KeyError`
# * `ZeroDivisionError`

# ---

# ## 3. Logical Error

# A Logical Error occurs when the program runs successfully but produces the wrong result.

# Example:

# ```python
# length = 5
# width = 4

# area = length + width

# print(area)
# ```

# Output:

# ```text
# 9
# ```

# But the correct formula for area is:

# ```python
# area = length * width
# ```

# So the program runs without an error, but the logic is wrong.

# ---

# ## Summary

# | Error Type    | Meaning                                   |
# | ------------- | ----------------------------------------- |
# | Syntax Error  | Python syntax/rules are incorrect         |
# | Runtime Error | Error occurs while the program is running |
# | Logical Error | Program runs but gives the wrong result   |

# ### Easy way to remember:

# **Syntax Error → Code is written incorrectly**

# **Runtime Error → Problem occurs during execution**

# **Logical Error → Code runs, but the answer is wrong**
