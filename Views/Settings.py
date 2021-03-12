from colorama import Fore, Back, Style

userName = 'RCA'
existingPassword = '***********'
newPassword = '***********'
confirmPassword = '***********'


class Colors:
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'


print(f'\n                       {Fore.CYAN}AUTO BELL >> User Settings{Style.RESET_ALL} \n')
print(
    f'              User name           {Colors.bg.lightgrey}{Fore.BLACK}      {userName}           {Style.RESET_ALL}\n')
print(
    f'              Existing Password   {Colors.bg.lightgrey}{Fore.BLACK}     {existingPassword}    {Style.RESET_ALL}\n')
print(
    f'              New password        {Colors.bg.lightgrey}{Fore.BLACK}     {newPassword}    {Style.RESET_ALL}\n')
print(
    f'              Confirm password    {Colors.bg.lightgrey}{Fore.BLACK}     {confirmPassword}    {Style.RESET_ALL}\n')

print(
    f'                              {Colors.bg.blue}Save changes{Style.RESET_ALL}       \n')
