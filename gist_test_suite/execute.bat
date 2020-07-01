@ECHO OFF
cd C:\gist_test_suite\gist_test_suite
pytest -v -s test_suite.py --html=.\output_files\Report.html --self-contained-html
pause