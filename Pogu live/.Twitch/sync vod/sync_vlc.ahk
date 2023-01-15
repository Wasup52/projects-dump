; #############################################################################################################################################
; #  This script sends your keystrokes to all running instances of VLC media player. It doesn't work if you use a mouse.                      #
; #                                                                                                                                           #
; #  These things should work:                                                                                                                #
; #                                                                                                                                           #
; #  forward: Ctrl + right / Alt + right / Shift + right                                                                                      #
; #  backward: Ctrl + left / Alt + left / Shift + left                                                                                        #
; #  play/pause: space                                                                                                                        #
; #  speed up: ]                                                                                                                              #
; #  speed down: [                                                                                                                            #
; #  You can easily add in other keystrokes below the line: ~^down::LoopControlSend(Windows, "^{down}")                                       #
; #                                                                                                                                           #
; #  This doesn't sync the videos perfectly, so you can use the following 4 keys: left, right, up, down to control the active window only.    #
; #                                                                                                                                           #
; #  left very short backward jump                                                                                                            #
; #  right very short forward jump                                                                                                            #
; #  up medium backward jump                                                                                                                  #
; #  down medium forward jump                                                                                                                 #
; #############################################################################################################################################


ScriptVersion = 1.1
#Singleinstance,force

GoSub, MainProgram
return

mainprogram:
    WinGet, id, list,,, Program Manager
    i := 0, count := id, title := "VLC"
    loop % id {
        WinGetTitle, this_title, % "ahk_id " id%a_index%
        if !instr(this_title, title) ; or if this_title not contains %title%
            count--, id%a_index% := ""
    }
    Loop, %id%
    {
        StringTrimRight, this_id, id%a_index%, 0
        Windows := this_id . "," . Windows
    }
    StringTrimRight, Windows, Windows, 1

    #NoEnv ; Recommended for performance and compatibility with future AutoHotkey releases.
    SendMode Input ; Recommended for new scripts due to its superior speed and reliability.

    ~]::LoopControlSend(Windows, "]")
    ~[::LoopControlSend(Windows, "[")
    ~j::LoopControlSend(Windows, "j")
    ~k::LoopControlSend(Windows, "k")
    ~space::LoopControlSend(Windows, "{space}")

    ~+left::LoopControlSend(Windows, "+{left}")
    ~!left::LoopControlSend(Windows, "!{left}")
    ~^left::LoopControlSend(Windows, "^{left}")
    ~+right::LoopControlSend(Windows, "+{right}")
    ~!right::LoopControlSend(Windows, "!{right}")
    ~^right::LoopControlSend(Windows, "^{right}")
    ~^up::LoopControlSend(Windows, "^{up}")
    ~^down::LoopControlSend(Windows, "^{down}")

    ; for active windows only. use this to adjust speed when out of sync
    ~left::ActiveWindowSend(Windows, "+{left}")
    ~right::ActiveWindowSend(Windows, "+{right}")
    ~up::ActiveWindowSend(Windows, "^{left}")
    ~down::ActiveWindowSend(Windows, "^{right}")
return

LoopControlSend(Windows, x)
{
    WinGet, active_id, ID, A

    is_valid_window = 0
    Loop,Parse,Windows,CSV
    {
        if active_id = %A_LoopField%
        {
            is_valid_window = 1
            break
        }
    }

    if is_valid_window
    {
        Loop,Parse,Windows,CSV
        {
            if active_id <> %A_LoopField%
            {
                ControlSend, , %x%, Ahk_Id %A_LoopField%
            }
        }
    }
}

ActiveWindowSend(Windows, x)
{
    WinGet, active_id, ID, A

    is_valid_window = 0
    Loop,Parse,Windows,CSV
    {
        if active_id = %A_LoopField%
        {
            is_valid_window = 1
            break
        }
    }

    if is_valid_window
    {
        SendInput, %x%
    }
}