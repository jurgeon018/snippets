# # https://stackoverflow.com/questions/44054128/using-python-to-open-cmd-and-automatically-enter-a-password

# # https://stackoverflow.com/questions/23739832/hardcode-password-instead-of-being-prompted-for-one
# # https://stackoverflow.com/questions/40850563/how-to-send-the-password-after-user-name-in-command-prompt-using-python

# # https://stackoverflow.com/questions/44054128/using-python-to-open-cmd-and-automatically-enter-a-password

# # https://docs.microsoft.com/en-us/sysinternals/downloads/psexec

# from subprocess import Popen, PIPE, run, call, check_output

# # pwd = 'sG8Yms%#Qh'
# pwd = '69018'
# # command = ['echo', 's']
# command = ['runas', '/noprofile', '/user:jurgeon019', 'cmd']


# # proc = Popen(
# #     command, 
# #     stdin=PIPE, 
# #     # stdout=PIPE, 
# #     # stderr=PIPE,
# #     universal_newlines=True,
# #     shell=True,
# # )
# # proc.stdin.write(pwd)
# # proc.stdin.flush()
# # # out = proc.stdout.read()
# # # print("out: ", out)
# # # proc.stdin.write('whoami')
# # # proc.stdin.flush()
# # # out = proc.stdout.read()
# # # print("out: ", out)
# # stdout, stderr = proc.communicate('whoami')
# # print("stdout: ", stdout)
# # print("stderr: ", stderr)



# # p = Popen(
# #     # 'cmd.exe', 
# #     'runas /noprofile /user:jurgeon019 cmd', 
# #     stdin=PIPE,
# #              stdout=PIPE, stderr=PIPE,
# #              universal_newlines=True,)
# # cmds = [
# #     # 'echo s',
# #     # 'whoami',
# #     # # 'wch'
# #     '69018',
# #     'whoami',
# #     # 'runas /noprofile /user:jurgeon019 cmd',
# #     'whoami',
# # ]
# # for cmd in cmds:
# #     print('cmd:', cmd)
# #     p.stdin.write(cmd + "\n")
# # p.stdin.close()
# # print('before p.stdout.read()')
# # print(p.stdout.read())
# # print('after p.stdout.read()')




# # import subprocess

# # args = ['runas', '/user:jurgeon019', 'cmd.exe']

# # proc = subprocess.Popen(args, 
# #                         stdin=subprocess.PIPE, 
# #                         # stdout=subprocess.PIPE, 
# #                         # stderr=subprocess.PIPE
# #                         )

# # proc.stdin.write(b'69018\n')
# # proc.stdin.flush()

# # stdout, stderr = proc.communicate()
# # print (stdout)
# # print (stderr)

# # import subprocess

# # user = jurgeon019

# # args=["runas", f"/user:{user}", "cmd"]
# # proc = subprocess.Popen(args, 
# #                         stdin=subprocess.PIPE, 
# #                         # stdout=subprocess.PIPE, 
# #                         # stderr=subprocess.PIPE,
# #                         universal_newlines=True,
# #                     )
# # passw='69018'
# # proc.stdin.write(passw)
# # proc.stdin.write('whoami')
# # proc.stdin.flush()

# # stdout, stderr = proc.communicate()
# # print (stdout)
# # print (stderr)










# import win32console, win32con, time
# import subprocess

# username = "jurgeon019"
# password ="69018"

# free_console=True
# try:
#     win32console.AllocConsole()
# except win32console.error as exc:
#     if exc.winerror!=5:
#         raise
#     ## only free console if one was created successfully
#     free_console=False

# stdin=win32console.GetStdHandle(win32console.STD_INPUT_HANDLE)

# p = subprocess.Popen(
#     ["runas", f"/user:{username}","whoami"],
#     # ["runas", f"/user:{username}","cmd.exe"],
#     stdout=subprocess.PIPE,
# )
# while True:
#     print('!')
#     # if p.stdout.read(1)==":":
#     if True:
#         for c in "{}\r".format(password):  # end by CR to send "RETURN"
#             ## write some records to the input queue
#             x=win32console.PyINPUT_RECORDType(win32console.KEY_EVENT)
#             x.Char=str(c)
#             x.KeyDown=True
#             x.RepeatCount=1
#             x.VirtualKeyCode=0x0
#             x.ControlKeyState=win32con.SHIFT_PRESSED
#             stdin.WriteConsoleInput([x])
#         print(p.stdout.read())
#         print(p.stdout.read())
#         p.wait()
#         print(p.stdout.read())
#         print('1')
#         break







import subprocess

command = 'runas /noprofile /user:jurgeon019 cmd'
command = 'sudo echo s'
pst = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE)
pst.stdin.write(b'69018')
pst.communicate(b"69018")


