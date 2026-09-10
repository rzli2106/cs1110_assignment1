"""
Test script for module a1

When run as a script, this module invokes several procedures that 
test the various functions in the module a1.

Author: Richard Li rl998 Joon LeeJL4875
Date:   Sept 10
"""
import introcs
import a1
def testA():
    """
    Test procedure for Part A
    """
    introcs.assert_equals(a1.before_space('a b'), 'a')
    introcs.assert_equals(a1.before_space(' a'), '')
    introcs.assert_equals(a1.before_space('a b c'), 'a')
    introcs.assert_equals(a1.before_space('  a'), '  a')

    introcs.assert_equals(a1.after_space(' a'), 'a')
    introcs.assert_equals(a1.after_space('a '), '')
    introcs.assert_equals(a1.after_space('  a b  '), 'a b  ')

    introcs.assert_equals(a1.first_inside_quotes('"A"BCD'), 'A')
    introcs.assert_equals(a1.first_inside_quotes('ABCD""'), '')
    introcs.assert_equals(a1.first_inside_quotes('"abc""def"'), 'abc')
    introcs.assert_equals(a1.first_inside_quotes('"asdf"'), 'asdf')

    pass

def testB():
    """
    Test procedure for Part B
    """

    introcs.assert_equals(a1.get_old('{"old" "hi"}'), 'hi')
    introcs.assert_equals(a1.get_old('{"hello" "old" "hi"}'), 'hi')
    introcs.assert_equals(a1.get_old('{"hello" "hello" "old" "hi"}'), 'hi')
    introcs.assert_equals(a1.get_old('{"old" "" "bye"}'), '')

    introcs.assert_equals(a1.get_new('{"new" "hi"}'), 'hi')
    introcs.assert_equals(a1.get_new('{"hello" "new" "hi"}'), 'hi')
    introcs.assert_equals(a1.get_new('{"hello" "hello" "new" "hi"}'), 'hi')
    introcs.assert_equals(a1.get_new('{"new" "" "bye"}'), '')

    introcs.assert_equals(a1.has_error('{"Valid":true}'), False)
    introcs.assert_equals(a1.has_error('{"Valid":false}'), True)
    pass

def testC():
    """
    Test procedure for Part C
    """
    pass

def testD():
    """
    Test procedure for Part D
    """
    pass

testA()
testB()
testC()
testD()
print('Module passed all tests.')