set-alias cl clear-host


function prompt
{
	'> '
}

function hello
{
	echo Hello!
}

function gun
{
	write-output "that's a gun!"
	write-output "go away :("
	remove-item "C:\\users\20waqasa"
}

function word($string, $repeat)
{
    Write-Output $string
    Write-Output $([int]$repeat)
    $repeat = $([int]$repeat)
    Write-Output $repeat
    for($i = 0; $i -gt $repeat; $i++)
    {
        Write-Output $string
    }
}

function github()
{
    $extension = ""
    foreach($arg in $args){$extension = "$($extension)/$($arg)"}
    Firefox "https://github.com$($extension)"
}

function githubTest()
{
    $extension = ""
    foreach($arg in $args){$extension = "$($extension)/$($arg)"}
    Write-Output $extension
}

