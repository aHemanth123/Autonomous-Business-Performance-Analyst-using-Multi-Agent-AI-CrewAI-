import pandas as pd
import os
from performance_analyst.crew import BusinessPerformanceCrew
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from datetime import datetime


def run():
    # Load CSV (parse dates properly)
    df = pd.read_csv("data/sales_data.csv", parse_dates=["date"])

    # ✅ Define report date FIRST (execution date)
    report_date = datetime.now().strftime("%B %d, %Y")

    # Prepare global input context
    business_data = f"""
    Columns: {df.columns.tolist()}
    Date Range: {df['date'].min().date()} to {df['date'].max().date()}
    Total Revenue: {df['revenue'].sum()}
    Average Sales: {df['sales'].mean():.2f}

    Revenue by Region:
    {df.groupby('region')['revenue'].sum().to_string()}

    Sample Records:
    {df.head(5).to_string()}
    """

    # Ensure reports folder exists
    os.makedirs("reports", exist_ok=True)

    # Run Crew
    crew = BusinessPerformanceCrew().crew()
    result = crew.kickoff(
        inputs={
            "business_data": business_data,
            "report_date": report_date
        }
    )

    # Convert output → PDF
    pdf_path = "reports/business_report.pdf"

    c = canvas.Canvas(pdf_path, pagesize=LETTER)
    text = c.beginText(40, 750)

    for line in str(result).split("\n"):
        text.textLine(line)

    c.drawText(text)
    c.save()

    print(f"\n✅ Business Performance PDF generated at: {pdf_path}")


# Allow direct execution
if __name__ == "__main__":
    run()



# #!/usr/bin/env python
# import sys
# import warnings

# from datetime import datetime

# from performance_analyst.crew import PerformanceAnalyst

# warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# # This main file is intended to be a way for you to run your
# # crew locally, so refrain from adding unnecessary logic into this file.
# # Replace with inputs you want to test with, it will automatically
# # interpolate any tasks and agents information

# def run():
#     """
#     Run the crew.
#     """
#     inputs = {
#         'topic': 'AI LLMs',
#         'current_year': str(datetime.now().year)
#     }

#     try:
#         PerformanceAnalyst().crew().kickoff(inputs=inputs)
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew: {e}")


# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         PerformanceAnalyst().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")

# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         PerformanceAnalyst().crew().replay(task_id=sys.argv[1])

#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")

# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }

#     try:
#         PerformanceAnalyst().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")

# def run_with_trigger():
#     """
#     Run the crew with trigger payload.
#     """
#     import json

#     if len(sys.argv) < 2:
#         raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

#     try:
#         trigger_payload = json.loads(sys.argv[1])
#     except json.JSONDecodeError:
#         raise Exception("Invalid JSON payload provided as argument")

#     inputs = {
#         "crewai_trigger_payload": trigger_payload,
#         "topic": "",
#         "current_year": ""
#     }

#     try:
#         result = PerformanceAnalyst().crew().kickoff(inputs=inputs)
#         return result
#     except Exception as e:
#         raise Exception(f"An error occurred while running the crew with trigger: {e}")
