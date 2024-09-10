class fsa:
    def __init__(self):
        self.states=["q0","q1","q2"]
        self.current_state="q0"
    def reset(self):
        self.current_state="q0"
    def transition(self,char):
        if self.current_state=="q0":
            if char=='a':
                self.current_state="q1"
            else:
                self.current_state="q0"
        elif self.current_state=="q1":
            if char=="b":
                self.current_state="q2"
            elif char=='a':
                self.current_state="q1"
            else:
                self.current_state="q0"
        elif self.current_state=="q2":
            if char=='a':
                self.current_state="q1"
            else:
                self.current_state="q0"
    def is_accepting(self):
        return self.current_state=="q2"
    def run(self,input_string):
        self.reset()
        for char in input_string:
            self.transition(char)
        return self.is_accepting()
test_strings=["a","b","ab","aab","baba","aabb","xyzab"]
for s in test_strings:
    if fsa.run(s):
        print(f"the string'{s}' is accepted")
    else:
        print(f"the string'{s}' is rejeced")
