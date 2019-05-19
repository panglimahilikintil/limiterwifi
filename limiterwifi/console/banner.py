from .io import IO


_MAIN_BANNER = r"""{}
██╗     ██╗███╗   ███╗██╗████████╗███████╗██████╗  ██      ██╗██╗██████ ██╗
██║     ██║████╗ ████║██║╚══██╔══╝██╔════╝██╔══██╗ ██  ██  ██║██║██     ██║
██║     ██║██╔████╔██║██║   ██║   █████╗  ██████╔╝ ██ ████ ██║██║██████ ██║
██║     ██║██║╚██╔╝██║██║   ██║   ██╔══╝  ██╔══██╗ ████  ████║██║██     ██║
███████╗██║██║ ╚═╝ ██║██║   ██║   ███████╗██║  ██║ ███    ███║██║██     ██║
╚══════╝╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚═╝    ╚══╝╚═╝╚═╝    ╚═╝
                {}by panglimahilikintil   ~    limit drivices on network :3  
                                                v[_v_]

""".format(IO.Fore.LIGHTRED_EX, IO.Style.RESET_ALL + IO.style.BRIGHT)


def get_main_benner(version):
    return _MAIN_BANNER.replace('[_v_]', version)