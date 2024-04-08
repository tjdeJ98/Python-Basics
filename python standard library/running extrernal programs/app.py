import subprocess

# better approach
completed = subprocess.run(["dir"], capture_output=True)
print("args: ", completed.args)
print("returncode: ", completed.returncode)
print("stderr: ", completed.stderr)
print("stdout: ", completed.stdout)


# Old
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen
