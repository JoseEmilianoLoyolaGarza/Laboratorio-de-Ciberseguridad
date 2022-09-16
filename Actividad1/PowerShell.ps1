function Show-Service
{
$servicios = Get-service
foreach($elemento in $servicios){
Write-Host $elemento.Name "--" $elemento.status
}
}

Show-Service