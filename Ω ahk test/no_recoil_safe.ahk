$LButton::
{
    If GetKeyState("RButton", "P")
    {
        While GetKeyState("LButton", "P")
        {
            Click
            Sleep, 350
        }
    
    }
    Else
    {
        While GetKeyState("LButton", "P")
        {
            Click Left Down
        }
        Click Left Up
        Click
    }
}
Return
,::
{
    ExitApp
}
Return
