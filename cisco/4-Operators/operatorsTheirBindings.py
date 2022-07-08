#Operators and their bindings
print(9 % 6 % 2) # from left to right: first 9 % 6 gives 3, and then 3 % 2 gives 1.
print(2 ** 2 ** 3) # the exponentiation operator uses right-sided binding.
print(2 * 3 % 5)

# List of priorities
# -------------------------------------------------------------------------
# Priority     | Operator                                                 -
#--------------------------------------------------------------------------
#   1          | **                                                       -
#--------------------------------------------------------------------------
#   2          | +, - (note: unary operators located next to the right of -
#              |the power operator bind more strongly) [UNARY]            -
#--------------------------------------------------------------------------
#   3          | *, /, //, %                                              -
#              |                                                          -
#--------------------------------------------------------------------------
#   4          | +, -     [BINARY]                                        -
#              |                                                          -
#--------------------------------------------------------------------------
#