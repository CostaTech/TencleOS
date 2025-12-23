# TencleOS Calculator - TLang Version
# Simple console calculator - matches calculator.py functionality

use os
use sys

int << func >> ("================================")
int << func >> ("     TENCLEOS CALCULATOR      ")
int << func >> ("================================")
int << func >> ("")
int << func >> ("Enter first number:")
var a = input()
int << func >> ("Enter second number:")
var b = input()
int << func >> ("")
int << func >> ("Results:")
int << func >> ("--------")
sum_result = a + b
int << func >> ("Addition: ")
int << func >> (sum_result)
sub_result = a - b
int << func >> ("Subtraction: ")
int << func >> (sub_result)
mul_result = a * b
int << func >> ("Multiplication: ")
int << func >> (mul_result)
<< ! >func> if b == 0 {
    int << func >> ("Division: ERROR (divide by zero)")
} >> func << else {
    div_result = a / b
    int << func >> ("Division: ")
    int << func >> (div_result)
}
int << func >> ("")
int << func >> ("Press Enter to close...")
var wait = input()




