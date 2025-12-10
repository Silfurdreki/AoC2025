from operator import add

infile = "test.txt"

class machine():
    def __init__(self, raw_machine_list) -> None:
        self.req_joltages = self._init_joltages(raw_machine_list[-1])
        self.no_of_joltages = len(self.req_joltages)
        self.joltages = [0] * len(self.req_joltages)

        self.buttons = self._init_buttons(raw_machine_list[1:-1])
        self.required_presses = None

    def _init_joltages(self, raw_joltages):
        req_joltages = []
        for joltage in raw_joltages[1:-1].split(','):
            req_joltages.append(int(joltage))
        return req_joltages

    def _init_buttons(self, buttons_list):
        buttons = []
        for button in buttons_list:
            cur_button = [0] * self.no_of_joltages
            for i in button[1:-1:2]:
                cur_button[int(i)] = 1
            buttons.append(cur_button)
        return buttons

    def __repr__(self):
        return repr(self.req_joltages)

machines = []
with open(infile) as input:
    for line in input:
        machines.append(machine(line.strip().split(" ")))

machine = machines[0]
max_presses = []
for button in machine.buttons:
    joltage_is = [i for i, x in enumerate(button) if x == 1]
    max_presses.append(min([machine.req_joltages[x] for x in joltage_is]))
breakpoint()
