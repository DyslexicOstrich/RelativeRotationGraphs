import subprocess

subprocess.run (["python3", "update_database.py"])
subprocess.run (["python3", "process_data.py"])
subprocess.run (["python3", "plot.py"])
subprocess.run (["python3", "create_gif.py"])
