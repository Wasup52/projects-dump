class Question:

    def __init__(self, question, entry_id, possible_answer=[]):
        self.question = question
        self.entry_id = entry_id

        if possible_answer == []:
            self.isMCQ = False
        else:
            self.isMCQ = True
        
        self.possible_answer = possible_answer


    def check_answer(self, answer):
        return self.possible_answer.contains(answer)