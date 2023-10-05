# SOURCE https://stackoverflow.com/questions/62760929/how-can-i-run-a-streamlit-app-from-within-a-python-script
import sys
import streamlit.web.cli as cli


if __name__ == "__main__":
    sys.argv = ["streamlit", "run", "app.py"]
    sys.exit(cli.main())
