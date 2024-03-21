import u6

# Define the LabJack device and pins
device = u6.U6()
output_pin = 0  # Digital output pin
input_pin = 1  # Digital input pin


def toggle_output_pin():
    # Toggle the digital output pin
    device.getFeedback(u6.BitStateWrite(output_pin, 1))
    device.getFeedback(u6.BitStateWrite(output_pin, 0))


def read_input_pin_state():
    # Read the state of the digital input pin
    return device.getFeedback(u6.BitStateRead(input_pin))


# Test function to perform the described test
def test_toggle_output_and_read_input():
    toggle_output_pin()
    input_state = read_input_pin_state()
    assert input_state == 1, "Input pin state did not change as expected"


# Run the test
if __name__ == "__main__":
    test_toggle_output_and_read_input()
