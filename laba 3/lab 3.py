import copy

# Базовий клас Prototype
class DocumentTemplate:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def duplicate(self):
        return copy.deepcopy(self)

    def show(self):
        raise NotImplementedError("Subclasses must implement this method")

# Клас для текстового документа
class TextDocument(DocumentTemplate):
    def __init__(self, title, content, font):
        super().__init__(title, content)
        self.font = font

    def show(self):
        print(f"TextDocument:\n Title: {self.title}\n Font: {self.font}\n Content: {self.content}\n")

# Клас для таблиці
class Spreadsheet(DocumentTemplate):
    def __init__(self, title, content, rows, columns):
        super().__init__(title, content)
        self.rows = rows
        self.columns = columns

    def show(self):
        print(f"Spreadsheet:\n Title: {self.title}\n Size: {self.rows}x{self.columns}\n Content: {self.content}\n")

# Демонстрація патерну Prototype
def run_demo():
    print("== Створення шаблонів документів ==")
    text_template = TextDocument("Звіт", "Це шаблон звіту.", "Arial")
    sheet_template = Spreadsheet("Таблиця", "Шаблон фінансових даних", 10, 5)

    text_template.show()
    sheet_template.show()

    print("== Клонування шаблонів ==")
    text_clone = text_template.duplicate()
    sheet_clone = sheet_template.duplicate()

    # Змінюємо копії
    text_clone.title = "Звіт про прибутки"
    text_clone.content = "Детальний звіт за квартал"
    text_clone.font = "Times New Roman"

    sheet_clone.title = "Копія таблиці"
    sheet_clone.rows = 20

    print("Оригінали:")
    text_template.show()
    sheet_template.show()

    print("Копії:")
    text_clone.show()
    sheet_clone.show()

if __name__ == "__main__":
    run_demo()

