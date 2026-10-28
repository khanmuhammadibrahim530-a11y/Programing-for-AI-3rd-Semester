import os
import json
from fpdf import FPDF, XPos, YPos
from pygments import lex
from pygments.lexers import get_lexer_by_name


class CleanCodePDF(FPDF):
    def header(self):
        self.set_font("Courier", "B", 10)
        self.set_text_color(128, 128, 128)
        self.cell(
            0,
            10,
            "Programming for AI | Combined Assignment Document",
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

    def print_colored_code(self, code_text, lexer_name="python"):
        self.set_font("Courier", "", 10)
        lexer = get_lexer_by_name(lexer_name)
        tokens = lex(code_text, lexer)

        for token_type, value in tokens:
            token_str = str(token_type)
            if "Keyword" in token_str:
                self.set_text_color(0, 0, 255)  # Blue for keywords
                self.set_font("Courier", "B", 10)
            elif "String" in token_str:
                self.set_text_color(163, 21, 21)  # Dark Red for strings
                self.set_font("Courier", "", 10)
            elif "Comment" in token_str:
                self.set_text_color(0, 128, 0)  # Green for comments
                self.set_font("Courier", "I", 10)
            elif "Name.Function" in token_str or "Name.Builtin" in token_str:
                self.set_text_color(128, 0, 128)  # Purple for functions
                self.set_font("Courier", "B", 10)
            elif "Number" in token_str:
                self.set_text_color(9, 134, 115)  # Teal for numbers
                self.set_font("Courier", "", 10)
            else:
                self.set_text_color(0, 0, 0)  # Black
                self.set_font("Courier", "", 10)

            lines = value.split("\n")
            for i, line in enumerate(lines):
                if line:
                    clean_line = line.encode("latin-1", "replace").decode("latin-1")
                    self.write(5, clean_line)
                if i < len(lines) - 1:
                    self.ln(5)


def create_combined_pdf():
    pdf = CleanCodePDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(current_dir)

    notebook_files = [f for f in files if f.endswith(".ipynb")]

    # YAHAN FIX KIYA HAI: merge_all.py aur convertor.py ko list se bahar nikal diya aur csv ko bhi hata diya
    python_files = [
        f
        for f in files
        if f.endswith(".py") and f.lower() not in ["merge_all.py", "convertor.py"]
    ]

    python_files.sort()
    folder_name = os.path.basename(current_dir)

    print(
        f"Found {len(notebook_files)} Notebooks and {len(python_files)} actual Python files to merge (System files skipped)."
    )

    # 1. Jupyter Notebooks
    for nb in notebook_files:
        pdf.add_page()
        pdf.set_font("Courier", "B", 16)
        pdf.set_text_color(0, 51, 102)
        pdf.cell(
            0, 12, f"Notebook: {nb}", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align="L"
        )
        pdf.ln(5)

        try:
            with open(os.path.join(current_dir, nb), "r", encoding="utf-8") as f:
                data = json.load(f)
                for cell in data.get("cells", []):
                    cell_type = cell.get("cell_type", "")
                    source = "".join(cell.get("source", []))

                    if source.strip():
                        pdf.set_font("Courier", "B", 10)
                        pdf.set_text_color(128, 128, 128)
                        pdf.cell(
                            0,
                            6,
                            f"[{cell_type.upper()} CELL]",
                            new_x=XPos.LMARGIN,
                            new_y=YPos.NEXT,
                        )

                        if cell_type == "code":
                            pdf.print_colored_code(source, "python")
                        else:
                            pdf.set_font("Courier", "", 10)
                            pdf.set_text_color(0, 0, 0)
                            pdf.write(
                                5, source.encode("latin-1", "replace").decode("latin-1")
                            )
                        pdf.ln(8)
        except Exception as e:
            print(f"Notebook {nb} error: {e}")

    # 2. Python Files
    for py_file in python_files:
        pdf.add_page()
        pdf.set_font("Courier", "B", 16)
        pdf.set_text_color(0, 102, 51)
        pdf.cell(
            0,
            12,
            f"Python File: {py_file}",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
            align="L",
        )
        pdf.ln(5)

        try:
            with open(os.path.join(current_dir, py_file), "r", encoding="utf-8") as f:
                code_content = f.read()
                pdf.print_colored_code(code_content, "python")
        except Exception as e:
            print(f"File {py_file} error: {e}")

    # Output path automatically updates folder name (e.g., week01, week02)
    output_path = os.path.join(current_dir, f"{folder_name}_Final_Merged_Document.pdf")
    pdf.output(output_path)
    print(
        f"\n🎉 Success! Clean PDF created without system files: {folder_name}_Final_Merged_Document.pdf"
    )


if __name__ == "__main__":
    create_combined_pdf()
