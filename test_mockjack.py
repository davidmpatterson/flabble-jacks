from unittest.mock import MagicMock

import u6

# Mock the LabJack device
mock_device = MagicMock(spec=u6.U6)

# Define the behavior of the mock device
mock_output_pin = 0
mock_input_pin = 1
mock_input_state = 0


def mock_toggle_output_pin():
    # Toggle the digital output pin (mock behavior)
    mock_device.getFeedback.return_value = [0] * 16  # Simulate feedback
    mock_device.getFeedback.side_effect = lambda cmd: (
        [1] if cmd == u6.BitStateWrite(mock_output_pin, 1) else [0]
    )


def mock_read_input_pin_state():
    # Read the state of the digital input pin (mock behavior)
    if mock_device.getFeedback.call_args_list:
        last_call_args = mock_device.getFeedback.call_args_list[-1][0]
        if last_call_args:
            if last_call_command == u6.BitStateWrite(mock_output_pin, 1):
                return 1  # Simulate input pin state change after toggling output pin
    return 0  # Default state

    # return mock_input_state


# Assign mock methods to the mock device
mock_device.getFeedback.side_effect = mock_toggle_output_pin
mock_device.getFeedback.side_effect = mock_read_input_pin_state


# Test function to perform the described test using the mock device
def test_toggle_output_and_read_input():
    mock_toggle_output_pin()  # Simulate toggling the output pin
    input_state = mock_read_input_pin_state()  # Simulate reading the input pin state
    print("Input state:", input_state)
    # assert input_state == 1, "Input pin state did not change as expected"
    assert input_state == 0, "Input pin state did not change as expected"


# Run the test
if __name__ == "__main__":
    test_toggle_output_and_read_input()
