class QuizBrain:

    def __init__(self, q_list):
        self.qsn_num=0
        self.qsn_list=q_list
        self.score=0

    def check_ans(self, user_ans, correct_ans):
        if (user_ans.lower()==correct_ans.lower()):
            print("you got it right.")
            self.score+=1
        else:
            print("That's wrong")
        print(f"The correct ans was {correct_ans}")


    def next_qsn(self):
        current_qsn=self.qsn_list[self.qsn_num]
        self.qsn_num +=1
        user_ans=input(f"Q.{self.qsn_num} {current_qsn.text}(True/false): ")
        self.check_ans(user_ans,current_qsn.answer)
        print(f"Your currrent score is {self.score}/{self.qsn_num}\n")

    def still_has_qsn(self):
        return self.qsn_num<len(self.qsn_list)



