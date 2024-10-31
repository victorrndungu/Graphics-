from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os

# Create a PDF object
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_left_margin(15)
pdf.set_right_margin(15)
# Initialize PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)

# Title
pdf.cell(0, 10, "Interview Questions Assignment for Ethics and Compliance Assessment", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="C")


# Define the sections and questions with assignments
sections = {
    "Section 1: General Information": [
        (1, "Can you provide a brief overview of your role and responsibilities within the company?", "Abigail Wahu"),
        (2, "How long has the company had a formal ethics/compliance program in place?", "Anita Njeri"),
    ],
    "Section 2: Organizational Structures Promoting Ethical Culture": [
        (3, "Does the company have an official code of ethics or conduct? If so, could you briefly describe its key components?", "Charlene Njambi"),
        (4, "How are ethical values and standards communicated to employees (e.g., training, workshops, handbooks)?", "Consolata Barasa"),
        (5, "What role do leadership and senior management play in promoting ethical culture within the company?", "Gatanna Gachiri"),
        (6, "Is there a specific department or team dedicated to ethics and compliance? If so, what are their responsibilities?", "Lance Munyao"),
        (7, "Does the company have any formal committees (e.g., ethics committees) that oversee ethical issues or policy adherence?", "Lisa Wanjiku"),
        (8, "How does the company ensure that ethical standards are upheld across different departments and regions (if applicable)?", "Abigail Wahu"),
    ],
    "Section 3: Making Ethics Actionable": [
        (9, "How does the company make ethics an actionable part of daily operations and decision-making processes?", "Anita Njeri"),
        (10, "Are there any mechanisms in place for employees to report unethical behaviour (e.g., hotlines, anonymous reporting systems)?", "Charlene Njambi"),
        (11, "How does the company ensure that employees feel safe and supported in reporting unethical behaviour?", "Consolata Barasa"),
        (12, "How are ethical violations investigated, and what disciplinary actions are taken when violations occur?", "Gatanna Gachiri"),
        (13, "Does the company provide ongoing training or resources to ensure that employees understand and adhere to ethical standards?", "Lance Munyao"),
        (14, "Are there any reward or recognition programs that acknowledge employees for ethical behaviour or decision-making?", "Lisa Wanjiku"),
        (15, "How does the company ensure that third-party vendors, contractors, and partners also adhere to ethical standards?", "Abigail Wahu"),
    ],
    "Section 4: Ethical Challenges and Continuous Improvement": [
        (16, "What are some common ethical challenges that the company faces, and how are they addressed?", "Anita Njeri"),
        (17, "How does the company stay updated on new ethics and compliance regulations or emerging trends in business ethics?", "Charlene Njambi"),
        (18, "Are there any recent initiatives or improvements the company has made to strengthen its ethical culture?", "Consolata Barasa"),
        (19, "How does the company measure the effectiveness of its ethics and compliance program?", "Gatanna Gachiri"),
        (20, "Can you share an example of a situation where ethics or integrity played a key role in shaping a business decision?", "Lance Munyao"),
    ],
    "Section 5: Personal Perspective": [
        (21, "In your opinion, what is the most important factor in fostering an ethical culture within an organization?", "Lisa Wanjiku"),
        (22, "How do you personally contribute to maintaining or enhancing the ethical culture in the organization?", "Abigail Wahu"),
    ]
}

pdf.set_font("Times New Roman", "", 12)
for section, questions in sections.items():
    pdf.set_font("Times New Roman", "B", 14)
    pdf.cell(0, 10, section, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Times New Roman", "", 12)
    for q_num, question, person in questions:
        pdf.cell(0, 10, f"{q_num}. {question} ({person})", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

# Define output directory and file name
output_dir = "Test Labs/output_directory"
pdf_output_path = os.path.join(output_dir, "Assignment.pdf")

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Save the PDF
pdf.output(pdf_output_path)