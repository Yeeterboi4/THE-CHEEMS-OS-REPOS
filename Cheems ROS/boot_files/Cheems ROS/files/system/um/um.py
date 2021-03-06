import os, colorama, time
from distutils.dir_util import copy_tree

colorama.init()

ignore = []
update_file_data = None
files_to_replace = None
update_file_g = ''
update_file_ndir_g = ''
log = []
files = []

oldcd = os.getcwd()
os.chdir('../../')
install_path = os.getcwd()
os.chdir(oldcd)

def decomp(update_file_ndir):
    global update_file_ndir_g

    try:

        update_file_ndir_g = update_file_ndir
        command1 = 'echo Q | decomp x ' + update_file_ndir_g + ' >nul'

        os.system(command1)
    except Exception as e:
        command2 = '@RD /s /q ' + update_file_g
        os.system(command2)
        print(colorama.Fore.RED + 'ERROR: Could Not Decompile ' + update_file_ndir_g + colorama.Style.RESET_ALL)
        e = ' PYTHON ERROR: ', e
        log.append('ERROR: Could Not Decompile ' + update_file_ndir_g + e)

def ignore(files_to_ignore,desc=True):
    global update_file_g
    try:
        global ignore, log, update_file_g
        if desc == True:
            print('CE: Setted ignored files')
        log.append('SET ignore=' + files_to_ignore)
        ignore = files_to_ignore
    except Exception as e:
        command2 = '@RD /s /q ' + update_file_g
        os.system(command2)
        print(colorama.Fore.RED + 'ERROR: Could Not Find Ignore File: ' + str(files_to_ignore[0]) + colorama.Style.RESET_ALL)
        e = ' PYTHON ERROR: ', e
        log.append('ERROR: Could Not Find Ignore File: ' + str(files_to_ignore[0]) + e)

def updatefile(update_file,desc=True):
    try:
        global update_file_data, ignore, files, update_file_g, log  

        with open(update_file + '/ignore.txt') as f: files_to_ignore = f.readlines()
        ignore = files_to_ignore
        log.append('SET updatefile=' + update_file)

        for x in os.listdir(update_file):
            if x != 'ignore.txt' and x != 'update_log.txt' and x != 'ver.txt':
                files.append(x)
                    
        if desc == True:
            print('CE: Setted Update File')
        update_file_g = update_file
    except Exception as e:
        command2 = '@RD /s /q ' + update_file_g
        os.system(command2)
        print(colorama.Fore.RED + 'ERROR: Could Not Find Update File: ' + str(update_file_g) + colorama.Style.RESET_ALL)
        e = ' PYTHON ERROR: ', e
        log.append('ERROR: Could Not Find Update File: ' + str(update_file_g) + e)

def InstallUpdate(desc=True):
    try:
        global ignore, install_path, files, update_file_g, update_file_ndir_g

        with open(update_file_g + '/update_log.txt') as f: update_log = f.readlines()
        with open(update_file_g + '/ver.txt') as f: version = f.readlines()

        log.append('SET updatelog=' + str(update_log))
        log.append('SET updateversion=' + str(version))

        i = 0
        if desc == True:
            print('CE: Started Install:\n')

            print('Update Log v' + version[0] + ': ')
            
        _update = -1
        _update_log = ''
        for update in update_log:
            _update += 1
            _update_log = _update_log + update_log[_update]
            if desc == True:
                print(' ' + update_log[_update])
        log.append('$UpdateFiles : ' + _update_log)

        if desc == True:
            print('')

        item = -1
        
        if desc == True:
            print('Installation: ')

        for x in os.listdir(install_path + '/' + files[item]):
            if x.endswith(".dat") or x.endswith(".txt") or x.endswith(".log"):
                if i != len(ignore) - 1:
                    i += 1
                if str(x) in ignore[i] or str(x) in str(files):
                    log.append('FOUND ' + ignore[i] + 'or ' + str(x))
                else:
                    if desc == True:
                        print(colorama.Fore.YELLOW + ' WARNING: Not In Ignore: ' + x + colorama.Style.RESET_ALL)
                    log.append('WARNING File not in ignore : ' + x)

        for file in files:

            item += 1

            src = update_file_g + '/' + files[item]
            target = install_path + '/' + files[item]

            log.append('SET Source Path ' + str(item) + ' : ' + update_file_g + ' file: ' + files[item])
            log.append('SET Install Path ' + str(item) + ' : ' + install_path + ' file: ' + files[item])

            copy_tree(src, target)
            if desc == True:
                print(' Installed File ' + file)

        log.append('$ItemFiles : ' + str(item))
        log.append('$LastItemFile : ' + files[item])

        log.append('END')

        cur_line = -1


        update_log_name = 'update' + version[0] + '.log'
        with open(update_log_name, 'w') as f:
            for object in log:
                cur_line += 1
                f.write(log[cur_line] + '\n')

        command2 = '@RD /s /q ' + update_file_g
        os.system(command2)
    except Exception as e:
        command2 = '@RD /s /q ' + update_file_g
        os.system(command2)
        print(colorama.Fore.RED + 'ERROR: Could Not Install Update ' + colorama.Style.RESET_ALL)
        e = 'ERROR: Could Not Install Update' + str(e)
        log.append(e)

        cur_line = -1

        update_log_name = 'update_unkown_version.log'
        with open(update_log_name, 'w') as f:
            for object in log:
                cur_line += 1
                f.write(log[cur_line] + '\n')

        command2 = '@RD /s /q ' + update_file_g
        os.system(command2)
    return version
