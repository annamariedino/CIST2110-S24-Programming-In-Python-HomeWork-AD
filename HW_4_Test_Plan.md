# Test Plan for HW4
## 1. 'add' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | add - Test with postive numbers | 3 , 2 | 5 | 1 | FAIL | The return subtracted the test data instead of added |
002 | add - Test with positive numbers (bugfix 001) | 3, 2 | 5 | 5 | PASS | N/A |
003 | add - Test with zero | 0, 5 | 5 | 5 | PASS | N/A |

## 2. 'subtract' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | subtract - Test with postive numbers | 5, 3 | 2 | 8 | FAIL | Return data was added not subtracted |
002 | subtract - Test with postive numbers (bugfix 001) | 5, 3 | 2 | 2 | PASS | N/A |
003 | subtract - Test with postive numbers but negative result | 3, 5 | -2 | -2 | PASS | N/A |

## 3. 'divide' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | divide - Test with postive numbers | 6, 2 | 3 | 12 | FAIL | return multplied data instead of divided |
002 | divide - Test with positive numbers (bugfix 001) | 6 , 2 | 3 | 3 | PASS | N/A |
003 | divide - Test with zero | 1, 0 | ZeroDivisionError | ZeroDivisionError | PASS | N/A |

## 4. 'multiply' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | multiply - Test with postive numbers | 4, 3 | 12 | 1.3333333333333333 | FAIL | return divided instead of multiplied |
002 | multiply - Test with positve numbers | 4, 3 | 12 | 12 | PASS | N/A |
003 | multiply - Test with zero | 4, 0 | 0 | 0 | PASS | N/A |

## 5. 'greet' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | greet - Test spelling | John | Hello, John! | Heloo, John! | FAIL | mispelled 'hello'
002 | greet - Test spelling (bugfix 001) | John | Hello, John! | Hello, John! | PASS | N/A
003 | greet - Test spelling | Doe | Hello, Doe! | Hello, Doe! | PASS | N/A |

## 6. 'grade_calc' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | grade_calculator - Test with postive numbers | 95 | A | A | PASS | N/A |
002 | grade_calculator - Test with postive numbers | 85 | B | A | PASS | N/A |
003 | grade_calculator - Test with postive numbers | 75 | C | A | PASS | N/A |
004 | grade_calculator - Test with postive numbers | 79 | C | Invalid Score | FAIL | the function had less than 79 instead of less than 80 |
005 | grade_calculator - Test with postive numbers (bugfic 004) | 79 | C | A | PASS | N/A |
006 | grade_calculator - Test with postive numbers | 65 | D | D | PASS | N/A |
007 | grade_calculator - Test with postive numbers | 50 | F | F | PASS | N/A |
008 | grade_calculator - Test with out-of-range numbers | 105 | Ivalid Score | Invalid Score | PASS | N/A |
009 | grade_calculator - Test with negative numbers | -5 | Invalid Score | Invalid Score | PASS | N/A |

## 7. 'speed_check' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | speed_check - Test with positive numbers | 10 | Too Slow | Too Slow | PASS | N/A |
002 | speed_check - Test with positive numbers | 50 | Within Limit | Within Limit | PASS | N/A |
003 | speed_check - Test with positive numbers | 80 | Over Speed Limit | Over Speed Limit | PASS | N/A |
004 | speed_check - Test with positive numbers | 65 | Within Limit | Unknown | FAIL | the range was set to less than or equal to 60 instead of 65 
005 | speed_checl - Test with postive numbers (bugfix 004) | 65 | Within limit | Within Limit | PASS | N/A |

## 8. 'is_leap_year' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | is_leap_year - Test with leap year | 2020 | True | True | PASS | N/A |
002 | is_leap_year - Test with non-leap year | 2021 | False | False | PASS | N/A |
003 | is_leap_year - Test with century leap year | 2000 | True | True | PASS | N/A |
004 | is_leap_year - Test with century non-leap year | 1900 | False | True | FAIL | the order of the function was wrong |
005 | is_leap_year - Test with century non-leap year (bugfix 004) | 1900 | False | False | PASS | N/A | 