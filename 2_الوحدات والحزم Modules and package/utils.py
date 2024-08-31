def greet(name): 
    print('Hello', name)


class Car: 
    def __init__(self, model, date) -> None:
        self.model = model
        self.date =date


names = ["Ahmed", "Mohamed", "Jawad", "Osama"]

if __name__ == '__main__':
    for name in names: 
        greet(name)