$response = Invoke-RestMethod -Uri "http://localhost:8000/health"

if ($response.status -eq "ok" -and $response.service -eq "DualSub") {
    Write-Host "DualSub is working correctly."
    exit 0
}

Write-Host "Health check failed."
exit 1