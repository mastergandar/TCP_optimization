import subprocess
import winreg


class MakeGrate:
    def __init__(self):
        super().__init__()

        self.Net_TCP = subprocess.Popen(
            ['powershell', 'Set-NetTCPSetting -SettingName internet -AutoTuningLevelLocal normal;'
                           'Set-NetTCPSetting -SettingName internet -ScalingHeuristics disabled;'
                           'Set-NetTCPSetting -SettingName internet -Timestamps disabled;'
                           'Set-NetTCPSetting -SettingName internet -EcnCapability disabled;'
                           'Set-NetTCPSetting -SettingName internet -MaxSynRetransmissions 2;'
                           'Set-NetTCPSetting -SettingName internet -NonSackRttResiliency disabled;'
                           'Set-NetTCPSetting -SettingName internet -InitialRto 2000;'
                           'Set-NetTCPSetting -SettingName internet -MinRto 300'],
            stderr=subprocess.PIPE)

        self.Net_Offload = subprocess.Popen(
            ['powershell', 'Set-NetOffloadGlobalSetting -ReceiveSegmentCoalescing disabled;'
                           'Set-NetOffloadGlobalSetting -ReceiveSideScaling enabled;'
                           'Set-NetOffloadGlobalSetting -Chimney disabled'])

        self.NetSH = subprocess.Popen(
            ['powershell', 'netsh interface ipv4 set subinterface "Ethernet" mtu=1500 store=persistent;'
                           'netsh interface ipv6 set subinterface "Ethernet" mtu=1500 store=persistent;'
                           'netsh int tcp set supplemental internet congestionprovider=CUBIC'],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        self.DE = subprocess.Popen(['powershell', 'Disable-NetAdapterLso -Name *;'
                                                  'Enable-NetAdapterChecksumOffload -Name *'],
                                   stderr=subprocess.PIPE)

        self.register = {'LocalPriority': 4, 'HostsPriority': 5, 'DnsPriority': 6, 'NetbtPriority': 7,
                         'NetworkThrottlingIndex': 0xffffffff, 'SystemResponsiveness': 10, 'Size': 3,
                         'LargeSystemCache': 1, 'MaxUserPort': 65534, 'TcpTimedWaitDelay': 30, 'DefaultTTL': 64,
                         'NonBestEffortLimit': 0, 'Do not use NLA': 1}

        self.Software_sys_profile = 'SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile'
        self.System_service = 'SYSTEM\\CurrentControlSet\\Services'
        self.Provider = 'Tcpip\\ServiceProvider'
        self.LargeCache = 'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management'

        self.perm = 'Hello from the other side!'

        self.errors_DE = self.DE.communicate(input=self.perm)
        self.output_SH, self.errors_SH = self.NetSH.communicate(input=self.perm)
        self.errors_Offload = self.Net_Offload.communicate(input=self.perm)
        self.errors_TCP = self.Net_TCP.communicate(input=self.perm)

    def reg_opt(self):
        try:
            opened_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.Software_sys_profile, 0, winreg.KEY_WRITE)
            winreg.SetValueEx(opened_key, 'NetworkThrottlingIndex', 0, winreg.REG_DWORD,
                              self.register['NetworkThrottlingIndex'])
            winreg.SetValueEx(opened_key, 'SystemResponsiveness', 0, winreg.REG_DWORD,
                              self.register['SystemResponsiveness'])
            winreg.CloseKey(opened_key)
        except WindowsError as e:
            return e

    def make_opt(self):

        try:
            self.Net_TCP.wait()
            self.Net_Offload.wait()
            self.NetSH.wait()
            self.DE.wait()
            self.reg_opt()
            if self.errors_TCP[1] != b'' or None \
                    and self.errors_Offload[1] != b'' or None \
                    and self.errors_SH != b'' or None \
                    and self.errors_DE[1] != b'' or None:
                raise TypeError
            else:
                return 'TCP optimization complete!'
        except TypeError:
            return 'One or more TCP settings load error!'

    def __str__(self):
        return self.make_opt()
