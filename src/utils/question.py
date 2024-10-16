import random


class QuestionManager:
    def __init__(self, Question):
        self.original_subjects = {
            'math': Question.math.copy(),
            'computer_science': Question.computer_science.copy(),
            'english': Question.english.copy(),
            'literature': Question.literature.copy(),
            'history_geography': Question.history_geography.copy(),
            'natural_sciences': Question.natural_sciences.copy(),
            'civic_education': Question.civic_education.copy(),
            'technology': Question.technology.copy()
        }
        self.subjects = self.original_subjects.copy()
        self.used_questions = set()
        self.current_mode = 'all'  # Mặc định là random tất cả các môn

    def set_mode(self, mode):
        # Đặt chế độ random: 'all' cho tất cả các môn, hoặc tên của một môn cụ thể
        if mode in self.original_subjects or mode == 'all':
            self.current_mode = mode
            self.reset()  # Reset để áp dụng chế độ mới
        else:
            raise ValueError(f"Chế độ không hợp lệ. Chọn 'all' hoặc một trong {list(self.original_subjects.keys())}")

    def get_random_question(self):
        if self.current_mode == 'all':
            available_subjects = [subject for subject, questions in self.subjects.items() if questions]
        else:
            available_subjects = [self.current_mode] if self.subjects[self.current_mode] else []

        if not available_subjects:
            print("Đã hết câu hỏi! Reset danh sách.")
            self.reset()
            if self.current_mode == 'all':
                available_subjects = [subject for subject, questions in self.subjects.items() if questions]
            else:
                available_subjects = [self.current_mode]

        subject = random.choice(available_subjects)
        question = random.choice(self.subjects[subject])
        self.subjects[subject].remove(question)
        self.used_questions.add(question['image_path'])

        return subject, question

    def reset(self):
        if self.current_mode == 'all':
            self.subjects = {subject: questions.copy() for subject, questions in self.original_subjects.items()}
        else:
            self.subjects = {self.current_mode: self.original_subjects[self.current_mode].copy()}
        self.used_questions.clear()
        print(f"Đã reset câu hỏi cho chế độ: {self.current_mode}")
