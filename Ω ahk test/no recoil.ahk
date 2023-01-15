$LButton::
{
    If GetKeyState("RButton", "P")
    {
        While GetKeyState("LButton", "P")
        {
            If GetKeyState("XButton1", "P")
            {
                Click
                Sleep, 350
            }
            Else
            {
                Click Left Down
            }
            
        }
        Click Left Up
    }
    Else
    {
        While GetKeyState("LButton", "P")
        {
            Click Left Down
        }
        Sleep 75
        Click Left Up
        ; Click
    }
}
Return
,::Suspend

