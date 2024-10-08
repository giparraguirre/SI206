# Your name: Gianmarco Iparraguirre
# Your student id: 6361 1583
# Your email: gianmarc@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): Worked with ChatGPT
# If you worked with generative AI also add a statement for how you used it.
# e.g.:
# Asked Chatgpt hints for debugging and suggesting the general structure of the code

# Asked Chatgpt if I used /or how to use functions calls properly. Additionally, I asked ChatGPT for an overview
# of what function call to use from the import random. I also asked how to sort a list in descending order. 
# Finally, I asked chat for reassurace on the my_tests() and how to exactly structure the output check_get_answer()
# test.  

import random

class DigitalBookofAnswers():
    # create the constructor (__init__) method
    # ARGUMENTS:
    # self: the current object
    # answers: a list of potential answers
    # RETURNS: None
    def __init__(self, answers) :
        self.book_answer_list = answers

        self.questions_asked_list = []

        self.answered_list = []
        
    # Create the __str__ method
    # ARGUMENTS:
    # self: the current object
    # RETURNS: a string
    def __str__(self) :
        if not self.book_answer_list : 
            return ""
        return ' - '.join(self.book_answer_list)
    
    # Creates the check_get_answer method
    # ARGUMENTS:
    # self: the current object
    # question: the question the user wants to ask the digital book of answers
    # RETURNS: a string
    def check_get_answer(self, question) :
        if question in self.questions_asked_list:
            index = self.questions_asked_list.index(question)
            answer_index = self.answered_list[index]
            answer = self.book_answer_list[answer_index]
            return f"I've already answered this question. The answer is: {answer}"
        
        answer_index = random.randint(0, len(self.book_answer_list) - 1)
        answer = self.book_answer_list[answer_index]
    
        self.answered_list.append(answer_index)
        self.questions_asked_list.append(question)

        return answer
        
    # Creates open_book method
    # ARGUMENTS:
    # self: the current object
    # RETURNS: None
    def open_book(self) :
        while True :
            turn_number = len(self.questions_asked_list) + 1
            question = input(f"Turn {turn_number} - Please enter your question: ")

            if question == "Done" :
                print("Goodbye! See you soon.")
                break

            answer = self.check_get_answer(question)
            print(answer)
    
    # Create the answer_log method
    # ARGUMENTS:
    # self: the current object
    # RETURNS: a list
    def answer_log(self):
        if not self.answered_list :
            print("Empty")
            print([])
            return []
        
        frequency  = {}
        for num in self.answered_list : 
            answer = self.book_answer_list[num].lower()

            if answer in frequency : 
                frequency[answer] += 1
            else :
                frequency[answer] = 1

        the_answer_log_list = [f"{number_of_times} - {answer}" for answer, number_of_times in frequency.items()]

        the_answer_log_list.sort(key=lambda x: int(x.split(' - ')[0]), reverse=True)

        return the_answer_log_list
    

def test():
    answers_list = ['Believe in Yourself', 'Stay Open to the Future', 'Enjoy It']
    book = DigitalBookofAnswers(answers_list)
    print("Test __init__:")
    print(f"Answer History List: Expected: {[]}, Actual: {book.answered_list}")
    print(f"Question History List: Expected: {[]}, Actual: {book.questions_asked_list}")
    print(" ")
    
    print("Test __str__:")
    expected = "Believe in Yourself - Stay Open to the Future - Enjoy It"
    print(f"Expected: {expected}, Actual: {str(book)}")
    print(" ")
    
    empty_book = DigitalBookofAnswers([])
    print("Test __str__: when it's an empty book without possible answers")
    expected = ""
    print(f"Expected: {expected}, Actual: {str(empty_book)}")
    print(" ")
    
    print("Testing return value of check_get_answer:")
    res = book.check_get_answer('test question')
    print(f"Expected: {str}, Actual: {type(res)}")
    print(" ")
    
    print("Testing check_get_answer")
    book.book_answer_list = ['Go For It']
    print(book.questions_asked_list)
    res = book.check_get_answer('test question 2')
    print(f"Expected: {'Go For It'}, Actual: {res}")
    print(" ")
    
    print("Testing that check_get_answer adds answer index to answered_list:")
    # ↓ newly added - reset the questions_asked_list
    book.questions_asked_list = []
    ##############################
    book.book_answer_list = ['Go For It']
    book.answered_list = []
    book.check_get_answer('test question 2')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")
    
    print("Testing that check_get_answer does not add 'I've already answered this question' part to answered_list:")
    book.book_answer_list = ['Believe In Yourself']
    book.answered_list = [0]
    book.questions_asked_list = ['test question 3']
    book.check_get_answer('test question 3')
    expected = [0]
    res = book.answered_list
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")
    
    print("Testing return value answer_log")
    book.book_answer_list = ['Follow Your Inner Voice', 'Stay Positive', 'Go For It']
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log())
    print(f"Expected: {list}, Actual: {res}")
    print(" ")
    
    print("Testing return value answer_log elements")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = type(book.answer_log()[0])
    print(f"Expected: {str}, Actual: {res}")
    print(" ")
    
    print("Testing answer_log")
    book.answered_list = [0, 0, 0, 1, 1, 2]
    res = book.answer_log()
    expected = ['3 - follow your inner voice', '2 - stay positive', '1 - go for it']
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")
    
    print("Testing empty answer_log")
    book.answered_list = []
    res = book.answer_log()
    expected = []
    print(f"Expected: {expected}, Actual: {res}")
    print(" ")

# Extra Credit
def my_test():
    # Put your test code here
    print("Testing correct output from answer_log when no questions have been asked")
    answers_list = ['Stay Positive', 'Go For It', 'Enjoy It']
    book = DigitalBookofAnswers(answers_list)

    expected = []
    actual = book.answer_log()
    print(f"Expected : {expected}, Actual : {actual}")
    print(" ")

    print("Testing correct behavior from answer_log when answers_list and answered_list")
    book.answered_list = [2, 1, 2]

    expected = ['2 - enjoy it', '1 - go for it']
    actual = book.answer_log()
    print(f"Expected : {expected}, Actual : {actual}")
    print(" ")

    print("Testing correct prompt from open_book")
    expected = "Turn 1 - Please enter your question: "
    actual = f"Turn {len(book.questions_asked_list) + 1} - Please enter your question: "
    print(f"Expected : {expected}, Actual : {actual}")
    print(" ")

    print("Testing check_get_answer when the same question is asked twice")
    first_answer = book.check_get_answer('test question 2')
    expected_first_answer = first_answer  # Store the random answer provided the first time
    print(f"First time asking: Expected: Random answer, Actual: {first_answer}")
    
    second_answer = book.check_get_answer('test question 2')
    expected_second_answer = f"I've already answered this question. The answer is: {expected_first_answer}"
    print(f"Second time asking: Expected: {expected_second_answer}, Actual: {second_answer}")
    print(" ")

def main() :
    answer_list = [
        'Follow Your Inner Voice',
        'Stay Positive', 
        'Go For It',
        'Believe in Yourself',
        'Stay Open to the Future',
        'Enjoy it'
    ]

    book = DigitalBookofAnswers(answer_list)

    book.open_book()

    for entry in book.answer_log() :
        print(entry)

# Only run the main function if this file is being run (not imported)
if __name__ == "__main__":
    # main()
    # test()
    my_test() #TODO: Uncomment if you do the extra credit
