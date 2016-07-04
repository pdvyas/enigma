import string

alphabets = string.ascii_uppercase

from perm_data import data as perm_data

char_index = {a:b for b, a in enumerate(alphabets)}
index_char = dict(enumerate(alphabets))

class Rotor(object):

    def __init__(self, name, setting=None):
        self.name = name
        if setting:
            self.set(setting)
        else:
            self.setting = None
        self.perms = perm_data[name]

    def forward_convert(self, char):
        return self.convert("forward", char)

    def backward_convert(self, char):
        return self.convert("backward", char)

    def convert(self, direction, char):
        enter = (char_index[char] + self.setting) % len(alphabets)
        c = self.perms[direction][enter]
        exit = (char_index[c] - self.setting) % len(alphabets)
        return index_char[exit]

    def set(self, setting):
        if not setting in alphabets:
            raise ValueError("Not valid setting")
        self.setting = char_index[setting]

    def step(self):
        ret = self.at_notch()
        self.setting = (self.setting + 1) % len(alphabets)
        return ret

    def at_notch(self):
        if index_char.get(self.setting) in self.perms["notch"]:
            return True
        return False

class Reflector(Rotor):

    def convert(self, direction, char):
        return self.perms[direction][char_index[char]]

class Machine(object):

    def __init__(self, reflector, fixed, rotors, setting):
        self.reflector = Reflector(reflector)
        self.fixed = Rotor(fixed, setting[0])
        self.rotors = [Rotor(name, setting) for name, setting in zip(rotors, setting[1:])]

    def convert(self, msg):
        ret = []
        for char in msg:
            ret.append(self.convert_char(char))
        return "".join(ret)

    def convert_char(self, char):
        self.step_rotors()
        c = char
        for rotor in list(reversed(self.rotors)) + [self.fixed, self.reflector]:
            c = rotor.forward_convert(c)

        c = self.fixed.backward_convert(c)
        for rotor in self.rotors:
            c = rotor.backward_convert(c)
        return c

    def step_rotors(self):
        if self.rotors[1].at_notch():
            self.rotors[1].step()
            self.rotors[0].step()
        if self.rotors[2].step():
            self.rotors[1].step()
