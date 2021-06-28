import subprocess


class MakeInfo:
    def __init__(self):
        super().__init__()
        self.Shell = subprocess.Popen(['powershell', 'Get-NetAdapterLso -Name *;'
                                                     'Get-NetAdapterChecksumOffload *;'
                                                     'Get-NetOffloadGlobalSetting;'
                                                     'Get-NetTCPSetting -SettingName internet'],
                                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.net = subprocess.Popen(['powershell', 'netsh int tcp show global'],
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        self.perm = 'Hello from the other side!'

        self.output_Shell, self.errors_Shell = self.Shell.communicate(input=self.perm)
        self.output_net, self.errors_net = self.net.communicate(input=self.perm)

    def diag(self):
        try:
            self.Shell.wait()
            self.net.wait()
            if self.errors_Shell != b'' or None \
                    and self.errors_net != b'' or None:
                raise TypeError
            else:
                pass
        except TypeError:
            return 'One or more TCP settings load error!'

    def __str__(self):
        return str(self.output_Shell.decode('cp866') + self.output_net.decode('cp866'))
