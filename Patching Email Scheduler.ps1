# Set email parameters
$smtpServer = "smtp.office365.com"
$smtpPort = "587"
$senderEmail = "your_email@outlook.com"
$senderPassword = "your_password"
$receiverEmail = "receiver_email@outlook.com"
$subject = "Email Subject Goes Here"

# Determine the date of the third Tuesday of the current month
$date = Get-Date
$thirdTuesday = Get-Date -Date "$($date.Year)-$($date.Month)-01" | Where-Object { $_.DayOfWeek -eq "Tuesday" } | Select-Object -Index 2
$thirdTuesdayString = $thirdTuesday.ToString("yyyy-MM-dd")

# Check if today is the third Tuesday of the month and the time is 8:30 am
if ($date.ToString("yyyy-MM-dd") -eq $thirdTuesdayString -and $date.ToString("HH:mm") -eq "08:30") {
    # If today is the third Tuesday at 8:30 am, send the email
    $message = "Send your email message here"
    $mailParams = @{
        SmtpServer = $smtpServer
        Port = $smtpPort
        UseSSL = $true
        Credential = New-Object System.Net.NetworkCredential($senderEmail, $senderPassword)
        From = $senderEmail
        To = $receiverEmail
        Subject = $subject
        Body = $message
    }
    try {
        Send-MailMessage @mailParams
        Write-Host "Email sent successfully."
    }
    catch {
        Write-Host "An error occurred while sending the email: $_"
    }
}
