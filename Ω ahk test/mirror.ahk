;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;   Mirror.ahk mirrors mouse clicks on one half of the screen to the other half
; http://superuser.com/questions/393738/
;
;   (cl) 2012- Synetech inc., Alec Soroudi
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;   Hotkeys:
;       Alt+Shift+Q                     to toggle mirroring
;       Ctrl+Shift+Q                    to toggle autofire
;       Ctrl+Alt+Shift+Q            to completely pause the script (mouse behaves normally)
;       Ctrl+Alt+Shift+Win+Q    to quit
;
;       Defaults to single-click, mirrored
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
#SingleInstance force
CoordMode, Mouse, Screen
SetDefaultMouseSpeed, 0
SetMouseDelay, -1
SendMode Play                                       ;Try modes Event, Input, or Play


;Variables
SysGet, MonitorWorkArea, MonitorWorkArea, %A_Index%
Half            :=  (MonitorWorkAreaRight - MonitorWorkAreaLeft) >> 1
Mirror      :=  1
Autofire    :=  0



;Main function
Dupe(action, var) {
    ;Calculate other half
    MouseGetPos, x,y
    Global Half
    if (x<Half) {
        Left := (Half + x)
    }
    else {
        Left := (x - Half)
    }

    Global Mirror
    if (action=0) {                             ;Mouse
        if (var=0) {                                ;Left-click
            if Mirror
                Click %Left% %y% Left
            Click %x% %y% Left
        }

        else if (var=1) {                       ;Right-click
            Click %Left% %y% Right
            Click %x% %y% Right
        }

        else if (var=2) {                       ;Middle-click
            Click %Left% %y% Middle
            Click %x% %y% Middle
        }

        else if (var=3) {                       ;Button4-click
            Click %Left% %y% X1
            Click %x% %y% X1
        }

        else if (var=4) {                       ;Button5-click
            Click %Left% %y% X2
            Click %x% %y% X2
        }
    }


;   else if (action=1) {                    ;Keyboard - do what???
;   }
}



;Hotkeys
!+q::                                                       ;Pause mirroring with Alt+Shift+Q
    Mirror := !Mirror
    MsgBox  Mirror: %MonitorWorkArea%, %MonitorWorkArea%
return

^+q::                                                       ;Toggle autofire with Ctrl+Shift+Q
    Autofire := !Autofire
;   MsgBox  Autofire: %Autofire%
return

^!+q::                                                  ;Pause script with Ctrl+Alt+Shift+Q
    Suspend
;   if (A_IsSuspended = 1)
;       MsgBox  Hotkeys suspended
;   else
;       MsgBox  Hotkeys resumed
return

^!+#q::                                                 ;Quit with Ctrl+Alt+Shift+Win+Q
;   MsgBox Quitting
    ExitApp
return

+#q::                                                       ;Reload/restart script with Shift+Win+Q
;   MsgBox Reloading
    Reload
return



;Handlers
*$LButton::
Loop {
       if (Mirror)
            Dupe(0, 0)
        GetKeyState, State, LButton, P
        if (!Autofire || State = "U")
            Break
}
return

*$RButton::
Loop {
        if (Mirror)
            Dupe(0, 1)
        GetKeyState, State, RButton, P
        if (!Autofire || State = "U")
            Break
}
return

*$MButton::
Loop {
        if (Mirror)
            Dupe(0, 2)
        GetKeyState, State, MButton, P
        if (!Autofire || State = "U")
            Break
}
return

*$XButton1::
Loop {
        if (Mirror)
            Dupe(0, 3)
        GetKeyState, State, XButton1, P
        if (!Autofire || State = "U")
            Break
}
return

*$XButton2::
Loop {
        if (Mirror)
            Dupe(0, 4)
        GetKeyState, State, XButton2, P
        if (!Autofire || State = "U")
            Break
}
return
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;