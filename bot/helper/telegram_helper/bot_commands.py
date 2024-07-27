#!/usr/bin/env python3
from bot import CMD_SUFFIX, config_dict

class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = [f'mirror1{CMD_SUFFIX}', f'm1{CMD_SUFFIX}']
        self.QbMirrorCommand = [f'qbmirror{CMD_SUFFIX}', f'qm{CMD_SUFFIX}']
        self.YtdlCommand = [f'ytdl1{CMD_SUFFIX}', f'y1{CMD_SUFFIX}']
        self.LeechCommand = [f'leech1{CMD_SUFFIX}', f'l1{CMD_SUFFIX}']
        self.QbLeechCommand = [f'qbleech{CMD_SUFFIX}', f'ql{CMD_SUFFIX}']
        self.YtdlLeechCommand = [f'ytdlleech1{CMD_SUFFIX}', f'yl1{CMD_SUFFIX}']
        if config_dict['SHOW_EXTRA_CMDS']:
            self.MirrorCommand.extend([f'unzipmirror{CMD_SUFFIX}', f'uzm{CMD_SUFFIX}', f'zipmirror{CMD_SUFFIX}', f'zm{CMD_SUFFIX}'])
            self.QbMirrorCommand.extend([f'qbunzipmirror{CMD_SUFFIX}', f'quzm{CMD_SUFFIX}', f'qbzipmirror{CMD_SUFFIX}', f'qzm{CMD_SUFFIX}'])
            self.YtdlCommand.extend([f'ytdlzip{CMD_SUFFIX}', f'yz{CMD_SUFFIX}'])
            self.LeechCommand.extend([f'unzipleech{CMD_SUFFIX}', f'uzl1{CMD_SUFFIX}', f'zipleech1{CMD_SUFFIX}', f'zl1{CMD_SUFFIX}'])
            self.QbLeechCommand.extend([f'qbunzipleech1{CMD_SUFFIX}', f'quz1l{CMD_SUFFIX}', f'qbzipleech1{CMD_SUFFIX}', f'qzl{CMD_SUFFIX}'])
            self.YtdlLeechCommand.extend([f'ytdlzipleech1{CMD_SUFFIX}', f'yzl1{CMD_SUFFIX}'])
        self.CloneCommand = [f'clone1{CMD_SUFFIX}', f'c1{CMD_SUFFIX}']
        self.CountCommand = f'count1{CMD_SUFFIX}'
        self.DeleteCommand = f'del1{CMD_SUFFIX}'
        self.CancelMirror = f'cancel1{CMD_SUFFIX}'
        self.CancelAllCommand = [f'cancelall1{CMD_SUFFIX}', 'cancellallbot']
        self.ListCommand = f'list{CMD_SUFFIX}'
        self.SearchCommand = f'search{CMD_SUFFIX}'
        self.StatusCommand = [f'status1{CMD_SUFFIX}', f's1{CMD_SUFFIX}', 'statusall']
        self.UsersCommand = f'users1{CMD_SUFFIX}'
        self.AuthorizeCommand = [f'authorize1{CMD_SUFFIX}', f'a1{CMD_SUFFIX}']
        self.UnAuthorizeCommand = [f'unauthorize1{CMD_SUFFIX}', f'ua1{CMD_SUFFIX}']
        self.AddBlackListCommand = [f'blacklist{CMD_SUFFIX}', f'bl{CMD_SUFFIX}']
        self.RmBlackListCommand = [f'rmblacklist{CMD_SUFFIX}', f'rbl{CMD_SUFFIX}']
        self.AddSudoCommand = f'addsudo{CMD_SUFFIX}'
        self.RmSudoCommand = f'rmsudo{CMD_SUFFIX}'
        self.PingCommand = [f'ping{CMD_SUFFIX}', f'p{CMD_SUFFIX}']
        self.RestartCommand = [f'restart{CMD_SUFFIX}', f'r{CMD_SUFFIX}', 'restartall']
        self.StatsCommand = [f'stats{CMD_SUFFIX}', f'st{CMD_SUFFIX}']
        self.HelpCommand = f'help{CMD_SUFFIX}'
        self.LogCommand = f'log{CMD_SUFFIX}'
        self.ShellCommand = f'shell{CMD_SUFFIX}'
        self.EvalCommand = f'eval{CMD_SUFFIX}'
        self.ExecCommand = f'exec{CMD_SUFFIX}'
        self.ClearLocalsCommand = f'clearlocals{CMD_SUFFIX}'
        self.BotSetCommand = [f'bsetting{CMD_SUFFIX}', f'bs{CMD_SUFFIX}']
        self.UserSetCommand = [f'usetting{CMD_SUFFIX}', f'us{CMD_SUFFIX}']
        self.BtSelectCommand = f'btsel{CMD_SUFFIX}'
        self.CategorySelect = f'ctsel{CMD_SUFFIX}'
        self.SpeedCommand = [f'speedtest{CMD_SUFFIX}', f'sp{CMD_SUFFIX}']
        self.RssCommand = f'rss{CMD_SUFFIX}'
        self.LoginCommand = 'login'
        self.AddImageCommand = f'addimg{CMD_SUFFIX}'
        self.ImagesCommand = f'images{CMD_SUFFIX}'
        self.IMDBCommand = f'imdb{CMD_SUFFIX}'
        self.AniListCommand = f'anime{CMD_SUFFIX}'
        self.AnimeHelpCommand = f'animehelp{CMD_SUFFIX}'
        self.MediaInfoCommand = [f'mediainfo{CMD_SUFFIX}', f'mi{CMD_SUFFIX}']
        self.MyDramaListCommand = f'mdl{CMD_SUFFIX}'
        self.GDCleanCommand = [f'gdclean{CMD_SUFFIX}', f'gc{CMD_SUFFIX}']
        self.BroadcastCommand = [f'broadcast1{CMD_SUFFIX}', f'bc1{CMD_SUFFIX}']

BotCommands = _BotCommands()
