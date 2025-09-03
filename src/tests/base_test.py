import unittest
from io import StringIO
from contextlib import redirect_stdout

    
class Tests(unittest.TestCase):

    def capture_output(self, func, *args, **kwargs):
        buffer = StringIO()
        with redirect_stdout(buffer):
            func(*args, **kwargs)
        return buffer.getvalue()
  
  
    def run_cases(self, func, cases, capture_print=False,num_inputs=None, num_outputs=1, ):
        if num_inputs is None:
            num_inputs = len(cases[0]) - num_outputs

        passed = 0
        failed = 0

        for i, case in enumerate(cases):
            if not isinstance(case, (tuple, list)):
                case = (case,)

            inputs = case[:num_inputs]
            expected = case[num_inputs:num_inputs + num_outputs]

            if capture_print:
                output = self.capture_output(func, *inputs)
            else:
                output = func(*inputs)

            if num_outputs == 1:
                output_to_check = output
                expected_to_check = expected[0]
            else:
                output_to_check = output
                expected_to_check = tuple(expected)
            try:
                self.assertEqual(output_to_check, expected_to_check,
                             msg=f"Failed case {i}: inputs={inputs}, expected={expected_to_check}, got={output_to_check}")
            except AssertionError as e:
                print(e)
                failed += 1
            else:
                passed += 1
        total = len(cases)
        print(f"Testing {func.__name__}:")
        print(f"Ran {total} cases: {passed} passed, {failed} failed.")
        self.assertEqual(failed, 0, msg=f"{failed} test(s) failed")


    def assert_raises(self, func, expected_exception, cases, expected_message=None):
        for i, case in enumerate(cases):
            if not isinstance(case, (tuple, list)):
                case = (case,)

            with self.assertRaises(expected_exception) as context:
                func(*case)

            if expected_message is not None:
                self.assertEqual(
                    str(context.exception),
                    expected_message,
                    msg=f"Case {i} failed: expected message '{expected_message}', got '{context.exception}'"
                )



    # This is a template for how to write a test function
    # def __test_name__(self):
    #     run_cases = [
            # input1, input2,output1,output2
    #     ]

    #     self.run_cases(__func_name__,run_cases, False,2,2)   



if __name__ == "__main__":
    unittest.main()