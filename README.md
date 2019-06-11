# Python Conversor

Given an input (.wav, .morse or .txt), convert it to the other two extensions.

app.py is the code that needs to be executed, with a audio (.wav), binary (.morse) or text (.txt) file as argument, in order to complete the conversion.

based on the argument file, the app.py calls functions in the intermediary.py file, that makes the conversions and return the converted data back to app.py, who then send the data to filemanager.py, which writes this data on files in the same directory that the user executed the program.

unit tests are written in the sample_test.py file, and can be executed with Pytest. some default test files are inside the "test" directory, and are the ones used in the unit tests.