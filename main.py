import random

from reportlab.lib.colors import blue
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas
from operations.operations import (
    add_problem,
    subtract_problem,
    multiply_problem,
    divide_problem,
)

if __name__ == "__main__":

    problem1 = add_problem()
    problem2 = subtract_problem()
    problem3 = multiply_problem()
    problem4 = divide_problem()

    problem_list = [problem1, problem2, problem3, problem4]

    canvas = Canvas("test.pdf", pagesize=LETTER)

    # Set font to Times New Roman with 12-point size
    canvas.setFont("Times-Roman", 12)

    # Draw blue text one inch from the left and ten
    # inches from the bottom
    canvas.drawString(1 * inch, 10 * inch, random.choice(problem_list).create_problem())
    canvas.drawString(1 * inch, 9 * inch, random.choice(problem_list).create_problem())
    canvas.drawString(1 * inch, 8 * inch, random.choice(problem_list).create_problem())
    canvas.drawString(1 * inch, 7 * inch, random.choice(problem_list).create_problem())
    canvas.drawString(1 * inch, 6 * inch, random.choice(problem_list).create_problem())
    canvas.drawString(1 * inch, 5 * inch, random.choice(problem_list).create_problem())
    canvas.drawString(1 * inch, 4 * inch, random.choice(problem_list).create_problem())
    canvas.drawString(1 * inch, 3 * inch, random.choice(problem_list).create_problem())
    canvas.drawString(1 * inch, 2 * inch, random.choice(problem_list).create_problem())
    canvas.drawString(1 * inch, 1 * inch, random.choice(problem_list).create_problem())

    # Save the PDF file
    canvas.save()
