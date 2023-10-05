# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# TODO ADD Task-scheduler-problem path to this project.
# import PycharmProjects.Task-scheduler-problem

import setup
import pandas as pd
import streamlit_dashboard
import streamlit_runner
import subprocess
import os


def main():
    run_streamlit_dashboard()
    data_triage()
    google_drive_import_new()


# TODO fix this somehow pre 1.19
def run_streamlit_dashboard():
    """
    uses subprocess for cross-platform running of dashboard
    :return:
    """
    # FIXME
    import runpy

    file_globals = runpy.run_path("streamlit_runner.py")


def main_menu():
    """
    a mstables inspired txt based menu like page 209 figure 7-6 Murach Python
    :return:
    """
    print("main_menu run but its empty")


# TODO setup Databench Should run each night 11pm.
# TODO add view Todays_Schedule if available otherwise
# TODO run user through do you have a list in CSV I can import otherwise import by hand
# TODO offer to import from googledrive or excel file, import the sample from yourdatatalking/data_pipeline/
def google_drive_import_old():  # TODO old change to MasterGoalsMMDDYY or MasterGoals073123 as it is now updated for date
    """
    pull data from google drive csv for TODO task-scheduler-app
    :return:
    """
    import pandas as pd

    SHEET_ID = "1-QFHeOYXZt6_wL3UElMnUgiGs9ccmKeE3rBGpfA9ru0"
    SHEET_NAME = "AAPL"
    SHEET_ID = "1-QFHeOYXZt6_wL3UElMnUgiGs9ccmKeE3rBGpfA9ru0"
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
    df = pd.read_csv(url)
    print(df.head())


def google_drive_import_new():  # TODO old change to MasterGoalsMMDDYY or MasterGoals073123 as it is now updated for date
    """
    pull data from google drive csv for TODO task-scheduler-app
    :return:
    """
    import pandas as pd

    SHEET_IDS = {
        "Export Summary": "Summary Page",
        "Heat_Filter": "Predator Vision Grid",
        "Master_Proj_List": "Main Blank List",
        "Proj_List": "Detailed Main List",
        "Learning_Checklist": "P_10 Curriculum",
        "Aima_study": "Ch 1 to Ch 29 topics",
    }

    SHEET_ID = "1-QFHeOYXZt6_wL3UElMnUgiGs9ccmKeE3rBGpfA9ru0"
    SHEET_NAME = "AAPL"
    SHEET_ID = "1-QFHeOYXZt6_wL3UElMnUgiGs9ccmKeE3rBGpfA9ru0"
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"
    df = pd.read_csv(url)
    print(df.head())


def data_triage():
    """
    scans TOOL_BOX for TODO adds to Andrew_Tasks.csv in PycharmProjects/Task-scheduler-problem into daily_routine
    :return:
    """
    pass


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # streamlit_runner.run_streamlit_dashboard()
    main()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
