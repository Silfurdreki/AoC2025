infile = "input.txt"

class machine():
    def __init__(self, raw_machine_list) -> None:
        self.no_of_lights = len(raw_machine_list[0][1:-1])
        self.req_lights = self._init_lights(raw_machine_list[0])
        self.lights = int('0' * self.no_of_lights, base=2)

        self.buttons = self._init_buttons(raw_machine_list[1:-1])
        self.required_presses = None

    def _init_lights(self, lights_str):
        req_lights = ''
        for char in lights_str[1:-1]:
            if char == ".":
                req_lights = req_lights + '0'
            else:
                req_lights = req_lights + '1'
        return int(req_lights, base=2)

    def _init_buttons(self, buttons_list):
        buttons = []
        for button in buttons_list:
            cur_button = [0] * self.no_of_lights
            for i in button[1:-1:2]:
                cur_button[int(i)] = 1
            buttons.append(int(''.join(str(x) for x in cur_button), base=2))
        return buttons

    def __repr__(self):
        return repr(self.required_presses)

    def press_all_buttons(self, initial_state):
        final_states = []
        for button in self.buttons:
            final_states.append(initial_state ^ button)
        return final_states

machines = []
with open(infile) as input:
    for line in input:
        machines.append(machine(line.strip().split(" ")))

for machine in machines:
    buttons_pressed = 0
    states = [machine.lights]
    new_states = []
    state_found = False
    while not state_found:
        for state in states:
            new_states.extend(machine.press_all_buttons(state))
        buttons_pressed += 1
        states = list(set(new_states))
        if machine.req_lights in states:
            machine.required_presses = buttons_pressed
            state_found = True

print(sum([x.required_presses for x in machines]))
