import os
import json
from fpdf import FPDF, XPos, YPos


class CodeToPDF(FPDF):
    def header(self):
        self.set_font("Courier", "B", 10)
        self.set_text_color(128, 128, 128)
        self.cell(
            0,
            10,
            "Programming for AI | Week 01 Combined Document",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
            align="R",
        )
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Courier", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(
            0,
            10,
            f"Page {self.page_no()}",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
            align="C",
        )


def create_combined_pdf():
    pdf = CodeToPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Current folder jahan script pari hui hai
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Saari files ki list banana
    files = os.listdir(current_dir)
    notebook_files = [f for f in files if f.endswith(".ipynb")]
    python_files = [
        f
        for f in files
        if f.endswith(".py") and f != "merge_all.py" and f != "convertor.py"
    ]

    # Pehle files ko sort kar letay hain sequence wise
    python_files.sort()

    print(
        f"Found {len(notebook_files)} Jupyter Notebook and {len(python_files)} Python files to merge."
    )

    if not notebook_files and not python_files:
        print(
            "Koi .ipynb ya .py files nahi mili! Kindly check karein ke files isi folder mein hain."
        )
        return

    # 1. Processing Jupyter Notebook First
    for nb in notebook_files:
        pdf.add_page()
        pdf.set_font("Courier", "B", 16)
        pdf.set_text_color(0, 51, 102)  # Dark Blue Title
        pdf.cell(
            0, 12, f"Notebook: {nb}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L"
        )
        pdf.ln(5)

        pdf.set_font("Courier", "", 10)
        pdf.set_text_color(0, 0, 0)

        try:
            with open(os.path.join(current_dir, nb), "r", encoding="utf-8") as f:
                data = json.load(f)
                for cell in data.get("cells", []):
                    cell_type = cell.get("cell_type", "")
                    source = "".join(cell.get("source", []))

                    if source.strip():
                        pdf.set_font("Courier", "B", 10)
                        pdf.set_text_color(100, 100, 100)
                        pdf.cell(
                            0,
                            6,
                            f"[{cell_type.upper()} CELL]",
                            new_x=XPos.LMARGIN,
                            new_y=YPos.NEXT,
                        )

                        pdf.set_font("Courier", "", 10)
                        pdf.set_text_color(0, 0, 0)
                        for line in source.split("\n"):
                            clean_line = line.encode("latin-1", "replace").decode(
                                "latin-1"
                            )
                            pdf.cell(
                                0, 5, clean_line, new_x=XPos.LMARGIN, new_y=YPos.NEXT
                            )
                        pdf.ln(4)
        except Exception as e:
            print(f"Notebook {nb} read karne mein masla aaya: {e}")

    # 2. Processing 10 Python Files
    for py_file in python_files:
        pdf.add_page()
        pdf.set_font("Courier", "B", 16)
        pdf.set_text_color(0, 102, 51)  # Dark Green Title
        pdf.cell(
            0,
            12,
            f"Python File: {py_file}",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
            align="L",
        )
        pdf.ln(5)

        pdf.set_font("Courier", "", 10)
        pdf.set_text_color(0, 0, 0)

        try:
            with open(os.path.join(current_dir, py_file), "r", encoding="utf-8") as f:
                for line in f:
                    clean_line = (
                        line.rstrip("\n").encode("latin-1", "replace").decode("latin-1")
                    )
                    pdf.cell(0, 5, clean_line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        except Exception as e:
            print(f"File {py_file} read karne mein masla aaya: {e}")

    # Final PDF Save karna
    output_path = os.path.join(current_dir, "Week01_Final_Merged_Document.pdf")
    pdf.output(output_path)
    print(f"\n🎉 Success! Combined PDF created: Week01_Final_Merged_Document.pdf")


if __name__ == "__main__":
    create_combined_pdf()
